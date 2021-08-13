

import   os
import   re
import   sys
import cv2
import  time
import   datetime
import  random  as  rn 
import  minimalmodbus
import  serial
import  time  as  tm
import  numpy   as  np 
 
def  save_1():
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
  
  d=str(datetime.datetime.now())
  font=cv2.FONT_ITALIC  
  textsize = cv2.getTextSize(d,font,1,1)[0]
  w1,h1=textsize
  still=d[17:19]
  filename=str(int(still))+'_aria'+'.avi'
  destination=(cwd+'/'+filename)
  cap = cv2.VideoCapture(0)
  w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
  h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
  fourcc = cv2.VideoWriter_fourcc(*'MJPG')
  out = cv2.VideoWriter(destination,fourcc,15.0,(int(w),int(h)))
  
 
  while(cap.isOpened()):  
   ##self.pushButton_34.clicked.connect(lambda : out.release())   
   d=str(datetime.datetime.now())
   ret, frame = cap.read()
   if ret==True: 
###=======================================================for   update   plc  function
    plc()
####======================================================
    cv2.putText(frame,"Aria_fanavaran",(round(20),round(20)),font,.65,(255,255,255),1)
    Sh,En=plc()
    global_En=0 
    global_Sh=0
    #self.Sh.clicked.connect(lambda : self.list0_Sh.append(Sh))
    #self.Sh.clicked.connect(lambda  :  self.Sh_change())
    if Sh!="disconnect":
     #self.global_En_0=self.list0_Sh[-1]     ###addade   clicked	 
     #print(type(self.global_En_0))
     #self.global_En=abs(self.global_En_0-Sh)
     global_En=0 
     global_Sh=0
    
    #print(self.global_En,Sh,self.list0_Sh[-1])
    # if En!="disconnect":
     # b=En
     # self.En.clicked.connect(lambda   :  list0_En.append(b))
     # if  list0_En!=[]:
      # L0En=list0_En[:-1]
      # En=En-float(L0En[0])
	  
    cv2.putText(frame,('Sh=' +str(global_Sh)),(round(w-w1-50),round(h-h1-25)),font,1,(230,200,200),1)
    cv2.putText(frame,('En=' +str(global_En)),(round(w-w1-50),round(h-h1-50)),font,1,(230,200,200),1)
    cv2.putText(frame,d,(round(w-w1-50),round(h-h1)),font,.75,(255,255,255),1)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.resizeWindow('aria', (650, 400)) 
    if cv2.waitKey(1) & 0xFF == ord('O'):
     break
   else:
    break
  ##cap.release()
  out.release()
  cv2.destroyAllWindows()
  
  
def  plc(): 
  try: 
   instrument=minimalmodbus.Instrument('COM1',1)
   instrument.serial.baudrate=9600     #Baudrate
   instrument.serial.bytesize=8
   instrument.serial.parity=serial.PARITY_NONE
   instrument.serial.stopbits=1
   instrument.serial.timeout=1        #seconds
   instrument.CLOSE_PORT_AFTER_EACH_CALL = True
   instrument.debug = True
   instrument.mode = minimalmodbus.MODE_RTU   
   print("##=================================================================================================##")
   print("##=================================================================================================##")
   instrument.read_registers(registeraddress=200, numberOfRegisters=16, functioncode=3)
   print(type(r))
   print(len(r))
   print(str(r))
   ###-------------------split
   b=r[4]      ###low
   b=np.int32(b)
   ###-----------------a
   a=r[3]  ####high
   v=np.int32(65536)
   a=a*v
   a=np.int32(a)
   ###==============
   Sh=a+b                 ####shib   
   #print(type(c))
   #print(c)
   ######------------------------------------------------------------------------------
   ###---------------------------------------------------------------------------------
   ##----------------------------------------------------------------------------------encoder 201-202
   b=r[2]      ###low
   b=np.int32(b)
   ###-----------------a
   a=r[1]  ####high
   v=np.int32(65536)
   a=a*v
   a=np.int32(a)
   ###==============
   En=a+b           ###encoder
   #print(type(E))
   #print(E)
   return(Sh,En)
   return(Sh,En)
  except:
   return("disconnect","disconnect")
####==================================================================
####================================================================== 
  
save_1()
