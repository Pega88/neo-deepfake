from boa.interop.Neo.Storage import Get, Put, Delete, GetContext
from boa.interop.Neo.Runtime import Serialize, Deserialize



def Main(operation, args):
    ctx = GetContext()
    if operation == 'create_asset':
        return create_video_asset(ctx, args[0], args[1])

    elif operation == 'check_asset':
        return is_video_asset(ctx, args[0], args[1])


    # user operations
    elif operation == 'create_request':
        # video_hash, requester, text_hash
        create_request(ctx, args[0], args[1], args[2])
        return True

    # elif operation == 'cancel_request':
    #    return True

    # actor operations
    elif operation == 'approve_request':
        return True

    # gets all requests that need to be approved for that video
    elif operation == 'list_requests':
        list_requests(ctx, args[0])
        return True;

    return False


def create_video_asset(ctx, owner, video_hash):
    Put(ctx, video_hash, owner)
    print("stored video hash ", video_hash, "for owner ", owner)
    return True


def is_video_asset(ctx, owner, video_hash):
    return Get(ctx, video_hash) == owner


# creates a request for the given video_hash, requested by a user, for a specific text hash
def create_request(ctx, video_hash, requester, text_hash):
    open_requests = get_open_requests_for_video(ctx, video_hash)
    request_id = video_hash + requester + text_hash
    request = {"requester": requester, "text": text_hash}
    open_requests[request_id] = request
    save_open_requests_for_video(ctx, video_hash, open_requests)


def approve_request(ctx, video_hash, requester, text_hash):
    request_id = video_hash + requester + text_hash
    open_requests = get_open_requests_for_video(ctx, video_hash)
    request = open_requests[request_id]
    print("request:" + request)
    open_requests[request_id] = None
    print("request:" + request)
    save_open_requests_for_video(ctx, video_hash, open_requests)

    # and add it to the approved ones
    approved_requests = get_approvals_for_video(ctx, video_hash)
    print("retrieved ", len(approved_requests), " approvals")
    approved_requests[request_id] = request
    save_approvals_for_video(ctx, video_hash, approved_requests)


def list_requests(ctx, video_hash):
    open_requests = get_open_requests_for_video(ctx, video_hash)
    print("requets for video hash:")
    print(open_requests)
    return open_requests


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
