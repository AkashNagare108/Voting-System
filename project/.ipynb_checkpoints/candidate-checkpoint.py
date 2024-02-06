from project.database import *
import datetime

count=0
def candidate_info(cn):
    
    candidate_name=input("Candidate Name:- ")
    
    print("Candidate Date of Birth:- ")
    year=input("Year:- ")
    year_int=int(year)

    print("Note:- enter month in number e.g- january = 01:- ")
    month=input("Month:- ")
    month_int=int(month)

    date=input("Date:- ")
    date_int=int(date)

    dob=datetime.date(year_int,month_int,date_int)
    print(dob)

    d=datetime.date.today()
    age_in_days=d-dob
    age=age_in_days.days//365

    if age>=24:
        print("You Are Eligible To Stand ^_^...")
        pname=input("Party Name:- ")
        constitution=get_consist(cn)
        print("Press:- ")
        for con in constitution:
            print(con)
        cid=int(input("Constitution ID:- "))
        cursor=cn.execute(f"SELECT constitution_name FROM constitution WHERE cid={cid}")
        constitution_name=cursor.fetchall()
        insert_tbl4(cn,candidate_name,dob,pname,constitution_name,count)
        #return cid
    else:
        print("Not Eligible To Stand in Election -_-!!")
        
    
    