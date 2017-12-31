#!/usr/bin/python

# ===========================================================================
# INA219 Class
# ===========================================================================

class INA219:
    # ===========================================================================
    #   I2C ADDRESS/BITS
    # ==========================================================================
    __INA219_ADDRESS                         = 0x40    # 1000000 (A0+A1=GND)
    __INA219_READ                            = 0x01
    # ===========================================================================

    # ===========================================================================
    #    CONFIG REGISTER (R/W)
    # ===========================================================================
    __INA219_REG_CONFIG                      = 0x00
    # ===========================================================================
    __INA219_CONFIG_RESET                    = 0x8000  # Reset Bit
    __INA219_CONFIG_BVOLTAGERANGE_MASK       = 0x2000  # Bus Voltage Range Mask
    __INA219_CONFIG_BVOLTAGERANGE_16V        = 0x0000  # 0-16V Range
    __INA219_CONFIG_BVOLTAGERANGE_32V        = 0x2000  # 0-32V Range

    __INA219_CONFIG_GAIN_MASK                = 0x1800  # Gain Mask
    __INA219_CONFIG_GAIN_1_40MV              = 0x0000  # Gain 1, 40mV Range
    __INA219_CONFIG_GAIN_2_80MV              = 0x0800  # Gain 2, 80mV Range
    __INA219_CONFIG_GAIN_4_160MV             = 0x1000  # Gain 4, 160mV Range
    __INA219_CONFIG_GAIN_8_320MV             = 0x1800  # Gain 8, 320mV Range

    __INA219_CONFIG_BADCRES_MASK             = 0x0780  # Bus ADC Resolution Mask
    __INA219_CONFIG_BADCRES_9BIT             = 0x0080  # 9-bit bus res = 0..511
    __INA219_CONFIG_BADCRES_10BIT            = 0x0100  # 10-bit bus res = 0..1023
    __INA219_CONFIG_BADCRES_11BIT            = 0x0200  # 11-bit bus res = 0..2047
    __INA219_CONFIG_BADCRES_12BIT            = 0x0400  # 12-bit bus res = 0..4097

    __INA219_CONFIG_SADCRES_MASK             = 0x0078  # Shunt ADC Resolution and Averaging Mask
    __INA219_CONFIG_SADCRES_9BIT_1S_84US     = 0x0000  # 1 x 9-bit shunt sample
    __INA219_CONFIG_SADCRES_10BIT_1S_148US   = 0x0008  # 1 x 10-bit shunt sample
    __INA219_CONFIG_SADCRES_11BIT_1S_276US   = 0x0010  # 1 x 11-bit shunt sample
    __INA219_CONFIG_SADCRES_12BIT_1S_532US   = 0x0018  # 1 x 12-bit shunt sample
    __INA219_CONFIG_SADCRES_12BIT_2S_1060US  = 0x0048  # 2 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_4S_2130US  = 0x0050  # 4 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_8S_4260US  = 0x0058  # 8 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_16S_8510US = 0x0060  # 16 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_32S_17MS   = 0x0068  # 32 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_64S_34MS   = 0x0070  # 64 x 12-bit shunt samples averaged together
    __INA219_CONFIG_SADCRES_12BIT_128S_69MS  = 0x0078  # 128 x 12-bit shunt samples averaged together

    __INA219_CONFIG_MODE_MASK                = 0x0007  # Operating Mode Mask
    __INA219_CONFIG_MODE_POWERDOWN           = 0x0000
    __INA219_CONFIG_MODE_SVOLT_TRIGGERED     = 0x0001
    __INA219_CONFIG_MODE_BVOLT_TRIGGERED     = 0x0002
    __INA219_CONFIG_MODE_SANDBVOLT_TRIGGERED = 0x0003
    __INA219_CONFIG_MODE_ADCOFF              = 0x0004
    __INA219_CONFIG_MODE_SVOLT_CONTINUOUS    = 0x0005
    __INA219_CONFIG_MODE_BVOLT_CONTINUOUS    = 0x0006
    __INA219_CONFIG_MODE_SANDBVOLT_CONTINUOUS = 0x0007
    # ===========================================================================

    # ===========================================================================
    #   SHUNT VOLTAGE REGISTER (R)
    # ===========================================================================
    __INA219_REG_SHUNTVOLTAGE                = 0x01
    # ===========================================================================

    # ===========================================================================
    #   BUS VOLTAGE REGISTER (R)
    # ===========================================================================
    __INA219_REG_BUSVOLTAGE                  = 0x02
    # ===========================================================================

    # ===========================================================================
    #   POWER REGISTER (R)
    # ===========================================================================
    __INA219_REG_POWER                       = 0x03
    # ===========================================================================

    # ==========================================================================
    #    CURRENT REGISTER (R)
    # ===========================================================================
    __INA219_REG_CURRENT                     = 0x04
    # ===========================================================================

    # ===========================================================================
    #    CALIBRATION REGISTER (R/W)
    # ===========================================================================
    __INA219_REG_CALIBRATION                 = 0x05
    # ===========================================================================

    # Constructor
    def __init__(self, address, bus):
        self._bus = bus
        self._address = address

        self._ina219SetCalibration_32V_2A()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


    def _twosToInt(self, val, len):
        # Convert twos compliment to integer

        if val & (1 << len - 1):
            val = val - (1<<len)

        return val

    def _ina219SetCalibration_32V_2A(self):
        self._ina219_currentMultiplier_A = 0.0001  # Current LSB = 100uA per bit (1000/100 = 10)
        self._ina219_powerMultiplier_W = 0.0005    # Power LSB = 1mW per bit (2/1)

        # Set Calibration register to 'Cal' calculated above
        data = [(0x1000 >> 8) & 0xFF, 0x1000 & 0xFF]
        self._bus.write_i2c_block_data(self._address, self.__INA219_REG_CALIBRATION, data)

        # Set Config register to take into account the settings above
        config = self.__INA219_CONFIG_BVOLTAGERANGE_32V | \
                 self.__INA219_CONFIG_GAIN_8_320MV | \
                 self.__INA219_CONFIG_BADCRES_12BIT | \
                 self.__INA219_CONFIG_SADCRES_12BIT_1S_532US | \
                 self.__INA219_CONFIG_MODE_SANDBVOLT_CONTINUOUS

        data = [(config >> 8) & 0xFF, config & 0xFF]
        self._bus.write_i2c_block_data(self._address, self.__INA219_REG_CONFIG, data)

    def _getBusVoltage_raw(self):
        hibyte = self._bus.read_byte_data(self._address, self.__INA219_REG_BUSVOLTAGE)
        result = (hibyte << 8) + self._bus.read_byte_data(self._address, self.__INA219_REG_BUSVOLTAGE+1)

        # Shift to the right 3 to drop CNVR and OVF and multiply by LSB
        return (result >> 3) * 4

    def _getShuntVoltage_raw(self):
        result = self._bus.read_i2c_block_data(self._address, self.__INA219_REG_SHUNTVOLTAGE, 2)
        if result[0] >> 7 == 1:
            testint = (result[0]*256 + result[1])
            othernew = self._twosToInt(testint, 16)
            return othernew
        else:
            return (result[0] << 8) | (result[1])

    def _getCurrent_raw(self):
        result = self._bus.read_i2c_block_data(self._address, self.__INA219_REG_CURRENT, 2)
        if result[0] >> 7 == 1:
            testint = (result[0]*256 + result[1])
            othernew = self._twosToInt(testint, 16)
            return othernew
        else:
            return (result[0] << 8) | (result[1])

    def _getPower_raw(self):
        result = self._bus.read_i2c_block_data(self._address, self.__INA219_REG_POWER, 2)
        if result[0] >> 7 == 1:
            testint = (result[0]*256 + result[1])
            othernew = self._twosToInt(testint, 16)
            return othernew
        else:
            return (result[0] << 8) | (result[1])

    def getShuntVoltageV(self):
        value = self._getShuntVoltage_raw()
        return value * 0.00001

    def getBusVoltageV(self):
        value = self._getBusVoltage_raw()
        return value * 0.001

    def getCurrentA(self):
        valueDec = self._getCurrent_raw()
        return valueDec * self._ina219_currentMultiplier_A

    def getPowerW(self):
        valueDec = self._getPower_raw()
        return valueDec * self._ina219_powerMultiplier_W
