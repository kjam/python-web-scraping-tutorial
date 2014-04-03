from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

MY_EMAIL = ''
MY_PASSWORD = ''
MY_PROFILE_NAME = ''

browser = webdriver.Firefox()
browser.get('http://netflix.com')
browser.find_element_by_link_text('Sign In').click()
email = browser.find_element_by_css_selector('input#email')
email.send_keys(MY_EMAIL)
pw = browser.find_element_by_css_selector('input#password')
pw.send_keys(MY_PASSWORD, Keys.RETURN)
browser.implicitly_wait(10)  # seconds
browser.find_element_by_link_text(MY_PROFILE_NAME).click()
browser.maximize_window()
rows = browser.find_elements_by_css_selector('div.mrow')

for r in rows:
    if 'Top Picks' in r.text:
        top_pix = r
        break

movie_recs = top_pix.find_elements_by_css_selector(
    'div.agMovieSet div.agMovie')


first_movie = movie_recs[0].location
scroll_down = ActionChains(browser).move_by_offset(
    10, first_movie.get('y') - 10)
scroll_down.perform()

movie_dict = {}

for movie in movie_recs:
    movie_link = movie.find_element_by_css_selector('a.bobbable')
    try:
        arrow = top_pix.find_element_by_css_selector('div.next.sliderButton')
        if arrow.location.get('x') - movie_link.location.get('x') < 80:
            hover = ActionChains(browser).move_to_element(arrow)
            hover.perform()
            sleep(4)
        hover = ActionChains(browser).move_to_element(movie_link)
        hover.perform()
    except Exception, e:
        print e
        hover = ActionChains(browser).move_to_element(arrow)
        hover.perform()
        sleep(5)
        move_off_arrow = ActionChains(browser).move_by_offset(-450, -130)
        move_off_arrow.perform()
        hover = ActionChains(browser).move_to_element(movie_link)
        hover.perform()
    try:
        movie_info = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'BobMovie')))
        title = movie_info.find_element_by_class_name('title').text
        link = movie_info.find_element_by_class_name(
            'mdpLink').get_attribute('href')
        desc = movie_info.find_element_by_class_name(
            'bobMovieContent').text.split('\n')[0]
        cast = movie_info.find_element_by_tag_name('dd').text
        movie_dict[title] = {'link': link, 'title': title,
                             'desc': desc, 'cast': cast}
    except:
        print "taking too long!"
    scroll_off = ActionChains(browser).move_by_offset(30, -130)
    scroll_off.perform()
    sleep(2)
