import json


def getUser():
    with open("schemas/userDb.json","+r") as file:
        return json.load(file)
    
    
def saveUser(newUser):
    with open("schemas/userDb.json","+w") as file:
        return file.write(json.dumps(newUser,indent=4))