# importing libraries
import pandas as pd
import numpy as np

df = pd.read_csv('Yelp_Reviews.csv')

# =====================
# === BUSINESS DATA ===
# =====================

yelp_businesses = df.groupby('business_id').size()

# 01 - Highest Number of Reviews
print('BUSINESS MEAN :: ', yelp_businesses.mean())

# 02 - Average Number of Reviews
print('BUSINESS MAX :: ', yelp_businesses.max())


# =====================
# === REVIEWER DATA ===
# =====================

print()

# 3A - Average number of reviews


print('3A :: ', df.groupby('user_id').size().mean())

# 3B - Average number of cool votes

# TODO: some error here
print('3B :: ', df.groupby('user_id').count()['cool_votes'].sum())
print('3B :: ', len(df['user_id'].unique()))

# 3C - Average number of funny votes
# 3D - Average number of useful votes

# 3E - What is the average of the log of the number of reviews per reviewer? find the average of the feature vector by first taking the natural log of each entry and then calculating the average. You will have to handle the log of 0 when a reviewer has no votes in that category. The log of 0 is -Inf. Replace -Inf with NaN (Not a Number) and omit these instances when calculating the average.
# 3F - What is the average of the log of the number of cool votes per reviewer?
# 3G - What is the average of the log of the number of funny votes per reviewer?    
# 3H - What is the average of the log of the number of useful votes per reviewer? 

# 3I - Find the average of the percentage of total cool votes out of total votes for each reviewer.
# 3J - Find the average of the percentage of total funny votes out of total votes for each reviewer.
# 3K - Find the average of the percentage of total useful votes out of total votes for each reviewer. 

# 3L - Average review text length (in non-space characters)
# 3M - Year in which the reviewer wrote the most reviews. Once you have this for each reviewer, subtract the minimum possible year (2005) from each so that your final feature values are 0, 1, 2 etc.










