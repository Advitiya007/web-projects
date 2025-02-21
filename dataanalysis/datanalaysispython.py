# # Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'student_performance.csv' with your dataset path
#panda functions that we used = readcsv,head,info,decsirbe,sortvalues,fillna,dropna,inplace attrb,numeric ,rename..the usuage of each one is
#specified calong with the mistakes than can be easily avoided 
#a bit of idea taken from 
#https://www.analyticsvidhya.com/blog/2021/05/pandas-functions-13-most-important/
data = pd.read_csv("Student_Performance_Dataset.csv")

# Display dataset overview
print("Dataset Overview:")
print(data.head())
print("\nDataset Information:")
print(data.info())
print("\nStatistical Summary:")
print(data.describe())

# ---- Data Cleaning ----
# Handle missing values by replacing them with the mean of each column
# data.fillna(data.mean(), inplace=True)

# Remove duplicate entries needed to drop if 1 student's value 2 times
data.drop_duplicates(inplace=True)

numeric_data = data.select_dtypes(include=['number'])

# seaborn heatmap
#++ERROR arrised because data set cpnsiting of not only numerics
#numeric data usuage 
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
# sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()



# Attendance vs Test Scores (Scatter Plot)
plt.figure(figsize=(8, 6))
y=data['Test_Series_Avg']
x=data['Attendance (%)']
# sns.scatterplot(x=data['Attendance'], y=data['Test_Scores'], color="blue")
# scatterplot converted to scatter of matplotlib
plt.scatter(x,y,color="blue")
plt.title("Attendance vs Test Scores")
plt.xlabel("Attendance (%)")
plt.ylabel("Test Scores")
plt.show()

# # Distribution of Test Scores
plt.figure(figsize=(8, 6))
# # sns.histplot(data['Test_Scores'], bins=10, kde=True, color="green")
l=[50,60,70,80,90,100]
x=data['Test_Series_Avg']
plt.title("Distribution of Test Scores ")
plt.xlabel("Test Scores")
plt.ylabel("Frequency")
plt.hist(x,"auto",(0,200),edgecolor="black")
plt.show()
#Distribution of Test Scores in decreasing order
plt.title("Distribution of Test Scores in decreasing order")
plt.xlabel("Test Scores")
plt.ylabel("Frequency")
plt.hist(x,"auto",(0,200),edgecolor="black",cumulative=-1)
plt.show()


# wanted to find out the colm names to avoid confusion
print(data.columns)

#grouping the data by tehir student id .. test series avg mean
a = data.groupby(by='Student_ID').Test_Series_Avg.mean()

# Sorting data in terms of their test series avg
a_sort = a.sort_values(ascending=True)
print(a_sort)

#groupig data again to this time student id and attendance basis
#create d anew var c stored this in c cause attendance % was giving an error obv
c=data.rename(columns={'Attendance (%)': 'Attendance', 'Test_Series_Avg': 'Test_Series_Avg'}, inplace=False)

# b=data.groupby(by='Student_ID').'Attendance (%)'.mean()
b=c.groupby(by='Student_ID').Attendance.mean()

# Sorting data in terms of their attendance
b_sort = b.sort_values(ascending=True)
print(b_sort)

# Identifying top 10 performers
top_performers = data.nlargest(10, 'Test_Series_Avg')
print("\nTop 10 Performers:")
print(top_performers)

# # ---- Factor Impact Analysis ----
# # Analyzing impact of Study Hours on Test Scores
plt.figure(figsize=(8, 6))
sns.lineplot(x=data['Math_Score'], y=data['Test_Series_Avg'], marker="o", color="red")
plt.title("Math_Score vs Test_Series_Avg")
plt.xlabel("Math_Score")
plt.ylabel("Test_Series_Avg")
plt.show()

sns.lineplot(x=data['Science_Score'], y=data['Test_Series_Avg'], marker="o", color="red")
plt.title("Science_Score vs Test_Series_Avg")
plt.xlabel("Science_Score")
plt.ylabel("Test_Series_Avg")
plt.show()

sns.lineplot(x=data['English_Score'], y=data['Test_Series_Avg'], marker="o", color="red")
plt.title("English_Score vs Test_Series_Avg")
plt.xlabel("English_Score")
plt.ylabel("Test_Series_Avg")
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data['Test_Series_Avg'], bins=10, kde=True, color="green")
plt.title("Distribution of Test Scores")
plt.xlabel("Test Series avg")
plt.ylabel("Frequency")
plt.show()

# pairplot=sns.pairplot(data)
# plt.show()
#changin color
sns.pairplot(data, plot_kws={'color': 'pink'})  
plt.show()

#used the following for refernce of seaborn more graphs
#https://www.geeksforgeeks.org/types-of-seaborn-plots/

# changed the name of the rows 
#made coreections to the og too
data.rename(columns={'Attendance (%)': 'Attendance', 'Test_Series_Avg': 'Test_Series_Avg'}, inplace=True)

# Plot lmplot
lmplot = sns.lmplot(x='Attendance', y='Test_Series_Avg', data=data, palette='Set1')
plt.show()

#swarm plot 
#adding size cause all values r enot shown warning
#changing figure canvas to show all attendance
plt.figure(figsize=(10, 6))
smplot = sns.swarmplot(x='Attendance', y='Test_Series_Avg', data=data, palette='Set1',size=4)
plt.show()
#violin
plt.figure(figsize=(10, 6))
vplot = sns.violinplot(x='Attendance', y='Test_Series_Avg', data=data,color='purple')
plt.show()
#box
plt.figure(figsize=(10, 6))

bxplot = sns.boxplot(x='Attendance', y='Test_Series_Avg', data=data,color='yellow')
plt.show()


attendance_groups = pd.cut(data['Attendance'], bins=[0, 50, 75, 100], labels=["Low", "Medium", "High"])
grouped_data = data.groupby(attendance_groups)['Test_Series_Avg'].mean()
print("\nAverage Test Scores by Attendance Level:")
print(grouped_data)

# Plot Average Test Scores by Attendance Level
plt.figure(figsize=(8, 6))
grouped_data.plot(kind="bar", color="purple")
plt.title("Average Test Scores by Attendance Level")
plt.xlabel("Attendance Level")
plt.ylabel("Average Test Scores")
plt.show()

print("THANK YOU SO MUCH THIS ENDS THE DATA ANALYSIS OF STUDENT PERFORMANCE CSV FILE ")



