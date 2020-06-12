import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import ranking

def normalize(percent):
    normalizedPercents = []
    for x in percent:
        temp = x/sum(percent);
        normalizedPercents.append(temp)
    return normalizedPercents

ranking_object = ranking.Ranker()
data = pd.read_csv('data.csv')
#this line gets the percentage of yes answers for each type of social media
fig, axs = plt.subplots(3, figsize=(22,20))
fig.suptitle('Info')
percents = [len(data[data['web1a'] == 1])/len(data), len(data[data['web1b'] == 1])/len(data), len(data[data['web1c'] == 1])/len(data), len(data[data['web1d'] == 1])/len(data), len(data[data['web1e'] == 1])/len(data), len(data[data['web1f'] == 1])/len(data), len(data[data['web1g'] == 1])/len(data), len(data[data['web1h'] == 1])/len(data)]
#x axis labels
labels = ['Twitter','Instagram','Facebook','Snapchat','YouTube','WhatsApp','Pinterest','LinkedIn']
#graph, with the x axis labels and y values

for passnum in range(len(percents)-1,0,-1):
    for i in range(passnum):
        if percents[i]<percents[i+1]:
            temp = percents[i]
            percents[i] = percents[i+1]
            percents[i+1] = temp

            temp1 = labels[i]
            labels[i] = labels[i+1]
            labels[i+1] = temp1

dictionary = dict(zip(labels, percents))
iterator = 0
for i in dictionary:
    dictionary[i] = iterator + 1
    iterator += 1
ranking_object.add_ranking("Social Media Usage", dictionary)

axs[0].bar(labels, percents)
#labels
axs[0].set_xlabel('Platforms', fontsize=12, labelpad=5)
axs[0].set_ylabel('Frequency', fontsize=12, labelpad=5)
#title
axs[0].set_title('Social Media Usage')
#used to show to graph



percents2 = [len(data[data['device1a'] == 1])/len(data), len(data[data['device1b'] == 1])/len(data), len(data[data['device1c'] == 1])/len(data), len(data[data['device1d'] == 1])/len(data)]
#x axis labels
labels2 = ['Phone','Tablet','Desktop/Laptop','Game Console']
normalized = normalize(percents2)

for passnum in range(len(normalized)-1,0,-1):
    for i in range(passnum):
        if normalized[i]>normalized[i+1]:
            temp3 = normalized[i]
            normalized[i] = normalized[i+1]
            normalized[i+1] = temp3

            temp4 = labels2[i]
            labels2[i] = labels2[i+1]
            labels2[i+1] = temp4
normalizedNums = [1,2,3,4]
dictionary2 = dict(zip(labels2, normalizedNums))

#graph, with the x axis labels and y values
axs[1].bar(labels2, normalized)
#labels
axs[1].set_xlabel('Platform Used', fontsize=12, labelpad=5)
axs[1].set_ylabel('Frequency', fontsize=12, labelpad=5)
#title
axs[0].set_title('Platform Ownership')
#used to show to graph


labels3 = ['Twitter','Instagram','Facebook','Snapchat','YouTube','WhatsApp','Pinterest','LinkedIn']
percents3 = [2,2,2,1,3,2,2,2]
percents4, labels4 = ranking_object.two_sort(percents3,labels3)
dictionary3 = dict(zip(labels4,percents4))
print(percents4)
ranking_object.add_ranking("Social Media Availablity", dictionary3)
axs[2].bar(labels3, percents3)
#labels
axs[2].set_xlabel('Social Media', fontsize=12, labelpad=5)
axs[2].set_ylabel('Availability', fontsize=12, labelpad=5)
#title
axs[0].set_title('Social Media Availablity')



# plt.show()

