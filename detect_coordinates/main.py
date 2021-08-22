import os
import numpy as np
import sys
import cv2
from NomeroffNet.YoloV5Detector import Detector
from NomeroffNet.TextDetector import TextDetector

from NomeroffNet import TextDetector
from NomeroffNet import textPostprocessing

# Specify device
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

# NomeroffNet path
NOMEROFF_NET_DIR = os.path.abspath('../')

sys.path.append(NOMEROFF_NET_DIR)

detector = Detector()
detector.load()

imgs = [
    '21_5_2014_7_42_58_269.bmp',
    '21_5_2014_19_16_58_117.bmp'
]
base_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'in',
    'PhotoBaseFull')
img_paths = []
for p in imgs:
    img_paths.append(os.path.join(base_dir, p))

# load models
textDetector = TextDetector.get_static_module("eu")
textDetector.load("latest")

# Detect numberplate
frame_nums = []
xx = []
yy = []

for img_no, img_path in enumerante(img_paths):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    targetBoxes = detector.detect_bbox(img)

    for targetBox in targetBoxes:
        frame_nums.append(img_no)
        xx.append(int(min(targetBox[0], targetBox[2])))
        yy.append(int(min(targetBox[1], targetBox[3])))

result = zip(frame_nums, xx, yy)
