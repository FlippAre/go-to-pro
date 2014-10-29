import os
from bottle import route, request, static_file, run

@route('/')
def root():
    return static_file('web/main.html', root='.')

@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('fileToUpload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.csv'):
        return "File extension not allowed."

    save_path = "./tmp"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)

if __name__ == '__main__':
    run(host='localhost', port=8080)