from selenium import webdriver
import os
from urllib.request import urlopen
from contextlib import closing
import xml.etree.ElementTree
from getpass import getpass
from pyowm import OWM
import re
import requests
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import urllib.request
import urllib.request, urllib.error, urllib.parse


#Optimisation - 1, Using msvcrt module to break down runtime of code in sections according to user instead of continuous execution.
import msvcrt
#User Menu, Input based module selection

print("\n\t\t\t\t\tWelcome to the Python and Selenium toolset\n")
pp=1
while(pp>0):
    print("1. Multiple Link opener")
    print("2. Weather report")
    print("3. Image scraper")
    print("4. News scraper")
    print("5. Facebook login automation\n")
    print("6. Exit\n")
    n=input("Enter your selection: ")
    try:
        n=int(n)
    except:
        print("\nERROR: String input, please try again\n")
        print('\npress any key to continue: ')
        char = msvcrt.getch()
        continue
    #Accessing the Multiple link opener module
    if(n==1):
        k=int(input('With prefix (https://www.) (1) or without (2) ?'))
        s=input('Enter the links to be opened: (separated by spaces): ')
        l=s.split()
        t=len(l)
        #Optimisation - 2, creating list through implicit list iterations
        if(k==2):
            for elements in l:
                elements = ['https://www.' + elements + '' for elements in l]
        elif(k==1):
            for elements in l:
                elements = [elements for elements in l]
        def open_tab_page(page, page_number):
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[page_number])
            driver.get(page)
        # initialise driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com")
        page_number = 1
        for page in elements:
            open_tab_page(page, page_number)
            page_number +=1
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        print('\n')
        
    #Accessing the Weather report module
    elif(n==2):
        owm=OWM('3282e54688306ae3571e778e51429885')
        s=input('Enter the city to get weather details: ')
        print("\n")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(s)
        weather = observation.weather
        temperature=weather.temperature('celsius')
        wind = weather.wind()
        humid = weather.humidity
        status = weather.detailed_status
        print('The temperature in '+s+' is '+ str(temperature) + ' degrees celsius')
        print('Wind speeds are '+str(wind)+' m/s')
        print('Humidity is '+str(humid)+' %')
        print('Current status of '+s+' is '+status)
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        print('\n')

    #Accessing the Image scraper module
    elif(n==3):
        #Using OS directory to create folders in working directory
        parent_dir = "C:/Users/aksha/Desktop/Fall 2K20-21/pics/"
        
        directory = "images"
        
        # Path 
        path = os.path.join(parent_dir, directory) 
        
        os.mkdir(path)
        
        #taking user input
        print("What do you want to download?")
        download = input()
        site = 'https://www.google.com/search?tbm=isch&q='+download
        
        
        #providing driver path
        driver = webdriver.Chrome(executable_path='C:\Windows\System32\drivers\chromedriver.exe')
        
        #passing site url
        driver.get(site)
        
        
        #if you just want to download 10-15 images then skip the while loop and just write
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        
        
        #below while loop scrolls the webpage 7 times(if available)
        '''
        i = 0
        
        while i<7:  
        	#for scrolling page
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            
            try:
        		#for clicking show more results button
                driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
            except Exception as e:
                pass
            time.sleep(5)
            i+=1
        '''
        
        #parsing
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        
        #closing web browser
        driver.close()
        
        
        #scraping image urls with the help of image tag and class used for images
        img_tags = soup.find_all("img", class_="rg_i")
        
        
        count = 0
        for i in img_tags:
            print(i['src'])
            try:
        		#passing image urls one by one and downloading
                urllib.request.urlretrieve(i['src'], str(count)+".jpg")
                count+=1
                print("Number of images downloaded = "+str(count),end='\r')
            except Exception as e:
                pass
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        input()       
            
   
    #Accessing the News scraper module
    elif(n==4):
        news_url = "https://news.google.com/news/rss"
        with closing(urlopen(news_url)) as page:
            xml_page = page.read()
        print("\nDisplaying the top 5 stories of today:\n")
        e = xml.etree.ElementTree.fromstring(xml_page)
        p = 1
        for it in e.iter('item'):
            if(p>5):
                break
            
            else:
                print(it.find('title').text)
                print(it.find('link').text)
                print(it.find('pubDate').text)
                print('\n')
                p=p+1
        #Optimisation - 4 , using the msvcrt module to break loop operations according to user input.
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        input()
        
        #Accessing the Facebook automated login module
    elif(n==5):
        username=input('Enter username:')
        password=getpass()
        url='https://facebook.com'
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('u_0_b').click()
        print('\npress any key to exit: ')
        char = msvcrt.getch()
        
    elif(n==6):
        print("Exitiing!")
        break
    
    #In case of invalid input
    else:
        print("Invalid input")
        print('\npress any key to continue: ')
        char = msvcrt.getch()
