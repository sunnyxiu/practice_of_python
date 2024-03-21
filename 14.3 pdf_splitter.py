from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

class PdfFileSplitter:
    def __init__(self, path_string):
        self.path = Path.cwd() / path_string
        self.pdf_reader = PdfReader(self.path)

    def split(self, breakpoint):
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()
        for page in self.pdf_reader.pages[:breakpoint]:
            self.writer1.add_page(page)
        for page in self.pdf_reader.pages[breakpoint:]:
            self.writer2.add_page(page)

    def write(self, filename):
        self.path1 = Path(f"{Path.cwd()} / {filename}_1.pdf")
        self.path2 = Path(f"{Path.cwd()} / {filename}_2.pdf")
        with self.path1.open(mode="wb") as output_pdf1:
            self.writer.write(output_pdf1)
        with self.path2.open(mode="wb") as output_pdf2:
            self.writer.write(output_pdf2)

    
        

        
        
        
        
