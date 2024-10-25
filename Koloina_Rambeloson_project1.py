#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:34:27 2024

@author: koloina
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

"""
DATA CLEANING
"""

#Removing spaces from the column names
df.columns = df.columns.str.replace(' ', '_')

#Replacing NaNs in Revenue_(Millions) and Metascore with the column mean value
df= df.fillna({
    'Revenue_(Millions)': df['Revenue_(Millions)'].mean(),
    'Metascore': df['Metascore'].mean()
})

"""
PROJECT
"""

#Finding the highest rated movie
highest_rated_movie = df.loc[df['Rating'].idxmax()]
print('The highest rated movie is:', highest_rated_movie)

#Average revenue of all movies in the dataset
avg_revenue = df['Revenue_(Millions)'].mean()
print('Average revenue of all movies:', avg_revenue)

#Average revenue of movies from 2015 to 2017
data_15_17= df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_revenue_15_17= data_15_17['Revenue_(Millions)'].mean()
print('Average revenue from 2015-2017:', avg_revenue_15_17)

#Number of movies released in 2016
movies_2016 = df[df['Year'] == 2016].shape[0]
print('Number of movies released in 2016:', movies_2016)

#Movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan'].shape[0]
print('Number of movies directed by Christopher Nolan:', nolan_movies)

#Number of movies that have a rating of at least 8.0
high_rating_movies_count = df[df['Rating'] >= 8.0].shape[0]
print('Number of movies with a rating of at least 8.0:', high_rating_movies_count)

#Median rating of movies directed by Christopher Nolan
nolan_median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print('Median rating of movies directed by Christopher Nolan:', nolan_median_rating)

#The year with the highest average rating
year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()
print('Year with the highest average rating:', year_highest_avg_rating)

#Percentage increase in number of movies made between 2006 and 2016
movies_2006 = df[df['Year'] == 2006].shape[0]
#movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print('Percentage increase between 2006 and 2016:', percentage_increase)


#Finding the most common actor in all the movies.
# Split the 'Actors' column into lists, removing any extra spaces
#Then explode the lists into separate rows
actors = df['Actors'].str.split(r',\s*').explode()
#Most common actor
most_common_actor = actors.value_counts().idxmax()
print('Most common actor in all the movies:', most_common_actor)

#Number of unique genres in the dataset
genre = df['Genre'].str.split(r',\s*').explode()
# Get unique genres
unique_genre = genre.value_counts().count()
print('Number of unique genres in the dataset:', unique_genre)
