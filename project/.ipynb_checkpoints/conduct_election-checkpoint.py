import datetime
from project.database import *
#lst=[]

def to_conduct_election(cn):
    
    cname=input("Constitution Name:- ").lower()
    cursor=cn.execute("SELECT constitution_name FROM constitution WHERE constitution_name=?",(cname,))
    consist=cursor.fetchone()
    if consist is None:
        details(cn,cname)
    else:
        print("Election details is Already present for this consistency...")
        return

def details(cn,cname):
    print("Enter Date of Commencement:- \n")
    
    print("Enter Duration:")
    vote_start=input("Enter Election Date(YYYY-DD-MM) :")
    date = datetime.datetime.strptime(vote_start,'%Y-%d-%m').date()

    print("Enter the Voting Start Time :")
    start_time=input("Enter Time (HH:MM) :")
    time = datetime.datetime.strptime(start_time,'%H:%M').time()
    start_date = date.strftime('%d %b %Y')
    start_time = time.strftime('%H:%M')

    print("Enter End Date:")
    vote_end=input("Enter Date(YYYY-DD-MM) :")
    date1 = datetime.datetime.strptime(vote_end,'%Y-%d-%m').date()

    print("Enter the Start Time :")
    end_time=input("Enter Time (HH:MM) :")
    time1 = datetime.datetime.strptime(end_time,'%H:%M').time()
    end_date = date1.strftime('%d %b %Y')
    end_time = time1.strftime('%H:%M')
    duration=date1-date
    
    insert_tbl1(cn,cname,vote_start,start_time,vote_end,end_time)

    print(f'Start date :{start_date} {start_time}')
    print(f'Election Duration:{duration} days')
    print(f'Election End:{end_date} {end_time}')
    
  
    

    
    
    
    
    
    
    