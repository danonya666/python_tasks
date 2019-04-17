def to_json(func):
    def wrapped(*args):
        jsoned = {}
        res = func(*args)
        for i in res:
            key = i[0]
            val = i[1]
            jsoned[key] = val
        return jsoned

    return wrapped


@to_json
def get_data():
    return [["data", 42]]


print(get_data())
