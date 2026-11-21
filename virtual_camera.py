
import cv2
import time

image = cv2.imread("photo.jpg")

if image is None:
    print("cannt lode file photo")
    exit()


image = cv2.resize(image, (1280, 720))

print("virtual camera")
print("press q to exit")

while True:
    
    cv2.imshow("Virtual camera", image)

    
    if cv2.waitKey(33) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
