import pandas as pd

# ----------- WRITE CSV -----------

# Create a simple dataset (dictionary)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("output.csv", index=False)

print("CSV file written successfully!")


# ----------- READ CSV -----------

# Read the CSV file
df_read = pd.read_csv("output.csv")

# Display the contents
print("\nData read from CSV:")
print(df_read)