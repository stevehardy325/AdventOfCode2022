from PIL import Image
import numpy as np

class ImageHandler:
    def __init__(self, outname):
        self.outname = outname
        self.images = []
        self.run_num = 1

    def createSnapshot(self, blocks, rocks, sand):
        rocks_xs = [rock[0] for rock in rocks]
        rocks_ys = [rock[1] for rock in rocks]
        max_x = max(rocks_xs) + 500
        max_y = max(rocks_ys) + 3

        im = Image.new("RGB", (max_x, max_y))
        for blockx, blocky, in blocks:
            im.putpixel((blockx, blocky), (255, 0, 0))
        for rockx, rocky, in rocks:
            im.putpixel((rockx, rocky), (255, 255, 255))
        sandx, sandy = sand
        im.putpixel((sandx, sandy), (255, 255, 0))
        self.images.append(im)
        print(len(self.images))
        if len(self.images) == 1000:
            print('dumping')
            self.outputgif(outname='{:05d}.gif'.format(self.run_num))
            self.images = []
            self.run_num += 1


    def outputgif(self, outname=None):
        if outname is None:
            outname = self.outname
        print('saving to {}'.format(outname))
        self.images[0].save(outname,save_all=True, append_images=self.images[1:], optimize=True, duration=50, loop=0)