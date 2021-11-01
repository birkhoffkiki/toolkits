import cv2
import os
from lib.segmentation import BinarySegmentation
from lib.easyprocess import EasyProcessing
from PIL import Image
from tqdm import tqdm


def show_img(img1):
    Image.fromarray(img1).show()
def process_image(file):
    img_p = os.path.join(root, file)
    img = cv2.imread(img_p)[..., ::-1]
    mask = bg(img, 'global_threshold')
    # show_img(img)
    # show_img(mask)
    ratio = bg.foreground_ratio(mask)
    if ratio < 0.15:
        bad_samples.append(file)
        p = os.path.join(tmp, file.split('/')[-1])
        cv2.imwrite(p, img[..., ::-1])


if __name__ == '__main__':
    count = 100
    root = '/home/kara/DATA/CytoRefSR/20x'
    tmp = '/mnt/diskarray/mjb/Projects/TEMP/CytorefSR/sparser_images'
    if not os.path.exists(tmp):
        os.makedirs(tmp)
    file_path = '/home/kara/DATA/CytoRefSR/all.txt'
    bad_sample_path = '/home/kara/DATA/CytoRefSR/bad_samples.txt'
    bad_samples = []
    bg = BinarySegmentation(200, 250, background_is_white=True)

    ep = EasyProcessing(8)


    with open(file_path) as f:
        all_files = [line.strip() for line in f]

    ep.apply(process_image, all_files)

    with open(bad_sample_path, 'w') as f:
        f.writelines(bad_samples)


