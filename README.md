# Excel to Printable Marksheets
#### Video Demo: < https://youtu.be/e0uc3vBZjHA?si=YLMfHoJ04YJrXlMA >


#### About my project:

I built a program that converts an Excel file of students with their test scores into printable marksheets in PDF form. In this demo, I first convert the Excel file into a CSV, then run my Python script to generate the PDFs automatically. The template used was designed by me in Canva, and its resolution and precise mm measurements played a crucial role in making it work properly. I have used FPDF library for this purpose. FPDF library was explained in lecture, used in Shirtificate problem from Week 08 and therefore, was very clear to me. Hence, i used that library, even if it meant to face another problem, i.e resolution in mm of the given Image.

#### Rules Or Mandatory Conditions for perfect working of CODE :

1. The Code is written using co-ordinates (pixels) of the marksheet.temp.png , Hence, changing the image entirely, resizing the Image or trying to Make its size smaller will crack the code.

2. resolutions of the image :
	in pixel - 1654 x 2339
	in mm - 210 x 297

3. why the resolution in Image and mm is different ? The library i used in creation of this project was FPDF and it only supports images with 'mm resolution' of 210 x 297 or lower. To make it happen, i used a website 	called "Resize  image in mm".

4. The name of the Excel/Csv file used should be "Test Scores" (case sensitive).

5. The program does not automatically convert excel file to csv so please make sure to check if you have done it yourself.
