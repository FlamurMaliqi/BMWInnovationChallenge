import openpyxl

# Pfad zur Excel-Datei
file_path = 'test_file.xlsx'

# Öffne die Excel-Datei
workbook = openpyxl.load_workbook(file_path)

# Wähle das erste Arbeitsblatt aus
worksheet = workbook["Übersicht-Overview"]

relativ_path = 'test-dictionary/'

# Iteriere über die Zellen im Arbeitsblatt
for row in worksheet.iter_rows(min_row=7):
    cell = row[0]
    # Überprüfe, ob die Zelle einen Hyperlink enthält
    father_path = ''
    if cell.value:
        if '. ' in cell.value:
            father_path = 'Band_' + cell.value.replace('. ', '-').replace(' ', '_').replace('&', 'und') 
        
   

# Schließe die Excel-Datei
workbook.close()