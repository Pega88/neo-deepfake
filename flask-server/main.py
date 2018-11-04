from flask import Flask, request, jsonify
import subprocess, requests, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    # res = requests.post('http://localhost:8080/goToBlockchain', json={"mytext":"lalala"})
    # if res.ok:
    #     print(res.json())
    return 'Hello, World!'


@app.route('/goToBlockchain', methods=['GET', 'POST'])
def go_to_chain():
    content = request.json
    write_to_file(request.json)
    return jsonify(content)


@app.route('/status/')
def get_status():
    try:
        result = subprocess.check_output(['./run.sh'], shell=False)
        result = [line for line in str(result).split("\n") if str(line).startswith("Result")]
        return str(result)
    except subprocess.CalledProcessError as e:
        return e
        return "An error occurred while trying to fetch task status updates."


def write_to_file(args):
    with open("settings.py", "w") as f:
        f.write("ENABLE_AUTO_INVOKE = True \n")
        for arg in args:
            f.write(arg + '= ' + json.dumps((args[arg])) + '\n')


