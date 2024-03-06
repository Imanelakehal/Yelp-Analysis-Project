# Yelp-Analysis-Project

What Is Yelp?
Founded in 2004, Yelp is a popular online directory for discovering local businesses ranging from bars, restaurants, and cafes to hairdressers, spas, and gas stations.

How Does Yelp Work?
You can search Yelp via its website or with the official apps on iOS and Android smart devices. Listings are sorted by business type and results are filtered by geographical location, price range, and unique features like outdoor seating, delivery service, or the ability to accept reservations.

Yelp has a strong social aspect and encourages its users to leave written reviews, star ratings, and photos of their experience with each business they visit.

Each Yelp account has a friends list that can be populated by connecting the app with Facebook and a smartphone or tablet's address book. Reviews posted on Yelp can also be reviewed by other users, while popular reviewers have the potential to be promoted to Yelp Elite status.

Yelp Dataset
The Yelp dataset is a subset of Yelp's businesses, reviews, and user data that has been made publicly available for use for personal, educational, and academic purposes. Available as JSON files, use it to teach students about databases, to learn NLP, or for sample production data while you learn how to make mobile apps. This dataset contains 6,685,900 reviews, 192,609 businesses, 200,000 pictures in 10 metropolitan areas.

Yelp Dataset

Yelp JSON
users



user_id	string	22 character unique user id, maps to the user in user.json
name	string	the user's first name
review_count	integer	the number of reviews they've written
yelping_since	string	when the user joined Yelp, formatted like YYYY-MM-DD
friends	array	array of strings, an array of the user's friend as user_ids
useful	integer	number of useful votes sent by the user
funny	integer	number of funny votes sent by the user
cool	integer	number of cool votes sent by the user
fans	integer	number of fans the user has
elite	array	the years the user was elite
average_stars	float	average rating of all reviews
compliment_hot	integer	number of hot compliments received by the user
compliment_more	integer	number of more compliments received by the user
compliment_profile	integer	number of profile compliments received by the user
compliment_cute	integer	number of cute compliments received by the user
compliment_list	integer	number of list compliments received by the user
compliment_note	integer	number of note compliments received by the user
compliment_plain	integer	number of plain compliments received by the user
compliment_cool	integer	number of cool compliments received by the user
compliment_funny	integer	number of funny compliments received by the user
compliment_writer	integer	number of writer compliments received by the user
compliment_photos	integer	number of photo compliments received by the user
business



business_id	string	22 character unique string business id
name	string	the business's name
address	string	the full address of the business
city	string	the city
state	string	2 character state code, if applicable
postal code	string	the postal code
latitude	float	latitude
longitude	float	longitude
stars	float	star rating, rounded to half-stars
review_count	integer	number of reviews
is_open	integer	0 or 1 for closed or open, respectively
attributes	object	business attributes to values. note: some attribute values might be objects
categories	array	an array of strings of business categories
hours	object	an object of key day to value hours, hours are using a 24hr clock
rating



review_id	string	22 character unique review id
user_id	string	22 character unique user id, maps to the user in user.json
business_id	string	22 character business id, maps to business in business.json
stars	integer	star rating
date	string	date formatted YYYY-MM-DD
text	string	the review itself
useful	integer	number of useful votes received
funny	integer	number of funny votes received
cool	integer	number of cool votes received
checkin



business_id	
string
22 character business id, maps to business in business.json
date	string	"2016-04-26 19:49:16, 2016-08-30 18:36:57, 2016-10-15 02:45:18, 2016-11-18 01:54:50, 2017-04-20 18:39:06, 2017-05-03 17:58:02"
Requirements
Requirement 1: Data Analysis and Visualization

I. Business Analysis:

Identify the most common merchants in the United States (Top 20).
Find the top 10 cities with the most merchants in the United States.
Identify the top 5 states with the most merchants in the United States.
Find the most common merchants in the United States and display their average ratings (Top 20).
Analyze and list the top 10 cities with the highest average ratings.
Count the number of categories.
Identify and list the top 10 categories with the highest frequency.
List the top 20 merchants with the most five-star reviews.
Summarize the types and quantities of restaurants for different cuisines (Chinese, American, Mexican).
Analyze the review counts for restaurants of different cuisines.
Explore the distribution of ratings for restaurants of different cuisines.
II. User Analysis:

Analyze the yearly growth of user sign-ups.
Count the "review_count" for users.
Identify and list the most popular users based on their number of fans.
Calculate the ratio of elite users to regular users each year.
Display the yearly proportions of total users and silent users (those who haven't written reviews).
Summarize the yearly statistics for new users, review counts, elite users, tip counts, and check-in counts.
Present the results in tables and line graphs.
Provide insights and analysis of the results.
III. Review Analysis:

Count the yearly number of reviews.
Summarize the count of helpful, funny, and cool reviews each year.
Create a ranking of users based on their total reviews each year.
Extract the top 20 common words from reviews.
Perform word cloud analysis on reviews after part-of-speech filtering.
Generate a word relationship graph for selected words (e.g., Chinese, steak).
IV. Rating Analysis:

Analyze the distribution of ratings (1-5).
Count the frequency of ratings on each day of the week.
Identify the top 5 merchants with the most 5-star ratings.
V. Check-in Analysis:

Count the yearly check-in frequency.
Analyze the check-in frequency for each hour of the day.
Identify the cities where check-ins are most frequent.
Create a ranking of all merchants based on check-in frequency.
VI. Comprehensive Analysis:

Identify the top 5 merchants in each city based on rating frequency, average rating, and check-in frequency.
Requirement 2: Big Data Application Development Develop a web application using any familiar programming language (e.g., JavaEE, Go, C++, Android, IOS) with the following features:

I. Search:

Display a list of recommended nearby merchants based on the user's current location.
View detailed information about each merchant by clicking on them.
Implement sorting options based on "review recommendations," "distance," and "ratings."
Allow filtering by distance, ratings, facilities, etc.
II. Review Recommendations:

Define algorithms based on user consumption history for personalized recommendations.
Display recommended merchants in the search list, prioritizing them.
III. Business Recommendations:

Provide suggestions to merchants for successful operations (e.g., wake-up services, WiFi availability, parking, credit card payments).
IV. Friend Recommendations:

Recommend potential friends to users.
V. Sentiment Analysis for Reviews:
