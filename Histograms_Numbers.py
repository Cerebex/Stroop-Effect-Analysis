import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_file_name = 'stroopdata.csv'
stroopdata = pd.read_csv(data_file_name)

# print stroopdata

#Histogram of Stroopdata Congruent distribution
stroopdata.Congruent.hist(bins = 6)
plt.title('Distribution of Congruent Test Times')
plt.xlabel('Time to Completion (seconds)')
plt.ylabel('Count')
plt.show()

#Histogram of Stroopdata distribution
stroopdata.Incongruent.hist(bins = 6)
plt.title('Distribution of Incongruent Test Times')
plt.xlabel('Time to Completion (seconds)')
plt.ylabel('Count')
plt.show()

#Age Distribution for Survival
p = sns.boxplot(data = stroopdata)
p.set(title = 'Test Completion Time Distribution', 
        xlabel = 'Test Type', 
        ylabel = 'Completion Time', 
        xticklabels = ['Congruent', 'Incongruent'])
plt.show()

stroopdata['Difference'] = stroopdata['Incongruent'].sub(stroopdata['Congruent'], axis=0)
stroopdata_averages = stroopdata.mean(axis=0)
stroopdata_std = stroopdata.std(axis=0)

#Histogram of Stroopdata difference distribution
stroopdata.Difference.hist(bins = 12)
plt.title('Distribution of the Difference in Test Times')
plt.xlabel('Time to Completion (seconds)')
plt.ylabel('Count')
plt.show()

Stroopdata_datareview = pd.DataFrame(
	data= [stroopdata_averages, stroopdata_std],
	index = ['Mean', 'Standard Deviation'])
print Stroopdata_datareview

standard_error = Stroopdata_datareview.loc['Standard Deviation', 'Difference']/np.sqrt(len(stroopdata))

df = len(stroopdata.iloc[:,0]) - 1


t = (Stroopdata_datareview.iloc[0,1] - Stroopdata_datareview.iloc[0,0])/standard_error

t_squared = np.square(t)/(np.square(t) + df)

Stroopdata_statistics = pd.DataFrame(
	data= [standard_error, df, t, t_squared],
	index = ['Standard Error', 'Df', 'T-statistic', 'T Squared'],
	columns = ['T Test'])

print Stroopdata_statistics

# Stroopdata_datareview.to_csv(path_or_buf='/Users/samuelmiller/Documents/Udacity/Data Analyst Nanodegree/Statistics/Final Project Submission #1/stroopdata_datareview.csv')
 