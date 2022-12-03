import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestMoviePage():

    def test_movie_page_with_review(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get('http://127.0.0.1:5000')
        search_element = chrome_driver.find_element('name', 'movie_query')
        search_element.click()
        search_element.send_keys("Terrifier 2")
        search_element.submit()
        url = '/movie/663712'
        movie = chrome_driver.find_element('xpath', '//a[@href="'+url+'"]')
        movie.click()
        with pytest.raises(Exception):
            no_reviews = chrome_driver.find_element('xpath', "//*[contains(text(), 'Este filme não tem críticas')]")
        new_review = chrome_driver.find_element('xpath', "//*[contains(text(), 'Escrever nova crítica')]")
        assert new_review is not None

    def test_movie_page_without_review(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.get('http://127.0.0.1:5000')
        search_element = chrome_driver.find_element('name', 'movie_query')
        search_element.click()
        search_element.send_keys("Terrifier")
        search_element.submit()
        url = '/movie/420634'
        movie = chrome_driver.find_element('xpath', '//a[@href="'+url+'"]')
        movie.click()
        no_reviews = chrome_driver.find_element('xpath', "//*[contains(text(), 'Este filme não tem críticas')]")
        assert no_reviews is not None
        new_review = chrome_driver.find_element('xpath', "//*[contains(text(), 'Escrever nova crítica')]")
        assert new_review is not None
