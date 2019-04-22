def remove_keys(dict1, ignored):
    if isinstance(ignored, dict):
        for key in ignored:
            if isinstance(ignored[key], bool) and ignored[key] == True:
                if dict1 is not None and key in dict1:
                    del dict1[key]
            if isinstance(ignored[key], dict) or isinstance(ignored[key], list):
                arg1 = None
                if dict1 is not None and key in dict1:
                    arg1 = dict1[key]
                remove_keys(arg1, ignored[key])
    if isinstance(ignored, list):
        if dict1 is not None and isinstance(dict1, list):
            for item in dict1:
                remove_keys(item, None, ignored[0])

