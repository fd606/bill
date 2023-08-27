from json import loads, dumps

def readjson(filename):
    with open(filename , "r") as f:
        return loads(f.read())

def writejson(filename, data):
    with open(filename, "w") as f:
        f.write(dumps(data, indent=4))
