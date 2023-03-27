#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
img=cv2.imread('doraemon.jpg')
#Original image
cv2.imshow('Original Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#BGR2HSV
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


hsv_img1=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


#BGR2GRAY
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


#RGB2GRAY
gray_img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


#HSV TO RGB
rgb_img=cv2.cvtColor(hsv_img,cv2.COLOR_HSV2RGB)
cv2.imshow('HSV TO RGB',rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


#HSV TO BGR
bgr_img=cv2.cvtColor(hsv_img1,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV TO BGR',bgr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


#RGB to YCrCb
YCrCb_img=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB2YCrCb',YCrCb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


#BGR TO YCrCb
YCrCb_img1=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB2YCrCb',YCrCb_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


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


# In[ ]:


hsv = cv2.cvtColor(scolor, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
cv2.imshow("Hue-image",h)
cv2.imshow("Saturation-image",s)
cv2.imshow("Gray-image",v)
Merged_HSV=cv2.merge((h,s,v))
cv2.imshow('Merged HSV Image',Merged_HSV)
cv2.waitKey(0)
cv2.destoryAllWindows()


# In[ ]:




