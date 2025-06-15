import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('Advertising.csv')

# Print column names to verify
print("Columns in the dataset:", data.columns)

# Check the first few rows of the dataset
print(data.head())

# Visualize the relationship between advertising spend and sales
plt.figure(figsize=(12, 6))

# Scatter plot for TV advertising vs Sales
plt.subplot(1, 3, 1)
sns.scatterplot(data=data, x='TV', y='Sales', color='blue')
plt.title('TV Advertising vs Sales')
plt.xlabel('TV Advertising Spend')
plt.ylabel('Sales')

# Scatter plot for Radio advertising vs Sales
plt.subplot(1, 3, 2)
sns.scatterplot(data=data, x='Radio', y='Sales', color='orange')
plt.title('Radio Advertising vs Sales')
plt.xlabel('Radio Advertising Spend')
plt.ylabel('Sales')

# Scatter plot for Newspaper advertising vs Sales
plt.subplot(1, 3, 3)
sns.scatterplot(data=data, x='Newspaper', y='Sales', color='green')
plt.title('Newspaper Advertising vs Sales')
plt.xlabel('Newspaper Advertising Spend')
plt.ylabel('Sales')

plt.tight_layout()
plt.show()

# Optionally, you can perform a regression analysis
import statsmodels.api as sm

# Define the independent variables (X) and dependent variable (y)
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())
