
from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def insert_data():
    return "This is a post url "    


if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')
