import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file

data = pd.read_csv("sales.csv")

# Display sales data

print("Retail Sales Data:")
print(data)

# Calculate total sales

total = data["Sales"].sum()

print("\nTotal Sales:", total)

# Display bar chart

plt.bar(data["Product"], data["Sales"])

plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.title("Retail Sales Dashboard")

plt.show()