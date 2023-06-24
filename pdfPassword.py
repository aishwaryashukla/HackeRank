from datetime import timedelta, date
import pikepdf
import datetime
dt  = datetime.date(2015, 1, 20)
print(dt.day)

start_date = date(2021, 1, 1)
end_date = date(2022, 1, 1)
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
        
def open_pdf(f,msg):
    with pikepdf.open(f,password=msg) as pdf:
        num_pages = len(pdf.pages)
        print("Total pages:", num_pages)
        
for single_date in daterange(start_date, end_date):
    msg = "aish"+single_date.strftime("%d%m")

    try:
        open_pdf("icici.pdf",msg)
        print(msg)
    except:
        print(end='')