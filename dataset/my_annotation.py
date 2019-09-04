import xml.etree.ElementTree as ET
import cv2
import os

sets=['train', 'val', 'test']

classes = ["kite","balloon","bird-nest"]

wd = os.getcwd()
bboxfilepath = os.path.join(wd, 'labels') 
imagefilepath = os.path.join(wd, 'images') 


def convert_annotation_xml(image_id, list_file):
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


def convert_annotation_txt(image_id, list_file):
    in_file = open('%s/%s.txt'%(bboxfilepath, image_id))
    in_image= cv2.imread('%s/%s.jpg'%(imagefilepath, image_id))
    if in_image is None:
        print("no such file %s.jpg." % image_id)
        return
    height, width, _ = in_image.shape

    for line in in_file.readlines():
        s = line.split(" ")
        cls_id = int(s[0])
        xctr, yctr, xwid, ywid = map(float, s[1:])
        ymin = yctr - ywid/2
        ymax = yctr + ywid/2
        xmin = xctr - xwid/2
        xmax = xctr + xwid/2

        xmin = int(xmin * width)
        ymin = int(ymin * height)
        xmax = int(xmax * width)
        ymax = int(ymax * height)

        bbox = [xmin, ymin, xmax, ymax]
        list_file.write(" " + ",".join([str(a) for a in bbox]) + ',' + str(cls_id))


def convert_annotation(image_id, list_file):
    if os.path.isfile('%s/%s.xml'%(bboxfilepath, image_id)):
        convert_annotation_xml(image_id, list_file)
    elif os.path.isfile('%s/%s.txt'%(bboxfilepath, image_id)):
        convert_annotation_txt(image_id, list_file)
    else:
        print("no such file %s.txt." % image_id)


for image_set in sets:
    image_ids = open('main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/%s.jpg'%(imagefilepath, image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

