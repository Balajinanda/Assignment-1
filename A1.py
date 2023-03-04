# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 19:46:36 2023

@author: Balaj
"""

#Importing Libraries
import pandas as pds
import matplotlib.pyplot as plt

#read csv file
Budget = pds.read_csv("budget.csv")
print(Budget)

#defining line function    


def line(Budget):
    
    
    """ 
       By selecting 5 departments and their year-wise budget
       then plot a line graph
    """
    
  
    plt.figure(figsize = (10,5))
    
    #plotting the data
    plt.plot(Budget["Year"], Budget["Department of the Treasury"], \
             label = "Department of the Treasury")
    plt.plot(Budget["Year"], Budget["Department of Agriculture"], \
             label = "Department of Agriculture")
    plt.plot(Budget["Year"], Budget["Department of Veterans Affairs"], \
             label = "Department of Veterans Affairs")
    plt.plot(Budget["Year"], Budget["Department of Defense"], \
             label = "Department of Defense")
    plt.plot(Budget["Year"], Budget["Department of Energy"], \
         label = "Department of Energy")    
    #plotting labels and legend
    plt.xlabel("Year")
    plt.ylabel("Budget")
    plt.title("Year-wise Budget from 1976 to 2022")
    plt.legend()
    plt.show()


#read csv file 2
IPL = pds.read_csv("ipl_2023_dataset.csv")
print(IPL)

#defining bar function


def bar(IPL):
   
    """ 
       By selecting teams and price of their total players
       then plot a bar graph
    """
   
    plt.figure(figsize = (20,5))
    
    #plotting bar graph  
    plt.bar(IPL['Team'], IPL['Price Cr'])

    #plotting labels
    plt.xlabel('Team', fontsize=18)
    plt.ylabel('Price', fontsize=16)
    plt.title("Price of total players in each team")
    plt.legend()
    plt.show()


#defining pie function


def pie(IPL):
   
    """ 
       By selecting percentage of different players from all teams
       them plot a pie chart 
     """

    
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    totaltype = IPL['Type'].value_counts()
  
    #plotting pie chart
    
    plt.figure(figsize = (8,10))
    plt.pie(totaltype.values, labels = totaltype.index, \
            autopct = '%1.1f%%', colors = colors, shadow = True)
    plt.title("Percentage Of Different Players")
    plt.legend(title = 'Categories', bbox_to_anchor = (1, 0, 0.5, 1))
    plt.show()
    

#function calling
line(Budget)
bar(IPL)
pie(IPL)




