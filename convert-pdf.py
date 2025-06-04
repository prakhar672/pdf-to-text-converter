import PyPDF2

def extract_text_from_pdf(pdf_path, txt_output):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""

            for page in reader.pages:
                text += page.extract_text() + "\n"

        with open(txt_output, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

        print(f"✅ Text extracted and saved to '{txt_output}'")
    except FileNotFoundError:
        print("❌ PDF file not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Run it
extract_text_from_pdf("sample.pdf", "output.txt")
