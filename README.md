# In this project I will take a look at a UFO Sightings Dataset found on Kaggle.
## To access the website go to: https://share.streamlit.io/willcg123/ufo-data/main 
Data Used: UFO Sightings

Purpose: Website that shows and compares UFO sightings around the world.

Queries:
Main page:
Dropdowns with different sections
Map:
Will have a heatmap of most popular UFO sightings areas around the world
This will be separated by state and country
Maybe 2 separate maps one of just US states and other with map of the whole world sorted by country

Date:
Have a chart of UFO Sightings by year, showing most UFO sightings by year
This will be able to be sorted with a slider so it can be sorted by year, month, and day
Could have calendar that the user can choose specific dates to see all UFO sightings that have been on that specific date historically. 
Will list out all UFO sightings 
Shape:
Shape is an important factor in UFO Sightings so I will look at most popular shapes and also most popular shapes each year and, in each country,/state
Duration:
Have a sorted graph of duration of sighting with date and location as x axis and duration as y axis
Statistical Analysis:
Could do analysis to determine if a specific state or country gets on average more UFO sightings
Ex. Perform hypothesis testing to see if one state has more than the rest of the states

Methodology

To accomplish these queries, I will be using Python and packages within Python such as Streamlit, Pandas, MatPlotLib, Numpy, and more to import data and separate/filter it for the purposes I mentioned above. 
For the map, I will create a heatmap of each state and country and have a legend to show differences in the number of sightings. I will also look have it interactive where the user will be able to slide the range or specific year and look at changes throughout history. 
There will also be a bar chart to show the total number of ufo sightings per year and per month as well as separated by individual day of the month. I will also create another graph or combine it with the date graph to show the shape of each of the UFO sightings coupled with date, or location.
I will have a chart showing duration and location which will be sorted by ascending based off duration
Finally, I plan to do some statistical analysis to test whether some states or countries have a higher number of sightings, or test if a certain year or month has higher by doing hypothesis testing in python.
This is my tentative plan, I plan to accomplish most of the queries that I mentioned however, more could be added or some could be tweaked to make the website more user friendly and easy to comprehend. 
