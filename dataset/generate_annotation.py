import xml.etree.ElementTree as ET
import cv2
import os

sets=['train', 'val', 'test']

classes = ["kite", "balloon","bird-nest"]

wd = os.getcwd()
bboxfilepath = os.path.join(wd, 'voc_new') 
imagefilepath = os.path.join(wd, 'image') 

def convert_annotation(image_id, list_file):
    in_file = open('%s/%s.xml'%(bboxfilepath, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

for image_set in sets:
    image_ids = open('main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/%s.jpg'%(imagefilepath, image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

