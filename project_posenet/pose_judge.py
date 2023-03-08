from pose_engine import KeypointType
import numpy as np
EDGES = (
    (KeypointType.NOSE, KeypointType.LEFT_EYE),
    (KeypointType.NOSE, KeypointType.RIGHT_EYE),
    (KeypointType.NOSE, KeypointType.LEFT_EAR),
    (KeypointType.NOSE, KeypointType.RIGHT_EAR),
    (KeypointType.LEFT_EAR, KeypointType.LEFT_EYE),
    (KeypointType.RIGHT_EAR, KeypointType.RIGHT_EYE),
    (KeypointType.LEFT_EYE, KeypointType.RIGHT_EYE),
    (KeypointType.LEFT_SHOULDER, KeypointType.RIGHT_SHOULDER),
    (KeypointType.LEFT_SHOULDER, KeypointType.LEFT_ELBOW),
    (KeypointType.LEFT_SHOULDER, KeypointType.LEFT_HIP),
    (KeypointType.RIGHT_SHOULDER, KeypointType.RIGHT_ELBOW),
    (KeypointType.RIGHT_SHOULDER, KeypointType.RIGHT_HIP),
    (KeypointType.LEFT_ELBOW, KeypointType.LEFT_WRIST),
    (KeypointType.RIGHT_ELBOW, KeypointType.RIGHT_WRIST),
    (KeypointType.LEFT_HIP, KeypointType.RIGHT_HIP),
    (KeypointType.LEFT_HIP, KeypointType.LEFT_KNEE),
    (KeypointType.RIGHT_HIP, KeypointType.RIGHT_KNEE),
    (KeypointType.LEFT_KNEE, KeypointType.LEFT_ANKLE),
    (KeypointType.RIGHT_KNEE, KeypointType.RIGHT_ANKLE),
)
def calculate_leftelbow(pose):
    #angles = []

    # 左ひじの角度
    x1 = pose.keypoints.get(KeypointType.LEFT_WRIST).point.x
    y1 = pose.keypoints.get(KeypointType.LEFT_WRIST).point.y
    x0 = pose.keypoints.get(KeypointType.LEFT_ELBOW).point.x
    y0 = pose.keypoints.get(KeypointType.LEFT_ELBOW).point.y
    x2 = pose.keypoints.get(KeypointType.LEFT_SHOULDER).point.x
    y2 = pose.keypoints.get(KeypointType.LEFT_SHOULDER).point.y

    deg = np.round(inner_Calc(x0, x1, x2, y0, y1, y2))
    print('角度',deg)
    #angles.append(deg)

def calculate_jointAngles(pose):
    """
    ひじの角度の計算
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
    angles.append(deg)

    # 右ひじの角度
    x1 = pose.keypoints.get(KeypointType.RIGHT_WRIST).point.x
    y1 = pose.keypoints.get(KeypointType.RIGHT_WRIST).point.y
    x0 = pose.keypoints.get(KeypointType.RIGHT_ELBOW).point.x
    y0 = pose.keypoints.get(KeypointType.RIGHT_ELBOW).point.y
    x2 = pose.keypoints.get(KeypointType.RIGHT_SHOULDER).point.x
    y2 = pose.keypoints.get(KeypointType.RIGHT_SHOULDER).point.y

    deg = np.round(inner_Calc(x0, x1, x2, y0, y1, y2))
    angles.append(deg)

    return angles


def inner_Calc(x0, x1, x2, y0, y1, y2):
    """
    内積の計算
    ＊関数呼び出し必要ない

    Parameters
    ----------
    x0 : TYPE
        DESCRIPTION.
    x1 : TYPE
        DESCRIPTION.
    x2 : TYPE
        DESCRIPTION.
    y0 : TYPE
        DESCRIPTION.
    y1 : TYPE
        DESCRIPTION.
    y2 : TYPE
        DESCRIPTION.

    Returns
    -------
    deg : TYPE
        DESCRIPTION.

    """
    
    if all([x0, x1, x2, y0, y1, y2]):
        va = np.array([x1-x0, y1-y0])
        vb = np.array([x2-x0, y2-y0])

        innr = np.inner(va, vb)
        nrm = np.linalg.norm(va)*np.linalg.norm(vb)
        deg = np.rad2deg(np.arccos(np.clip(innr/nrm, -1.0, 1.0)))

    else:
        deg = -1

    return deg
def pose_check(pose, angles):
    """
    ポーズの判定f

    Parameters
    ----------
    pose : TYPE class 'pose_engine.Pose'
        DESCRIPTION.pose informasion keypoint
    angles : TYPE list
        DESCRIPTION.関節の角度

    Returns
    -------
    result : TYPE 文字列
        DESCRIPTION.判定結果

    """
    result = ''
    rHandUp = 0
    lHandUp = 0

    if angles[1] > 120 and pose.keypoints.get(KeypointType.RIGHT_WRIST).point.y < pose.keypoints.get(KeypointType.RIGHT_EYE).point.y:
        rHandUp = 1

    if angles[0] > 120 and pose.keypoints.get(KeypointType.LEFT_WRIST).point.y < pose.keypoints.get(KeypointType.LEFT_EYE).point.y:
        lHandUp = 1

    if rHandUp == 1 and lHandUp == 1:
        result = 'BANZAI'
        print(result)
    elif rHandUp == 1:
        result = 'RIGHT HAD UP'
        print(result)
    elif lHandUp == 1:
        result = 'LEFT HAD UP'
        print(result)

    return result