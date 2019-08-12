import os,sys
path = "/home/dolphin9/code/MyRecognitionSystem/dataset"
print ("当前工作目录为 %s" % path)

traindir = './train'
print ("traindir = %s" % traindir)
trainfiles = os.listdir(traindir)

jpgdir = './kite'
print ("jpgdir = %s" % jpgdir)
jpgfiles = os.listdir(jpgdir)

txtdir = './txt'
print ("txtdir = %s" % txtdir)
txtfiles = os.listdir(txtdir)

kitedir = './kite'
print ("kitedir = %s" % kitedir)
kitefiles = os.listdir(kitedir)


# 输出所有文件和文件夹
for file in trainfiles:
    if file[-3:] == 'jpg':
       os.rename(traindir+'/'+file,jpgdir+'/'+file)
    else:
       os.rename(traindir+'/'+file,txtdir+'/'+file)
       
#for jpgfile in jpgfiles:
#        for txtfile in txtfiles:
#                if jpgfile[:-4] == txtfile[:-4]:
#                      os.rename(jpgdir+'/'+jpgfile,traindir+'/'+jpgfile)
#                      os.rename(txtdir+'/'+txtfile,traindir+'/'+txtfile)
#                      continue
#        pass
#for txtfile in trainfiles:
#        for jpgfile in jpgfiles:
#                if jpgfile[:-4] == txtfile[:-4]:
#                        if txtfile[-3:] == 'txt':
#                                filename1 = traindir+ '/' + txtfile
                                #print(filename1)
#                                filename2 = jpgdir + '/' + txtfile
                                #print(filename2)
#                                os.system('cp %s %s' % (filename1, filename2)) 
#                                if os.path.isfile(filename2):
#                                       print ('copy file success')
                                        
#for jpgfile in kitefiles:
#        txtfile = jpgfile[:-4] + '.txt'
#        if txtfile in kitefiles:
#                pass
#        else:
#                os.rename(kitedir+'/'+jpgfile,'./kite_new'+jpgfile)
#                print(jpgfile)
