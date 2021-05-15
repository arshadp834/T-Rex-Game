from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np 
	
class cordinates(): 
    replaybutton =(360, 214) 
    dinasaur = (149, 239 ) 
	 
def restartGame(): 
    pyautogui.click(cordinates.replaybutton) 
    pyautogui.keyUp('up') 

def press_space(): 
    pyautogui.keyUp('up') 
   # pyautogui.keyDown('space') 
    #time.sleep(0.05) 
    print("jump")  
    time.sleep(0.10) 
    pyautogui.keyUp('space') 
    pyautogui.keyDown('up') 

def imageGrab():  
    box = (cordinates.dinasaur[0]+30, cordinates.dinasaur[1], 
		cordinates.dinasaur[0]+120, cordinates.dinasaur[1]+4) 
    image = ImageGrab.grab(box) 
    
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    
    print(a.sum()) 
    return a.sum() 
	
restartGame() 
while True: 
	
	if(imageGrab()!= 500): 
		press_space() 
		
		time.sleep(0.1) 
 
 
