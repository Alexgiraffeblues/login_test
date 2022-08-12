class TestFixture:
    def setup_class(self):
        print('1. 打开浏览器')
        
    def teardown_class(self):
        print('5. 关闭浏览器')
    
    def setup(self):
        print('2. 打开登录页面')
        
    def teardown(self):
        print('4. 关闭登录页面')
        
    def test_func_01(self):
        print('3. 输入用户名1，密码1，验证码1，点击登录')
        
    def test_func_02(self):
        print('3. 输入用户名2，密码2，验证码3，点击登录')
        
    def test_func_03(self):
        print('3. 输入用户名3，密码3，验证码3，点击登录')