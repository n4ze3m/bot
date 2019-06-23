import urllib.request
import random
import time


count = 0
while (count <= 5):
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    
    upper_words = [word for word in words if word[0].isupper()]
    name_words  = [word for word in upper_words if not word.isupper()]
    one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
    def rand_name():
        name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
        return name
    for n in range(1):
        name = rand_name()
    def randString(length=10):
        your_letters='abcdefghi'
        return ''.join((random.choice(your_letters) for i in range(length)))
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.get(" URL ")
    el = driver.find_element_by_link_text("Get Started")
    el.click()
    def randString(length=10):
        your_letters='YOUR NAME WITHOUT SPACE'
        return ''.join((random.choice(your_letters) for i in range(length)))
    fbox = driver.find_element_by_class_name('vl-input-lg')
    fbox.send_keys(randString()+" P")

    def randString(length=10):
        your_letters='fsoreproplkjhnm'
        return ''.join((random.choice(your_letters) for i in range(length)))

    ebox = driver.find_element_by_id('form_email')
    ebox.send_keys(randString()+"@desoz.com")

    subbtn = driver.find_element_by_class_name('vl-btn-lg')
    subbtn.click()


    time.sleep(10)
    driver.close();

count=count+1
