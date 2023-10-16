import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
plt.style.use('ggplot')

matplotlib.rcParams['figure.figsize'] = (12,8)

# Read in all data sources
file_paths = ["C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/adolescent-fertility.csv", "C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/adolescent-fertility-15-19.csv", "C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/crude-birth-rate.csv", "C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/fertility-rate-vs-the-share-living-in-extreme-poverty.csv", "C:/Users/CiaranO'Brien/OneDrive - Delta Capita Group/Documents/Data Home/Over Population/fertility-vs-contraception.csv"]

dfs = [pd.read_csv(f) for f in file_paths]

# Merge data sources into one
merged_df = pd.merge(dfs[0], dfs[1], on=["Location", "Code", "Year"], how="outer")
for df in dfs[2:]:
    merged_df = pd.merge(merged_df, df, on=["Location","Code", "Year"], how="outer")


merged_df['Population'] = merged_df['Population'].astype('Int64')

# Drop rows where the Year column is less than 1950

merged_df.drop(merged_df[merged_df['Year']<=1950].index, inplace = True)

# What is causing the drop in birth rate? (Correlate)

birth_rate_yearly_averages = merged_df.groupby('Year')['Birth_rate'].mean()

birth_rate_yearly_averages.plot()

plt.yscale('linear')
plt.xlabel('Year')
plt.ylabel('Birth rate (per 1000 Women')
plt.title('Birth Rate Over Time')
plt.grid(True)

plt.show()

merged_df = merged_df.loc[:, ['Birth_rate_10_to_14_years_old', 'Birth_rate_15_to_19_years_old', 'Birth_rate', 'share_of_population_below_poverty_line', 'Contraceptive prevalence ages 15-49']]
correlation_matrix = merged_df.corr(numeric_only=True)

sns.heatmap(correlation_matrix, annot=True)
print(list(merged_df))
plt.show()







# What countries/regions have the greatest drop in birth rate?
# How is this impacting global population?


