import numpy as np

def calculate_angle(coordinates:list[list[float]])->float:
    a = np.array(coordinates[0]) # First
    b = np.array(coordinates[1]) # Mid
    c = np.array(coordinates[2]) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 
