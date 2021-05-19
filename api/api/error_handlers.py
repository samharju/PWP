from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import exception_handler


def _get_error_messages(data):
    """Parse error messages from default error responses"""
    out = []
    for key, value in data.items():

        if isinstance(value, (list, dict)):
            out.append(f'{key}: {" ".join([str(v) for v in value])}')
        else:
            out.append(str(value))
    return out if len(out) > 1 else out[0]


def custom_exception_handler(exc, context):
    # https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        msg = _get_error_messages(response.data)
        if isinstance(response.data, (list, dict)) and len(response.data) > 1:
            error = {
                '@message': 'Multiple errors',
                '@messages': msg
            }
        else:
            error = {
                '@message': msg
            }
        mason = {'@error': error}
        return Response(
            status=response.status_code,
            data=mason,
            headers=response.headers
        )

    return response


def mason_error(msg, status=HTTP_400_BAD_REQUEST):
    """Constructor for view-specific error responses"""
    return Response(
        data={
            '@error': {
                '@message': msg
            }
        },
        status=status
    )
