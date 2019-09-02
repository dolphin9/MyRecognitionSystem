import os
import random 

def deleteUnused(bboxfilepath, bboxes,images):
    bboxNames = {bbox[:-4] for bbox in bboxes}
    imageNames = {image[:-4] for image in images} 
    delNames = bboxNames.difference(imageNames)
    for delName in delNames:
        delbbox = "%s/%s.txt" %(bboxfilepath, delName)
        print(delbbox)
        os.remove(delbbox)

trainval_percent = 0.1
train_percent = 0.9
bboxfilepath = 'Annotation'
imagefilepath = 'JPEGImages'
txtsavepath = 'ImageSets'
total_bbox = os.listdir(bboxfilepath)
total_image = os.listdir(imagefilepath)

# deleteUnused(bboxfilepath, total_bbox, total_image)

num = len(total_bbox)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval   = open('ImageSets/Main/trainval.txt', 'w')
ftest       = open('ImageSets/Main/test.txt', 'w')
ftrain      = open('ImageSets/Main/train.txt', 'w')
fval        = open('ImageSets/Main/val.txt', 'w')
for i in list:
    name = total_bbox[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else: fval.write(name)
    else: ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close() 
