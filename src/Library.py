#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Log as log

def mapValue(key, data, data_map, old_map_data = {}, value_size = 8):
    ''' Mapping function
    Used to name and convert digital data to human readable format
    Input:
     * key          - index of the value
     * data         - all the values for mapping: dict with int keys
     * data_map     - map for the values: dict with int keys
     * old_map_data - previous data state
     * value_size   - size of the value in the data array

    data_map:
      - name: Some Good value     ## Item readable unique identificator

        type: number              ## Could be any of: number, binmap, hex, char

        enabled: true             ## Map value or just skip it with return only name and original value

        size: 1                   ## How much following items described by this item - if it's bigger than usual value_size.
                                  #  Covered items will be marked as links to this description

        default_value: 0          ## Type: number.
                                  # Will be used if previous value is None while execute math

        math: N*10                ## Type: number.
                                  #  Expression to calculate actual value using provided formula.
                                  #  You can use next symbols:
                                  #    "N"              - will be replaced by a new raw value
                                  #    "P"              - will be replaced by a previous mapped value
                                  #    "*/+-%<>()&|!="  - some math operators & helpers
                                  #    "0123456789."    - numeric values with floating point

        table:                    ## Type: number, will be skipped if math is set.
          0:   3                  #  It describes 2d chart with linear interpolation between the
          1.5: 6                  #  points. It's good alternative for math - just measure actual
          3:   9                  #  value and prepare a table with measured data.
          6:   75
          10:  15

        map:                      ## Type: binmap.
          - name: Submap Value 1  #  Used to prepare submap with boolean values like flags.
          - name: Submap Value 2
    '''
    desc = data_map.get(key)
    if desc is None: # Skipping not mapped value
        return {key: data.get(key)}

    if not isinstance(desc, dict): # It's a link, to process value we need to go to the key
        return mapValue(desc, data, data_map, value_size)

    name = desc.get('name', key)
    if not desc.get('enabled', True): # Mapping disabled - just returning actual value
        return {name: data.get(key)}

    size = desc.get('size', 1)
    value = None
    for i in xrange(key, key+size):
        if not data.has_key(i):
            log.error('Unable to find required data value %d for mapping key %d' % (i, key))
        elif i != key: # Creating a link
            dm_val = data_map.get(i)
            if dm_val != None and not isinstance(dm_val, int):
                log.error('Replacing by link the wrong mapping %d contains %s' % (i, dm_val))
            data_map[i] = key
            if value != None:
                value = (value<<(i-key)*value_size) + data[i]
        else:
            value = data[i]

    t = desc.get('type', 'number')
    if t == 'number':
        if value != None:
            if isinstance(desc.get('math'), str):
                value = evaluateMath(desc['math'], value, old_map_data.get(name, desc.get('default_value', 0)))
            elif isinstance(desc.get('table'), dict):
                table = desc['table']
                if table.has_key(value):
                    value = table[value]
                else:
                    # Finding table keys for our value
                    lt = gt = 0
                    for i in table.keys():
                        if value < i:
                            gt = i
                            break
                        lt = i

                    # Math linear interpolation between those values
                    value = (table[lt] * (gt - value) + table[gt] * (value - lt)) / (gt - lt)
            value = round(value, desc.get('round', 2))
    elif t == 'binmap':
        fout = {}
        for i, fd in enumerate(desc.get('map', [])):
            if not fd.get('enabled', True):
                continue
            fname = fd.get('name', i)
            mask = 1<<i
            if value is None:
                fout[fname] = None
            else:
                fout[fname] = value & mask == mask
            fout[fname] = fd.get(fout[fname], fout[fname])
        value = fout
    elif t == 'hex':
        if value != None:
            value = format(value, '0%dx' % (value_size/4 * size)).upper()
    elif t == 'char':
        if value != None:
            value = ''.join([ chr(val) for val in data[key:key+size] ])
    else:
        log.error('Unable to map %s wrong type %s' % (desc.get('name'), t))

    return {name: value}

def evaluateMath(math, value, old_value):
    '''Function to use with any math processes'''
    # If it's not a string - there is nothing to evaluate
    if not isinstance(math, str):
        return math
    # Leave only good symbols in the math expression
    math = ''.join(c for c in math if c in 'NP0123456789.*/+-%<>()&|!=')
    math = math.replace('N', str(value)).replace('P', str(old_value))
    try:
        value = eval(math)
    except Exception as e:
        log.error('Unable to evaluate %s due to error: %s' % (math, e))
    return value

def mergeDicts(dict1, dict2):
    ''' Merging dicts of dicts function
    Simple recursive merging of 2 dicts, that contains a tree of dicts.

    Input:
     * dict1        - original data dict, will be changed if there is some changes
     * dict2        - new with data to update

    Output: dict with changed keys tree, on leaves contains original values
    '''
    keys_out = {}
    for key in dict2:
        dict1[key] = dict1.get(key, None)
        if dict1[key] == dict2[key]:
            continue
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            out = mergeDicts(dict1[key], dict2[key])
            if out:
                keys_out[key] = out
        else:
            keys_out[key] = dict1[key]
            dict1[key] = dict2[key]

    return keys_out
