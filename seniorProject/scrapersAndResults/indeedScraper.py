# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:23:58 2020

@author: Charlie

This is a scraper for indeed.com 
"""

from bs4 import BeautifulSoup
from xlwt import Workbook

import requests

wb = Workbook()

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
  
    



sheetNames = ['deepLearning', 'machineLearning', 'AI', 'bioinformatics']
k = 0

urls = ['https://www.indeed.com/jobs?q=deep+learning&start=',
        'https://www.indeed.com/jobs?q=machine+learning&start=', 
        'https://www.indeed.com/jobs?q=artificial+intelligence&start=',
        'https://www.indeed.com/jobs?q=bioinformatics&start=']

# for each url
for url in urls:
    
    j = 0
    jobArray = []
    
    # for each page
    for i in range(100):
        
        sauce = requests.get(url + "{}".format(j)).text
        
        
        soup = BeautifulSoup(sauce, 'lxml')
    
    
        
    # for each posting
        for jobCard in soup.find_all('div', class_= "jobsearch-SerpJobCard"):
        
            newJob = job()
            title = jobCard.find('a', class_='jobtitle')['title']
            newJob.title = title
            
            company = jobCard.find('span', class_='company')
            if type(company)!= type(None):
                newJob.company = company.text.strip()
            
            location = jobCard.find('div', class_='recJobLoc')['data-rc-loc']
            newJob.location = location
            
            datePosted = jobCard.find('span', class_='date').text
            newJob.datePosted = datePosted
            
            salary = jobCard.find('span', class_='salaryText')
            if type(salary)!=type(None):
                salary=salary.text.strip()
                newJob.salary = salary
            
            newJob.link = 'indeed.com' + jobCard.find('a', class_='jobtitle')['href']
        
            if newJob not in jobArray:
                jobArray.append(newJob)
            
            
            
        j+=10
        
        
        
    #for item in jobArray:
    #    print(item.title)
    #    print(item.company)
    #    print(item.location)
    #    print(item.datePosted)
    #    print(item.salary)
    #    print(item.link)
    #    print('\n')
    #    
        
    print(len(jobArray))
    
    
    
    sheet = wb.add_sheet(sheetNames[k])
    k+=1
    
    for i in range(len(jobArray)):
        j = 0
        sheet.write(i, j, jobArray[i].title)
        j+=1
        sheet.write(i, j, jobArray[i].company)
        j+=1
        sheet.write(i, j, jobArray[i].location)
        j+=1
        sheet.write(i, j, jobArray[i].datePosted)
        j+=1
        sheet.write(i, j, jobArray[i].salary)
        j+=1
        sheet.write(i, j, jobArray[i].link)
        j+=1
    
    
wb.save('indeedData.xlsx')
    
    
    
    

