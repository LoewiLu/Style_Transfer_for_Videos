#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:41:31 2019

@author: loewi
"""

import cv2
import glob
import os
import tkinter as tk
from tkinter import filedialog
import shutil
import re

def getPath():
    fname = filedialog.askopenfilename(title='open video file', filetypes=[('mp4 files', '*.mp4'), ('All Files', '*')])
    #crashed while proceed on MacOS
    return fname


def video2Imgs(videopath, frame_time = 2):

    if os.path.exists(folder_path + '/imgs'):
        shutil.rmtree(folder_path + '/imgs')
    os.makedirs(folder_path + '/imgs')
    
    cap = cv2.VideoCapture(videopath)
    ret, frame = cap.read() #ret:bool, False if ends; frame: 3D matrix
    
    n = count = 1    
    while ret:
        ret, frame = cap.read()
        pic_path = folder_path + '/imgs/'

        if count % frame_time == 0: #proceed every frame_time
            p = pic_path +  '/frame_' + str(n) + '.jpg'
            cv2.imwrite(p, frame)  
            n += 1
            
        count += 1   
        
    cap.release()
    

def rgb2Bw(img, filename, reverse):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if not reverse:
        mask = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)[1]
    else:
        mask = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imwrite(filename, mask)


def makeMask(reverse = False):
    
    if os.path.exists(folder_path + '/imgs_mask'):
        shutil.rmtree(folder_path + '/imgs_mask')
    
    shutil.copytree(folder_path + '/imgs', folder_path + '/imgs_mask')
    p = folder_path + '/imgs_mask/*.jpg'
    
    for filename in glob.glob(p):
        
        img = cv2.imread(filename)
        rgb2Bw(img,filename, reverse) #binarization of the image
        img = cv2.imread(filename)

def sort_key(s):
    return int(re.findall('(\d+)\.',s)[0])

def imgs2Video(file_path):
    
    if not os.path.exists(folder_path + '/output'):
        os.makedirs(folder_path + '/output')
    
    img_lst = []
    
    for filename in sorted(glob.glob(file_path), key = sort_key):
        #print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        img_lst.append(img)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(folder_path + '/output/' +'project_final.mp4', fourcc, 18.0, (width, height))
    
    for img in img_lst:
        out.write(img)
        
    out.release()


if __name__ is '__main__':
    #videopath = getPath()
    videopath = '/Users/loewi/Documents/project_July/swan_close.mp4'
    folder_path, _ = os.path.split(videopath)
    
    video2Imgs(videopath, frame_time = 2)
    makeMask(reverse = False) #BGW
    #gererate() #NST  the result should be stored in the folder named ../generated/
    imgs2Video(folder_path + '/generated/*.jpg')
    
#%%
