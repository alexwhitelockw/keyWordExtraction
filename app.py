from flask import Flask, render_template, request
from gensim.summarization import keywords
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def text_upload():
    return render_template("index.html")

@app.route('/results', methods=["GET", "POST"])
def key_word():

    kwOutput = keywords(request.form['textUp'],
                        split=True)

    return render_template("kwResults.html",
                           keywords=kwOutput)

if __name__ == '__main__':
    #app.run()
    http_server=WSGIServer(("", 5000), app)
    http_server.serve_forever()
