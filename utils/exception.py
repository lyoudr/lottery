from rest_framework.exceptions import APIException
from rest_framework import status

class CustomNotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    
    def __init__(self, detail=None, code=None):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.code = code