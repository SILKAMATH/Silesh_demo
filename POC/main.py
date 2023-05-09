from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # initialize web driver

print("enter url of base website")
Website1 = input()
print("enter url of new website")
Website2 = input()
#with webdriver.Chrome(options=chrome_options) as driver:  # navigate to the url
driver.get(Website1)

f = open(Website1, encoding="utf8")
content = f.read()
soup = BeautifulSoup(content, 'html.parser')
lst_class = ([node['class'] for node in soup.find_all() if node.has_attr('class')])
lst_class = flatten_list = [j for sub in lst_class for j in sub]  # flatten the list
lst_id = ([node['id'] for node in soup.find_all() if node.has_attr('id')])

print(lst_class)
print(lst_id)

lst_high = []

for class_name in lst_class:
    myDiv = driver.find_element(By.CLASS_NAME, class_name).value_of_css_property("font-size")
    # find font-size by id/class
    print("baseline font size - ", myDiv)

    driver.get(Website2)
    myDivX = driver.find_element(By.CLASS_NAME, class_name).value_of_css_property("font-size")
    print("Changed font size - ", myDivX)

    if myDiv != myDivX:
        print(class_name + ' have different font sizes')
        lst_high.append(class_name)
        myDivT = driver.find_element(By.CLASS_NAME, class_name)  # - to find the text
        print("text to be highlighted - ", myDivT.text)
        x = myDivT.text.split("\n")
        for i in x:
            for text in soup.find_all(string=i):
                text.wrap(soup.new_tag("mark"))
    else:
        print(class_name + ' have the same font size')

for id in lst_id:
    driver.get(Website1)
    myDiv = driver.find_element(By.ID, id).value_of_css_property("font-size")
    # find font-size by id/class
    print("baseline font size - ", myDiv)

    driver.get(Website2)
    myDivX = driver.find_element(By.ID, id).value_of_css_property("font-size")
    print("Changed font size - ", myDivX)

    if myDiv != myDivX:
        print(id + ' have different font sizes')
        lst_high.append(id)
        myDivT = driver.find_element(By.ID, id)  # - to find the text
        x = myDivT.text.split("\n")
        for i in x:
             for text in soup.find_all(string=i):
                 text.wrap(soup.new_tag("mark"))
    else:
        print(id + ' have the same font size')

print(lst_high)
with open("C:/Users/silkamath/Desktop/Webpage1/Lesson4/Result.html", "w") as fp:
    fp.write(str(soup))
