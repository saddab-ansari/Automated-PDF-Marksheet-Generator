import csv
import os
from fpdf import FPDF

os.makedirs("Marksheets", exist_ok=True)

def create_pdf_template(): # Function 1 ============================================================
    pdf = FPDF()
    pdf.add_page()
    pdf.image("marksheet.temp.png", x=0, y=0, w=210, h=297)
    return pdf

def fill_student_data(pdf ,Name, grade, English, Science, Maths, History, Arts): # Function 2 ======
    
    pdf.set_font("Arial", size=38) #Student Name
    pdf.text(70, 90, Name)

    pdf.set_font("Arial", size=32) #Grade
    pdf.set_text_color(15, 45, 112)
    pdf.text(107.5, 107, grade)    

    pdf.set_font("Arial", size=23) #Subject Scores
    pdf.set_text_color(0, 0, 0)
    pdf.text(119.5, 152, English )
    pdf.text(119.5, 170, Science )
    pdf.text(119.5, 188.4, Maths )
    pdf.text(119.5, 207.6, History)
    pdf.text(119.5, 226, Arts )

def save_pdf(pdf, Name): # Function 3 =============================================================
    
    pdf.output(os.path.join("Marksheets", f"{Name}.pdf"))

def main(): # MAIN ================================================================================
    
    grade = input("What grade is your Class? ") 
    with open("Test Scores.csv") as file :
        reader = csv.reader(file)
        next(reader)        
        
        for name, english, science, maths, history, arts in reader :
           
            pdf = create_pdf_template()
            fill_student_data(pdf, name, grade, english, science, maths, history, arts)
            save_pdf(pdf, name)
        
if __name__ == "__main__":
    main()