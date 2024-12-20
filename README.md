# PDF to Markdown Converter

This project is a simple GUI application that converts PDF files to Markdown format using the Docling library. The application allows users to select a PDF file and convert it into a Markdown file with ease.

## Features

- Convert PDF files to Markdown format.
- Easy-to-use graphical user interface (GUI).
- Supports OCR (Optical Character Recognition) for scanned documents.
- Handles table structures in PDFs.

## Requirements

- Python 3.10 and above
- PyTorch
- Tkinter (Tk)
- Docling

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/pdf-to-markdown-converter.git
   cd pdf-to-markdown-converter
   ```

2. Install the required packages:

   ```bash
   pip3 install torch torchvision torchaudio  #CPU_Only
   pip install tk
   pip install docling
   ```

   Note: PyTorch installation may vary depending on your system. Please refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/) for specific instructions.

3. Ensure you have Tkinter installed. It usually comes pre-installed with Python on most systems, but if not, you may need to install it separately.

## Usage

1. Run the application:

   ```bash
   python pdf2md.py
   ```

2. Click on "Browse" to select a PDF file you want to convert.

3. Click on "Convert" to generate a Markdown file.

4. The converted Markdown file will be saved in the same directory as the original PDF file with the same name but with a `.md` extension.

## Troubleshooting

If you encounter an OpenMP runtime error, try setting the following environment variable before running the script:

```bash
set KMP_DUPLICATE_LIB_OK=TRUE
```

Or add this line at the beginning of your Python script:

```python
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
```
## References

For more information about Docling and its features, check out the official documentation: [Docling Documentation](https://github.com/DS4SD/docling).

```
@techreport{Docling,
  author = {Deep Search Team},
  month = {8},
  title = {Docling Technical Report},
  url = {https://arxiv.org/abs/2408.09869},
  eprint = {2408.09869},
  doi = {10.48550/arXiv.2408.09869},
  version = {1.0.0},
  year = {2024}
}
```
