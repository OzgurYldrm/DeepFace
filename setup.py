import os
import pandas as pd
def setup_system():
    dir = os.getcwd()
    
    #Creating Log Directory
    if os.listdir(".").count("log")==0:
        log_path = dir + "\\" + "log"
        os.mkdir(log_path)
        print("Creating log directory")

    #Creating Log File
    if os.listdir(dir+"\\log").count("log.xlsx")==0:
        df = pd.DataFrame(columns=['Time','Age','Gender','id',"CamId"])
        log_path = dir + "\\" + "log\\log.xlsx"
        df.to_excel(log_path,index=False)
        print("Creating log file")

    #Creating Faces Directory
    if os.listdir(".").count("faces")==0:
        log_path = dir + "\\" + "faces"
        os.mkdir(log_path)
        os.replace("images.jpg", "faces/images.jpg")
        print("Creating Face Directory")

def read_log():
    path = "log/log.xlsx"
    df = pd.read_excel(path)
    return df