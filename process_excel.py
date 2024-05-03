import openpyxl
import os

# Pfad zur Excel-Datei
file_path = 'test_file.xlsx'


def process_excel(file_path):
    # Öffne die Excel-Datei
    workbook = openpyxl.load_workbook(file_path)

    # Wähle das erste Arbeitsblatt aus
    worksheet = workbook["Übersicht-Overview"]

    dict_of_paths = {}

    father_path = ''
    # Iteriere über die Zellen im Arbeitsblatt
    for row in worksheet.iter_rows(min_row=7):
        cell = row[0]
        cell_yes = row[24]
        cell_file_extension = row[23]

        if cell.value and cell_yes.value == "Yes":
            path = father_path + '/' + cell.value.replace(' ', '_')
            dict_of_paths[path] = cell_file_extension.value
        elif cell.value:
            father_path = 'Band_' + cell.value.replace('.', '-').replace(' ', '_').replace('&', 'und')

    workbook.close()
    return dict_of_paths


def check_files_exist(file_paths):
    """
    Check if the directories at the given paths contain a file with the given extension.

    Parameters:
    file_paths (list): A list of directory paths.
    file_extension (str): The file extension to check for.

    Returns:
    dict: A dictionary where the keys are the directory paths and the values are booleans indicating whether the directory contains a file with the given extension.
    """
    result = {}
    for path, file_extension in file_paths.items():
        path = "test_directionary/" + path
        if os.path.exists(path):
            for file in os.listdir(path):
                if os.path.splitext(file)[1] == file_extension:
                    result[path] = True
                    break
            else:
                result[path] = False
        else:
            result[path] = False
    return result


print(check_files_exist(process_excel(file_path)))
#print(process_excel(file_path))