

                        DATA STREAM A223  SPECIFICATION



..PAGE

   SPECIFICATIONS FOR DATA STREAM INFORMATION
   ------------------------------------------

   ENGINE USAGE:
       5.7L  SFI  (LT1) (VIN = P)    1994 1Y - CAR AUTOMATIC TRANSMISSION
*      5.7L  SFI  (LT1) (VIN = P)    1995 1Y - CAR AUTOMATIC TRANSMISSION


   DATA PIN: READ DATA ON PIN "M" OF ALDL CONNECTOR

   BAUD RATE: 8192


  PAGE
MODE 0  (RETURN TO NORMAL MODE)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $56
        - MODE NUMBER           = $00
        - MESSAGE CHECKSUM

        ECM RESPONSE:
         NORMAL MESSAGES


MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 0)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $00
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $92
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 60
        - CHECKSUM

MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 1)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $01
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $84
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 46
        - CHECKSUM

MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 2)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $02
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $8B
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 53
        - CHECKSUM

MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 4)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $04
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $83
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 45
        - CHECKSUM

MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 5)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $05
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $B7
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 97
        - CHECKSUM

MODE 1  (TRANSMIT FIXED DATA STREAM MESSAGE 6)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $57
        - MODE NUMBER           = $01
        - MESSAGE NUMBER        = $06
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $7C
        - MODE NUMBER           = $01
        - DATA BYTE 1
          .
          .

        - DATA BYTE 38
        - CHECKSUM

MODE 10 (CLEAR MALFUNCTION CODES - TESTER TO ECM)
        ALDL REQUEST:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $56
        - MODE NUMBER           = $0A
        - CHECKSUM

        THE ECM WILL RESPOND WITH THE FOLLOWING MESSAGE:
        - MESSAGE ID            = $F4
        - MESSAGE LENGTH        = $56
        - MODE NUMBER           = $0A
        - CHECKSUM

..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 60
..HEAD04L ALDL MODE 1 MESSAGE 0 DATA LIST
WORD #   DATA NAME   DESCRIPTION
 1       MALFFW10    LOGGED MALF FLAG WORD 10
          0   CODE 86  LOW RATIO
          1   CODE 85  TCC STUCK ON
          2   CODE 84  3-2 DOWNSHIFT FEEDBACK FAULT (ODM)
          3   CODE 83  TCC CONTROL FEEDBACK FAULT (ODM)
          4   CODE 82  SHIFT A SOLENOID FAULT (ODM)
          5   CODE 81  SHIFT B SOLENOID FAULT (ODM)
          6   CODE 80  TRANSMISSION COMPONENT SLIPPING
          7   CODE 79  TRANSMISSION OVER TEMPERATURE

 2       MALFFW2     LOGGED MALF FLAG WORD 2
          0   CODE 27  EGR ELECTRICAL FAULT (ODM)
          1   CODE 26  CCP ELECTRICAL FAULT (ODM)
          2   CODE 25  MAT SENSOR HIGH
          3   CODE 23  MAT SENSOR LOW
          4   CODE 16  LO-RES FAILURE
          5   CODE 13  LEFT O2 SENSOR FAILED
          6   CODE 12  NO REFERENCE PULSES
          7   CODE 11  MALF INDICATOR LAMP (MIL) FAULT

 3       MALFFW3     LOGGED MALF FLAG WORD 3
          0   CODE 43  ESC FAILURE
          1   CODE 42  EST GROUNDED
          2   CODE 41  EST OPEN
          3   CODE 36  HI-RES FAILURE
          4   CODE 48  MASS AIR FLOW SYSTEM FAILURE
          5   CODE 47  NOT USED
          6   CODE 32  EGR SYSTEM FAULT
          7   CODE 29  EAS ELECTRICAL FAULT (ODM)

         MALFFW4     LOGGED MALF FLAG WORD 4
          0   CODE 61  A/C LOW CHARGE
          1   CODE 55  FUEL SYSTEM LEAN
          2   CODE 54  NOT USED
          3   CODE 52  ENGINE OIL TEMPERATURE LOW
          4   CODE 50  SYSTEM VOLTAGE LOW
          5   CODE 46  FUEL ENABLE FAILURE
          6   CODE 45  LEFT O2 SENSOR RICH
          7   CODE 44  LEFT O2 SENSOR LEAN

 5       MALFFW5     LOGGED MALF FLAG WORD 5
          0   CODE 69  A/C CLUTCH CIRCUIT OPEN
          1   CODE 68  A/C RELAY SHORTED
          2   CODE 67  A/C PRESSURE TRANSDUCER DEGRADED
          3   CODE 66  A/C PRESSURE TRANSDUCER OPEN/SHORT
          4   CODE 65  RIGHT O2 SENSOR RICH
          5   CODE 64  RIGHT O2 SENSOR LEAN
          6   CODE 63  RIGHT O2 SENSOR FAILED
          7   CODE 62  OIL TEMPERATURE HIGH

 6       MALFFW6     LOGGED MALF FLAG WORD 6
          0   CODE 78  FAN 2 FAULT (ODM)
          1   CODE 77  FAN 1 FAULT (ODM)
          2   CODE 71  A/C EVAPORATOR TEMP SENSOR FAILED
          3   CODE 70  A/C CLUTCH RELAY FAULT (ODM)
          4   CODE 31  NOT USED
          5   CODE 19  NOT USED
          6   CODE 18  INJECTOR CIRCUIT
          7   CODE 17  NOT USED

 7       MALFFW7     LOGGED MALF FLAG WORD 7
          0   CODE 57  NOT USED
          1   CODE 56  NOT USED
          2   CODE 49  NOT USED
          3   CODE 34  MAP SENSOR LOW
          4   CODE 33  MAP SENSOR HIGH
          5   CODE 39  NOT USED
          6   CODE 35  NOT USED
          7   CODE 24  OUTPUT SPEED LOW

 8       MALFFW8     LOGGED MALF FLAG WORD 8
          0   CODE 53  SYSTEM VOLTAGE HIGH
          1   CODE 51  PROM/FLASH ERROR
          2   CODE 38  BRAKE SWITCH STUCK OFF
          3   CODE 37  BRAKE SWITCH STUCK ON
          4   CODE 22  THROTTLE POSITION LOW
          5   CODE 21  THROTTLE POSITION HIGH
          6   CODE 15  COOLANT TEMPERATURE LOW
          7   CODE 14  COOLANT TEMPERATURE HIGH

   9      SDINMW1    INPUT MODE WORD 1
          0   1 = A/C CLUTCH STATUS
          1   1 = A/C REQUEST
          2   NOT USED
          3   NOT USED
          4   NOT USED
          5   NOT USED
          6   1 = PARK/NEUTRAL SWITCH
          7   1 = CRUISE ACTIVE

  10      SDINMW2    INPUT MODE WORD 2
          0   1 = TCC BRAKE SWITCH
          1   NOT USED
          2   NOT USED
          3   1 = TRANSMISSION MODE A
          4   1 = TRANSMISSION MODE B
          5   1 = TRANSMISSION MODE C
          6   1 = SPARK RETARD REQUEST
          7   1 = ASR ACTIVE

  11      SDOUTMW1   OUTPUT MODE WORD 1
          0   1 = TCC CONTROL
          1   1 = TCC ENABLE
          2   1 = SHIFT A       SEE TABLE
          3   1 = SHIFT B       SEE TABLE
          4   NOT USED
          5   NOT USED
          6   NOT USED
          7   NOT USED


              SHIFT B  SHIFT A  GEAR
              ----------------------
                0        0       3RD
              ----------------------
                0        1       4TH
              ----------------------
                1        0       2ND
              ----------------------
                1        1       1ST
              ----------------------

  12      SDOUTMW2   OUTPUT MODE WORD 2
          0   1 = FAN 1 RELAY
          1   1 = FAN 2 RELAY
          2   1 = A.I.R. PUMP
          3   1 = A/C CLUTCH
          4   NOT USED
          5   NOT USED
          6   NOT USED
          7   NOT USED

 13      SDSTMW1     STATUS MODE WORD 1
          0   1 = ENGINE CLOSED LOOP
          1   1 = LEFT O2 READY
          2   1 = RIGHT O2 READY
          3   1 = LEARN ENABLED
          4   NOT USED
          5   1 = CATALYTIC CONVERTER OVERTEMP
          6   NOT USED
          7   NOT USED

 14      SDSTMW2     STATUS MODE WORD 2
          0   1 = POWER ENRICHMENT ACTIVE
          1   1 = KICKDOWN PATTERN
          2   1 = MALF 43A ACTIVE
          3   1 = MALF 43C ACTIVE
          4   1 = MALF 43D ACTIVE
          5   1 = INJECTOR FAULT DETECTED THIS RUN CYCLE
          6   1 = FEDS ENABLED
          7   1 = RESET OCCURRED THIS RUN CYCLE

 15      MALFFW11    LOGGED MALF FLAG WORD 11
          0   CODE 94  TRANS MANUAL LAMP CKT
          1   CODE 93  SERVICE VEHICLE SOON LAMP CKT
          2   CODE 92  NORM/PERF LAMP CKT
          3   CODE 91  1-4 LAMP CKT
          4   CODE 90  TCC SOLENOID CKT
          5   CODE 89  NOT USED
          6   CODE 88  NOT USED
          7   CODE 87  NOT USED

 16      PRNDLFLG    RANGE INDICATION
          0   1 = LOW
          1   1 = DRIVE 2
          2   1 = DRIVE 3
          3   1 = DRIVE 4
          4   1 = NOT USED
          5   1 = REVERSE
          6   1 = PARK/NEUTRAL
          7   1 = INVALID

 17      SDCYLID     CYLINDER ID     (LOWER BYTE)
                      N = CYLINDER ID
 18      NEWRFPRT    PRESENT MINOR LOOP REFERENCE PERIOD (MSB)
 19      NEWRFPRT+1  PRESENT MINOR LOOP REFERENCE PERIOD (LSB)
                      RPM = 2949120/N
                      MSECS = N * .005078
 20      GP6ERPMC    COEFFICIENT OF VARIATION OF RPM
                      N = % * 10.24
 21      ISESDD      DESIRED IDLE SPEED
                      N = RPM / 12.5
 22      NTRPMX      RPM VARIABLE SCALED 25 RPM / BIT
                      N = RPM / 25
 23      COOLDEGR    RAW LINEARIZED COOLANT TEMPERATURE
                      DEG C = .75N - 40
                      DEG F = 1.35N - 40
 24      OILDEG      LINEARIZED OIL TEMPERATURE TERM
                      DEGC = .8N - 40
                      DEG F = 1.44N - 40
 25      MATDEGND    NON-DEFAULTED MAT VARIABLE
                      DEG C = .75N - 40
                      DEG F = 1.35N - 40
 26      NOT USED
 27      ADACPRES    A/D RESULT FROM A/C PRESSURE TRANSDUCER
                      VOLTS = 5N/255
                      PSI = 1.833N  - 14.95
 28      ADMAP       A/D RESULT FROM MANIFOLD PRES. SENSOR INPUT
                      VOLTS = 5N/255
                      (kpa = (N + 28.06)/2.71)
 29      ADTHROTT    A/D RESULT FROM TPS INPUT
                      VOLTS = 5N/255
 30      NTPSLDT     THROTTLE POSITION LOAD AXIS VARIABLE
                      % TPS = N/2.55
 31      ADIGNVLT    A/D RESULT FROM IGNITION VOLTAGE INPUT
                      VOLTS = N/10
 32      NVADBARO    NON-VOLATILE COMPUTED A/D BARO
                      VOLTS = 5N/255
                      (kpa = (N + 28.06)/2.71)
 33      ADLO2RAW    RAW A/D COUNTS FROM LEFT O2 SENSOR (EECC)
                      mV = 4.44N
 34      ADRO2RAW    RAW A/D COUNTS FROM RIGHT O2 SENSOR (EECC
                      mV = 4.44N
 35      NOT USED
 36      ADDO2B      A/D RESULT FROM DIAG O2 B (RIGHT) INPUT
                      mV = 4.44N
 37      BLMCELL     BLOCK LEARN MULTIPLIER CELL NUMBER
                      N = CELL
 38      LBLM        LEFT BANK BLOCK LEARN MULTIPLIER
                      N = COUNTS
 39      RBLM        RIGHT BANK BLOCK LEARN MULTIPLIER
                      N = COUNTS
 40      LCORRCL     CLOSED LOOP CORRECTION FOR LEFT O2 SENSOR
                      N = COUNTS
 41      RCORRCL     CLOSED LOOP CORRECTION FOR RIGHT O2 SENSOR
                      N = COUNTS
 42      GP6EBPWL    GMP6-E LEFT BASE PULSE WIDTH (MSB)
 43      GP6EBPWL+1  GMP6-E LEFT BASE PULSE WIDTH (LSB)
                      MSEC = N/65.536
 44      GP6EBPWR    GMP6-E RIGHT BASE PULSE WIDTH (MSB)
 45      GP6EBPWR+1  GMP6-E RIGHT BASE PULSE WIDTH (LSB)
                      MSEC = N/65.536
 46      GP6EAFND    GMP6-E NON-DEFAULTED AIRFLOW (MSB)
 47      GP6EAFND+1  GMP6-E NON-DEFAULTED AIRFLOW (LSB)
                      GM/SEC = 512N/65536
 48      CCPDC       OUTPUT DUTY CYCLE FOR CCP
                      %DC = N/2.55
 49      ISSPMP      IAC PRESENT MOTOR POSITION
                      MOTOR POSITION = N
 50      ISMNMPKA    KEEP-ALIVE IAC MINIMUM MOTOR POSITION
                      KA MINIMUM MOTOR POSITION = N
 51      GP6ESPKO    SPARK OUTPUT
                      DEGREES = N
 52      GP6ENOCK    KNOCK RETARD
                      DEGREES = N/16
 53      GP6EP2CT    UP INTEGRATED KNOCK SENSOR INPUT (MSB)
 54      GP6EP2CT+1  UP INTEGRATED KNOCK SENSOR INPUT (LSB)
                      N = ESC COUNTS
 55      NOT USED
 56      GP6TEGR     EGR DUTY CYCLE
                      %DC = N/2.55
 57      MALFFW12    LOGGED MALF FLAG WORD 12
          0   CODE 99  TACH OUTPUT CKT FAULT
          1   CODE 98  TORQUE DELIVERED CKT FAULT
          2   CODE 97  4K PULSES CKT FAULT (VSS)
          3   CODE 96  OIL LEVEL LAMP CKT FAULT
          4   CODE 95  OIL LIFE LAMP CKT FAULT
          5   CODE 60  NOT USED
          6   CODE 40  NOT USED
          7   CODE 30  NOT USED

 58      MPH         VEHICLE SPEED
                      MPH = N
 59      TIME        ENGINE RUN TIME (MSB)
 60      TIME+1      ENGINE RUN TIME (LSB)
                      SECONDS = N
..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 46
..HEAD04L ALDL MODE 1 MESSAGE 1 DATA LIST
WORD #   DATA NAME   DESCRIPTION
 1       MALFFW7     MALF FLAGWORD #7
          0   CODE 57  NOT USED
          1   CODE 56  NOT USED
          2   CODE 49  NOT USED
          3   CODE 34  MAP SENSOR LOW
          4   CODE 33  MAP SENSOR HIGH
          5   CODE 39  NOT USED
          6   CODE 35  NOT USED
          7   CODE 24  OUTPUT SPEED LOW

 2       MALFFW8     MALF FLAGWORD #8
          0   CODE 53  SYSTEM VOLTAGE HIGH
          1   CODE 51  PROM/FLASH ERROR
          2   CODE 38  BRAKE SWITCH STUCK OFF
          3   CODE 37  BRAKE SWITCH STUCK ON
          4   CODE 22  THROTTLE POSITION LOW
          5   CODE 21  THROTTLE POSITION HIGH
          6   CODE 15  COOLANT TEMPERATURE LOW
          7   CODE 14  COOLANT TEMPERATURE HIGH

 3       MALFFW9     MALF FLAGWORD #9
          0   CODE 76  LONG SYSTEM VOLTAGE HIGH
          1   CODE 75  SYSTEM VOLTAGE LOW
          2   CODE 74  ASR ACTIVE FAULT
          3   CODE 73  FORCE MOTOR CURRENT
          4   CODE 72  OUTPUT SPEED LOSS
          5   CODE 59  TRANSMISSION TEMPERATURE LOW
          6   CODE 58  TRANSMISSION TEMPERATURE HIGH
          7   CODE 28  PRESSURE SWITCH MANIFOLD

 4       MALFFW10    MALF FLAGWORD #10
          0   CODE 86  LOW RATIO
          1   CODE 85  TCC STUCK ON
          2   CODE 84  3-2 DOWNSHIFT FEEDBACK FAULT (ODM)
          3   CODE 83  TCC CONTROL FEEDBACK FAULT (ODM)
          4   CODE 82  SHIFT A SOLENOID FAULT (ODM)
          5   CODE 81  SHIFT B SOLENOID FAULT (ODM)
          6   CODE 80  TRANSMISSION COMPONENT SLIPPING
          7   CODE 79  TRANSMISSION OVER TEMPERATURE

 5       MALFFW11    MALF FLAGWORD #11
          0   CODE 94  TRANS MANUAL LIGHT FAULT (ODM)
          1   CODE 93  SERVICE VEH. SOON LIGHT FAULT (ODM)
          2   CODE 92  TRANS PERF LIGHT FAULT (ODM)
          3   CODE 91  NOT USED
          4   CODE 90  TCC ENABLE FAULT (ODM)
          5   CODE 89  MAX ADAPT AND LONG SHIFT
          6   CODE 88  NOT USED
          7   CODE 87  HIGH RATIO

 6       ADTHROT     A/D RESULT FROM TPS INPUT
                      VOLTS = 5N/255
 7       NDTHRPOS    CURRENT NON-DEFAULTED POSITION OF THROTTLE
                      N = A/D COUNTS
 8       NE          ENGINE SPEED (FILTERED) MSB
 9       NE+1        ENGINE SPEED (FILTERED) LSB
                      RPM = N/8
 10      VEHSPEED    VEHICLE SPEED (FILTERED)
                      MPH = N/2
 11      PRESSURE    CURRENT TORQUE SIGNAL PRESSURE
                      PSI = N
 12      CURRENT     REFERENCE CURRENT FORCE MOTOR CIRCUIT
                      AMPS = N/51.2
 13      CURRACT     ACTUAL CURRENT SAMPLED FROM A/D
                      AMPS = N/51.2
 14      FMDC        FORCE MOTOR DUTY CYCLE
                      % = N/2.55
 15      PRNDLFLG    RANGE FLAGWORD
          0   1 = LOW GEAR
          1   1 = DRIVE 2
          2   1 = DRIVE 3
          3   1 = DRIVE 4
          4   1 = NOT USED
          5   1 = REVERSE
          6   1 = PARK/NEUTRAL
          7   1 = ILLEGAL RANGE
 16      ADBAT       TRANSMISSION IGNITION VOLTAGE VARIABLE
                      VOLTS = N/10
 17      GEAR        CURRENT COMMANDED GEAR OF TRANSMISSION
                      GEAR = N + 1
 18      CURADPT     CURRENT ADAPTIVE MODIFIER
                      PSI = N
 19      CURCELL     CURRENT ADAPTIVE MODIFIER INDEX WITHIN TABLE
                      N = CELL
 20      ERROR12     ERROR BETWEEN DESIRED AND ACTUAL SHIFT TIMES FOR LATEST
                      SECONDS = N/40
 21      ERROR23     ERROR BETWEEN DESIRED AND ACTUAL SHIFT TIMES FOR LATEST
                      SECONDS = N/40
 22      SLIP        ABSOLUTE VALUE OF SLIP (MSB)
 23      SLIP+1      ABSOLUTE VALUE OF SLIP (LSB)
                      RPM = N/8    (SIGNED)
 24      TIME12      TIME OF LATEST 1-2 UPSHIFT
                      SECONDS = N/40
 25      TIME23      TIME OF LATEST 2-3 UPSHIFT
                      SECONDS = N/40
 26      PROMIDB     PROM ID FOR TRANSMISSION (MSB)
 27      PROMIDB+1   PROM ID FOR TRANSMISSION (LSB)
                      ID = N
 28      DSSDC       3-2 PWM SOL.% DUTY CYCLE
                      %DC = N/2.55
 29      MPH         1 MPH/BIT ROAD SPEED VARIABLE
                      MPH = N
 30      NORAWA      RAW OUTPUT SPEED (MSB)
 31      NORAWA+1    RAW OUTPUT SPEED (LSB)
                      RPM = N/8
 32      CLDEGFLT    COOLANT VARIABLE, FILTERED - ENGINE
                      DEG C = .75N - 40
                      DEG F = 1.35N - 40
 33      TRANDEGA    NORMALIZED TRANSMISSION FLUID TEMPERATURE
                      DEG C = .75N - 40
                      DEG F = 1.35N - 40
 34      TCCDC       TCC PWM SOLENOID DUTY CYCLE (MSB)
 35      TCCDC+1     TCC PWM SOLENOID DUTY CYCLE (LSB)
                      %DC = (256MSB + LSB)/655.36
 36      SDINMW1     INPUT MODE WORD 1
          0   A/C CLUTCH STATUS
          1   A/C REQUEST
          2   NOT USED
          3   NOT USED
          4   NOT USED
          5   NOT USED
          6   PARK/NEUTRAL SWITCH
          7   CRUISE ACTIVE
 37      SDINMW2     INPUT MODE WORD 2
          0   TCC BRAKE SWITCH
          1   NOT USED
          2   NOT USED
          3   TRANSMISSION MODE A
          4   TRANSMISSION MODE B
          5   TRANSMISSION MODE C
          6   SPARK RETARD REQUEST
          7   ASR ACTIVE
 38      SDOUTMW1    OUTPUT MODE WORD 1
          0   TCC CONTROL
          1   TCC ENABLE
          2   SHIFT A
          3   SHIFT B
          4   NOT USED
          5   NOT USED
          6   NOT USED
          7   NOT USED
 39      SDSTMW1     STATUS MODE WORD 1
          0   1 = ENGINE CLOSED LOOP
          1   1 = LEFT O2 READY
          2   1 = RIGHT O2 READY
          3   1 = LEARN ENABLED
          4   NOT USED
          5   1 = CATALYTIC CONVERTER OVERTEMP
          6   NOT USED
          7   NOT USED
 40      SDSTMW2     STATUS MODE WORD 2
          0   1 = POWER ENRICHMENT ACTIVE
          1   1 = KICKDOWN PATTERN
          2   1 = MALF 43A ACTIVE
          3   1 = MALF 43C ACTIVE
          4   1 = MALF 43D ACTIVE
          5   1 = INJECTOR FAULT DETECTED THIS RUN CYCLE
          6   1 = FEDS ENABLED
          7   1 = RESET OCCURRED THIS RUN CYCLE
 41      SDTCCOFF    SERIAL DATA TCCOFF MODE WORD
          0   1 = RANGE CONTINGENCY
          1   1 = MIN TPS CONTINGENCY
          2   1 = BRAKE ON, TCC OFF
          3   1 = NEGATIVE DELTA TPS
          4   1 = TCC SLIP CONTINGENCY
          5   1 = A/C ON CONTINGENCY
          6   1 = TCC ENGAGED
          7   NOT USED

 42      SDADPTBL    SERIAL DATA ADAPTABLE SHIFT MW
          0   1 = NOT IN NORMAL MODE
          1   1 = LAST WAS STANDARD ADAPT
          2   1 = LONG SHIFT DELAY
          3   1 = LONG SHIFT TIME
          4   1 = NOT WITHIN TPS RANGE
          5   1 = EXCESSIVE DELTA TPS
          6   1 = IN HOT MODE
          7   1 = EXCESSIVE DELTA VEHICLE SPEED

 43      NOT USED
 44      MISCSTAT    MISC STATUS BITS
          0   1 = START OF SHIFT
          1   1 = END OF SHIFT
          2   1 = POWERTRAIN IN MOTION
          3   1 = IGNITION OFF
          4   NOT USED
          5   NOT USED
          6   NOT USED
          7   NOT USED

 45      ODMTRNOP    OPEN CIRCUIT STATUS
          0   1 = TCC CONTROL
          1   1 = TCC ENABLE
          2   1 = SHIFT A SOLENOID
          3   1 = SHIFT B SOLENOID
          4   1 = 3-2 DSS SOLENOID
          5   NOT USED
          6   NOT USED
          7   NOT USED

 46      ODMTRNSH    SHORT CIRCUIT STATUS
          0   1 = TCC CONTROL
          1   1 = TCC ENABLE
          2   1 = SHIFT A SOLENOID
          3   1 = SHIFT B SOLENOID
          4   1 = 3-2 DSS SOLENOID
          5   NOT USED
          6   NOT USED
          7   NOT USED
..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 53
..HEAD04L ALDL MODE 1 MESSAGE 2 DATA LIST
WORD #   DATA NAME   DESCRIPTION
 1       NOT USED
 2       NEWMLF2     NEW MALF FLAG WORD 2
          0   CODE 27  EGR ELECTRICAL FAULT (ODM)
          1   CODE 26  CCP ELECTRICAL FAULT (ODM)
          2   CODE 25  MAT SENSOR HIGH
          3   CODE 23  MAT SENSOR LOW
          4   CODE 16  LO-RES FAILURE
          5   CODE 13  LEFT O2 SENSOR FAILED
          6   CODE 12  NO REFERENCE PULSES
          7   CODE 11  MALF INDICATOR LAMP (MIL) FAULT
 3       NEWMLF3     NEW MALF FLAG WORD 3
          0   CODE 43  ESC FAILURE
          1   CODE 42  EST GROUNDED
          2   CODE 41  EST OPEN
          3   CODE 36  HI-RES FAILURE
          4   CODE 48  MASS AIR FLOW SYSTEM FAILURE
          5   CODE 47  NOT USED
          6   CODE 32  EGR SYSTEM FAULT
          7   CODE 29  EAS ELECTRICAL FAULT (ODM)
 4       NEWMLF4     NEW MALF FLAG WORD 4
          0   CODE 61  A/C LOW CHARGE
          1   CODE 55  FUEL SYSTEM LEAN
          2   CODE 54  NOT USED
          3   CODE 52  OIL TEMPERATURE LOW
          4   CODE 50  SYSTEM VOLTAGE LOW
          5   CODE 46  FUEL ENABLE FAILURE
          6   CODE 45  LEFT O2 SENSOR RICH
          7   CODE 44  LEFT O2 SENSOR LEAN
 5       NEWMLF5     NEW MALF FLAG WORD 5
          0   CODE 69  A/C CLUTCH CIRCUIT OPEN
          1   CODE 68  A/C RELAY SHORTED
          2   CODE 67  A/C PRESSURE TRANSDUCER DEGRADED
          3   CODE 66  A/C PRESSURE TRANSDUCER OPEN/SHORT
          4   CODE 65  RIGHT O2 SENSOR RICH
          5   CODE 64  RIGHT O2 SENSOR LEAN
          6   CODE 63  RIGHT O2 SENSOR FAILED
          7   CODE 62  OIL TEMPERATURE HIGH
 6       NEWMLF6     NEW MALF FLAG WORD 6
          0   CODE 78  FAN 2 FAULT (ODM)
          1   CODE 77  FAN 1 FAULT (ODM)
          2   CODE 71  A/C EVAPORATOR TEMP SENSOR FAILED
          3   CODE 70  A/C CLUTCH RELAY FAULT (ODM)
          4   CODE 31  NOT USED
          5   CODE 19  NOT USED
          6   CODE 18  NOT USED
          7   CODE 17  NOT USED
 7       NOT USED
 8       NOT USED
 9       NOT USED
 10      NOT USED
 11      NOT USED
 12      NOT USED
 13      NOT USED
 14      MALFFW2     LOGGED MALF FLAG WORD 2
          0   CODE 27  EGR ELECTRICAL FAULT (ODM)
          1   CODE 26  CCP ELECTRICAL FAULT (ODM)
          2   CODE 25  MAT SENSOR HIGH
          3   CODE 23  MAT SENSOR LOW
          4   CODE 16  LO-RES FAILURE
          5   CODE 13  LEFT O2 SENSOR FAILED
          6   CODE 12  NO REFERENCE PULSES
          7   CODE 11  MALF INDICATOR LAMP (MIL) FAULT
 15      MALFFW3     LOGGED MALF FLAG WORD 3
          0   CODE 43  ESC FAILURE
          1   CODE 42  EST GROUNDED
          2   CODE 41  EST OPEN
          3   CODE 36  HI-RES FAILURE
          4   CODE 48  MASS AIR FLOW SYSTEM FAILURE
          5   CODE 47  NOT USED
          6   CODE 32  EGR SYSTEM FAULT
          7   CODE 29  EAS ELECTRICAL FAULT (ODM)
 16      MALFFW4     LOGGED MALF FLAG WORD 4
          0   CODE 61  A/C LOW CHARGE
          1   CODE 55  FUEL SYSTEM LEAN
          2   CODE 54  NOT USED
          3   CODE 52  OIL TEMPERATURE LOW
          4   CODE 50  SYSTEM VOLTAGE LOW
          5   CODE 46  FUEL ENABLE FAILURE
          6   CODE 45  LEFT O2 SENSOR RICH
          7   CODE 44  LEFT O2 SENSOR LEAN
 17      MALFFW5     LOGGED MALF FLAG WORD 5
          0   CODE 69  A/C CLUTCH CIRCUIT OPEN
          1   CODE 68  A/C RELAY SHORTED
          2   CODE 67  A/C PRESSURE TRANSDUCER DEGRADED
          3   CODE 66  A/C PRESSURE TRANSDUCER OPEN/SHORT
          4   CODE 65  RIGHT O2 SENSOR RICH
          5   CODE 64  RIGHT O2 SENSOR LEAN
          6   CODE 63  RIGHT O2 SENSOR FAILED
          7   CODE 62  OIL TEMPERATURE HIGH
 18      MALFFW6     LOGGED MALF FLAG WORD 6
          0   CODE 78  FAN 2 FAULT (ODM)
          1   CODE 77  FAN 1 FAULT (ODM)
          2   CODE 71  A/C EVAPORATOR TEMP SENSOR FAILED
          3   CODE 70  A/C CLUTCH RELAY FAULT (ODM)
          4   CODE 31  NOT USED
          5   CODE 19  NOT USED
          6   CODE 18  NOT USED
          7   CODE 17  NOT USED
 19      MALFFW7     LOGGED MALF FLAG WORD 7
          0   CODE 57  NOT USED
          1   CODE 56  NOT USED
          2   CODE 49  NOT USED
          3   CODE 34  MAP SENSOR LOW
          4   CODE 33  MAP SENSOR HIGH
          5   CODE 39  NOT USED
          6   CODE 35  NOT USED
          7   CODE 24  OUTPUT SPEED LOW
 20      MALFFW8     LOGGED MALF FLAG WORD 8
          0   CODE 53  SYSTEM VOLTAGE HIGH
          1   CODE 51  PROM/FLASH ERROR
          2   CODE 38  BRAKE SWITCH STUCK OFF
          3   CODE 37  BRAKE SWITCH STUCK ON
          4   CODE 22  THROTTLE POSITION LOW
          5   CODE 21  THROTTLE POSITION HIGH
          6   CODE 15  COOLANT TEMPERATURE LOW
          7   CODE 14  COOLANT TEMPERATURE HIGH
 21      MALFFW9     LOGGED MALF FLAG WORD 9
          0   CODE 76  LONG SYSTEM VOLTAGE HIGH
          1   CODE 75  SYSTEM VOLTAGE LOW
          2   CODE 74  ASR ACTIVE FAULT
          3   CODE 73  FORCE MOTOR CURRENT
          4   CODE 72  OUTPUT SPEED LOSS
          5   CODE 59  TRANSMISSION TEMPERATURE LOW
          6   CODE 58  TRANSMISSION TEMPERATURE HIGH
          7   CODE 28  PRESSURE SWITCH MANIFOLD
 22      MALFFW10    LOGGED MALF FLAG WORD 10
          0   CODE 86  LOW RATIO
          1   CODE 85  TCC STUCK ON
          2   CODE 84  3-2 DOWNSHIFT FEEDBACK FAULT (ODM)
          3   CODE 83  TCC CONTROL FEEDBACK FAULT (ODM)
          4   CODE 82  SHIFT A SOLENOID FAULT (ODM)
          5   CODE 81  SHIFT B SOLENOID FAULT (ODM)
          6   CODE 80  TRANSMISSION COMPONENT SLIPPING
          7   CODE 79  TRANSMISSION OVER TEMPERATURE
 23      MALFFW11    LOGGED MALF FLAG WORD 11
          0   CODE 94  TRANS MANUAL LIGHT FAULT (ODM)
          1   CODE 93  SERVICE VEH. SOON LIGHT FAULT (ODM)
          2   CODE 92  TRANS PERF LIGHT FAULT (ODM)
          3   CODE 91  NOT USED
          4   CODE 90  TCC ENABLE FAULT (ODM)
          5   CODE 89  MAX ADAPT AND LONG SHIFT
          6   CODE 88  NOT USED
          7   CODE 87  HIGH RATIO
 24      MALFFW12    LOGGED MALF FLAG WORD 12
          0   CODE 99  TACH OUTPUT FAULT (ODM)
          1   CODE 98  TORQUE DELIVERED FAULT (ODM)
          2   CODE 97  4K PULSES PER MILE FAULT (ODM)
          3   CODE 96  OIL LEVEL LIGHT FAULT (ODM)
          4   CODE 95  OIL LIFE LIGHT FAULT (ODM)
          5   CODE 60  NOT USED
          6   CODE 40  NOT USED
          7   CODE 30  NOT USED
 25      NVRATIO     RATIO OF ENGINE SPEED TO VEHICLE SPEED
                      N = RATIO
 26      NEWRFPRT    PRESENT MINOR LOOP REFERENCE PERIOD (MSB)
 27      NEWRFPRT+1  PRESENT MINOR LOOP REFERENCE PERIOD (LSB)
                      RPM = 2949120/N
 28      SDINMW2     INPUT MODE WORD 2
          0   TCC BRAKE SWITCH
          1   NOT USED
          2   NOT USED
          3   TRANSMISSION MODE A
          4   TRANSMISSION MODE B
          5   TRANSMISSION MODE C
          6   SPARK RETARD REQUEST
          7   ASR ACTIVE
 29      PRNDLFLG    PRNDL POSITION
          0   1 = LOW GEAR
          1   1 = DRIVE 2
          2   1 = DRIVE 3
          3   1 = DRIVE 4
          4   1 = NOT USED
          5   1 = REVERSE
          6   1 = PARK/NEUTRAL
          7   1 = ILLEGAL RANGE
 30      ODM1OPFL    ODM1 OPEN FAULT WORD
          0   1 = FAN 1 OPEN FAILURE
          1   1 = FAN 2 OPEN FAILURE
          2   1 = TACH OUTPUT OPEN FAILURE
          3   1 = TORQUE AVAILABLE OPEN FAILURE
          4   1 = EGR 1 OPEN FAILURE
          5   1 = ELECTRIC AIR SWITCH OPEN FAILURE
          6   1 = TRANSMISSION PERFORMANCE LIGHT OPEN FAILURE
          7   1 = ODM 1 OVER VOLTAGE FAILURE

 31      ODM1SHFL    ODM1 SHORT FAULT WORD
          0   1 = FAN 1 SHORT FAILURE
          1   1 = FAN 2 SHORT FAILURE
          2   1 = TACH OUTPUT SHORT FAILURE
          3   1 = TORQUE AVAILABLE SHORT FAILURE
          4   1 = EGR 1 SHORT FAILURE
          5   1 = ELECTRIC AIR SWITCH SHORT FAILURE
          6   1 = TRANSMISSION PERFORMANCE LIGHT SHORT FAILURE
          7   1 = ODM 1 OVER TEMPERATURE FAILURE

 32      ODM2OPFL    ODM2 OPEN FAULT WORD
          0   1 = CHECK TRANSMISSION LIGHT OPEN FAILURE
          1   1 = 4K PULSES/MILE OPEN FAILURE
          2   1 = OIL LEVEL OPEN FAILURE
          3   1 = TRANSMISSION MANUAL LIGHT OPEN FAILURE
          4   1 = SHIFT A OPEN FAILURE
          5   1 = SHIFT B OPEN FAILURE
          6   1 = 3-2 SHIFT SOLENOID/C.A.R.S. OPEN FAILURE
          7   1 = ODM 2 OVER VOLTAGE FAILURE

 33      ODM2SHFL    ODM2 SHORT FAULT WORD
          0   1 = CHECK TRANSMISSION LIGHT SHORT FAILURE
          1   1 = 4K PULSES/MILE SHORT FAILURE
          2   1 = OIL LEVEL SHORT FAILURE
          3   1 = TRANSMISSION MANUAL LIGHT SHORT FAILURE
          4   1 = SHIFT A SHORT FAILURE
          5   1 = SHIFT B SHORT FAILURE
          6   1 = 3-2 SHIFT SOLENOID/C.A.R.S. SHORT FAILURE
          7   1 = ODM 2 OVER TEMPERATURE FAILURE

 34      ODM3OPFL    ODM3 OPEN FAULT WORD
          0   1 = CHECK ENGINE LIGHT (MIL) OPEN FAILURE
          1   1 = A/C CLUTCH OPEN FAILURE
          2   1 = OIL LIFE OPEN FAILURE
          3   1 = NOT USED
          4   1 = CCP OPEN FAILURE
          5   1 = TCC ENABLE SOLENOID OPEN FAILURE
          6   1 = TCC CONTROL SOLENOID OPEN FAILURE
          7   1 = ODM 3 OVER VOLTAGE FAILURE

 35      ODM3SHFL    ODM3 SHORT FAULT WORD
          0   1 = CHECK ENGINE LIGHT (MIL) SHORT FAILURE
          1   1 = A/C CLUTCH SHORT FAILURE
          2   1 = OIL LIFE SHORT FAILURE
          3   1 = NOT USED
          4   1 = CCP SHORT FAILURE
          5   1 = TCC ENABLE SOLENOID SHORT FAILURE
          6   1 = TCC CONTROL SOLENOID SHORT FAILURE
          7   1 = ODM 3 OVER TEMPERATURE FAILURE

 36      QACTMF01    OBD-II ACTIVE MALF FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
 37      QACTMF02    OBD-II ACTIVE MALF FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
 38      QACTMF03    OBD-II ACTIVE MALF FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
 39      QACTMF04    OBD-II ACTIVE MALF FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
 40      QACTMF05    OBD-II ACTIVE MALF FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
 41      QACTMF06    OBD-II ACTIVE MALF FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
 42      QHSTMF01    OBD-II HISTORY MALF FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
 43      QHSTMF02    OBD-II HISTORY MALF FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
 44      QHSTMF03    OBD-II HISTORY MALF FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
 45      QHSTMF04    OBD-II HISTORY MALF FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
 46      QHSTMF05    OBD-II HISTORY MALF FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
 47      QHSTMF06    OBD-II HISTORY MALF FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
 BYTES 48-53 NOT USED
..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 45
..HEAD04L ALDL MODE 1 MESSAGE 4 DATA LIST
WORD #   DATA NAME   DESCRIPTION
  1-17   VIN         VEHICLE IDENTIFICATION NUMBER
  18-21  ENDMODEL    END MODEL PART NUMBER
  22-37  SIDERAIL    SIDE RAIL NUMBER
  38-41  M1BTPTRN    MODULE 1 BIT PATTERN NUMBER
  42-45  GP6EM2P1    MODULE 2 (GMP6-E) PART NUMBER BYTE
..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 97
..HEAD04L ALDL MODE 1 MESSAGE 5 DATA LIST
WORD #   DATA NAME   DESCRIPTION
  1      QLSTCY01    OBD-II ACTIVE LAST CYCLE FLAG 1    SAME AS ACTIVE OBD II
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  2      QLSTCY02    OBD-II ACTIVE LAST CYCLE FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  3      QLSTCY03    OBD-II ACTIVE LAST CYCLE FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  4      QLSTCY04    OBD-II ACTIVE LAST CYCLE FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  5      QLSTCY05    OBD-II ACTIVE LAST CYCLE FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  6      QLSTCY06    OBD-II ACTIVE LAST CYCLE FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  7      QACTMF01    OBD-II ACTIVE MALF FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  8      QACTMF02    OBD-II ACTIVE MALF FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  9      QACTMF03    OBD-II ACTIVE MALF FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  10     QACTMF04    OBD-II ACTIVE MALF FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  11     QACTMF05    OBD-II ACTIVE MALF FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  12     QACTMF06    OBD-II ACTIVE MALF FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  13     QMILFG01    OBD-II MIL REQUESTED FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  14     QMILFG02    OBD-II MIL REQUESTED FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  15     QMILFG03    OBD-II MIL REQUESTED FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  16     QMILFG04    OBD-II MIL REQUESTED FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  17     QMILFG05    OBD-II MIL REQUESTED FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  18     QMILFG06    OBD-II MIL REQUESTED FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  19     QHSTMF01    OBD-II HISTORY MALF FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  20     QHSTMF02    OBD-II HISTORY MALF FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  21     QHSTMF03    OBD-II HISTORY MALF FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  22     QHSTMF04    OBD-II HISTORY MALF FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  23     QHSTMF05    OBD-II HISTORY MALF FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  24     QHSTMF06    OBD-II HISTORY MALF FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  25     QIMRDY01    OBD-II TEST COMPLETED FLAG 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  26     QIMRDY02    OBD-II TEST COMPLETED FLAG 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  27     QIMRDY03    OBD-II TEST COMPLETED FLAG 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  28     QIMRDY04    OBD-II TEST COMPLETED FLAG 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  29     QIMRDY05    OBD-II TEST COMPLETED FLAG 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  30     QIMRDY06    OBD-II TEST COMPLETED FLAG 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  31     QTRIPCLO    OBD-II TRIP COUNTER 1 - LOW BYTE
  32     QTRIPCHI    OBD-II TRIP COUNTER 1 - HIGH BYTE
  33     QTRIPCLO+1  OBD-II TRIP COUNTER 2 - LOW BYTE
  34     QTRIPCHI+1  OBD-II TRIP COUNTER 2 - HIGH BYTE
  35     QTRIPCLO+2  OBD-II TRIP COUNTER 3 - LOW BYTE
  36     QTRIPCHI+2  OBD-II TRIP COUNTER 3 - HIGH BYTE
  37     QTRIPCLO+3  OBD-II TRIP COUNTER 4 - LOW BYTE
  38     QTRIPCHI+3  OBD-II TRIP COUNTER 4 - HIGH BYTE
  39     QTRIPCLO+4  OBD-II TRIP COUNTER 5 - LOW BYTE
  40     QTRIPCHI+4  OBD-II TRIP COUNTER 5 - HIGH BYTE
  41     QTRIPCLO+5  OBD-II TRIP COUNTER 6 - LOW BYTE
  42     QTRIPCHI+5  OBD-II TRIP COUNTER 6 - HIGH BYTE
  43     QAKYON01    OBD-II FAULT ACTIVE THIS KEY-ON - 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  44     QAKYON02    OBD-II FAULT ACTIVE THIS KEY-ON - 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  45     QAKYON03    OBD-II FAULT ACTIVE THIS KEY-ON - 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  46     QAKYON04    OBD-II FAULT ACTIVE THIS KEY-ON - 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  47     QAKYON05    OBD-II FAULT ACTIVE THIS KEY-ON - 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  48     QAKYON06    OBD-II FAULT ACTIVE THIS KEY-ON - 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  49     QTPASS01    OBD-II TEST PASSED THIS KEY-ON - 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  50     QTPASS02    OBD-II TEST PASSED THIS KEY-ON - 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  51     QTPASS03    OBD-II TEST PASSED THIS KEY-ON - 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  52     QTPASS04    OBD-II TEST PASSED THIS KEY-ON - 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  53     QTPASS05    OBD-II TEST PASSED THIS KEY-ON - 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  54     QTPASS06    OBD-II TEST PASSED THIS KEY-ON - 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  55     NOT USED
  56     NOT USED
  57     NOT USED
  58     NOT USED
  59     QEVRST01    OBD-II CODE LATCHES - 1
          7         P0155       BANK 2 FRT HO2S HEATER CKT
          6         N/A
          5         P0135       BANK 1 HO2S HEATER CKT
          4         P1115       ECT CKT INT HIGH
          3         P1114       ECT CKT INT LOW
          2         P0118       ECT CKT HIGH INPUT
          1         P0117       ECT CKT LOW INPUT
          0         P0116       ECT CKT RANGE/ PERF PROBLEM
  60     QEVRST02    OBD-II CODE LATCHES - 2
          7         N/A
          6         P0153       BANK 2 FRT HO2S SLOW RESPONSE
          5         N/A
          4         P0133       BANK 1 HO2S SLOW RESPONSE
          3         N/A
          2         P0172       BANK 1 FUEL TRIM RICH
          1         P0171       BANK 1 FUEL TRIM LEAN
          0         P0161       BANK 2 REAR HO2S HEATER CKT
  61     QEVRST03    OBD-II CODE LATCHES - 3
          7         P0154       BANK 2 FRT HO2S CKT NOT ACTIVE
          6         P0134       BANK 1 HO2S CKT NOT ACTIVE
          5         P0151       BANK 2 FRT HO2S CKT LEAN
          4         P0131       BANK 1 HO2S CKT LEAN
          3         N/A
          2         P1153       BANK 2 FRT HO2S SWITCHING FLT
          1         N/A
          0         P1133       BANK 1 HO2S SWITCHING FLT
  62     QEVRST04    OBD-II CODE LATCHES - 4
          7         P0158       BANK 2 REAR HO2S CKT HIGH VOLT
          6         N/A
          5         P0160       BANK 2 REAR HO2S CKT NOT ACTIVE
          4         N/A
          3         N/A
          2         N/A
          1         P0152       BANK 2 FRT HO2S CKT RICH
          0         P0132       BANK 1 HO2S CKT RICH
  63     QEVRST05    OBD-II CODE LATCHES - 5
          7         P0420       BANK 2 CATALYST SYSTEM FAULT
          6         N/A
          5         N/A
          4         N/A
          3         P1158       BANK 2 REAR HO2S SHIFTED RICH
          2         N/A
          1         N/A
          0         N/A
  64     QEVRST06    OBD-II CODE LATCHES - 6
          7         N/A
          6         N/A
          5         N/A
          4         N/A
          3         N/A
          2         N/A
          1         P0175       BANK 2 FRT FUEL TRIM RICH
          0         P0174       BANK 2 FRT FUEL TRIM LEAN
  65     QCATPASS    OBD-II # OF CATALYST MONITOR PASSES
  66     QCATPASS+1
  67     QCATFAIL    OBD-II # OF CATALYST MONITOR FAILS
  68     QCATFAIL+1
  69     QO2H1FAL    OBD-II # OF O2 HEATER FAILS - R1
  70     QO2H1FAL+1
  71     QO2H2FAL    OBD-II # OF O2 HEATER FAILS - R2
  72     QO2H2FAL+1
  73     QO2R1FAL    OBD-II # OF O2 RESPONSE FAILS - R1
  74     QO2R1FAL+1
  75     QO2S1FAL    OBD-II # OF O2 SWITCH FAILS - R1
  76     QO2S1FAL+1
  77     QO2L1FAL    OBD-II # OF O2 LEAN FAILS - R1
  78     QO2L1FAL+1
  79     QO2I1FAL    OBD-II # OF O2 INACTIVE FAILS - R1
  80     QO2I1FAL+1
  81     QO2RCFAL    OBD-II # OF O2 RICH FAILS - R1
  82     QO2RCFAL+1
  83     QO2G1FAL    OBD-II # OF O2 GROUNDED FAILS - R1
  84     QO2G1FAL+1
  85     QO2I2FAL    OBD-II # OF O2 INACTIVE FAILS - R2
  86     QO2I2FAL+1
  87     QO2SHFAL    OBD-II # OF O2 SHORT HI FAILS - R2
  88     QO2SHFAL+1
  89     QO2SLFAL    OBD-II # OF O2 SHIFT LEAN FAILS-R2
  90     QO2SLFAL+1
  91     QO2SRFAL    OBD-II # OF O2 SHIFT RICH FAILS-R2
  92     QO2SRFAL+1
  93     DEVDIFOL    OBD-II MAX VALUE OF CATALYST EWMA
  94     QDOBLM10    BANK 1 ADAPTIVE SUM
  95     QDOBLM10+1
  96     QDOBLM20    BANK 2 ADAPTIVE SUM
  97     QDOBLM20+1
..PAGE
..HEAD02L ALDL DATA LIST
..HEAD03L NUMBER OF DATA WORDS - 38
..HEAD04L ALDL MODE 1 MESSAGE 6 DATA LIST
WORD #   DATA NAME   DESCRIPTION
  1      EADPT2      PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      NOT USED
  2      EADPT2+1    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      NOT USED
  3      EADPT2+2    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      NOT USED
  4      EADPT2+3    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      NOT USED
  5      EADPT2+4    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  6      EADPT2+5    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  7      EADPT2+6    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  8      EADPT2+7    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  9      EADPT2+8    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  10     EADPT2+9    PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  11     EADPT2+10   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  12     EADPT2+11   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  13     EADPT2+12   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  14     EADPT2+13   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  15     EADPT2+14   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  16     EADPT2+15   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  17     EADPT2+16   PRESSURE MODIFIER (ADAPTIVE) - 2ND GEAR
                      PSI = (N*.125)-16
  18     EADPT3      PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  19     EADPT3+1    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  20     EADPT3+2    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  21     EADPT3+3    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  22     EADPT3+4    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  23     EADPT3+5    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  24     EADPT3+6    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  25     EADPT3+7    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  26     EADPT3+8    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  27     EADPT3+9    PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  28     EADPT3+10   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  29     EADPT3+11   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  30     EADPT3+12   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  31     EADPT3+13   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  32     EADPT3+14   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  33     EADPT3+15   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  34     EADPT3+16   PRESSURE MODIFIER (ADAPTIVE) - 3ND GEAR
                      NOT USED
  35     SDADPTBL
          0      1 = NOT IN NORMAL MODE
          1      1 = LAST WAS STANDARD ADAPT
          2      1 = LONG SHIFT DELAY
          3      1 = LONG SHIFT TIME
          4      1 = NOT WITHIN TPS RANGE
          5      1 = EXCESSIVE DELTA TPS
          6      1 = IN HOT MODE
          7      1 = EXCESSIVE DELTA VEHICLE SPEED

  36     LSTADEL     LAST CHANGE TO ADAPTIVE MODIFIER
                      NOT USED
  37     CURADPT     CURRENT ADAPTIVE MODIFIER
                    PSI = (N*.125)-16
  38     CURCELL     CURRENT ADAPTIVE MODIFIER INDEX WITHIN TABLE
                      N = CELL
