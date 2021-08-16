def response_mapper(response_list, key=None):
    if key:
        return [stadistic[key] for stadistic in response_list]
    return response_list
