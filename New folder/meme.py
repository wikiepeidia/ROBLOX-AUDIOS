# Define the file paths
input_file = "name.txt"
output_file = "output.txt"

# Read the content from name.txt
with open(input_file, "r") as f:
    ids = f.read().splitlines()

# Convert each line to the required format
formatted_ids = [f'"rbxassetid://{id.strip()}"' for id in ids if id.strip()]

# Write the output to output.txt with commas and brackets
with open(output_file, "w") as f:
    f.write("[\n")
    f.write(",\n".join(formatted_ids))
    f.write("\n]")
