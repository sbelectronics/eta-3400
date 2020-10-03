# Scott's ETA-3400 Memory/IO Accessory Remake
(c) Scott Baker, http://www.smbaker.com/

youtube video: https://www.youtube.com/watch?v=gP17z7haC4o&ab_channel=smbakeryt

## Purpose

The ETA-3400 was a memory/IO accessory for Heathkit's ET-3400 and ET-3400-A trainers. It added a serial port, a cassette port, up to 4K of RAM, and 4K of ROM. The ROM included a terminal monitor that you could use to operate the trainer over serial, as well as a "Tiny Basic" ROM that allowed you to program the trainer in the BASIC programming language.

This project is a remake of that board, using slightly more modern components, but still in the vintage theme of the original.

## Recompiling the ATF16V8

The ATF16V8 is a programmable logic device that implements the IO addressing and some control line manipulation. It's programmed in a languaged called CUPL. You'll need the [WinCUPL tool](https://www.microchip.com/design-centers/fpgas-and-plds/splds-cplds/pld-design-resources) from Microchip in order to recompile the PLD. The desired output is the JED file, which you can program using a programmer such as TL866 with minipro software.

## Burning the ROM

I wrote a small python tool, makerom.py, that loaded the original heathkit ROMs into a 4K rom image (the way they're addressed is a little bit weird, the trainer puts them at 0x1400 to 0x23FF). I used a TL866 with minipro to burn it to a 28C64 EEPROM chip.

You might notice that roms/combined.bin is 5K instead of 4K. That's a mistake (the last 1K is all zeros), but that's also the way it was when I burned my ROM and made my video, so I left it as-is. In the future, I may look into finding a way to load more programs into the remainder of the ROM and make it addressable.

## Setting up the raspberry pi zero

The raspberry pi zero is entirely optional (the board features a RS232 port that can be used with an external terminal), but offers the ability to build a terminal directly into your ETA-3400. Some instructions on setting up the Pi Zero W

```bash
# disable serial console
sudo raspi-config
  5 - interfacing options
    P6 - serial
        No login shell
        Yes serial interface enabled

# install minicom
sudo apt-get -y install minicom
sudo minicom -s
  Port - /dev/serial0
  Baud - 2400
  Bits - 7,E,1
  Flow Control - off

# as an alternative to minicom, picocom can be used
sudo apt-get -y install picocom
picocom /dev/ttyS0 --baud 2400 -p 1 -d 7 -y e
```

## Gerbers

The gerbers are present in the gerbers directory.

* gerbers/v-0.2-initial .. This was my initial order, sent to jlcpcb, to make the boards used in the video.
