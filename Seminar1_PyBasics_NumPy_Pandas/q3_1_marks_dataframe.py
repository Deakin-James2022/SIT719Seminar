# Please create a pandas dataframe for the student unit marks. Bob = 80, 97, 85, 67, 80; Alice = 82, 67, 85, 62, 80; Eve = 89, 90, 85, 77, 80

import pandas as pd
# Create dictionary
data = {
    'Bob': [80, 97, 85, 67, 80],
    'Alice': [82, 67, 85, 62, 80],
    'Eve': [89, 90, 85, 77, 80]
}
# Create Pandas
df = pd.DataFrame(data)
print(df)
