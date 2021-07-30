from rest_framework.views import exception_handler


    
def customEcxeptionHandle(exc,context):
    handlers ={
        'ValidationError': _handle_generic_error,
        'IntegrityError' : _handle_numeric_error,
        'Http404' : _handle_generic_error,
    }

    response = exception_handler(exc, context)
    print("·········")
    print(response)
    if response is not None:
        response.data['satatus_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response 

def _handle_numeric_error(exc, context, response):
    print("5555555555555555555response")
    print(response)
    response.data = {
        'error':'Please, inserte only positive numbers'
    }
    return response


def _handle_generic_error(exc, context, response):
    return response
