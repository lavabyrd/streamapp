from flask import Flask
import threading

# Import the streamer file and function
import streamer

app = Flask(__name__)


@app.route('/')
def home():
    return "welcome to the home page. This is for personal use"

# Was using this as a method of starting the stream from an api call.
# This was not a requirement

@app.route('/start', methods=['GET'])
def start():
    # t.start()
    return "starting stream"

# At present this isn't working as you cannot just stop the thread and restart
# Need to investigate using a pause for the thread.

@app.route('/stop', methods=['GET'])
def stop():
    # t.stop()


# Takes the stream and assigns it to its own thread
# Tells it to also be a daemon so it'll cancel if the main process ends
t = threading.Thread(target=streamer.streamstart)
t.daemon=True

if __name__ == '__main__':
    t.start()
    app.run(debug=False)
