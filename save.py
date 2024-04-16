import os
import cv2
import datetime
import numpy as np

def show_log(df):
    background = np.zeros((512,512))
    dates = df.tail(5)["Time"].dt.time
    for i,j in enumerate(df[["Age","Gender","id"]].tail(5).values):
        loc = 0,(i+1)*100
        text = str(dates.iloc[i])[0:8] + "  " + str(j)
        background = cv2.putText(background, text,loc, cv2.FONT_HERSHEY_SIMPLEX ,  1, (255,0,0), 1, cv2.LINE_AA)
    cv2.imshow('log', background) 

def save_face(face):
    path = os.getcwd() + "\\faces"
    count = len(os.listdir(path)) + 1
    id = str(count) + ".png"
    file_name = path + "\\" + id
    cv2.imwrite(file_name,face)
    return id

def determine(df,id,cam,time):
    hist = np.where(df["id"]==id)[0]
    if hist.shape[0]==0:
        print("First entry")
        return 0
    else:
        last_log = hist[-1]
        if df.iloc[last_log]["CamId"] == cam:
            time_delta = time - df.iloc[last_log]["Time"]
            time_delta = int(time_delta.total_seconds())
            if time_delta>30:      
                print("Repeated")
                return 1
            else:
                return 2
        else:
            print("Other Camera")
            return 3

def save_log(df,age,gender,id,cam):
    time = datetime.datetime.now()
    d = determine(df,id,cam,time)
    if d==0:
        new_row = {'Time':time,'Age':age,'Gender':gender,'id':id,'CamId':cam}
        df.loc[len(df)] = new_row
        show_log(df)
    elif d==1:
        new_row = {'Time':time,'Age':age,'Gender':gender,'id':id,'CamId':cam}
        df.loc[len(df)] = new_row
        show_log(df)
    elif d==2:
        pass
    elif d==3:
        new_row = {'Time':time,'Age':age,'Gender':gender,'id':id,'CamId':cam}
        df.loc[len(df)] = new_row
        show_log(df)
    return df

def get_age_gender(df,id):
    try:
        hist = np.where(df["id"]==id)[0]
        series = df.iloc[hist[-1]]
        age,gender = series["Age"],series["Gender"]
        return age,gender
    except:
        return -1,"Null"