
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pdf2image import convert_from_path




# pixel scan pdf
pdf_filepath = '/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf'
# windows
# poppler_path = r"C:\Users\sarah\Desktop\Release-25.12.0-0\poppler-25.12.0\Library\bin
img = convert_from_path(pdf_filepath)
data = []
for i in range(len(img)):
    img[i].save(f'/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf{i+1}.png', 'PNG')
    data.append(f'/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf{i+1}.png')


df = pd.DataFrame(data)
# arr = df.to_numpy()
print(df)
# ml model -> find trends, predict wavelength indicators