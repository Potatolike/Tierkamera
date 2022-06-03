from flask import Flask, render_template, send_from_directory, request
import os

PICTURES_PER_PAGE=21
DIRECTORY_PATH = '/root/webcam/static'
app = Flask(__name__)

@app.get('/')
@app.get('/home')
def get_home():
    picturecount = len(os.listdir(DIRECTORY_PATH))
    page = request.args.get('page', default = 0, type = int)
    offset = page*PICTURES_PER_PAGE
    return render_template('index.html', title='Tierkamera', page=page, offset=offset, offsetend=offset+PICTURES_PER_PAGE, picturecount=picturecount)

@app.post('/')
@app.post('/home')
def post_home():
    size = 0
    for ele in os.scandir(DIRECTORY_PATH):
        size+=os.stat(ele).st_size
    print(size)
    if size > 1000000000:
        os.remove(DIRECTORY_PATH + '0.jpg')
        for count, f in enumerate(os.listdir(DIRECTORY_PATH)):
            f_name, f_ext = os.path.splitext(f)
            f_name = DIRECTORY_PATH + str(count)
 
            new_name = f'{f_name}{f_ext}'
            os.rename(f, new_name)

    index = str(len(os.listdir(DIRECTORY_PATH)))
    os.system(f'wget http://127.0.0.1:8080/?action=snapshot -O /root/webcam/static/{index}.jpg')
    try:
        return send_from_directory(DIRECTORY_PATH, index+".jpg", as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
   app.run(host='0.0.0.0')
