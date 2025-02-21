cd ..
cd ..
D:
cd compile/pyautoGUI_scripe
pyinstaller --hidden-import=PIL._imaging --hidden-import=PIL._imagingft --onefile --add-data "image_png;image_png" --add-data "saves;saves" main.py