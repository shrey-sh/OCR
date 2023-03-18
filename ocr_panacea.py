from PIL import Image
from flask import Flask, request, jsonify
import warnings
import os
from pytesseract import pytesseract
from werkzeug.utils import secure_filename

warnings.filterwarnings('ignore')


path_to_tesseract = r'tesseract/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "tesseract/tessdata"'
UPLOAD_FOLDER = 'files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/invoice_data", methods=['POST'])
def invoice_data():

    if request.method == "POST":
        file = request.files['file']
        if file.filename != '':
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            filename = file.filename
            os.chdir(UPLOAD_FOLDER)
            try:
                os.remove('invoice.png')
            except:
                pass

            os.rename(filename, 'invoice.png')
            img = Image.open(r'invoice.png')
            result = pytesseract.image_to_string(img, config=tessdata_dir_config)

    return jsonify({'msg': result})

if __name__ == '__main__':
    app.run(debug=True)

