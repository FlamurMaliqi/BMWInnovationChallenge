import openpyxl

# Pfad zur Excel-Datei
file_path = 'test_file.xlsx'

def process_excel(file_path):
    # Öffne die Excel-Datei
    workbook = openpyxl.load_workbook(file_path)

    # Wähle das erste Arbeitsblatt aus
    worksheet = workbook["Übersicht-Overview"]

    relativ_path = 'test-dictionary/'
    list_of_paths = []

    father_path = ''
    # Iteriere über die Zellen im Arbeitsblatt
    for row in worksheet.iter_rows(min_row=7):
        cell = row[0]
        cell_yes = row[22]
        if cell_yes == 1:
            continue
        if cell.value == "Template":
            break
        # Überprüfe, ob die Zelle einen Hyperlink enthält
        if cell.value:
            if '. ' in cell.value:
                father_path = 'Band_' + cell.value.replace('. ', '-').replace(' ', '_').replace('&', 'und') 
                continue
            path = father_path + '/' + cell.value.replace(' ', '_')
            list_of_paths.append(path)

    workbook.close()
    return list_of_paths
            
    # Schließe die Excel-Datei

print(process_excel(file_path))