from boa.interop.Neo.Storage import Get, Put, GetContext
from boa.interop.Neo.Runtime import Serialize, Deserialize

#build ../neo-deepfake/main.py test 07070707 07 True False False create_request video_id AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y txt_hash
#build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_id x x
#build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_id x x
#build ../neo-deepfake/main.py test 07070707 07 True False False approve_request video_id AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y txt_hash
#build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_id x x
#build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_id x x

def Main(arg0, arg1, arg2, arg3):
    ctx = GetContext()
    if arg0 == 'create_asset':
        return create_video_asset(ctx, arg1, arg2)

    elif arg0 == 'check_asset':
        return is_video_asset(ctx, arg1, arg2)


    # user operations
    elif arg0 == 'create_request':
        # video_hash, requester, text_hash
        create_request(ctx, arg1, arg2, arg3)
        return True

    elif arg0 == 'cancel_request':
        return cancel_request()

    # actor operations
    elif arg0 == 'approve_request':
        approve_request(ctx, arg1, arg2, arg3)
        return True

    # gets all requests that need to be approved for that video
    elif arg0 == 'list_requests':
        return list_requests(ctx, arg1)

    elif arg0 == 'list_approvals':
        return list_approvals(ctx, arg1)

    return False


# creates a request for the given video_hash, requested by a user, for a specific text hash
def create_request(ctx, video_hash, requester, text_hash):
    request_id = generate_request_id(video_hash, requester, text_hash)
    open_requests = get_open_requests_for_video(ctx, video_hash)

    # create request object to add to
    request = {"request_id": request_id, "requester": requester, "text": text_hash}

    open_requests[request_id] = request
    save_open_requests_for_video(ctx, video_hash, open_requests)


def list_requests(ctx, video_hash):
    open_requests = get_open_requests_for_video(ctx, video_hash)
    return open_requests


def list_approvals(ctx, video_hash):
    approved_requests = get_approvals_for_video(ctx, video_hash)
    return approved_requests


def approve_request(ctx, video_hash, requester, text_hash):
    request_id = generate_request_id(video_hash, requester, text_hash)
    open_requests = get_open_requests_for_video(ctx, video_hash)
    request = open_requests[request_id]
    open_requests[request_id] = None
    save_open_requests_for_video(ctx, video_hash, open_requests)

    # and add it to the approved ones
    approved_requests = get_approvals_for_video(ctx, video_hash)
    approved_requests[request_id] = request
    save_approvals_for_video(ctx, video_hash, approved_requests)


def generate_request_id(video_hash, requester, text_hash):
    return video_hash + text_hash  # + requester


def cancel_request():
    return True


def create_video_asset(ctx, owner, video_hash):
    Put(ctx, video_hash, owner)
    return True


def is_video_asset(ctx, owner, video_hash):
    return Get(ctx, video_hash) == owner


def get_open_requests_for_video(ctx, video_hash):
    request_key = "r_" + video_hash
    requests = Get(ctx, request_key)
    if not requests:
        return {}
    else:
        return Deserialize(requests)


def save_open_requests_for_video(ctx, video_hash, open_requests):
    request_key = "r_" + video_hash
    Put(ctx, request_key, Serialize(open_requests))


def get_approvals_for_video(ctx, video_hash):
    request_key = "a_" + video_hash
    requests = Get(ctx, request_key)
    if not requests:
        return {}
    else:
        return Deserialize(requests)


def save_approvals_for_video(ctx, video_hash, approved_requests):
    request_key = "a_" + video_hash
    Put(ctx, request_key, Serialize(approved_requests))
