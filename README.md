# 📄 Automated PDF Marksheet Generator

![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![Library](https://img.shields.io/badge/Library-FPDF-green.svg)
![Design](https://img.shields.io/badge/Design-Canva-blueviolet.svg)

## 🎥 Video Demonstration
[![Marksheet Generator Demo](https://img.youtube.com/vi/e0uc3vBZjHA/maxresdefault.jpg)](https://youtu.be/e0uc3vBZjHA)  
*(Click the image above to watch the full demonstration on YouTube!)*

## 📝 Project Overview
This Python-based automation tool converts student test scores from a spreadsheet into beautifully formatted, ready-to-print PDF marksheets. 

Originally developed as my CS50P Final Project, this script iterates through a CSV database, overlays the student data onto a custom-designed Canva template, and exports individual PDF files. The project heavily relies on the **FPDF library** (introduced in CS50P Week 8) to handle precise coordinate mapping and PDF generation.

## ⚠️ Crucial Requirements & Constraints
**To ensure the code runs perfectly and the layout does not break, you must adhere to the following rules:**

* 📁 **File Naming:** The input data file **must** be named exactly `Test Scores.csv` (case-sensitive). 
* 🔄 **File Format:** The program reads `.csv` files, not `.xlsx`. You must manually export/convert your Excel spreadsheet to a CSV format before running the script.
* 🖼️ **Template Dimensions:** The code maps text to specific coordinate pixels based on `marksheet.temp.png`. Changing, resizing, or compressing this image will completely break the layout.
   * **Required Pixel Resolution:** `1654 x 2339 px`
   * **Required FPDF (mm) Resolution:** `210 x 297 mm` (Standard A4 Size)
   * *Note: FPDF only supports image rendering in millimeter dimensions. The template was strictly resized using an external mm-resizer tool to perfectly match the 210x297mm constraint.*

# 👤 Author

**Saddab Sabir Ansari.**

💼 [LinkedIn](www.linkedin.com/in/saddab-ansari) | 💼 Email - saddabansari254@gmail.com
