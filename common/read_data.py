import json
from config import BASE_DIR

def get_login_info():
    with open(BASE_DIR + '/data/login.json', encoding = 'utf-8') as f:
        login_info = json.load(f)
    
    new_user_list = []
    for d in login_info:
        d.pop('desc')
        new_user_list.append(tuple(d.values()))
    return new_user_list
        