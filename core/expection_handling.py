from urllib import request
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger(__name__)
def extract_error_messages(data):
    messages = []

    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, (list, tuple)):
                messages.extend(map(str, value))
            else:
                messages.append(str(value))
    elif isinstance(data, (list, tuple)):
        messages.extend(map(str, data))
    else:
        messages.append(str(data))

    messages = messages or ["Something went wrong!"]
    return "\n".join(messages)



def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    logger.exception(request, exc_info=True)

    if response is not None:
        return Response(
            {
                "success": False,
                "message": extract_error_messages(response.data),
                "errors": response.data,
            },
            status=response.status_code,
        )

    # For unhandled exceptions (500)
    return Response(
        {
            "success": False,
            "message": "Internal server error",
            "errors": {},
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
