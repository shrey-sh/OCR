from PIL import Image
from flask import Flask, request, jsonify
import warnings
import os
from pytesseract import pytesseract
from werkzeug.utils import secure_filename

warnings.filterwarnings('ignore')


path_to_tesseract = r'C:/Program Files (x86)/tesseract/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/tesseract/tessdata"'
UPLOAD_FOLDER = 'D:/Internship_work/RFPautomation/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# path_to_image = 'sample_invoices.png'
#
# # Point tessaract_cmd to tessaract.exe
# # pytesseract.tesseract_cmd = path_to_tesseract
#
# # Open image with PIL
# img = Image.open(path_to_image)

# Extract text from image
# text = pytesseract.image_to_string(img)

# text = pytesseract.image_to_string(img, config=tessdata_dir_config)

@app.route("/invoice_data", methods=['POST'])
def invoice_data():
    # try:

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


    # except:
    #     return abort(403)


if __name__ == '__main__':
    app.run(debug=True)

# for row in text.split('/n'):
#     if row.startswith('TOTAL '):
#         print('true')
#         data = row.split()[-1]
#         print(data)