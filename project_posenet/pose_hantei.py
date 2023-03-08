import cv2

from pose_engine import PoseEngine
from PIL import Image
from PIL import ImageDraw
from pose_judge import *

import numpy as np
import os

#pil_image = Image.open('/tmp/couple.jpg').convert('RGB')
engine = PoseEngine(
    '/home/io-circle/windowapps/title/project_posenet/models/mobilenet/posenet_mobilenet_v1_075_481_641_quant_decoder_edgetpu.tflite')

# カメラの読込み
# 内蔵カメラがある場合、下記引数の数字を変更する必要あり
cap = cv2.VideoCapture(0)
# 動画終了まで、1フレームずつ読み込んで表示する。
while(cap.isOpened()):
    # 1フレーム毎　読込み
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    poses, inference_time = engine.DetectPosesInImage(Image.fromarray(frame))
    #print('Inference time: %.f ms' % (inference_time * 1000))

    for pose in poses:
        if pose.score < 0.4: continue
        calculate_leftelbow(pose)
        angles = calculate_jointAngles(pose)
        pose_check(pose,angles)
        #print('\nPose Score: ', pose.score)
        #for label, keypoint in pose.keypoints.items():
            #print('  %-20s x=%-4d y=%-4d score=%.1f' %
                #(label.name, keypoint.point[0], keypoint.point[1], keypoint.score))


    # GUIに表示

    # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()