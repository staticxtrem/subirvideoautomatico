from flask import Flask, render_template, request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/subir-video', methods=['POST'])
def subir_video():
    video = request.files['video']
    title = request.form['title']
    hashtags = request.form['hashtags']
    upload_time = request.form['upload-time']

    # Lógica para subir el video a Google Drive
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    file_drive = drive.CreateFile()
    file_drive.SetContentFile(video)
    file_drive.Upload()

    # Lógica para procesar los datos y programar la subida del video a una hora específica
    # Aquí puedes agregar el código necesario para trabajar con la hora de subida y la planificación

    return 'Video subido correctamente'


if __name__ == '__main__':
    app.run()
