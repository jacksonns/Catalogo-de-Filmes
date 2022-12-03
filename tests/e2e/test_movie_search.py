from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestMovieSearch():

    def test_movie_search(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get('http://127.0.0.1:5000')
        search_element = chrome_driver.find_element('name', 'movie_query')
        search_element.click()
        search_element.send_keys("Cidade de Deus")
        search_element.submit()
        url = '/movie/598'
        element = chrome_driver.find_element('xpath', '//a[@href="'+url+'"]')
        assert element is None

