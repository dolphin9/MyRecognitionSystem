from PIL import ImageFont
import xml.etree.ElementTree as ET
import cv2
import os
import numpy as np

classes = ["kite", "balloon","bird-nest"]

wd = os.getcwd()
bboxfilepath = os.path.join(wd, 'labels') 
imagefilepath = os.path.join(wd, 'images') 
imagesavepath = os.path.join(wd, 'rects') 

def draw_xml(name):
    img_file = "%s/%s.jpg" % (imagefilepath, name)
    lbl_file = "%s/%s.xml" % (bboxfilepath, name)
    img = cv2.imread(img_file)
    # h, w, _ = img.shape
    # print(h, w)

    with open(lbl_file, "r") as f:
        tree = ET.parse(f)
        root = tree.getroot()

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            xmin, ymin, xmax, ymax = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
            img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (1, 1, 0, 0), 2)

    cv2.imwrite("%s/%s.jpg" % (imagesavepath, name), img)

def draw_txt(name):
    img_file = "%s/%s.jpg" % (imagefilepath, name)
    lbl_file = "%s/%s.txt" % (bboxfilepath, name)
    img = cv2.imread(img_file)
    if img is None:
        print("no such file %s.jpg" % name)
        return
    h, w, _ = img.shape
    # print(h, w)
        
    # font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
    #             size=np.floor(3e-2 * img.shape[1] + 0.5).astype('int32'))
    fontFace = cv2.FONT_HERSHEY_PLAIN
    fontScale = 1.0
    thickness = 1

    with open(lbl_file, "r") as f:
        for line in f.readlines():
            groups = line.split(' ')
            cls_id = int(groups[0])
            label = classes[cls_id]
            # xmin, ymin, xmax, ymax = map(float, groups[1:])
            # yctr, xctr, ywid, xwid = map(float, groups[1:])
            xctr, yctr, xwid, ywid = map(float, groups[1:])
            # ywid, xwid, yctr, xctr = map(float, groups[1:])
            ymin = yctr - ywid/2
            ymax = yctr + ywid/2
            xmin = xctr - xwid/2
            xmax = xctr + xwid/2
            # print((xmin, ymin), (xmax, ymax))

            xmin = int(xmin * w)
            ymin = int(ymin * h)
            xmax = int(xmax * w)
            ymax = int(ymax * h)

            label_size = cv2.getTextSize(label, fontFace, fontScale, thickness)
            top, left, bottom, right = ymin, xmin, ymax, xmax
            if top - label_size[1] >= 0:
                text_origin = (left, top - label_size[1])
            else:
                text_origin = (left, top + 1)

            img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (1, 1, 0, 0), 2)
            img = cv2.putText(img, label, text_origin, color=(128, 128, 128),
                    fontFace=fontFace, fontScale=fontScale)

    cv2.imwrite("%s/%s.jpg" % (imagesavepath, name), img)

def draw(name):
    if os.path.isfile('%s/%s.xml'%(bboxfilepath, name)):
        draw_xml(name)
    elif os.path.isfile('%s/%s.txt'%(bboxfilepath, name)):
        draw_txt(name)
    else:
        print("no such file %s.txt" % name)

with open("main/train.txt", "r") as f:
    for name in f.readlines():
        draw(name[:-1])
