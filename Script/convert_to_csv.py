import os
import csv

# 🔁 Set this to the path where your summary TXT file is located
base_path = r"C:\Users\ameen\Desktop\GIS projects\Mapping Environmental Degradation Hotspots Across Ontario Using APECs"
input_path = os.path.join(base_path, "apec_summary_results.txt")
output_path = os.path.join(base_path, "apec_summary.csv")

# 📄 Create the CSV file
with open(output_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["City", "Source_File", "Line_Number", "Matched_Text"])

    with open(input_path, "r", encoding="utf-8") as f:
        current_file = None
        for line in f:
            line = line.strip()
            if line.startswith("📄"):
                current_file = line[2:].strip(": ")
                city = os.path.basename(os.path.dirname(current_file))
            elif line.startswith("- Line") and current_file:
                parts = line.split(": ", 1)
                line_number = parts[0].split("Line")[1].strip()
                matched_text = parts[1] if len(parts) > 1 else ""
                writer.writerow([city, os.path.basename(current_file), line_number, matched_text])

print(f"✅ CSV saved to: {output_path}")
