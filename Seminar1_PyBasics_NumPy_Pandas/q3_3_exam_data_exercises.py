# Please import the following dictionary to pandas dataframe
import pandas as pd
import numpy as np

# Create dictionary
exam_data = {
    'name': ['Alice', 'Dee', 'Kathy', 'Homes', 'Boris',
             'Hanson', 'Bourne', 'Matt', 'Jason', 'Jarvis'],
    'score': [115, 7, 15.5, np.nan, 9, 19, 15.5, np.nan, 8.5, 19.5],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Import dictionary into Pandas
df = pd.DataFrame(exam_data, index=labels)
print("Original DataFrame:")
print(df)

# 1. Change 'Dee' to 'Eve' using replace()
df['name'] = df['name'].replace('Dee', 'Eve')
print("\n1. After replacing Dee with Eve:")
print(df)

# 2. Find rows with missing values
print("\n2. Rows with missing values:")
print(df[df.isnull().any(axis=1)])

# 3. Find rows where attempts < 2 and score > 15
print("\n3. Rows where attempts < 2 and score > 15:")
print(df[(df['attempts'] < 2) & (df['score'] > 15)])

# 4. Replace NaN values with 10
df['score'] = df['score'].fillna(10)
print("\n4. After replacing NaN values with 10:")
print(df)
