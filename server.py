from project.database import *
from project.admin import *
from project.conduct_election import *
from project.voter import *
from project.voter_login import *

m_101="Thanks For Visiting --^_^--"
e_102="Invalid Choice -_-!"

def main():  
    cn=create_connection()
    create_table(cn)
    while True:
        option=['Admin Login','Voter Login','Exit']
        for no,opt in enumerate(option,1):
            print(f"{no}) {opt}")
        try:
            choice=int(input("Enter your choice:- "))
            if choice==1:
                admin(cn)
                #cname=add_constitution(cn)
                #insert_tbl2(cn,cname)
            elif choice==2:
                voter_login(cn)
   
            elif choice==3:
                print(m_101)
                break
                return
                
            else:
                print(e_102)
        except ValueError:
            print("Please ^_^ Enter Integer Value..!!")
            
main()