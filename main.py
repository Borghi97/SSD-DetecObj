import cv2
import os
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Crie um diretório para armazenar as capturas de tela, caso não exista
directory = 'screenshots'
if not os.path.exists(directory):
    os.makedirs(directory)

while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=0.5)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1].upper()
            if className == 'MOUSE':
                x, y, w, h = box
                #  captura de tela da região ao redor do objeto do mouse
                screenshot = img[y:y + h, x:x + w]
                # Gerar um nome de arquivo para a captura de tela
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"{directory}/{date_time}_mouse_screenshot.jpg"
                # Salve a captura de tela com o nome do arquivo
                cv2.imwrite(filename, screenshot)

            # desenhar bbox no obj
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, className, (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)
