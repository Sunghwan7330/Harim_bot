import os
import json

import cv2
import requests
import sys

LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40

def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None

def kakao_ocr_detect(image_path: str, appkey: str):
    """
    detect api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://kapi.kakao.com/v1/vision/text/detect'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()

    return requests.post(API_URL, headers=headers, files={"file": data})

def kakao_ocr_recognize(image_path: str, boxes: list, appkey: str):
    API_URL = 'https://kapi.kakao.com/v1/vision/text/recognize'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()

    return requests.post(API_URL, headers=headers, files={"file": data}, data={"boxes": json.dumps(boxes)})


day_array = ['mon', 'tue', 'wen', 'thu', 'fri']
image_path = "./image_menu"
input_file = '{}_{}_{}.jpg'
name_lunch = 'lunch'

appkey = ""
#image_path = "./image_menu/fri_lunch_a.jpg"


def convert_menu(image_path, output_file):
    """
    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        #print("원본 대신 리사이즈된 이미지를 사용합니다.")
    """

    output = kakao_ocr_detect(image_path, appkey).json()
    #print("[detect] output:\n{}\n".format(output))

    boxes = output["result"]["boxes"]
    boxes = boxes[:min(len(boxes), LIMIT_BOX)]
    output = kakao_ocr_recognize(image_path, boxes, appkey).json()
    #print("[recognize] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2)))
    #print(output["result"])

    f = open(output_file, "w")
    for menu in output["result"]["recognition_words"] :
        print(menu)
        f.write(menu + "\n")
    f.close()
    return

def main():
    filenames = os.listdir(image_path)
    for filename in filenames:
        full_filename = os.path.join(image_path, filename)
        if ".jpg" not in full_filename:
            continue
        output_name = full_filename.replace("jpg", "txt")
        convert_menu(full_filename, output_name)
    return
        
if __name__ == "__main__":
    main()
