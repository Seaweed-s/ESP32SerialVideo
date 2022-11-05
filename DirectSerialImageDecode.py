from math import floor
import serial.tools.list_ports
import serial
import cv2
import numpy as np
import time


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

print("setting baudrate")
serialInst.baudrate = 2000000
print("baudrate set")
serialInst.port = "COM9"
serialInst.setDTR(False)
serialInst.setRTS(False)
if not serialInst.isOpen():
    print("COM Port already open, closing")
    serialInst.close()
serialInst.open()
print("port open")


bytes = b''
start = time.time()
while True:
    print("loop")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    if serialInst.in_waiting:
        print("Serial")
        bytes += serialInst.read(2048)

        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')

        while a > b:
            print("less")
            bytes = bytes[a:]
            a = bytes.find(b'\xff\xd8')
            b = bytes.find(b'\xff\xd9')
            if a == -1 or b == -1:
                bytes += serialInst.read(2048)
            #print(a)
            #print(b)
        
        #print(a)
        #print(b)
        if a != -1 and b != -1:
            
            size = len(bytes)
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            print(len(jpg))
            
            if jpg:
                try:
                    i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                    cv2.imshow('i', i)
                    print("---------------")
                    FPS = 1/(time.time() - start)
                    print("FPS: ", FPS)
                    print("Bandwidth: ", floor(size * FPS / 1000), "KB/s")
                    print("Image: ", floor(len(jpg) * FPS / 1000), "KB/s")
                    start = time.time()
                except:
                    print("failed to decode (likely corrupt JPEG data)")
                #serialInst.reset_input_buffer

serialInst.close()
cv2.destroyAllWindows()
