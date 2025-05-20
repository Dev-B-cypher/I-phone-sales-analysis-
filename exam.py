import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("apple_sales_2024.csv")

# Summary statistics
summary_stats = df.describe()

# Total iPhone sales by region
region_iphone_sales = df.groupby('Region')['iPhone Sales (in million units)'].sum().sort_values(ascending=False)

# Top 5 states by iPhone sales
top_states_iphone = df.sort_values(by='iPhone Sales (in million units)', ascending=False).head(5)

# Correlation matrix
correlation = df.iloc[:, 2:].corr()

# Save correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='Blues')
plt.title('Correlation Matrix of Apple Product Sales')
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Display outputs
print("=== Summary Statistics ===")
print(summary_stats[['iPhone Sales (in million units)', 'iPad Sales (in million units)',
                     'Mac Sales (in million units)', 'Wearables (in million units)',
                     'Services Revenue (in billion $)']])

print("\n=== Total iPhone Sales by Region ===")
print(region_iphone_sales)

print("\n=== Top 5 States by iPhone Sales ===")
print(top_states_iphone[['State', 'Region', 'iPhone Sales (in million units)']])

print("\nCorrelation heatmap saved as 'correlation_heatmap.png'")
