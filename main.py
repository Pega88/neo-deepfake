from boa.builtins import concat
from boa.interop.Neo.Storage import Get, Put, GetContext, Delete
from boa.interop.Neo.Runtime import Serialize, Deserialize, CheckWitness
from boa.interop.Neo.Action import RegisterAction

# setup token
# build ../neo-deepfake/main.py test 07070707 02 True False False deploy x x x
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y x x
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf AVEcFtSVVzTS3DapRQwfM4tW9jP7ZnJ61m x x
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ x x
# build ../neo-deepfake/main.py test 07070707 07 True False False transfer AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ 5000
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y x x
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf AVEcFtSVVzTS3DapRQwfM4tW9jP7ZnJ61m x x
# build ../neo-deepfake/main.py test 07070707 02 True False False balanceOf APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ x x

# build ../neo-deepfake/main.py test 07070707 07 True False False create_request video_id APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ txt1
# build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_id x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_id x x
# build ../neo-deepfake/main.py test 07070707 07 True False False approve_request video_id APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ txt1
# build ../neo-deepfake/main.py test 07070707 07 True False False list_approvals video_id x x
# build ../neo-deepfake/main.py test 07070707 07 True False False list_requests video_id x x

# -------------------------------------------
# TOKEN SETTINGS
# -------------------------------------------

# https://github.com/CityOfZion/neo-python/issues/183 --> A: Helper.AddrStrToScriptHash('AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y').Data should work but does not
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'  # AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y -> KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr
# fanboy = b'R\x99\x93\xf3\xdf\xc9\xd3\xa4#\xd5\xf8\x9e\x14\x11y\x1d\xd2B\xa1S' #APJd31aTbK4T3qsj45e6uL39FTwX8EGuHJ --> L2ejWJVMwcXg7jwVnmiC8fRfMM8mbBpTxAoZKXXzSRgwggAGP3sC
video_owner = b'\x93\xa8\x04\xf5B\'\xfci\xeb\xed@\xef\x82\xf7x\%di\xe0'  # AVEcFtSVVzTS3DapRQwfM4tW9jP7ZnJ61m --> L2mRdKbKBUFRsAhvs1wbog5SrSyyysSmYg8NwCZqC87YogGb3Qb2
# Script hash of the contract owner

# Name of the Token
TOKEN_NAME = 'DeepFake Token'

# Symbol of the Token
TOKEN_SYMBOL = 'DVL'

# Number of decimal places
TOKEN_DECIMALS = 8

# Total Supply of tokens in the system
TOKEN_TOTAL_SUPPLY = 10000000 * 100000000  # 10m total supply * 10^8 ( decimals)

ctx = GetContext()

# -------------------------------------------
# Events
# -------------------------------------------

OnTransfer = RegisterAction('transfer', 'addr_from', 'addr_to', 'amount')
OnApprove = RegisterAction('approve', 'addr_from', 'addr_to', 'amount')


def Main(arg0, arg1, arg2, arg3):
    if arg0 == 'create_asset':
        video_id = arg1
        owner = arg2
        return create_video_asset(ctx, video_id, video_owner)

    # user operations
    elif arg0 == 'create_request':
        # video_id, requester, text_hash
        return create_request(ctx, arg1, arg2, arg3)

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

    elif arg0 == 'name':
        return TOKEN_NAME

    elif arg0 == 'decimals':
        return TOKEN_DECIMALS

    elif arg0 == 'symbol':
        return TOKEN_SYMBOL

    elif arg0 == 'totalSupply':
        return TOKEN_TOTAL_SUPPLY

    elif arg0 == 'balanceOf':
        account = arg1
        return do_balance_of(ctx, account)

    elif arg0 == 'transfer':
        t_from = arg1
        t_to = arg2
        t_amount = arg3
        return do_transfer(ctx, t_from, t_to, t_amount)

    elif arg0 == 'transferFrom':
        t_from = arg1
        t_to = arg2
        t_amount = arg3
        return do_transfer_from(ctx, t_from, t_to, t_amount)

    elif arg0 == 'approve':
        t_owner = arg1
        t_spender = arg2
        t_amount = arg3
        return do_approve(ctx, t_owner, t_spender, t_amount)


    elif arg0 == 'allowance':
        t_owner = arg1
        t_spender = arg2
        return do_allowance(ctx, t_owner, t_spender)

    elif arg0 == "deploy":
        return deploy()

    return 'unknown operation'
    return False


########################
########################
###                  ###
###  OPEN REQUESTS   ###
###                  ###
########################
########################

# creates a request for the given video_id, requested by a user, for a specific text hash
def create_request(ctx, video_id, requester, text_hash):
    # hold 500 DVL in escrow
    if not do_transfer(ctx, requester, OWNER, 500):
        print("could not put money in escrow")
        return False

    request_id = generate_request_id(video_id, requester, text_hash)
    open_requests = get_open_requests_for_video(ctx, video_id)

    # create request object to add to
    request = {"request_id": request_id, "requester": requester, "text": text_hash}

    open_requests[request_id] = request
    save_open_requests_for_video(ctx, video_id, open_requests)
    return True


def list_requests(ctx, video_id):
    open_requests = get_open_requests_for_video(ctx, video_id)
    return open_requests


def get_open_requests_for_video(ctx, video_id):
    request_key = "r_" + video_id
    requests = Get(ctx, request_key)
    if not requests:
        return {}
    else:
        return Deserialize(requests)


def save_open_requests_for_video(ctx, video_id, open_requests):
    request_key = "r_" + video_id
    Put(ctx, request_key, Serialize(open_requests))


def cancel_request():
    return True


########################
########################
###                  ###
###    APPROVALS     ###
###                  ###
########################
########################


def approve_request(ctx, video_id, requester, text_hash):
    do_transfer(ctx, OWNER, video_owner, 450)

    request_id = generate_request_id(video_id, requester, text_hash)
    open_requests = get_open_requests_for_video(ctx, video_id)
    request = open_requests[request_id]
    open_requests[request_id] = None
    save_open_requests_for_video(ctx, video_id, open_requests)

    # and add it to the approved ones
    approved_requests = get_approvals_for_video(ctx, video_id)
    approved_requests[request_id] = request
    save_approvals_for_video(ctx, video_id, approved_requests)


def list_approvals(ctx, video_id):
    approved_requests = get_approvals_for_video(ctx, video_id)
    return approved_requests


def get_approvals_for_video(ctx, video_id):
    request_key = "a_" + video_id
    requests = Get(ctx, request_key)
    if not requests:
        return {}
    else:
        return Deserialize(requests)


def save_approvals_for_video(ctx, video_id, approved_requests):
    request_key = "a_" + video_id
    Put(ctx, request_key, Serialize(approved_requests))


def generate_request_id(video_id, requester, text_hash):
    return text_hash  # + requester


########################
########################
###                  ###
###   VIDEO OWNER    ###
###                  ###
########################
########################

def create_video_asset(ctx, video_id, video_owner):
    # check if current user is actually the provided key
    if CheckWitness(video_owner):
        request_key = "o_" + video_id
        print(request_key)
        Put(ctx, request_key, video_owner)
        return True
    return False


def is_video_owner(ctx, video_id, video_owner):
    request_key = "o_" + video_id
    return Get(ctx, request_key) == video_owner


########################
########################
###                  ###
###      NEP-5       ###
###                  ###
########################
########################

def do_balance_of(ctx, account):
    """
    Method to return the current balance of an address
    :param account: the account address to retrieve the balance for
    :type account: bytearray
    :return: the current balance of an address
    :rtype: int
    """

    if len(account) != 20:
        return 0

    return Get(ctx, account)


def do_transfer(ctx, t_from, t_to, amount):
    """
    Method to transfer NEP5 tokens of a specified amount from one account to another
    :param t_from: the address to transfer from
    :type t_from: bytearray
    :param t_to: the address to transfer to
    :type t_to: bytearray
    :param amount: the amount of NEP5 tokens to transfer
    :type amount: int
    :return: whether the transfer was successful
    :rtype: bool
    """

    if amount <= 0:
        return False

    if len(t_from) != 20:
        return False

    if len(t_to) != 20:
        return False

    if True:  # CheckWitness(t_from):

        if t_from == t_to:
            print("transfer to self!")
            return True

        from_val = Get(ctx, t_from)

        if from_val < amount:
            print("insufficient funds")
            return False

        if from_val == amount:
            Delete(ctx, t_from)

        else:
            difference = from_val - amount
            Put(ctx, t_from, difference)

        to_value = Get(ctx, t_to)

        to_total = to_value + amount

        Put(ctx, t_to, to_total)

        OnTransfer(t_from, t_to, amount)

        return True
    else:
        print("from address is not the tx sender")

    return False


def do_transfer_from(ctx, t_from, t_to, amount):
    """
    Method to transfer NEP5 tokens of a specified amount from one account to another
    :param t_from: the address to transfer from
    :type t_from: bytearray
    :param t_to: the address to transfer to
    :type t_to: bytearray
    :param amount: the amount of NEP5 tokens to transfer
    :type amount: int
    :return: whether the transfer was successful
    :rtype: bool
    """

    if amount <= 0:
        return False

    if len(t_from) != 20:
        return False

    if len(t_to) != 20:
        return False

    available_key = concat(t_from, t_to)

    available_to_to_addr = Get(ctx, available_key)

    if available_to_to_addr < amount:
        print("Insufficient funds approved")
        return False

    from_balance = Get(ctx, t_from)

    if from_balance < amount:
        print("Insufficient tokens in from balance")
        return False

    to_balance = Get(ctx, t_to)

    new_from_balance = from_balance - amount

    new_to_balance = to_balance + amount

    Put(ctx, t_to, new_to_balance)
    Put(ctx, t_from, new_from_balance)

    print("transfer complete")

    new_allowance = available_to_to_addr - amount

    if new_allowance == 0:
        print("removing all balance")
        Delete(ctx, available_key)
    else:
        print("updating allowance to new allowance")
        Put(ctx, available_key, new_allowance)

    OnTransfer(t_from, t_to, amount)

    return True


def do_approve(ctx, t_owner, t_spender, amount):
    """
    Method by which the owner of an address can approve another address
    ( the spender ) to spend an amount
    :param t_owner: Owner of tokens
    :type t_owner: bytearray
    :param t_spender: Requestor of tokens
    :type t_spender: bytearray
    :param amount: Amount requested to be spent by Requestor on behalf of owner
    :type amount: bytearray
    :return: success of the operation
    :rtype: bool
    """

    if len(t_owner) != 20:
        return False

    if len(t_spender) != 20:
        return False

    if not CheckWitness(t_owner):
        return False

    if amount < 0:
        return False

    # cannot approve an amount that is
    # currently greater than the from balance
    if Get(ctx, t_owner) >= amount:

        approval_key = concat(t_owner, t_spender)

        if amount == 0:
            Delete(ctx, approval_key)
        else:
            Put(ctx, approval_key, amount)

        OnApprove(t_owner, t_spender, amount)

        return True

    return False


def do_allowance(ctx, t_owner, t_spender):
    """
    Gets the amount of tokens that a spender is allowed to spend
    from the owners' account.
    :param t_owner: Owner of tokens
    :type t_owner: bytearray
    :param t_spender: Requestor of tokens
    :type t_spender: bytearray
    :return: Amount allowed to be spent by Requestor on behalf of owner
    :rtype: int
    """

    if len(t_owner) != 20:
        return False

    if len(t_spender) != 20:
        return False

    return Get(ctx, concat(t_owner, t_spender))


def deploy():
    """

    :param token: Token The token to deploy
    :return:
        bool: Whether the operation was successful
    """
    # if not CheckWitness(OWNER):
    #    print("Must be owner to deploy")
    #    return False

    if not Get(ctx, 'initialized'):
        # do deploy logic
        Put(ctx, 'initialized', 1)
        Put(ctx, OWNER, TOKEN_TOTAL_SUPPLY)
        # dispatch transfer event for minting
        OnTransfer(None, OWNER, TOKEN_TOTAL_SUPPLY)
        return True

    return False
