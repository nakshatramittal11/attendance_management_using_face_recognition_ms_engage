from cv2 import COLOR_BGR2RGB
import face_recognition as fr
import cv2
import numpy as np
import pandas as pd
import os
from datetime import datetime as dt
import streamlit as st
from io import StringIO
from PIL import Image

st.title('Attendance Management System')
run=st.checkbox('Run',key='1')
frame_window= st.image([])
face_dataset="face_dataset"      # path of image dataset
images=[]
class_names=[]
mylist=os.listdir(face_dataset)


# ----------------------upload image for dataset----------------------------------------------------------

def load_image(image_file):
	img = Image.open(image_file)
	return img

st.header('Add New Face')
st.caption('For Face Dataset')

uploaded_file = st.file_uploader("Choose a file(jpg, jpeg, png)",type=['jpg','jpeg','png'],key='2')
if uploaded_file is not None:
    with open(os.path.join(face_dataset,uploaded_file.name),"wb") as mf:
        mf.write((uploaded_file).getbuffer())
    st.success("File Saved")

# ----------------read all images from dataset into list--------------------------------------------------

for fx in mylist:
    current_img=cv2.imread(f'{face_dataset}/{fx}')
    images.append(current_img)
    class_names.append(os.path.splitext(fx)[0])


def findencoding(images):
    encode_list=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list


encode_list_known = findencoding(images)
print("encoding completed")

# ----------------------------------sort attendace according to date--------------------------------------

def sorted_date():
    with open('attendance_list.csv','r') as al:
        next(al)
        data_list=al.readlines()

        for data in data_list:
            x=data.split(',')
            entry_date=str(x[2])[:10]
            entry_name=str(x[0])

            with open(f'attendance/{entry_date}.csv','a+') as sd:
                y=f'{x[0]},{x[1]},{entry_date}\n'

            with open(f'attendance/{entry_date}.csv','r+') as sd:
                data_list1=sd.readlines()
                name_list1=[]

                for data1 in data_list1:
                    entry1=data1.split(',')
                    name_list1.append(str(entry1[0]))

                if entry_name not in name_list1:
                    sd.writelines(y)
                    sd.flush()

# ----------------mark attendance in attendance_list.csv--------------------------------------------------

def markattendance(name):
    with open ('attendance_list.csv','r+') as f:
        data_list= f.readlines()
        name_list=[]
        name_date=dict()
        
        for data in data_list:
            entry=data.split(',')
            name_list.append(entry[0])
            name_date[str(entry[0])]=str(entry[2])[:10]
        current=dt.now()
        dt_string=current.strftime('%H:%M:%S')
        x=str(dt.today())

        if name not in name_list:
            f.writelines(f'\n{name},{dt_string},{x[:10]}')
            f.flush()
        
        if name in name_list:            
            if name_date[name]!= x[:10]:
                f.writelines(f'\n{name},{dt_string},{x[:10]}')
                f.flush()
        sorted_date()

# ------------------------------show marked attendance----------------------------------------------------

st.header('Attendance Marked')
st.caption('(if not showing then click show attendance button again to refresh)')
df = pd.read_csv("attendance_list.csv")
if st.button('show attendance(Total)',key='3'):
    st.write(df)

# ------------------------------show marked attendance according to date----------------------------------

if st.button('Show Attendence (Sorted By Date)',key='5'):
    st.header('Show Attendace According To Date')
    st.caption('Select a Date From below SelectBox')
    sorted_attendance_list=os.listdir('attendance')
    option = st.selectbox('which date attendance you would like to display?', tuple(sorted_attendance_list))
    option=str(option)
    xy=pd.read_csv(f'attendance/{option}')
    # if st.button('Show Attendance(Date Wise)',key='4'):
    st.write(xy)

# ---------------------------------------use camera for face recognition----------------------------------

cap=cv2.VideoCapture(0)

while run:
    ret,img=cap.read()

    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,COLOR_BGR2RGB)

    faces_cur_frame=fr.face_locations(imgs)
    encode_cur_frame = fr.face_encodings(imgs,faces_cur_frame)

    for encode_face,face_loc in zip(encode_cur_frame,faces_cur_frame):
        matches=fr.compare_faces(encode_list_known,encode_face)
        face_dis= fr.face_distance(encode_list_known,encode_face)
        match_index=np.argmin(face_dis)
        if matches[match_index]:
            name=class_names[match_index].upper()
            markattendance(name)
            y1,x2,y2,x1=face_loc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.putText(img,name,(x1+6,y2+23),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0),2)
    
    frame_window.image(img)

else:
    st.write('Stopped')