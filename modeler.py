import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['nii.gz'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('index.html', home="home")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file: #and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('uploaded_file', filename=filename))
		return file.filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return render_template('index.html', display='uploads/' + filename)

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == '__main__':
	app.debug = True
	app.run()