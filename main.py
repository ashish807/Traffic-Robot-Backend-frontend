import unicodedata
from flask import Flask, jsonify,render_template,make_response
from flask_restful import Api,Resource
import os
import pickle
import cv2
import numpy as np
from flask import url_for, send_from_directory, request
import logging, os
import requests
from flask import Flask, request 
import re
from mysqlDataFetch import *
from werkzeug.utils import secure_filename
from gtts import gTTS
app = Flask(__name__)
api=Api(app)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)



@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods = ['POST'])
class Upload(Resource):
    def post(self,lang):
        if request.method == 'POST':
            print(lang)
            finalResult=chatAnswer(lang)
            headers = {'Content-Type': 'text/html','charset':'utf-8'}
            print(finalResult)
            if(finalResult!="No"):
                return make_response(render_template('response.html',output=finalResult),200,headers)
            else:
                sorry ="Sorry, I cannot answer that at the moment but I will improve myself"
                return make_response(render_template('response.html',output=sorry),200,headers)
        else:
            return "Didn't received"

api.add_resource(Upload,"/upload/<string:lang>")



if __name__ == '__main__':
    print("Initiated program")
    app.run(debug=True)
