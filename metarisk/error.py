import json
from django.http.response import HttpResponse
from metarisk import globals

# success constants
OK = 'OK'

# error constants
RISKTYPE_EXISTS = 'Risk type already exists'
RISKTYPE_CONTENT_DECODE_ERROR = "Invalid risk type object"
RISKTYPE_CONTENT_ERROR = "An error in the risk type json object"
RISKTYPE_NAME_EMPTY = "Risk type name is empty or not a string"
RISKTYPE_ATTR_INFO_EMPTY = "Risk type attribute name or type is empty or not a string"
RISKTYPE_NOT_EXISTS = "Risk type does not exist"
HTTP_METHOD_NOT_SUPPORTED = "Method not supported"
RISKTYPE_COULD_NOT_BE_CREATED = "Risk type could not be created"
RISKTYPE_ATTR_COULD_NOT_BE_CREATED =  "Risk type attribute could not be created"
RISKTYPE_ATTR_TYPE_INVALID = "Risk type attribute type is invalid"
RISKTYPE_ATTR_ENUM_INFO_EMPTY = "Risk type attribute enum info is invalid"
RISKTYPE_ATTR_ENUM_ENTRY_COULD_NOT_BE_CREATED = "Risk type attribute enum entry could not be created"

class RTException(Exception):
    def __init__(self, message, statuscode=400):
        Exception.__init__(self)
        self.message = message
        self.statuscode = statuscode

    def to_dict(self):
        rv = {}
        rv[globals.MSG] = self.message
        return rv

def handle_RT_exception(error):
    r = HttpResponse(content=json.dumps(error.to_dict()), content_type='application/json')
    r.status_code = error.statuscode
    return r