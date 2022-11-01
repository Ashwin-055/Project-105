import os
import cv2

path = "Imgs"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext == '.jpg':
        file_name = path+"/"+file
        #print(file_name)
        images.append(name)
images.sort(key=int)
count = len(images)
print(count,"\n",images)
frame=cv2.imread(path+"/"+images[0]+".jpg")
height,width,channel=frame.shape
size=(width,height)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

for i in range(0,count-1):
    frame=cv2.imread(path+"/"+images[i]+".jpg")
    out.write(frame)

out.release()
print("Done")