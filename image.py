import fitz  # PyMuPDF
from PIL import Image

import fitz  # PyMuPDF
from PIL import Image

# Path to your PDF file
pdf_path = 'D:\\VADS Consulting Private Limited\\GFPO-IT Dept - Accounting Software- AI - Accounting Software- AI\\OCR documents Bank statements\\05. 2024 - TD Bank 2659 - May.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through each page
for page_num in range(len(pdf_document)):
    # Get the page
    page = pdf_document.load_page(page_num)

    # Render the page to an image (pixmap)
    pix = page.get_pixmap()

    # Convert the pixmap to a PIL Image
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the image to a file
    # img_path = f'page_{page_num + 1}.png'
    #img.save(img_path)

    # Display the image
    img.show()

# Close the PDF file
pdf_document.close()
