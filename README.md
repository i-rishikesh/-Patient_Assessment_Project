# Patient Assessment Project

## 📌 Overview
This project extracts text from scanned patient assessment forms using OCR, processes the extracted text into structured JSON, and stores it in a PostgreSQL database.

## 🏗 Repository Structure
```
📂 patient_assessment_project
├── 📄 ocr_script.py         # Extracts text from images using OCR
├── 📄 parse_ocr.py         # Parses OCR text into structured JSON
├── 📄 store_in_db.py       # Saves JSON data into PostgreSQL
├── 📄 db_setup.sql         # SQL script to set up the database
├── 📄 sample_output.json   # Example JSON output
├── 📄 README.md            # Setup and usage instructions
```

## 🔧 Setup & Installation
### Prerequisites
- Python 3.8+
- PostgreSQL
- Tesseract OCR
- Required Python packages (install using `pip install -r requirements.txt`)

### Database Setup
1. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE patient_data;
   ```
2. Set up the tables:
   ```sh
   psql -U postgres -d patient_data -f db_setup.sql
   ```

### Running the Scripts
1. **Extract text from a form**:
   ```sh
   python ocr_script.py patient_form.pdf
   ```
2. **Parse extracted text**:
   ```sh
   python parse_ocr.py output_text.txt
   ```
3. **Store parsed data in PostgreSQL**:
   ```sh
   python store_in_db.py parsed_data.json
   ```

## 📜 Sample JSON Output
```json
{
    "name": "John Doe",
    "dob": "01-01-1980",
    "gender": "Male",
    "medications": ["Aspirin", "Metformin"],
    "allergies": ["Peanuts"]
}
```

## 🚀 Future Improvements
- Enhance OCR preprocessing for better text recognition.
- Improve text parsing using NLP techniques.
- Create a web interface for uploading forms and viewing extracted data.

---
📌 **Author**: Rishikesh  
📧 Contact: rishikeshmishra2102@gmail.com  
🔗 LinkedIn: [Profile](https://www.linkedin.com/in/rishikesh2102/)
