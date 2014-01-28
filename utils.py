import traceback
from re import compile

alphanum_pattern = compile("[\W_]+")

class BadRequestError(Exception): pass

def alphanum(string):
    return alphanum_pattern.sub("", string)

def log_error(e, message=None):
    try:
        print("-------------------")
        if message is not None: print(message)
        print("ERROR: " + str(e.__repr__()))
        print(traceback.format_exc())
        print("-------------------")
    except: print("ERROR IN log_error")

def request_arg(request, arg):
    try:
        ret = request.REQUEST[arg]
        if not ret:
            raise BadRequestError("%s empty" % arg)
        return ret
    except KeyError:
        raise BadRequestError("%s argument missing in request" % arg)

def optional_string_request_arg(request, arg):
    ret = request.REQUEST.get(arg)
    if not ret:
        return ""
    return ret

def optional_request_arg(request, arg):
    ret = request.REQUEST.get(arg)
    if not ret:
        return None
    return ret