from re import match
class APIError(Exception):
    def __init__(self,msg):
        self.msg=msg
        super().__init__(self.msg)
def checkstring(string,name):
    if not isinstance(string, str):
        raise TypeError(f"{name} must be a string")
    elif not string.isalpha():
        raise ValueError(f"{name} must be in English alphapatics only")

def checkint(num):
    if isinstance(num, int) :
        return True
    elif isinstance(num,str) and num.isdigit():
        return True
    else:
        return False

def checkhex(num:str):
    return bool(isinstance(num,str) and match("^[0-9a-f]+$",num))
def checkapi(apiresponse):
    if "error" in apiresponse.keys():
        raise APIError("Error: "+apiresponse["error"]["message"])
    