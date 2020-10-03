# Put the heathkit ROMs into the image at the proper locations.
# The second half of the Basic ROM actually goes up front.
# The last (None,0) is probably unnecessary.

rom_map = [("roms/ETA-3400_ROM_U106.bin", 1),
           ("roms/ETA-3400_ROM_U105.bin", 0),
           ("roms/ETA-3400_ROM_U105.bin", 1),
           ("roms/ETA-3400_ROM_U106.bin", 0),
           (None, 0)]

image = ""
for rom_part in rom_map:
    (fn, blk) = rom_part
    if (fn == None):
        for i in range(0,1024):
            image = image + chr(0)
    else:
        indata = open(fn, "rb").read()
        image = image + indata[(blk*1024):((blk*1024)+1024)]

open("roms/combined.bin", "wb").write(image)



