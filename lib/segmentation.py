import cv2
from skimage import morphology


class BinarySegmentation:
    supported_methods = ['global_threshold']

    def __init__(self, threshold: int, min_size: int, background_is_white=True):
        self.threshold = threshold
        self.min_size = min_size
        self.background_is_white = background_is_white

    def _global_threshold_segmentation(self, img):
        """
        :param img:
        :return:
        """
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray < self.threshold if self.background_is_white else gray > self.threshold
        mask = morphology.remove_small_objects(mask, min_size=self.min_size, connectivity=1) > 0
        return mask

    @staticmethod
    def foreground_ratio(mask):
        h, w = mask.shape
        total = mask.sum()
        return total/h/w

    def __call__(self, img, seg_method='global_threshold'):
        if seg_method == 'global_threshold':
            mask = self._global_threshold_segmentation(img)
        else:
            print(f'{seg_method} is not supported, current supported methods:{self.supported_methods}')
        return mask




