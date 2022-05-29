# Attendance Management Using Face Recognition

 ### Recognize The Faces And Take Automatic Attandance. :

## Motivation :
----------------------------
We seek to provide a valuable attendance service for students. Reduce manual process errors by providing automated and a reliable attendance system uses face recognition technology.

## Features :
---------------------------
* Check Camera
* Upload Faces With Their Names
* Recognize Faces & Attendance
* Show Attendance Overall
* Show Attendance Date Wise

## Tech Used :
--------------------------
Build With - 
* Python 3.9.7

Module Used -

All The Module are Latest Version.
* face_recognition
* numpy
* opencv_python
* pandas
* Pillow
* streamlit
* io
* os
* DateTime



Face Recognition Algorithms -
* HOG Algorithm

Software Used -
* VS CODE 

#### Installing the packages
--------------------------------------------------

let's install the necessary packages. 


To install the packagesopen the terminal or command line and paste the code from below

```
pip install opencv-python
```
```
pip install numpy
```
```
pip install pandas
```
```
pip install Pillow
```
```
pip install face_recognition
```
```
pip install streamlit
```

[ **Notice: During the package installization, sometime it shows some error, to avoid those error you can install those packages as admin. ]

## How To Use? 
----------------------
If you want to use it just follow the steps below.

1. First download or clone the project
2. Import the project to your favourit IDE
3. Create a python enviroment
4. Install all the packages 
5. Run the project using the command line or your IDE Run Button

## Test Run :
-----------------------
After creating the enviroment and installing the packages, open the IDE terminal/command line to run the program. Using the code below.

```
streamlit run app.py
```
Here is a demo to run the program. I'm Using the VS code IDE in my demo.

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/1.jpg?raw=true)

Click on Run to start the webapp face recognition

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/2.jpg?raw=true)

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/3.jpg?raw=true)

Click on Browse files to upload an image for dataset

NOTE :- File name should be same as person name spaces are not allowed use '_' instead of space

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/4.jpg?raw=true)

Select your desired file from your computer and upload

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/5.jpg?raw=true)

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/6.jpg?raw=true)

Click on show attendance (Total) to show total attendance in the database

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/7.jpg?raw=true)

Click on Show Attendance (Sorted by Date) 

Select date from the below options

![Test Run](https://github.com/nakshatramittal11/attendance_management_using_face_recognition_ms_engage/blob/main/ms%20pictures/8.jpg?raw=true)

Click on  Show Attendance (Sorted by Date) again to show the attendance of the given date

Youtube Video For Reference
https://www.youtube.com/watch?v=PuXIGsJb3FA

## Known Bugs :
------------------------------
This project have some bugs.
* The WebApp takes approx 40 seconds to configure any changes applied
* If any button is pressed it takes approx 30-40 seconds to refresh the screen and dislay the result
