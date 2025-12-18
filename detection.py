import magic, os
filepath = input("Filepath: ").strip()
if filepath.startswith("&"):
    filepath = filepath[1:].strip()
if (filepath.startswith('"') and filepath.endswith('"')) or (filepath.startswith("'") and filepath.endswith("'")):
    filepath = filepath[1:-1]
filepath = filepath.replace("''", "'")
if not os.path.exists(filepath):
    raise FileNotFoundError(filepath)
mime = magic.from_file(filepath, mime=True)
print(mime)