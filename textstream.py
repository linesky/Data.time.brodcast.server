from flask import Flask, render_template, Response
import datetime
import time
#pip install flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    while True:
        yield f"data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        time.sleep(1)

@app.route('/time')
def time_stream():
    return Response(generate(), mimetype='text/event-stream')

print("\x1bc\x1b[47;34m")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

