# World Population Analysis
This project is an analysis of the growth of global population from 1950 to 2023, using Python and various libraries and tools. The main goal of this project is to explore the trends and factors that affect the population growth and how it differs from the exponential model.

# Data Sources
The data used in this project comes from the following sources:    
- The data on birth rates, fertility rates, contraception prevalance and poverty was from www.ourworldindata.org  
- The data on global population was from www.macrotrends.net

These datasets can be found in the repository

# Data Processing
The data processing steps include:
- Reading the CSV files using pandas
- Converting the date columns to datetime objects using pandas
- Filtering the data by year and country using pandas
- Merging the data from different sources using pandas

# Data Analysis
The data analysis steps include:
- Plotting the population over time using matplotlib
- Fitting a linear regression model to the population data using numpy
- Calculating the R-squared value of the regression model using numpy
- Plotting the birth rate over time using matplotlib
- Calculating the correlation matrix of the selected variables using pandas
- Plotting the correlation matrix using seaborn

# Data Visualization
The data visualization steps include:
- Adding labels, titles, legends, and annotations to the plots using matplotlib
- Choosing appropriate colors, styles, and sizes for the plots using matplotlib and seaborn
- Saving the plots as PNG files using matplotlib

# Results
The main results of this project are:
- The global population has grown linearly rather than exponentially from 1950 to 2023, with an R-squared value of 0.9967 (to 4 significant figures).
- The birth rate has decreased significantly over time, from about 37 births per 1000 people in 1950 to about 18 births per 1000 people in 2023.
- The birth rate is negatively correlated with the contraceptive prevalence (-0.83) and positively correlated with the share of population below poverty line (0.75).

# Conclusion
- The conclusion of this project is:
- The global population growth is not following the exponential model, but rather a linear one.
- The factors that affect the population growth are mainly related to fertility, health, and development.
- The population growth can be influenced by policies and interventions that improve access to contraception and reduce poverty.

# Installation
To run this project on your local machine, you need to have Python 3 installed. You also need to install the following libraries:
- pandas
- numpy
- matplotlib
- seaborn

# Usage
You can also modify the code or add your own analysis as you wish.

# License
This project is licensed under the MIT License - see https://mit-license.org/ file for details.

# Author
This project was created by Ciaran O'Brien. You can contact me at ciaranjoeobrien@gmail.com or LinkedIn (https://www.linkedin.com/in/ciar%C3%A1nobrien/).

