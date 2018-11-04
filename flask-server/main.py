from flask import Flask, request, jsonify
import subprocess, requests, json

app = Flask(__name__)


@app.route('/')
def hello_world():
    # res = requests.post('http://localhost:8080/goToBlockchain', json={"mytext":"lalala"})
    # if res.ok:
    #     print(res.json())
    return 'Hello, World!'


@app.route('/deploy', methods=['POST'])
def deploy():
    write_to_file(request.json)
    try:
        result = subprocess.check_output(['./run.sh'], shell=False).decode("utf-8")
        #result = [line for line in result.split("\n") if str(line).startswith("Result")][0][7:]
        #result = result.replace('\'', '"')
        #print(result)
        return result
    except subprocess.CalledProcessError as e:
        return e
        return "An error occurred while trying to fetch task status updates."


def write_to_file(args):
    with open("settings.py", "w") as f:
        f.write("ENABLE_AUTO_INVOKE = True \n")
        for arg in args:
            f.write(arg + '= ' + json.dumps((args[arg])) + '\n')
