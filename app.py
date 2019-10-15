from flask import Flask,render_template,url_for,request
import pytesseract
from PIL import Image
from gtts import gTTS

import os

app=Flask(__name__)
@app.route('/')
def home():
	
	return render_template('home.html')


@app.route('/predict',methods=['GET', 'POST'])

def predict():
	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
	if request.method=='POST':
		image_path= request.form.get("imagepath")
		imagename= request.form.get("imagename")
		img = Image.open(image_path)
		text = pytesseract.image_to_string(img)
		print(text)
		
		f = open("{0}.txt".format(imagename), 'w')
		f.write(text)
		f.close()
		f = open('{0}.txt'.format(imagename))
		x = f.read()

		language = 'en'
		audio = gTTS(text = x , lang = language , slow = False)
		audio.save("{0}.wav".format(imagename))
		os.system("{0}.wav".format(imagename))
		print('saved audio')
		
	return render_template('result.html',text=text)

if __name__ == '__main__':
	app.run(debug=True)
