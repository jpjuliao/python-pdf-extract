import sys
import os
import fitz  # PyMuPDF

def extract_assets(pdf_path, output_folder):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        image_list = page.get_images(full=True)
        
        # Iterate through each image on the page
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            # Write the image bytes to a file
            image_path = os.path.join(output_folder, f"page_{page_number + 1}_image_{image_index + 1}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

    pdf_document.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <pdf_path> <output_folder>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(pdf_path):
        print("Error: PDF file not found.")
        sys.exit(1)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extract_assets(pdf_path, output_folder)
