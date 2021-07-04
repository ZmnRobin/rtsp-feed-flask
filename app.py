import pyrebase
from flask import Flask, render_template, Response,redirect,url_for,request
from flask_cors import CORS, cross_origin
from flask import *
import urllib
import os
import re
from urllib.request import urlopen
from flask import jsonify
import cv2
import imutils
from imutils.video import VideoStream


# email=input("Enter Email: ")
# password=input("Enter Password: ")
# user = auth.create_user_with_email_and_password(email, password)
# # user = auth.sign_in_with_email_and_password(email, password)
# print(user['idToken'])
# * ---------- Create App --------- *

app = Flask(__name__)

config={
    "apiKey": "AIzaSyCn0XwTht4s9V7itVW2cH0kRmzyr2OidlI",
    "authDomain": "shoplift-app-2aedf.firebaseapp.com",
    "databaseURL":"https://shoplift-app-2aedf.firebaseio.com",
    "projectId": "shoplift-app-2aedf",
    "storageBucket": "shoplift-app-2aedf.appspot.com",
    "messagingSenderId": "572175241985",
    "appId": "1:572175241985:web:c4f798d2b9dcf8654cc100"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/',methods=['GET','POST'])

def mainfunction():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('index'))
    return render_template('login.html')


rtsp_url ="rtsp://user1:User123456@192.168.0.200:554/cam/realmonitor?channel=1&subtype=0"

vs = VideoStream(rtsp_url).start()
# # vs2 = VideoStream(rtsp_url2).start()

def gen_frames():
    while True:
        frame = vs.read()
        if frame is None:
            continue
        else:
            frame, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/rtsp_feed', methods=['GET'])
# @cross_origin(supports_credentials=True)
def rtsp_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
# * ---------- Get home information ---------- *

@app.route('/home', methods=['GET'])
# @cross_origin(supports_credentials=True)
def index():
    return render_template('index.html')

@app.route('/products-training', methods=['GET'])
# @cross_origin(supports_credentials=True)
def productsTraining():
    return render_template('productsTraining.html')

@app.route('/new-station', methods=['GET'])
# @cross_origin(supports_credentials=True)
def newStation():
    return render_template('newStation.html')

@app.route('/my-account', methods=['GET'])
# @cross_origin(supports_credentials=True)
def myAccount():
    return render_template('myAccount.html')

@app.route('/add-camera', methods=['GET'])
# @cross_origin(supports_credentials=True)
def addCamera():
    return render_template('addCamera.html')

@app.route('/Camera-list', methods=['GET'])
# @cross_origin(supports_credentials=True)
def addCamerat():
    return render_template('cameraList.html')
    
@app.route('/Dataset-List', methods=['GET'])
# @cross_origin(supports_credentials=True)
def dataSetList():
    return render_template('DatasetList.html')

if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = 8889, debug=True, ssl_context='adhoc')
    app.run(debug=True)