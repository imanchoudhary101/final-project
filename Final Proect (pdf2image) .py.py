from pdf2image import convert_from_path
old_pdf = convert_from_path("10th Chemistry Important Questions.pdf",
                    poppler_path=r"Release-24.08.0-0.zip\poppler-24.08.0\Library\bin - ZIP archive, unpacked size 49,270,052 bytes")
for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")