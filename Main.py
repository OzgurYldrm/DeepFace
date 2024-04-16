from detection import detect_faces,find_face,get_info
from save import save_face,save_log,get_age_gender
from setup import setup_system,read_log
import cv2
import numpy as np
import pandas as pd
import time

def annotate(frame,area,age,gender):
    start_point = (area["x"],area["y"])
    end_point = (area["x"]+area["w"],area["y"]+area["h"])
    frame = cv2.rectangle(frame,start_point , end_point, (255,0,0), 2)
    text = str(age) + " " +str(gender)
    frame = cv2.putText(frame, text, start_point, cv2.FONT_HERSHEY_SIMPLEX ,  1, (255,0,0), 2, cv2.LINE_AA)
    return frame

setup_system()
df = read_log()

input_cam = 0
vid1 = cv2.VideoCapture(input_cam)

time.sleep(3)

while(True): 
    ret1, frame1 = vid1.read() 
    faces = detect_faces(frame1)
    for face in faces:
        face,area,conf = face.values()
        if conf>0.85:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)*255
            id,dist = find_face(face)
            if dist.size == 0:
                age,gender = get_info(face)
                print("No match. Saving...")
                name = save_face(face)
                df = save_log(df,age,gender,name,input_cam)
            else:
                index = np.where(dist.min())[0]
                name = id[index].item().split("\\")[-1]
                age,gender = get_age_gender(df,name)
                df = save_log(df,age,gender,name,input_cam)
            frame1 = annotate(frame1,area,age,gender)
    cv2.imshow('frame1', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

df.to_excel("log/log.xlsx",index=False)
vid1.release() 
cv2.destroyAllWindows()