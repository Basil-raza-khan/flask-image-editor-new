from flask import Flask, render_template, request, flash, send_from_directory
from werkzeug.utils import secure_filename
import cv2  # type: ignore
import os

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['STATIC_FOLDER'] = STATIC_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
def process_Image(filename, operation):
    print(f"The operation is {operation} and file name is {filename}")
    img = cv2.imread(os.path.join(UPLOAD_FOLDER, filename))
    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"{filename.split('.')[0]}.jpg"
            newFilename = os.path.join(STATIC_FOLDER, newFilename)
            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        case "cwebp": 
            newFilename = f"{filename.split('.')[0]}.webp"
            newFilename = os.path.join(STATIC_FOLDER, newFilename)
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cjpg": 
            newFilename = f"{filename.split('.')[0]}.jpg"
            newFilename = os.path.join(STATIC_FOLDER, newFilename)
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cpng": 
            newFilename = f"{filename.split('.')[0]}.png"
            newFilename = os.path.join(STATIC_FOLDER, newFilename)
            cv2.imwrite(newFilename, img)
            return newFilename
    pass

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get('operation')
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'error'
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return 'Error No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = process_Image(filename, operation)
            download_link = f"/download/{os.path.basename(new)}"
            flash(f"Your image has been processed and is available <a href='{download_link}' target='_blank'>here</a>")
            return render_template('index.html')
    
    return render_template("about.html")

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False)
