import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
plt.style.use('ggplot')

matplotlib.rcParams['figure.figsize'] = (12,8)

# World Population Data

population_df = pd.read_csv("C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/world-population-2023-10-14.csv")
population_df['date'] = pd.to_datetime(population_df['date'], format='%d/%m/%Y')
population_df['Year'] = population_df['date'].dt.strftime('%Y')
population_df_filtered = population_df.loc[(population_df['Year'] >= '1950') & (population_df['Year'] <= '2023')]
population_df_filtered.plot(x='Year', y='Population')

# Calculating the coefficient of determination
# Define a function to calculate R-squared
def r_squared(y, y_hat):
    # Get the mean of y
    y_bar = y.mean()

    # Calculate the total sum of squares
    ss_tot = ((y - y_bar) ** 2).sum()

    # Calculate the residual sum of squares
    ss_res = ((y - y_hat) ** 2).sum()

    # Calculate the R-squared value
    return 1 - (ss_res / ss_tot)



# Define predictor and response variables
x, y = population_df.Year, population_df.Population

# Convert x to a float
x = x.apply(lambda s: float(s))

# Fit a polynomial of degree 1 (linear)
coeffs = np.polyfit(x, y, 1)

# Get the predicted values
y_hat = np.polyval(coeffs, x)

# Calculate the R-squared value using the custom function
r_squared = r_squared(y, y_hat)

# View R-squared value
print(r_squared)

plt.show()

# From this we can see that the population very closely fits the linear model rather than an exponential.