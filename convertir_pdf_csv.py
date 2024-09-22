import os
import tabula

# Carpeta donde están los PDFs
pdf_folder = "pdfs/"

# Carpeta donde se guardarán los archivos CSV
output_folder = "csv_output/"

# Si la carpeta de salida no existe, la crea
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Recorre todos los archivos PDF de la carpeta
for file_name in os.listdir(pdf_folder):
    if file_name.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file_name)
        output_csv = os.path.join(output_folder, file_name.replace(".pdf", ".csv"))

        # Convierte el PDF a CSV
        tabula.convert_into(pdf_path, output_csv, output_format="csv", pages="all")

        print(f"Convertido: {file_name} a {output_csv}")

