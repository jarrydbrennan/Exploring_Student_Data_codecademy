# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())
# Print summary statistics for all columns
print(students.describe(include='all'))
# Calculate mean
print(students.math_grade.mean())
# Calculate median
print(students.math_grade.median())
# Calculate mode
print(students.math_grade.mode()[0])
# Calculate range
math_range = students.math_grade.max() - students.math_grade.min()
print(math_range)
# Calculate standard deviation
math_std = students.math_grade.std()
print(math_std)
# Calculate MAD
math_mad = students.math_grade.mad()
print(math_mad)
# Create a histogram of math grades
sns.histplot(x='math_grade',data=students)
plt.show()
plt.clf()
# Create a box plot of math grades
sns.boxplot(x='math_grade',data=students)
plt.show()
plt.clf()
# Calculate number of students with mothers in each job category
mjobs = students['Mjob'].value_counts()
print(mjobs)
# Calculate proportion of students with mothers in each job category
mjobs_prop = students['Mjob'].value_counts(normalize=True)
print(mjobs_prop)
# Create bar chart of Mjob
sns.countplot(x='Mjob',data=students)
plt.show()
plt.clf()
# Create pie chart of Mjob
students['Mjob'].value_counts().plot.pie()
plt.show()
plt.clf()

#dad_bod
sns.countplot(x='Fjob',data=students)
plt.show()
plt.clf()

students['Fjob'].value_counts().plot.pie()
plt.show()
plt.clf()

#poor_kids
sns.boxplot(x='absences', data=students)
plt.show()
plt.close()
sns.histplot(x='absences', data=students)
plt.show()
plt.close()