# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:23:58 2020

@author: Charlie

This is a scraper for stackOverflow
"""

from bs4 import BeautifulSoup
from xlwt import Workbook

import requests


class job:
    
    def __init__(self, title='', company='', location='', posted = '', salary='', link = ''):
        self.title = title
        self.company = company
        self.location = location
        self.datePosted = posted
        self.salary = salary
        self.link = link

        
    def __eq__(self, other):
        
        if (type(self)==type(other)):
            
            return (self.title == other.title) and (self.company == other.company)
        
        return False
    
    
wb = Workbook()
    
urls = ['https://stackoverflow.com/jobs?q=deep+learning&sort=i&pg=',
        'https://stackoverflow.com/jobs?q=machine+learning&sort=i&pg=',
        'https://stackoverflow.com/jobs?q=artificial+intelligence&sort=i&pg=',
        'https://stackoverflow.com/jobs?q=bioinformatics&sort=i&pg=']

sheetNames = ['deepLearning', 'machineLearning', 'AI', 'bioinformatics']
k = 0


for url in urls:
    
    jobArray = []
    
    # for each page
    for i in range(100):
        
        sauce = requests.get(url + "{}".format(i)).text
        
        
        soup = BeautifulSoup(sauce, 'lxml')
    
    
        
    # for each posting
        for jobCard in soup.find_all('div', class_= '-job'):
        
            
            newJob = job()
            title = jobCard.find('a', class_='s-link')['title']
            newJob.title = title
            
            company = jobCard.find('h3', class_='fc-black-700').find('span').text.strip()
            newJob.company = company
    
            location = jobCard.find('span', class_='fc-black-500').text.strip()
            newJob.location = location
            
    
            newJob.link = 'stackoverflow.com' + jobCard.find('a', class_='s-link')['href']
        
            if newJob not in jobArray:
                jobArray.append(newJob)
            
        #for item in jobArray:
        #    print(item.title)
        #    print(item.company)
        #    print(item.location)
        #    print(item.link)
        #    print('\n')
        
        
    print(len(jobArray))
    
    sheet1 = wb.add_sheet(sheetNames[k])
    k+=1
    
    
    for i in range(len(jobArray)):
        j = 0
        sheet1.write(i, j, jobArray[i].title)
        j+=1
        sheet1.write(i, j, jobArray[i].company)
        j+=1
        sheet1.write(i, j, jobArray[i].location)
        j+=1
#        sheet1.write(i, j, jobArray[i].datePosted)
#        j+=1
#        sheet1.write(i, j, jobArray[i].salary)
#        j+=1
        sheet1.write(i, j, jobArray[i].link)
        j+=1
    
    
wb.save('stackOverflowData.xlsx')

    
    
    

