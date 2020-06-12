import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import ranking
from matplotlib.pyplot import figure

figure(figsize=(16, 6))

ranking_object = ranking.Ranker()
data = pd.read_csv('data.csv')

labels = ['Twitter','Instagram','Facebook','Snapchat','YouTube','WhatsApp','Pinterest','LinkedIn']
values = []
letters = ['a','b','c','d','e','f','g','h']

for i in range(len(labels)):
    column = 'web1{}'.format(letters[i])
    values.append((data[data[column] == 1]['age'].mean()-35)/data[data[column] == 1]['age'].mean())

values, labels = ranking_object.two_sort_ascending(values, labels)
plt.bar(labels, values)
plt.title('Percent Difference Between Social Media Platforms and Preferred Age to Begin Investing ')
dictionary = ranking_object.convert_to_rankings(dict(zip(labels, values)))
ranking_object.add_ranking("Pct. Diff. of SM platforms and age to begin investing(35)", dictionary)
plt.show()

#the preferred age to start investing is 35
#this graph shows the percent difference between 35 and the average age or each social media platform