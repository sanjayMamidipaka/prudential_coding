import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn

data = pd.read_csv('data.csv')
#this line gets the percentage of yes answers for each type of social media
percents = [len(data[data['web1a'] == 1])/len(data), len(data[data['web1b'] == 1])/len(data), len(data[data['web1c'] == 1])/len(data), len(data[data['web1d'] == 1])/len(data), len(data[data['web1e'] == 1])/len(data), len(data[data['web1f'] == 1])/len(data), len(data[data['web1g'] == 1])/len(data), len(data[data['web1h'] == 1])/len(data)]
#x axis labels
labels = ['Twitter','Instagram','Facebook','Snapchat','YouTube','WhatsApp','Pinterest','LinkedIn']
#sets the size of the graph
plt.figure(figsize=(16,6))
#graph, with the x axis labels and y values
plt.bar(labels, percents)
#labels
plt.xlabel('Platforms', fontsize=12, labelpad=5)
plt.ylabel('Frequency', fontsize=12, labelpad=5)
#title
plt.title('Social Media Usage')
#used to show to graph

percents2 = [len(data[data['device1a'] == 1])/len(data), len(data[data['device1b'] == 1])/len(data), len(data[data['device1c'] == 1])/len(data), len(data[data['device1d'] == 1])/len(data)]
#x axis labels
labels2 = ['Phone','Tablet','Desktop/Laptop','Game Console']
#sets the size of the graph
plt.figure(figsize=(16,6))
#graph, with the x axis labels and y values
plt.bar(labels2, percents2)
#labels
plt.xlabel('Platform Used', fontsize=12, labelpad=5)
plt.ylabel('Frequency', fontsize=12, labelpad=5)
#title
plt.title('Platform Ownership')
#used to show to graph

#hi people
#hello world



plt.show()

