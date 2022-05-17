from rest_framework.response import Response
import json

def sendresponse(response_status, response_message, response_data, status_code):
    """ send response to client """
    print("status = ", response_status)
    if response_status == 'success':
        return Response({
            'status': response_status,
            'message': response_message,
            'data': response_data
        }, status=status_code)
    else:
        print(" -- here ")
        return Response({
            'status': response_status,
            'errors': response_message
        }, status=status_code)

def verify_keys(key_list, request, message):
    missing = []
    for key in key_list:
        if key not in request.data.keys():
            missing.append(key)
    
    if len(missing) != 0:
        message = {**message, **{f"{miss}": f"{miss} is required" for miss in missing}}
        print(message)
        raise Exception("):")