from flask import Flask, request, jsonify
import subprocess, requests, json

app = Flask(__name__)


@app.route('/create_asset', methods=['GET'])
def create_asset():
    return execute("create_asset.py")


@app.route('/get_video_owner', methods=['GET'])
def get_video_owner():
    return execute("get_video_owner.py")


@app.route('/approve_request_wrong', methods=['GET'])
def approve_request_wrong():
    return execute("approve_request_wrong.py")


@app.route('/approve_request', methods=['GET'])
def approve_request():
    return execute("approve_request.py")


@app.route('/create_request', methods=['GET'])
def create_request():
    return execute("create_request.py")


@app.route('/deploy', methods=['GET'])
def deploy():
    return execute("deploy.py")


@app.route('/list_approvals', methods=['GET'])
def list_approvals():
    return execute("list_approvals.py")


@app.route('/list_balance_actor', methods=['GET'])
def list_balance_actor():
    return execute("list_balance_actor.py")


@app.route('/list_balance_fanboy', methods=['GET'])
def list_balance_fanboy():
    return execute("list_balance_fanboy.py")


@app.route('/list_balance_owner', methods=['GET'])
def list_balance_owner():
    return execute("list_balance_owner.py")


@app.route('/list_requests', methods=['GET'])
def list_requests():
    return execute("list_requests.py")


def execute(filename):
    try:
        result = subprocess.check_output(['./run.sh', filename], shell=False).decode("utf-8")
        return str(result)
    except subprocess.CalledProcessError as e:
        return e
        return "An error occurred while trying to fetch task status updates."


"""
    Creating a request by Fanboy
"""

# open wallet fanboy.wallet
# build ../neo-deepfake/main.py test 07070707 07 True False False create_request video_1 AVEcFtSVVzTS3DapRQwfM4tW9jP7ZnJ61m hello_world
# build ../neo-deepfake/main.py test 07070707 07 True False False create_request video_1 APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ hello_world
# build ../neo-deepfake/main.py test 07070707 07 True False False create_request video_1 APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ bad_text
# build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_1 x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_1 x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_rejections video_1 x x
# build ../neo-deepfake/main.py test 07070707 07 True False False approve_request video_1 APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ hello_world
# build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_1 x x
"""
    approve request by Emma Watson
"""
# open wallet emmawatson.wallet
# build ../neo-deepfake/main.py test 07070707 07 True False False reject_request video_1 APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ bad_text
# build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_1 x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_1 x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_rejections video_1 x x
