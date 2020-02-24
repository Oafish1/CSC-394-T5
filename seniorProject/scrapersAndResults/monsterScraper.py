# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:55:56 2020

@author: Charlie
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

sheetNames = ['deepLearning', 'machineLearning', 'AI', 'bioinformatics']
k = 0

urls = ['https://www.monster.com/jobs/search/?q=deep-learning&stpage=1&page=10',
        'https://www.monster.com/jobs/search/?q=machine-learning&stpage=1&page=10',
        'https://www.monster.com/jobs/search/?q=artificial-intelligence&stpage=1&page=10',
        'https://www.monster.com/jobs/search/?q=bioinformatics&stpage=1&page=10']

for url in urls:
    
    jobArray = []

    sauce = requests.get(url).text
    
    soup = BeautifulSoup(sauce, 'lxml')
    
    for summary in soup.find_all('div', class_='summary'):
        newJob = job()
        newJob.title = summary.find('a').text
        newJob.company = summary.find('div', class_='company').find('span', class_='name').text
        newJob.location = summary.find('div', class_='location').find('span', class_='name').text
        newJob.link = summary.find('a')['href']
        
        if newJob not in jobArray:
            jobArray.append(newJob)
        
    
    
    
    #for item in jobArray:
    #    print(item.title)
    #    print(item.company)
    #    print(item.location)
    #    print(item.datePosted)
    #    print(item.salary)
    #    print(item.link)
    #    print('\n')
    #     
    #       
            
    
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
    #    sheet1.write(i, j, jobArray[i].datePosted)
    #    j+=1
    #    sheet1.write(i, j, jobArray[i].salary)
    #    j+=1
        sheet1.write(i, j, jobArray[i].link)
        j+=1
    
    print(len(jobArray))
    
wb.save('monsterData.xlsx')





