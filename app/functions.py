def file_to_dict(fname):
    '''Read json file and return dictionary'''
    data = {}

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
    except IOError:
        data["error"] = "No data file"

    return data