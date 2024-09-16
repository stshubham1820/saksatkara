from rest_framework import status

'''

    Here we are adding HTTP response status that should map with our response

'''


class response_status:
    status_code = {
    'data_not_created' : status.HTTP_304_NOT_MODIFIED,
    'data_not_found' : status.HTTP_404_NOT_FOUND,
    'required_field' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'update_failed' : status.HTTP_304_NOT_MODIFIED,
    'delete_failed' : status.HTTP_304_NOT_MODIFIED,
    'request_failed' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'json_parse_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'serializer_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'field_error' : status.HTTP_400_BAD_REQUEST,
    'success' : status.HTTP_200_OK,
    'created' : status.HTTP_201_CREATED,
    'updated' : status.HTTP_200_OK,
    'deleted' : status.HTTP_204_NO_CONTENT,
    'resumed' : status.HTTP_200_OK,
    'paused' : status.HTTP_200_OK,
    'enabled' : status.HTTP_200_OK,
    'server_error' : status.HTTP_500_INTERNAL_SERVER_ERROR,
    'value_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'key_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'service_request_timeout' : status.HTTP_500_INTERNAL_SERVER_ERROR,
    'access_forbidden_error' : status.HTTP_403_FORBIDDEN,
    'service_unavailable' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'attribute_error' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'password-incorrect' : status.HTTP_200_OK,
    'failed' : status.HTTP_400_BAD_REQUEST,
    'method_not_allowed' : status.HTTP_400_BAD_REQUEST,
    'audio_not_matched' : status.HTTP_401_UNAUTHORIZED,
    'invalid_access_key' : status.HTTP_401_UNAUTHORIZED,
    'audio_failed' : status.HTTP_400_BAD_REQUEST,
    'permission_denied':status.HTTP_403_FORBIDDEN,
    'key_limit_exceeded' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'user_already_exists' : status.HTTP_401_UNAUTHORIZED,
    'unspoken_audio' : status.HTTP_400_BAD_REQUEST,
    'lecture_already_recorded' : status.HTTP_422_UNPROCESSABLE_ENTITY,
    'already_accessed_accesstoken': status.HTTP_401_UNAUTHORIZED,
    }
