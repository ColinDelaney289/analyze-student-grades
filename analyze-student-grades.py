# Python Project Two
# Functions and Pandas Practice
# "Analyze Student Grades"

import pandas as pd

# Function for using a student's final grade
# to determine their letter grade
def assign_letter_grade(final_grade):
    if final_grade > 90:
        return 'A+' 
    elif final_grade > 80:
        return 'A'
    elif final_grade > 70:
        return 'B'
    elif final_grade > 60:
        return 'C'
    elif final_grade > 55:
        return 'D'
    else:
        return 'F'

# Load student/grade data from CSV file into a dataframe
file_name = "Grades_Short.csv"
df_grades = pd.read_csv(file_name, header=0)

# Add columns for average quiz grade and average assignment grade
grade_types = ["Quiz", "Assignment"]
for grade_type in grade_types:
    df_grades[grade_type+'_Average'] = (
        df_grades[grade_type+'_1'] + 
        df_grades[grade_type+'_2']
    ) / 2

# The final grade is calculated as the sum of the following:
# 10% of the quiz grade average;
# 20% of the assignment grade average;
# 30% of the mid-term exam grade;
# 40% of the final exam grade.
df_grades['Final_Grade'] = round((
    df_grades['Quiz_Average'] * 0.1 +   
    df_grades['Assignment_Average'] * 0.2 +    
    df_grades['Mid_Term_Exam'] * 0.3 +        
    df_grades['Final_Exam'] * 0.4             
),1)

# Add column for letter grade and apply function
# for determining the letter grade
df_grades['Letter_Grade'] = df_grades['Final_Grade'].apply(assign_letter_grade)

# Write dataframe with added columns to a new CSV file
new_file_name = "Grades_Short_New.csv"
df_grades.to_csv(new_file_name, index=False)