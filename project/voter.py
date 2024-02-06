from project.database import *
import random
import datetime

alpabet="abcdefghijklmnopqrstuvwxyz"
symbol="!@#$%&*"
num="1234567890"
password= alpabet+symbol+num
length=8

m_101="Thanks for Visisting --^_^--"
e_101="Invalid Choice -_-!"

chance=1
def voter_info(cn):
    cn=create_connection()
    create_table(cn)
    pswd="".join(random.sample(password,length))
    
    print("Please Enter Your Birth Date in Steps 1) Year 2) Month 3) Day:- ")
    #age=int(input("Age:- ")) 
    year_str=input("Year:- ")
    y_int=int(year_str)
    
    month_str=input("Month:- ")
    m_int=int(month_str)
    
    day_str=input("Day:- ")
    d_int=int(day_str)
    
    birthdate=datetime.date(y_int,m_int,d_int)
    #birthdate=datetime.date(year,month,day)
    print(birthdate)
    d=datetime.date.today()
    
    age_in_days=d-birthdate
    age=age_in_days.days//365
    if age >= 18:
        print("You Are Eligible For vote...")
        voter_name=input("Enter Full Name:- ")
        print("\n")
        print("Press.")
        consistency=get_consist(cn)
        for consist in consistency:
            print(consist)
        choose=int(input("Choose Consistency:- "))
        
        cursor=cn.execute(f"SELECT constitution_name FROM constitution WHERE cid={choose}")
        const=cursor.fetchall()
        print(f"Your Voter Password:- {pswd}")
        insert_tbl2(cn,voter_name,const,birthdate,age,pswd,chance)
        
    else:
        print("You Are not Eligible For vote")
        return
    
def update_v(cn):
    try:
        while True:
            voter_update=['Name','Constitution','Date Of Birth','Exit']
            for no,ch in enumerate(voter_update,1):
                print(f"{no}) {ch}")
            choice=int(input("Enter Choice:- "))
            
            if choice>=1 and choice<=len(voter_update):
                
                if choice ==1:
                    vid=int(input("Voter ID:- "))
                    vname=input("New Voter Name:- ")
                    update_voter(cn,vid,vname)
                    
                elif choice==2:
                    vid=int(input("Voter ID:- "))
                    print("Select Constitution which you want to update:- ")
                    consistency=get_consist(cn)
                    print(consistency)
                    cid=int(input("Constitution ID:- "))
                    cursor=cn.execute(f"SELECT constitution_name FROM constitution WHERE cid={cid}")
                    cname=cursor.fetchall()
                    update_constitution(cn,vid,cname)
        
                elif choice==3:
                    vid=int(input("Voter ID:- "))
                    print("Enter Date of Birth:- ")
                    year=input("Year:- ")
                    year_int=int(year)
                    
                    month=input("Month:- ")
                    month_int=int(month)
                    
                    date=input("Date:- ")
                    date_int=int(date)

                    dob=datetime.date(year_int,month_int,date_int)
                    print(f"This is Your New Birth Date :- {dob}")
                    update_dob(cn,vid,dob)
                    
                elif choice==4:
                    print(m_101)
                    break
                    return
            else:
                print(e_101)
    except ValueError:
        print("Please ^_^ Enter Integer Value...")
            
    