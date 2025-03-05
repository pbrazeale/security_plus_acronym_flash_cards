import pandas as pd


with open("security+_acronum_list.txt", "r") as list_txt, open(
    "data.txt", "w"
) as data_txt:
    for line in list_txt:
        comma_line = line.replace(" ", ",", 1).strip() + "\n"
        # print(repr(comma_line))
        data_txt.write(comma_line)


# Read the file manually and split only on the first comma
data = []
with open("data.txt", "r") as file:
    next(file)
    for line in file:
        parts = line.strip().split(",", 1)  # Split only on the first comma
        if len(parts) == 2:
            data.append(parts)  # Append correctly split parts
        else:
            data.append([parts[0], ""])  # Handle cases where no comma exists

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Acronym", "Spelled Out"])

# Save to CSV
df.to_csv("../data/acronym_list.csv", index=False)

# Print the first few rows for verification
print(df.head())
