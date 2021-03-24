#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# In[28]:


titanic = pd.read_csv("~/Desktop/MIS542titanic.csv")


# In[29]:


#What was the average cost in U.S. dollars of a first class ticket? 
#First, create a filter to find how many first class tickets there were.
first_class = titanic['Passanger Class']==1


# In[30]:


titanic_first = titanic.loc[first_class,:]
titanic_first.head()


# In[61]:


#Then, we take the average of the last column, "Fare in British Pounds".
average_price = titanic_first['Fare in British Pounds'].mean()

#Lastly, convert it to US dollars by multiplying the final answer by $1.28.
average_price * 1.28


# In[52]:


#How many passengers over 20 had siblings onboard? 
#First, create a filter to find out how many people over the age of 20 were on board.
over_20 = titanic['Age']>=20
titanic_over_20 = titanic.loc[over_20,:]
titanic_over_20.head()


# In[53]:


#Then, see which of those passengers had more than one sibling/spouses aboard.
titanic_siblings = titanic_over_20['Siblings/Spouses Aboard']>1
titanic_siblings_over_20 = titanic_over_20.loc[titanic_siblings,:]
titanic_siblings_over_20.head()


# In[54]:


#Finally, index and count the rows to see how many total there were. 
index = titanic_siblings_over_20.index
print(len(index))


# In[60]:


#What was the median age of those who did not survive?
#First, create a filter that assigns 1 = survived to all the rows. 

not_survive = titanic['Survived']==0
dead = titanic.loc[not_survive,:]
dead.head()


# In[65]:


#Then, take the average of the age to see the median age of those of died.
median_age = dead['Age'].median()
median_age


# In[67]:


#Who was the oldest person in third class?
#First, create a filter for those in the third class. 
which_class = titanic['Passanger Class']==3
third_class = titanic.loc[which_class,:]
third_class.head()


# In[68]:


#Then, find the eldest of the third class passangers. 
third_class['Age'].max()


# In[74]:


#What percent of the third class passengers survived?
#First, use the third class passengers filter to find out how many third class passengers there were.
index = third_class.index
print(len(index))


# In[75]:


#Then, apply a new filter to see how many people survived, then count them.

survived = third_class['Survived']==1
third_class_survived = third_class.loc[survived,:]
third_class_survived.head()


# In[76]:


index2 = third_class_survived.index
print(len(index2))


# In[78]:


#Then, do a simple percentage calculation. 
print((len(index2)/len(index))*100)


# In[81]:


#What was the youngest passenger killed? 
#First, filter out all the alive people.

dead = titanic['Survived']==0
dead = titanic.loc[dead,:]
dead.head()


# In[83]:


#Then, find the youngest member by using the minimum function.
dead['Age'].min()


# In[86]:


import matplotlib.pyplot as plt
import numpy as np


# In[91]:


#Use a pie chart to show the number of males and females. 
males = titanic['Sex']=="male"
males = titanic.loc[males,:]
index = males.index
print(len(index))


# In[92]:


females = titanic['Sex']=="female"
females = titanic.loc[females,:]
index2 = females.index
print(len(index2))


# In[94]:


my_data = [573,314]
my_labels = 'Males','Females'
plt.pie(my_data,labels = my_labels, autopct='%1.1f%%')
plt.title('Males vs. Females on the Titanic')
plt.axis('equal')
plt.show()


# In[102]:


#Use a bar chart to show the count of male survivors and the count of female survivors.
alive = titanic['Survived']==1
alive = titanic.loc[alive,:]

alive_females = alive['Sex']=="female"
alive_females = alive.loc[alive_females,:]
index = alive_females.index
females = len(index)

alive_males = alive['Sex']=="male"
alive_males = alive.loc[alive_males,:]
index2 = alive_males.index
males = len(index2)

survivors = ['Females', 'Males']
number = [females, males]


# In[175]:


plt.bar(survivors, number, color = ['pink','blue'])
plt.title('Female Survivors vs. Male Survivors')
plt.xlabel('Gender')
plt.ylabel('Survivors')
plt.show()


# In[178]:


#Use a bar chart to show the count of each age.
ages = titanic['Age'].value_counts().sort_index()
ages.plot(kind='bar', color='green')
plt.title('Age Distribution Onboard the Titanic')
plt.xlabel('Ages')
plt.ylabel('Number of People')
plt.xticks(np.arange(0,95, step=4))
plt.grid(True)
plt.show()


# In[207]:


#Use a scatter plot to show the distribution of fares over ages. 
age = titanic['Age']
fares = titanic['Fare in British Pounds']


# In[210]:


plt.scatter(age,fares)
plt.xlabel('Age')
plt.ylabel('Fare Price in British Pounds')
plt.yticks(np.arange(min(fares),max(fares)+1, 50))
plt.title('Fare Price in British Pounds by Age')
plt.grid(True)


# In[225]:


#Use a pie chart to emphasize the number of children onboard. 
children = titanic['Age']<20
children = titanic.loc[children,:]
index = children.index
children = len(index)
adults = titanic['Age']>=20
adults = titanic.loc[adults,:]
index2 = adults.index
adults = len(index2)

plt.pie([children, adults], explode = (0.2,0), labels=['Children','Adults'],
        autopct='%1.1f%%', shadow=True)
plt.title('Children vs. Adult Population Onboard the Titanic')
plt.show()


# In[252]:


#Make a horizontal bar plot that shows the populations of the different classes.
classes = titanic['Passanger Class']
classes = classes.value_counts().sort_index(ascending=False)
classes = [3,2,1]
population = [487, 184, 216]
labels = ['Third', 'Second', 'First']


# In[262]:


plt.barh(classes,population, color = ['r','g','b'], height = .5)
plt.title('Population of the Classes Onboard the Titanic')
plt.ylabel('Classes')
plt.xlabel('Population')
plt.yticks(classes, labels, rotation = 45)
plt.xticks(np.arange(0,550,step=50))
plt.show()


# In[ ]:




