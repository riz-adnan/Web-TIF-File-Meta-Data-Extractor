from flask import Flask,render_template,request,send_file,Response
from werkzeug.datastructures import FileStorage
from PIL import Image, UnidentifiedImageError
import os
import io
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')




@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return "No file part"

    file: FileStorage = request.files['file']
    
    if file.filename == '':
        return "No selected file"

    if file:
        # Read the PDF file content into memory
        tiff_image=Image.open(file)
        meta=tiff_image.tag_v2
        print("meta",meta)
        info=tiff_image.info
        print("info",info)
        
        tiff_image.save("./static/output.pdf", "PDF", resolution=100.0, save_all=True)
        
        
        
        # Use the content to display the PDF directly without saving it
        return render_template("display.html",info=info,meta=meta)

    return "Invalid file type"
    
if(__name__=="__main__"):
    app.run(debug=True, port=8000)