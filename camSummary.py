import pdfreader

# Open the pdf file
pdf_file = open("/Users/aishwaryashukla/Downloads/stmt.pdf", "rb")

# Create a PyPDF2 object
pdf_reader = pdfreader.
password = "Fastrack@12"
pdf_reader.decrypt(password)
# Get the number of pages
num_pages = pdf_reader.numPages

# Iterate over the pages
for page_num in range(num_pages):

    # Get the page object
    page = pdf_reader.getPage(page_num)

    # Get the text on the page
    text = page.extractText()

    # Print the text
    print(text)

# Close the pdf file
pdf_file.close()
