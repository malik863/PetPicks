from flask import Flask, render_template,request,jsonify
from PIL import Image
import numpy as np
import tensorflow as tf



app = Flask(__name__)


model = tf.keras.models.load_model('keras_model.h5')

target_size = (224,224)

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array,axis=0)

    return img_array


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files:
        return jsonify({
            'error':'There is no file'
        })

    file = request.files['file']

    if file.filename == '':
        return jsonify({
            'error':'No selected file'
        })
    
    try:
        img_array = preprocess_image(file)

        predictions = model.predict(img_array)
        print("hellllllllllllllllllllll0")
        class_index = np.argmax(predictions[0])
        

        if class_index == 0:
            result = 'cat'

        else:
            result  = 'dog'

        return jsonify({
            'result' : result
        })

    except Exception as e:
        return jsonify({
            'error':str(e)
        })
    





if __name__ == '__main__':
    app.run(debug=True)