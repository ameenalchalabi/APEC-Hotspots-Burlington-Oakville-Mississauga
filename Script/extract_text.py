import os
import fitz  # PyMuPDF

# 🔁 CHANGE THIS PATH to the folder containing your city folders
base_path = r"C:\Users\ameen\Desktop\GIS projects\Mapping Environmental Degradation Hotspots Across Ontario Using APECs"

# Loop through each city folder
for city in os.listdir(base_path):
    city_path = os.path.join(base_path, city)
    if os.path.isdir(city_path):
        for file in os.listdir(city_path):
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(city_path, file)
                output_txt_path = os.path.splitext(pdf_path)[0] + ".txt"

                try:
                    with fitz.open(pdf_path) as doc:
                        full_text = ""
                        for page in doc:
                            full_text += page.get_text()

                    with open(output_txt_path, "w", encoding="utf-8") as f:
                        f.write(full_text)

                    print(f"✅ Extracted text from: {pdf_path}")
                except Exception as e:
                    print(f"❌ Failed on {pdf_path}: {e}")

