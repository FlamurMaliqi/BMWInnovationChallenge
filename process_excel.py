import openpyxl

# Pfad zur Excel-Datei
file_path = 'test_file.xlsx'

# Öffne die Excel-Datei
workbook = openpyxl.load_workbook(file_path)

# Wähle das erste Arbeitsblatt aus
worksheet = workbook["Übersicht-Overview"]

# Iteriere über die Zellen im Arbeitsblatt
for row in worksheet.iter_rows(min_row=8, max_row=15):
    cell = row[0]
    # Überprüfe, ob die Zelle einen Hyperlink enthält
   

# Schließe die Excel-Datei
workbook.close()