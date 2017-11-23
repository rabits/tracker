import yaml

data1 = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None
]

data2 = [
    '00000000',
    '00001010',
    '11101010',
    '10010110',
    '01010001',
    '00000000',
    '00000000',
    '00000000',
    '00010100',
    '10000000',
    '01110001',
    '00000000',
    '00100000',
    '00000000',
    '00000000',
    '00000011',
    '11100001',
    '00000000',
    '10000000',
    '00000000',
    '00000000',
    '01101101',
    '01111010',
    '00000001',
    '00000000'
]

for i, v in enumerate(data2):
    data2[i] = int(v, 2)

data_map = {}
with open('config.user.yaml', 'rb') as f:
    data_map = yaml.load(f.read())['ALDL160'][0]['map']

import pprint
pp = pprint.PrettyPrinter(indent=2)

pp.pprint(data_map)

#######################################################

import sys
sys.path.append('src')
from Library import mapValue

out1 = {}
out2 = {}

for pos in data_map.keys():
    out1.update(mapValue(pos, data1, data_map))

pp.pprint(out1)

for pos in data_map.keys():
    out2.update(mapValue(pos, data2, data_map))

pp.pprint(out2)
