# Color Conversion
## AIM
To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.

## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Import cv2 and save and image as filename.jpg
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use cv2.cvtColor(src, code, dst, dstCn) to convert an image from one color space to another.
### Step4:
Split and merge the image using cv2.split and cv2.merge commands.
### Step5:
End the program and close the output image windows.

## Program:
```
# Developed By: Harini.B
# Register Number: 212221230035
```
```
# displaying original pic
import cv2
img=cv2.imread('doraemon.jpg')
#Original image
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
```
# i) Convert BGR and RGB to HSV and GRAY
# BGR2HSV
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RGB2HSV
hsv_img1=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# BGR2GRAY
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RGB2GRAY
gray_img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
```
# ii)Convert HSV to RGB and BGR
# HSV TO RGB
rgb_img=cv2.cvtColor(hsv_img,cv2.COLOR_HSV2RGB)
cv2.imshow('HSV TO RGB',rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# HSV TO BGR
bgr_img=cv2.cvtColor(hsv_img1,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV TO BGR',bgr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
```
# iii)Convert RGB and BGR to YCrCb
# RGB to YCrCb
YCrCb_img=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB2YCrCb',YCrCb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# BGR TO YCrCb
YCrCb_img1=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB2YCrCb',YCrCb_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
```
# iv)Split and Merge RGB Image
blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
cv2.imshow('B-Channel',blue)
cv2.imshow('G-Channel',green)
cv2.imshow('R-Channel',red)
merged_BGR=cv2.merge((blue,green,red))
cv2.imshow('Merged BGR Image',merged_BGR)
cv2.waitKey(0)
cv2.destoryAllWindows()
```
```
# v) Split and merge HSV Image
#Split:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
cv2.imshow("Hue-image",h)
cv2.imshow("Saturation-image",s)
cv2.imshow("Gray-image",v)
#Merge:
Merged_HSV=cv2.merge((h,s,v))
cv2.imshow('Merged HSV Image',Merged_HSV)
cv2.waitKey(0)
cv2.destoryAllWindows()
```

## Output:
### ORIGINAL IMAGE:
![dor1](https://user-images.githubusercontent.com/93427253/228025717-eed8f074-00a5-4b5f-aa93-63890a7319ef.png)

### i) BGR and RGB to HSV and GRAY
### BGR TO HSV:
![dor2](https://user-images.githubusercontent.com/93427253/228026843-62811246-2628-48d4-9e68-29538008f20c.png)

### RGB TO HSV:
![dor3](https://user-images.githubusercontent.com/93427253/228026894-c23b4bb8-5044-4b50-911e-6557330e837c.png)

### BGR TO GRAY:
![dor4](https://user-images.githubusercontent.com/93427253/228026949-c029cc5f-0e43-4cc3-a242-1bcfaf0c3708.png)

### RGB TO GRAY:
![dor5](https://user-images.githubusercontent.com/93427253/228026992-10b789a2-a3ab-4fe4-81fe-f2a1a67829d4.png)

### ii) HSV to RGB and BGR
### HSV TO RGB:
![dor6](https://user-images.githubusercontent.com/93427253/228027066-c1c8c95a-2e2c-4b49-ae66-5fb2add4b28c.png)

### HSV TO BGR:
![dor7](https://user-images.githubusercontent.com/93427253/228027283-e7a7496e-0b65-490c-925b-3b7171583ead.png)


### iii) RGB and BGR to YCrCb
### RGB TO YCrCb:
![dor8](https://user-images.githubusercontent.com/93427253/228027312-1062da5d-b745-4758-ae55-47511c721d79.png)

### BGR TO YCrCb:
![dor9](https://user-images.githubusercontent.com/93427253/228027335-459d4ba8-972f-4835-9d6f-f4148b3cb7b5.png)

### iv) Split and merge RGB Image
![dor10](https://user-images.githubusercontent.com/93427253/228027386-93b94eee-61a7-492d-b04b-187095a68082.png)


### v) Split and merge HSV Image
![dor11](https://user-images.githubusercontent.com/93427253/228027410-092e693a-4c01-4492-a5d7-fe80394aff96.png)


## Result:
Thus the color conversion was performed between RGB, HSV and YCbCr color models.
