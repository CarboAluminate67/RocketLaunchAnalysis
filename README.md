# Overview

I created a Python script to analyze data from a set of Launch and Launch vehicle data sets. The csv files I found included every recorded launch in history, launch vehicles, companies and agencies, etc. I created this small project to practice data analysis and introduce myself to the pandas library. During the project I asekd questions about the data concerning improvements of our launch vehicles overtime, statistics on the launch providers, and analyzing overall success rate.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results
1. Have Rockets improved overtime?   
    For this analysis I created two plots, the first being somewhat misleading: A scatter plot of thrust of launch vehicles plotted to the year of their first launch. This resulted in fairly scattered data points, but generally showed higher thrust vehicles being older. However more liftoff thrust does not mean better. To demonstrate this I created a second plot comparing the debut year of the launch vehicle, to the cost in USD per kg brought to LEO. This showed a clear regression and improvements into modern day rockets, as well as showed the increased frequency of launches within the last few years.
2. What Companies provide the most launches?
    To answer this I created a basic bar graph in ascending order showing which company has launched the most and least rockets, discluding any company/agency with less than 10 launches.
3. How do companies stand in success rate?
    To answer this I made a basic table in the terminal with a custom dataframe created from two different csv files, which gives the company, total launches, successes, and failures, compared to the worldwide average success rate of 95.58%. I then created a bar graph showing the companies with the highest success rates. Finally, I demonstrated the idea that success rate will approach the mean as the sample size increase, with a scatter plot of number of company wide launches to the respective companies success rate. 
# Development Environment

The project was completed in VScode using Python 3.12.0. I incorporated the numpy, pandas, and matplotlib libraries to create and manage dataframes, as well as plot the data that I collected.

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/)
* [Kaggle](https://www.kaggle.com/)

# Future Work

* Clean up data and eliminate unused csv files from archive
* Use additional graphic systems in the plots such as coloring to convey more data in one plot
* Update source data to include launches and veahicles further than 2020.