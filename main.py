from flat import Bill, Flatmate
from report import PdfReport, FileSharer

total = float(input("Enter the total amount to be payed(in Rs): "))
time = input("Enter the time period(eg. March 2020): ")
name1 = input("Enter the name of the 1st flatmate: ")
days1 = int(input(f"Enter the number of days {name1} stayed in the house: "))
name2 = input("Enter the name of the 2nd flatmate: ")
days2 = int(input(f"Enter the number of days {name2} stayed in the house: "))
theBill = Bill(total, time)
person1 = Flatmate(name1, days1)
person2 = Flatmate(name2, days2)
pdfReport = PdfReport('bill.pdf')
pdfReport.generate(person1, person2, theBill)
fileShare = FileSharer(pdfReport.filename)
print(f'Click this link for the bill - {fileShare.share()}')
