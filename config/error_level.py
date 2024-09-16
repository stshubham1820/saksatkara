
'''

    Here we are adding error_level that should map with our logging level
'''

class error_level:
    response_code = {
    'data_not_created' : 'error',
    'data_not_found' : 'warning',
    'required_field' : 'warning',
    'request_failed' : 'error',
    'json_parse_error' :'warning',
    'serializer_error' : 'warning',
    'field_error' : 'warning',
    'validation_error' : 'warning',
    'page_not_found' : 'error',
    'server_error' : 'error',
    'value_error' : 'error',
    'key_error' : 'error',
    'service_request_timeout' : 'error',
    'access_forbidden_error' : 'warning',
    'service_unavailable' : 'error',
    'attribute_error' : 'error',
    'out_of_stock' : 'warning',
    'update_failed' : 'error',
    'delete_failed' : 'error',
    'method_not_allowed' : 'warning',
    'audio_not_matched' : 'warning',
    'invalid_access_key' : 'warning',
    'audio_failed' : 'warning',
    'permission_denied' : 'warning',
    'key_limit_exceeded' : 'info',
    'user_already_exists' : 'warning',
    'unspoken_audio' : 'warning',
    'lecture_already_recorded' : 'warning',
    'already_accessed_accesstoken':'warning',
}


