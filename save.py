

import numpy as np
import cv2
import  os
import  time
import  random  as rn



class save_show():
 def __init__(self,cap):
   self.setupUi(cap)

 

 
 def    setupUi(self,cap):
  t=time.strftime('%X %x %Z')
  with open('Aria_save.txt') as f:
      content = f.readlines()
  content = [x.strip() for x in content] 
  w1=content[0]
  w2=content[1]
  
  cwd=w1+'/'+w2
  list1=os.listdir(w1)
  if list1!=[]:
   if  (w2)   in   list1:
    pass
   else:
    os.mkdir(cwd)
  
  destination=(cwd+'/'+w2+'aria.avi')
  #cap = cv2.VideoCapture(0)
  w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  out = cv2.VideoWriter(destination,fourcc, 20.0, (int(w),int(h)))
  
  font=cv2.FONT_ITALIC  
  text="2018/1/1/"
  textsize = cv2.getTextSize(text, font, 1, 1)[0]
  w1,h1=textsize
  
  while(cap.isOpened()):
   
   t=time.strftime('%X %x %Z')
   ret, frame = cap.read()
   if ret==True:
    print  (ret)
    cv2.putText(frame,t,(round(w-w1-200),round(380)),font,.75,(255,255,255),2)
    
    out.write(frame)
    cv2.imshow('aria',frame)
    if cv2.waitKey(1) & 0xFF == ord('O'):
     break
	
    cv2.resizeWindow('aria', (650, 391))
   else:
    print("Not Frame")
  
  cap.release()
  out.release()
  cv2.destroyAllWindows()  
  
 


# # if   cv2.VideoCapture(l[0]).isOpened():
 # # video=cv2.VideoCapture(l[0])
 # # save_show(video)

 # save_show(cv2.VideoCapture(1))
 
# # elif   cv2.VideoCapture(l[2]).isOpened():
 # # video=cv2.VideoCapture(l[2])
 # # save_show(video)
 
 
save_show(cv2.VideoCapture(0))
