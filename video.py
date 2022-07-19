#0 is your default webcam
#cap.read return bool value and the frame which is captured if ret is false it means frame is not captured prooperly
import cv2
cap = cv2.VideoCapture(0)
frame = None
while True:
    ret,frame = cap.read()
    if ret == False:
        continue
        
    cv2.imshow("Video Frame", frame)
    
    #wait for user input press q for stop
    #cv2 waitkey provides you to capture the char you pressed if press otherwise it will close anyhow but here not iuntil we [press q]
    #0 -255 is a 8 bit integer waitkey gives you 32 bit integer 0xff is number with 8 ones
    #if we do and of 8 bit which are 1 with 32 bit it gives the last 8bit that is required
    #ord('q') = 113 
    key_pres = cv2.waitKey(1) & 0xFF
    if key_pres == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
    