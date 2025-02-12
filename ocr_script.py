import pytesseract
import cv2
import json
import os
from pdf2image import convert_from_path
from PIL import Image

# Windows users: Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Thresholding
    return thresh

def extract_text(image_path):
    """Extract text from an image."""
    processed_img = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(processed_img)
    return extracted_text

def pdf_to_images(pdf_path):
    """Convert PDF pages to images."""
    images = convert_from_path(pdf_path)
    image_paths = []
    
    for i, img in enumerate(images):
        image_path = f"page_{i+1}.jpg"
        img.save(image_path, "JPEG")
        image_paths.append(image_path)
    
    return image_paths

def extract_text_from_pdf(pdf_path):
    """Extract text from all pages of a PDF."""
    images = pdf_to_images(pdf_path)
    full_text = ""

    for img in images:
        text = extract_text(img)
        full_text += text + "\n"
        os.remove(img)  # Delete temp images

    return full_text

# Test OCR on a sample image
image_path = "patient_form.jpg"
print("Extracted Text:", extract_text(image_path))

# Test OCR on a sample PDF
pdf_path = "patient_form.pdf"
print("Extracted Text from PDF:", extract_text_from_pdf(pdf_path))
