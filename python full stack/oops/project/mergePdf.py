from pypdf import PdfWriter
from pathlib import Path

def get_new_filename(file_path):
    file_path = Path(file_path)
    
    if not file_path.exists():
        return file_path  
    
    counter = 1
    while True:
        new_file = file_path.with_stem(f"{file_path.stem}_{counter}")
        if not new_file.exists():
            return new_file
        counter += 1
merger = PdfWriter()


file_path = "C:/Users/User/OneDrive/Documents/word/pdf/merged_output.pdf"
new_path = get_new_filename(file_path)
merger.append("C:/Users/User/OneDrive/Documents/word/pdf/html notes.pdf")
merger.append("C:/Users/User/OneDrive/Documents/word/pdf/Damodara_Sonali.pdf")
merger.write(new_path)

    

merger.close()
