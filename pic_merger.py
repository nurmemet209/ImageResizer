import os

from PIL import Image, ImageFont


class ImageMerger():
    def __init__(self):
        self.font = ImageFont.truetype("font\\simhei.ttf", 18)

    def merge(self, src_img_path, des_width, des_height=None):
        if os.path.exists(src_img_path) is False:
            print("图片不存在", src_img_path)
            return
        src_im = Image.open(src_img_path)
        orate = src_im.width / src_im.height;
        width = des_width;
        height = des_height;
        if des_height is None:
            height = width / orate;
            height = int(height)
        # print(width, height)
        if src_im.width > src_im.height:
            re_width = width
            re_height = re_width / orate;
            re_width = int(re_width)
            re_height = int(re_height)
            src_im = src_im.resize((re_width, re_height), Image.ANTIALIAS)
        else:
            re_height = height;
            re_width = orate * re_height
            re_width = int(re_width)

            src_im = src_im.resize((re_width, re_height), Image.ANTIALIAS)
        # print("调整之后", src_im.width, src_im.height)
        des_im = Image.new('RGB', (width, height), 0xffffff)
        box = self.get_box_pos(width, height, src_im.width, src_im.height)
        # print("粘贴区域",box)
        des_im.paste(src_im, box)
        des_im.save(src_img_path)

    def get_box_pos(self, des_width, des_height, src_width, src_height):
        del_width = des_width - src_width
        del_height = des_height - src_height;
        x1 = del_width / 2;
        y1 = del_height / 2
        x2 = x1 + src_width;
        y2 = y1 + src_height;
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        return (x1, y1, x2, y2)
