import pandas as pd
import numpy as np
import ranking

ranker = ranking.Ranker()
list1 = ranker.get_final_rankings()
ranking_vals = {'YouTube': 0, 'Facebook': 0, 'Instagram': 0, 'Pinterest': 0, 'LinkedIn': 0, 'Twitter': 0, 'Snapchat': 0, 'WhatsApp': 0}

for i in range(len(list1)):
    key = list(list1[i].keys())[0]
    new_dict = list1[i][key]
    for key, value in new_dict.items():
        if key.lower() == 'YouTube'.lower():
            ranking_vals['YouTube'] += 1
        elif key.lower() == 'Facebook'.lower():
            ranking_vals['Facebook'] += 1
        elif key.lower() == 'Instagram'.lower():
            ranking_vals['Instagram'] += 1
        elif key.lower() == 'Pinterest'.lower():
            ranking_vals['Pinterest'] += 1
        elif key.lower() == 'LinkedIn'.lower():
            ranking_vals['LinkedIn'] += 1
        elif key.lower() == 'Twitter'.lower():
            ranking_vals['Twitter'] += 1
        elif key.lower() == 'Snapchat'.lower():
            ranking_vals['Snapchat'] += 1
        elif key.lower() == 'WhatsApp'.lower():
            ranking_vals['WhatsApp'] += 1

new_dict = sorted(ranking_vals.items(), key=lambda x: x[1])

for i in dict(new_dict).keys():
    print(i)