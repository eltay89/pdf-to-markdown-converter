import os
import sys
import logging
import traceback
from pathlib import Path
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Set environment variable
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
logging.info("KMP_DUPLICATE_LIB_OK environment variable set to TRUE")

try:
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.datamodel.base_models import InputFormat
    logging.info("Docling modules imported successfully")
except ImportError as e:
    logging.error(f"Failed to import Docling modules: {e}")
    messagebox.showerror("Import Error", f"Failed to import Docling modules: {e}")
    sys.exit(1)

def convert_pdf():
    source = file_path.get()
    if source:
        try:
            logging.info(f"Starting conversion of {source}")
            
            # Create custom pipeline options
            pipeline_options = PdfPipelineOptions()
            pipeline_options.do_ocr = True
            pipeline_options.do_table_structure = True
            logging.debug("Pipeline options set")

            # Create a DocumentConverter instance with custom options
            converter = DocumentConverter(
                allowed_formats=[InputFormat.PDF],
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
            logging.debug("DocumentConverter instance created")

            # Convert the PDF
            logging.info("Starting PDF conversion")
            result = converter.convert(source)
            logging.info("PDF conversion completed")

            # Get the markdown content
            markdown_content = result.document.export_to_markdown()
            logging.debug("Markdown content extracted")

            # Create the output filename
            output_filename = Path(source).with_suffix(".md")
            logging.debug(f"Output filename set to {output_filename}")

            # Write the markdown content to a file
            output_filename.write_text(markdown_content, encoding="utf-8")
            logging.info(f"Markdown content written to {output_filename}")

            # Update status label
            status_label.config(text=f"Conversion complete. Saved as {output_filename}")
        except Exception as e:
            error_msg = f"Error during conversion: {str(e)}\n{traceback.format_exc()}"
            logging.error(error_msg)
            status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Conversion Error", error_msg)
    else:
        logging.warning("No file selected for conversion")
        status_label.config(text="Please select a PDF file first.")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    file_path.set(filename)
    logging.info(f"File selected: {filename}")

# Set up the main window
root = Tk()
root.title("PDF to Markdown Converter")
root.geometry("500x200")

# File path variable
file_path = StringVar()

# Create and place widgets
Label(root, text="Select PDF File:").pack(pady=10)

# Frame for file selection
Entry(root, textvariable=file_path, width=40).pack(pady=5)
Button(root, text="Browse", command=browse_file).pack(pady=5)

# Convert button
Button(root, text="Convert", command=convert_pdf).pack(pady=10)

# Status label
status_label = Label(root, text="", wraplength=400)
status_label.pack(pady=10)

# Start the GUI event loop
logging.info("Starting GUI event loop")
try:
    root.mainloop()
except Exception as e:
    logging.error(f"Error in GUI event loop: {e}")
    messagebox.showerror("GUI Error", f"An error occurred in the GUI: {e}")