import pandas as pd
from pathlib import Path

# Get absolute path of current script folder
script_dir = Path(__file__).resolve().parent

# Construct absolute path to CSV file (relative to project root)
csv_path = script_dir.parent / "data" / "csv" / "faculty.csv"

# Construct absolute path to output folder & file
output_dir = script_dir.parent / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)  # Create if doesn't exist
output_file = output_dir / "teacher_chunks.txt"

# Read the CSV file
df = pd.read_csv(csv_path)

teacher_chunks = []
for _, row in df.iterrows():
    # Build text chunk for each row, adapt column names if needed
    text = f"{row['Name']} can be contacted at {row['Mobile No.']}. Cabin is {row['Cabin No.']}."
    teacher_chunks.append(text)

# Write output text file
with open(output_file, "w", encoding="utf-8") as f:
    for line in teacher_chunks:
        f.write(line + "\n")

print(f"✅ Teacher data processed successfully. Output saved to:\n{output_file}")
