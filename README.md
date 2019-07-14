# Style Transfer for Videos

## Frame:
### 1. python GUI
First of all, choose the video we need and get path from open file:  
library: tkinter   
using `filedialog.askopenfilename()` to get the path

<center>
    <img src="https://github.com/LoewiLu/Style_Transfer_for_Videos/blob/master/gifs/ui.gif"/>
</center>

### 2. Video to Images 
library: openCV  
`cv2.VideoCapture`  
`cv2.imwrite`
<center>
    <img src="https://github.com/LoewiLu/Style_Transfer_for_Videos/blob/master/gifs/parts.gif"/>
</center>

### 3. Mask Making
Image Binarization   
library: openCV  
`cv2.imread`  
`cv2.cvtColor`  
`cv2.threshold`
<center>
    <img src="https://github.com/LoewiLu/Style_Transfer_for_Videos/blob/master/gifs/bgw.gif"/>
</center>

### 4. NST with Tensorflow

<center>
    <img src="https://github.com/LoewiLu/Style_Transfer_for_Videos/blob/master/gifs/cubism.gif"/>
</center>

### 5. Images to Video  
library: openCV  
`cv2.VideoWriter`
mask added:
<center>
    <img src="https://github.com/LoewiLu/Style_Transfer_for_Videos/blob/master/gifs/final.gif"/>
</center>

### 6. Audio Generation with GAN



