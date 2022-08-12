def pytest_html_report_title(report):
    report.title = '登录功能测试报告'
    
def pytest_configure(config):
    config._metadata['Author'] = '钟嘉鸿'