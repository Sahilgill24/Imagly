from flask import Flask,render_template,Response
import cv2
import mediapipe as mp
import pyautogui
from main import videoon
import threading



app=Flask(__name__)

@app.route('/')

def first():
    return render_template('first.html')


@app.route('/second')

def second():
    return render_template('page2.html')


@app.route('/home')

def index():
    return render_template('home.html')
    

@app.route('/video')


def func():
    return videoon()






@app.route('/about')

def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus')

def contact():
    return render_template('contact.html')

@app.route('/dragdrop')

def dragdrop():
    return render_template('drag.html')




if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)