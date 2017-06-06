# -*- coding: utf-8-*-
import re
import cv2
import sys, datetime
import smtplib
from client import app_utils

WORDS = ["CAPTURE"]

camIndex = 0
filepath = "/home/wesley/jasper_captures/"
imgType = ".jpg"

def isValid(text):
    return bool(re.search(r'\bcapture\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    cam = cv2.VideoCapture(camIndex)
    
    #Let the light levels adjust on the camera
    for i in xrange(30):
        retVal, img = cam.read()

    #Capture
    mic.say("3, 2, 1, Say Cheese.")
    retval, capture = cam.read()
    
    imagePath = "butthole" + imgType
    cv2.imwrite(imagePath, capture)
    del(cam)

    mic.say("Looking great. Would you like me to email this photo to you?")    
    handleResponse(mic, profile, mic.activeListen(), imagePath)

def handleResponse(mic, profile, text, imagePath):
    if app_utils.isPositive(str(text)):
        mic.say("Emailing photo.")
        app_utils.emailUser(profile, SUBJECT=imagePath, BODY="", imageFile=imagePath)
    else:
        mic.say("Photo saved.")
