import sys, pytest
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.11')
from tools.tool_login import login
from common.read_data import get_login_info

class TestLogin:
    # def setup_class(self):
    #     print('1. 打开浏览器')
        
    # def teardown_class(self):
    #     print('5. 关闭浏览器')
    
    # def setup(self):
    #     print('2. 打开登录页面')
        
    # def teardown(self):
    #     print('4. 关闭登录页面')
        
    @pytest.mark.parametrize('username, password, code, expect', get_login_info())
    def test(self, username, password, code, expect):
        assert expect == login(username, password, code)
        # print('3. 输入用户名，密码，验证码，点击登录')