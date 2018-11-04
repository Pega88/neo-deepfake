from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/status/')
def get_status():
    try:
        result = subprocess.check_output(['./run.sh'], shell=False)

        return result
    except subprocess.CalledProcessError as e:
        return e
        return "An error occurred while trying to fetch task status updates."

#
# if __name__ == '__main__':
#     app.run()