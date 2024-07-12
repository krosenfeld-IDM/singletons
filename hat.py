_contents = []

def pull():
    global _contents
    return _contents.pop()

def put(item):
    global _contents
    _contents.append(item)