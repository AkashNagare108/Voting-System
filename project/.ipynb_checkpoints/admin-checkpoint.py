from project.conduct_election import to_conduct_election
from project.voter import *
from project.database import *
from project.candidate import *
#import datetime
m_101="Thanks For Visiting --^_^--"
e_101="Invalid Choice -_-!"
e_102="username or password not valid -_-!"
def admin(cn):
    
    admin_data={1:{'name':'akash','password':'1234'}}
    aid= int(input("Admin ID:- "))
    pswd=input("Password:- ")
    cursor=cn.execute(f"SELECT paswd FROM admin_login WHERE aid={aid}")
    admin=cursor.fetchone()
    #if admin:
        #admin_id,a_pass=admin
    if aid in admin_data and pswd == admin_data[aid]['password']:
        while True:
            print("------Welcome Admin------")
            option=['To Conduct Election','Add Candidate','Add Voter','Update Voter','Logout']
            for no,opt in enumerate(option,1):
                print(f"{no}) {opt}")
            try:
                choice= int(input("Enter Choice:- "))
                if choice==1:
                    to_conduct_election(cn)
                elif choice==2:
                    candidate_info(cn)
            
                elif choice==3:
                    voter_info(cn)

                elif choice==4:
                    update_v(cn)
           
                elif choice==5:
                    print(m_101)
                    break
                else:
                    print(e_101)
                    
            except ValueError:
                print("Please ^_^ Enter Integer Value...!!!")
                
    else:
        print(e_102)