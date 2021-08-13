
import  minimalmodbus
import  serial
import  time  as  tm
import  numpy   as  np

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

#def   all_reg():
 # r200=instrument.read_register(registeraddress=200,numberOfDecimals=0, functioncode=3, signed=True)  ##int(temp)
 # #tm.sleep(1/1000000)   ##micro
 # r201=instrument.read_register(registeraddress=201, numberOfDecimals=0, functioncode=3, signed=True)  ##float(temp)
 # #tm.sleep(1/1000000)   ##micro
 # r202=instrument.read_register(registeraddress=202, numberOfDecimals=0, functioncode=3, signed=True)  ##int(PH)
 # #tm.sleep(1/1000000)   ##micro
 # r203=instrument.read_register(registeraddress=203, numberOfDecimals=0, functioncode=3, signed=True)  ##float(PH)
 # #tm.sleep(1/1000000)   ##micro
 # r204=instrument.read_register(registeraddress=204, numberOfDecimals=0, functioncode=3, signed=True)  ##int(tds)
 # #tm.sleep(1/1000000)   ##micro
 # r205=instrument.read_register(registeraddress=205, numberOfDecimals=0, functioncode=3, signed=True)  ##float(tds)
 # #tm.sleep(1/1000000)   ##micro
 # r206=instrument.read_register(registeraddress=206, numberOfDecimals=0, functioncode=3, signed=True)  ##int(press)
 # #tm.sleep(1/1000000)   ##micro
 # r207=instrument.read_register(registeraddress=207, numberOfDecimals=0, functioncode=3, signed=True)  ##float(press)
 # #tm.sleep(1/1000000)   ##micro
 # r211=instrument.read_register(registeraddress=211, numberOfDecimals=0, functioncode=3, signed=True)  ##int(encoder)
 # #tm.sleep(1/1000000)   ##micro
 # r212=instrument.read_register(registeraddress=212, numberOfDecimals=0, functioncode=3, signed=True)  ##float(encoder)
 # return (r200,r201,r202,r203,r204,r205,r206,r207,r211,r212)
 

##while(True):
def   return_plc(self):
 r=instrument.read_registers(registeraddress=200, numberOfRegisters=16, functioncode=3)
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


