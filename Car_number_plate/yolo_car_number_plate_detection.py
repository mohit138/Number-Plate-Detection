# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:03:30 2020

@author: mohit
"""

import cv2
import numpy as np
import glob
import random

# Load Yolo Model and Weights
net = cv2.dnn.readNet("yolov3_training_last_cars.weights", "yolov3_testing.cfg")

# Names Of classes
classes = ["number_plate"]

# path of images to be tested
images_path = glob.glob(r"E:\ML\YOLO_openCV\Number Plate Detection\Car_number_plate\Test_Set\*.jpg")


layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255,size = (len(classes),3))

random.shuffle(images_path)

# loop through images
for img_path in images_path:
    # load the image
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx = 0.6, fy=0.6)
    height, width, channel = img.shape
    
    
    blob = cv2.dnn.blobFromImage(img, 0.00392, (608,608), (0,0,0), True, crop=False)
    
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # show info on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cpy_img = img.copy()
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 30), font, 1, color,2 )
            number_plate = cpy_img[y:y+h,x:x+w]
            number_plate = cv2.resize(number_plate, None, fx = 5, fy=5)
            cv2.imshow("plate{}".format(i), number_plate)
            

    cv2.imshow("Image", img)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.destroyAllWindows()




