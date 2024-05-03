import os
import json


def take_snapshot(folder_path):
    snapshot = {}
    for root, dirs, files in os.walk(folder_path):
        root_path = os.path.relpath(root, folder_path)
        snapshot[root_path] = {
            'directories': dirs,
            'files': files
        }
    return snapshot


def save_snapshot(snapshot, output_file):
    with open(output_file, 'w') as f:
        json.dump(snapshot, f, indent=4)


def main():
    folder_path = input("Bitte geben Sie den Pfad zum Ordner ein: ")
    if not os.path.exists(folder_path):
        print("Der angegebene Ordner existiert nicht.")
        return

    snapshot = take_snapshot(folder_path)
    output_file = input("Bitte geben Sie den Namen der Ausgabedatei für den Snapshot ein: ")
    save_snapshot(snapshot, output_file)
    print("Snapshot wurde erfolgreich erstellt und unter", output_file, "gespeichert.")


if __name__ == "__main__":
    main()
