from PIL import Image
from pypdf import PdfReader, PdfWriter, PdfMerger
import os

# Splitting pdf pages
input_pdf = PdfReader("./sample/test.pdf")
print("split operation is in proccess")
for index, page in enumerate(input_pdf.pages):
    output = PdfWriter()
    output.add_page(page)
    output.write(f"./sample/split/{index+1}-page.pdf")
print("Split operation completed")


# Merging pdf files
print("Merge operation in process ")
output = PdfMerger()
for pdf in os.listdir("./sample/split/"):
    if pdf.endswith(".pdf"):
        pdf_file = PdfReader("./sample/split/" + pdf)
        output.append(pdf_file)
        print(pdf)
output.write("./sample/merge/merged.pdf")
print("Merge operation completed")

# Crop the pdf file
cropinput = PdfReader("./sample/test.pdf")
print("croping on process")
cropoutput = PdfWriter()
single_page = cropinput.pages[0]
single_page.mediabox.upper_left = [550, 0]
single_page.mediabox.lower_right = [50, 112]
cropoutput.add_page(single_page)
cropoutput.write("./sample/crop/crop.pdf")
print("cropping successfull")

# tilting the pdf page
tilt_output = PdfWriter()
print("Tilting is in process")
tilt_page = cropinput.pages[1]
tilt_page.rotate(270)
tilt_output.add_page(tilt_page)
tilt_output.write("./sample/tilt page/tilt.pdf")
print("Tilt successfull")


# pdf to image
import pypdfium2

pdf = pypdfium2.PdfDocument("./sample/test.pdf")
print("pdf to image is in process")
# render a single page
for i in range(len(pdf)):
    page = pdf[i]
    pil_image = page.render(scale=4).to_pil()
    pil_image.save(f"./sample/pdf-jpg/output{i+1}.jpg")
print("JPEG created successfully")


# convert jpg to pdf
for i in range(len(pdf)):
    image1 = Image.open(f"./sample/pdf-jpg/output{i+1}.jpg")
    outputImage = image1.convert("RGB")
    outputImage.save(f"./sample/jpg-pdf/output{i+1}.pdf")
print("Image convert to PDF")
