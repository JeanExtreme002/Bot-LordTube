import json

def get_json(filename):

    with open(filename) as file:
        return json.loads(file.read())


def get_login_from(filename):

    data = get_json(filename)

    if "login" in data and "email" in data["login"] and data["login"]["email"]: 
        email = data["login"]["email"] 
    else: 
        email = input("\n Email: ")

    if "login" in data and "password" in data["login"] and data["login"]["password"]: 
        password = data["login"]["password"] 
    else: 
        password = input(" Password: ")

    return {"email": email, "password": password}


def get_video_url_from(filename):

    data = get_json(filename)
    video_url = data["video"] if "video" in data and data["video"] else input(" Video URL: ")
    
    return {"videoUrl": video_url}


login_data = get_login_from("data.json")
send_data = get_video_url_from("data.json")

login_url = "https://lordtube.herokuapp.com/oauth/token"
send_url = "https://lordtube.herokuapp.com/api/videos/sendVideo"


