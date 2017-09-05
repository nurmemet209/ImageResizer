import os

from pic_merger import ImageMerger


class BatchResize():
    def __init__(self):
        self.main_dir = "C://software//导数据//AllCarRacing"
        self.resizer = ImageMerger()

    def get_file_ex(self, path):
        try:
            return os.path.splitext(path)[1]
        except:
            return None;

    def resize(self):
        file_list = os.listdir(self.main_dir)
        for item in file_list:
            banner_dir = self.main_dir + "//" + item + "//banner"
            banner_imgs = os.listdir(banner_dir)
            for banner_img in banner_imgs:
                banner_img_path = banner_dir + "//" + banner_img;
                if self.get_file_ex(banner_img_path) != ".jpg":
                    continue;
                try:
                    self.resizer.merge(banner_img_path, 1000, 1000)
                except:
                    print("文件错误", banner_img_path)

            showpic_dir = self.main_dir + "//" + item + "//showpic"
            showpic_imgs = os.listdir(showpic_dir)
            for showpic_img in showpic_imgs:
                showpic_img_path = showpic_dir + "//" + showpic_img;

                try:
                    self.resizer.merge(showpic_img_path, 1000)
                except:
                    print("文件错误", showpic_img_path)


resizer = BatchResize()
resizer.resize()
