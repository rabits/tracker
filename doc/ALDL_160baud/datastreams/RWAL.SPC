
                         RWAL.SPC
                         REAR WHEEL ANTI-LOCK BRAKING SYSTEM DATA STREAM

APPLICATIONS FOR LIGHT-DUTY TRUCKS:

              1988-91        C/K
              1989-91        M
              1989-91        S/T
              1990-91        R/V       (EXCEPT 3+3 CREW CAB MODELS)
              1990-94        G
*             1992-95        S/T PICK-UP ONLY
*             1992-95        C/K PICK-UP ONLY

The RWAL Fault codes may be read by monitoring the ALDL Pin H (PIN 12 FOR
 1995 S/T).
This pin does multiple functions, Speed signal to RWAL, diagnostic
code flash enable and diagnostic code readout.

The fault codes are pulsed on the ALDL Pin H. At zero speed this
line will be at B+ volts (battery voltage. The pulses will be 1
to 1.7 volts below B+. The pulse count will correspond to the
fault code, for example; a pulse count of 6 would correspond to
code 6.  The pulse width is approximately 4.0 to 4.5 milliseconds
with and equal space between pulses.  The fault code pulse count
is repeated at 600 millisecond intervals.


RWAL ALDL Pin H voltage test -

1.     Voltage is 8.0 to 16.0
       Voltage is within normal range.

       RWAL tests may proceed.

2.     Voltage is zero -
       This indicates a blown RWAL/DRAC ignition fuse, open in
       RWAL/DRAC igniton circuit, open circuit in speed signal to
       RWAL, short circuit in speed signal to RWAL.

3.     Voltage is low - less than 8.0 volts but not 0.0 -
       This indicates either low battery voltage, a poor connection
       from DRAC speed signal output, or a problem with the
       DRAC.

       Low battery voltage may be checked by looking at ECM voltage,
       however, this will not detect a poor connection or
       DRAC problem.

4.     Voltage is greater than 16.0 volts.
       Charging system is overcharging.

       This condition may be checked by looking at ECM voltage.




In counting code pulses, count the number of short flashes starting from the
long flash.  Include the long flash as a count.  NOTE! Sometimes the first
count sequence is short because the flashout started with the count already in
progress.  Subsequent counts, however, will be accurate.  If there is more than
one failure, only the first recognized failure code will be retained and
flashed.

No. of
Flashes    Failure detected              Probable Correction

1          Not used.                     N/A

2          Open isolation valve,         Ohmeter valve pin for 3.0 -
           wiring or faulty module.      6.0 ohms to ground.

3          Open dump valve wiring or     Ohmeter valve pin for 1.0 -
           faulty module.                3.0 ohms to ground.

4          Closed RWAL valve switch.     Faulty valve or wiring shorted.

5          Over 16 dump pulses           Remove/Replace module power plug
           generated.(This is disabled   to reset. Check out system for pos
           in 4WD).                      sible reasons.

6          Erratic sensor.               DRAC signal is quickly cutting in & out.

7          Internal fuse pellet blown,   Verify 3.0 - 6.0 ohms to ground before
           isolation output missing or   replacing module.
           valve wiring shorted-ground.

8          Dump output missing or valve  Verify 1.0 - 3.0 ohms to ground before
           wiring shorted-ground.        replacing module.

9          DRAC signal missing, wiring   Determine if DRAC signal is missing.
           open or shorted to ground.

10         Open brake wire or switch     Check for battery voltage with
           adjustment off.               ignition on and pedal up.

11         Not used.                     N/A

12         Not used.                     N/A

13         Module phase lock loop fail.  Faulty module.

14         Module program checksum fail. Faulty module.

15         Module RAM fail.              Faulty module.

16         No failure detected.          N/A
