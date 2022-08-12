def login(username, password, code):
    if username == 'admin' and password == '123456' and code == '8888':
        return '登录成功'
    else:
        return '登录失败'