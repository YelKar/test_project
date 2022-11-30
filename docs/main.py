from docx import Document
from colorama import Fore, Style, Back

doc = Document("мини_эссе.docx")

text = "\n\r\t".join([p.text for p in doc.paragraphs])

print(
    f"{Back.BLACK}{Style.BRIGHT}{Fore.WHITE}"
    f"\t\t\t\t\t\t\t\t\t{text:1200}\n"
    f"{Style.RESET_ALL}",
    "\n\n"
    f"{Fore.GREEN}{Style.BRIGHT}"
    f"Количество букв: {len(text)}"
    f"{Style.RESET_ALL}"
)
