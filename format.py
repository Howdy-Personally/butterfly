import cv2
import os
import json

num_classes={'dark bg':0,'dark leaf':1,'dark petal':2,
'light bg':3,'light leaf':4,'light petal':5}
def filename_format():
    dir = 'C:/Users/123/Desktop/senti-yolo/images/val'
    num=0
    for root, dirs, files in os.walk(dir):

        for file in files:
            if file.split('.')[1]=='JPG':
                filepath = os.path.join(root, file)
            
            try:
                
                num=num+1
                dst=dir+"/"+str(num)+".JPG"
                print(filepath,dst)
                os.rename(filepath, dst)
            except:
                pass

def labelme_2_yolo():
    dir = 'C:/Users/123/Desktop/senti-yolo/images/flower_val'
    for root, dirs, files in os.walk(dir):
        nums=0
        for file in files:
            nums+=1
            with open(dir+'/'+file,'r', encoding='utf-8') as f:
                f=f.read()
                f=json.loads(f)
                f = f['shapes']
                for iter in f:
                    x1=iter['points'][0][0]
                    y1=iter['points'][0][1]
                    x2=iter['points'][1][0]
                    y2=iter['points'][1][1]
                    x=str((x1+x2)/4480)
                    y=str((y1+y2)/4480)
                    w=str(abs(x2-x1)/2240)
                    h=str(abs(y2-y1)/2240)
                    txt=str(num_classes[iter['label']])+' '+x+' '+y+' '+w+' '+h
                    # print(txt,nums)
                    with open('C:/Users/123/Desktop/senti-yolo/labels/val/'+str(nums)+'.txt','a') as f2:
                        f2.write(txt+'\n')
            # print()

if __name__=="__main__":
    labelme_2_yolo()
