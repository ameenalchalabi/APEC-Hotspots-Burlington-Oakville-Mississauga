import pandas as pd

# Path to your current CSV
csv_path = r"C:\Users\ameen\Desktop\GIS projects\Mapping Environmental Degradation Hotspots Across Ontario Using APECs\apec_summary.csv"
output_path = csv_path.replace(".csv", "_with_coords.csv")

# Simple city-to-coordinates dictionary (add more as needed)
city_coords = {
    "Toronto": (43.651070, -79.347015),
    "Mississauga": (43.589045, -79.644120),
    "Guelph": (43.544804, -80.248167),
    "Ottawa": (45.421530, -75.697193),
    "Hamilton": (43.255721, -79.871102),
    "London": (42.984923, -81.245277),
    "Windsor": (42.314937, -83.036363),
    "Kingston": (44.231172, -76.485954),
    "Barrie": (44.389356, -79.690331),
    "Oakville": (43.467517, -79.687665)
}

# Load and map coordinates
df = pd.read_csv(csv_path)
df["Lat"] = df["City"].map(lambda c: city_coords.get(c, (None, None))[0])
df["Long"] = df["City"].map(lambda c: city_coords.get(c, (None, None))[1])

# Save the new CSV
df.to_csv(output_path, index=False)
print(f"✅ CSV with coordinates saved to: {output_path}")

