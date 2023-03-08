#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:36:04 2023

@author: io-circle
"""
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw
from pose_engine import KeypointType

import numpy as np
import os

#os.system('wget https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/'
 #         'Hindu_marriage_ceremony_offering.jpg/'
  #        '640px-Hindu_marriage_ceremony_offering.jpg -O /tmp/couple.jpg')
pil_image = Image.open('/tmp/couple.jpg').convert('RGB')
engine = PoseEngine(
    'models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')
poses, inference_time = engine.DetectPosesInImage(pil_image)
print('Inference time: %.f ms' % (inference_time * 1000))

def inner_Calc(x0, x1, x2, y0, y1, y2):
    if all([x0, x1, x2, y0, y1, y2]):
        va = np.array([x1-x0, y1-y0])
        vb = np.array([x2-x0, y2-y0])

        innr = np.inner(va, vb)
        nrm = np.linalg.norm(va)*np.linalg.norm(vb)
        deg = np.rad2deg(np.arccos(np.clip(innr/nrm, -1.0, 1.0)))

    else:
        deg = -1

    return deg

def calculate_jointAngles(pose):
    """
    unti
    """

    angles = []

    # 左ひじの角度
    x1 = pose.keypoints.get(KeypointType.LEFT_WRIST).point.x
    y1 = pose.keypoints.get(KeypointType.LEFT_WRIST).point.y
    x0 = pose.keypoints.get(KeypointType.LEFT_ELBOW).point.x
    y0 = pose.keypoints.get(KeypointType.LEFT_ELBOW).point.y
    x2 = pose.keypoints.get(KeypointType.LEFT_SHOULDER).point.x
    y2 = pose.keypoints.get(KeypointType.LEFT_SHOULDER).point.y

    deg = np.round(inner_Calc(x0, x1, x2, y0, y1, y2))
    print('角度',deg)
    angles.append(deg)
    

for pose in poses:
    if pose.score < 0.4: continue
    calculate_jointAngles(pose)
    print('\nPose Score: ', pose.score)
    for label, keypoint in pose.keypoints.items():
        print('  %-20s x=%-4d y=%-4d score=%.1f' %
              (label.name, keypoint.point[0], keypoint.point[1], keypoint.score))

