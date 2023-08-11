import os
import PyPDF2

# Set the directory path
directory = '/Users/minhnhat/Desktop/others/132'

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        # Create the file path
        filepath = os.path.join(directory, filename)

        # Open the PDF file in read-binary mode
        with open(filepath, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Check if the file is encrypted
            if pdf_reader.is_encrypted:
                # Provide the password to unlock the file
                pdf_reader.decrypt('unlockit') # Replace 'password' with the actual password
                
                # Create a PDF writer object
                pdf_writer = PyPDF2.PdfWriter()

                # Copy the pages of the unlocked PDF file into the PDF writer object
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                # Overwrite the original file with the unlocked content
                with open(filepath, 'wb') as new_file:
                    pdf_writer.write(new_file)
