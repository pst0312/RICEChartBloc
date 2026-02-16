import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pdf2image import convert_from_path
import os  # <--- Add this import

# pixel scan pdf
pdf_filepath = '/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf'

# 1. Create a "base" name without the .pdf extension
# This turns ".../LIST.pdf" into ".../LIST"
base_name = os.path.splitext(pdf_filepath)[0]

img = convert_from_path(pdf_filepath)

for i, page_image in enumerate(img):
    # 2. Create the new filename: Name + Number + .png
    # Example output: ".../GRANT ANALYSIS PDF LIST_page_1.png"
    output_path = f"{base_name}_page_{i + 1}.png"

    page_image.save(output_path, 'PNG')
    print(f"Saved: {output_path}")  # Optional: prints what it saved

# data = {}
# df = pd.Dataframe(data)
# arr = df.to_numpy()