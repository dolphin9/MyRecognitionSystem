import xml.etree.ElementTree as ET
import cv2

classes = ["kite", "balloon","bird-nest"]

def draw(name):
    img_file = "image/%s.jpg" % name
    lbl_file = "voc_new/%s.xml" % name
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

    cv2.imwrite("rects/%s.jpg" % name, img)

with open("main/train.txt", "r") as f:
    for name in f.readlines():
        draw(name[:-1])