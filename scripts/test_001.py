
import allure,pytest

class Test_001(object):


    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(tittle="这是测试方法一")
    def test_001(self):
        allure.attch("标题","标题内容")
        print("你好吗?")
        assert True