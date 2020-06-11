import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import ranking

ranking_object = ranking.Ranker()
fig, axs = plt.subplots(2, figsize=(16,8))

data = pd.read_csv('demographics.csv',index_col='Variable/Platform')

age_vals, columns = ranking_object.two_sort(list(data.loc['Ages 18-29']), list(data.columns))
axs[1].set_title('Started Retirement Saving Between 18-29')
axs[1].bar(columns, age_vals)
dict1 = ranking_object.convert_to_rankings(dict(zip(columns, age_vals)))
ranking_object.add_ranking('Started Retirement Saving Between 18-29', dict1)

age_vals, columns = ranking_object.two_sort(list(data.loc['30-49']), list(data.columns))
axs[0].set_title('Started Retirement Saving Between 30-49')
axs[0].bar(columns, age_vals)
dict2 = ranking_object.convert_to_rankings(dict(zip(columns, age_vals)))
ranking_object.add_ranking('Started Retirement Saving Between 30-49', dict2)

plt.show()

# Retirement funds can contribute to millions in revenue for Prudential
# According a survey which calculated when US investors started saving across different age ranges, two age groups stood out: 20-29 and 30-49 (around 75% of the survey)
# We can find a correlation between social media age domographics and when US investors begin looking into retirement savings
# The output shows the results

