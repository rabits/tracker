OBD1 ALDL 160 baud data
=======================

This document is about "How to understand what's happening in raw ALDL 160 baud binary data".

Basing on raw data from the ALDL-USB cable, ADX format file & csv with ALDLDroid parsed protocol we can understand the binary protocol that will help us to write ALDL module for the car computer.

Hardware
--------

* Car - Pontiac Firebird Trans AM V6 3.8L Turbo LC2 - adx format file you can find around. Also datastream for A008 available.
* Cable - I'm using ALDL-USB cable from 1320 Electronics (switch: 0100), but I think any convertor (even DIY) will work - because it's not a big deal to convert ALDL 160 baud pulses to actual UART pulses.

Step 1 - getting the ALDL raw data
----------------------------------

It's really simple. We just need to go inside the ADX file, check the connection settings and write a small python script (check [aldl_get_raw_data.py](aldl_get_raw_data.py)) to write down the binary data:

Now we can connect OBD connector to the car & usb connector to the notebook, run the script and power the car (but do not start the engine now, we need just some data to understand the structure) - and a bunch of fresh data will come to us:
```sh
python -u aldl_get_raw_data.py | tee 01_aldl_raw_data.bin.txt
```
After 10-20 sec you can turn ignition off. ECM will send last couple of packets and when you see new empty lines - stop the script by pressing Ctrl-C.

Check example step output: [01_aldl_raw_data.bin.txt](dump/01_aldl_raw_data.bin.txt)

Step 2 - format the data
------------------------

Ok, now we got some raw data from the car. How to understand it properly? Take a closer look - you should see the data cyclicity. That means it's not just a garbage data.

Format is pretty simple: `SbbbbbbbbSbbbbbbbb...` where **S** is sync bit and **b** is actual frame data bit. Each frame looks like this *(spaces is just to split the control bits)*:
```
1 11111111 0 bbbbbbbb 0 bbbbbbbb 0 bbbbbbbb ...
```

First of all you need to split the data by the SYNC head (`1 11111111`) and you will get a frames with control data.

Check the example step data: [02_splitted_frames.bin.txt](dump/02_splitted_frames.bin.txt)

Step 3 - clean the control bits
-------------------------------

After that you can remove sync header & sync bits from the data and get a frames raw data.

Check the example step data: [03_frames_raw_data.bin.txt](dump/03_frames_raw_data.bin.txt)

Step 4 - split bytes
--------------------

Last step is splitting the bytes and using the ADX xml file format (or any else like for your engine) to get properties offset and required steps & math to extract the data.

Check the example step data: [04_formatted_frames.bin.txt](dump/04_formatted_frames.bin.txt)

Support
-------
If you like this project, you can support our open-source development by a small Bitcoin donation.

Bitcoin wallet: `15phQNwkVs3fXxvxzBkhuhXA2xoKikPfUy`
