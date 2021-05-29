from temperature import get_temp
import cv2

def main():
   while(True):
       a = get_temp()
       #a = a.astype(int)
       FIRE_TEMP = 50
       print(a.shape)
       if a[a>FIRE_TEMP].shape[0] > 0:
          print("there is fire")
          print(a)
       else:
          print("No fire")
          print(a)
    # cv2.imshow("test",a)
    # cv2.waitKey(0)
    
if __name__ == "__main__":
   main()