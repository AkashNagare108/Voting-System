from project.database import *
from project.voter import *
from project.candidate import *
import datetime

voter="Voting System"
a="-"
width=40
b=a*width
vote=0
m_101="Thanks For Visiting ^_^..."
e_101="Invalid Choice -_-!!"
def voter_header():
    print(f"{b}\n {voter.center(width)} \n {b}")
def voter_login(cn):
    voter_header()
    vid=int(input("Voter ID:- "))
    vname=input("Voter Name:- ")
    vpass=input("Voter Password:- ")
    cursor=cn.execute(f"SELECT voter_name,voter_paswd FROM voter WHERE vid={vid}")
    vlogin=cursor.fetchone()
    if vlogin:
        v_name,v_pass=vlogin
        if vname==v_name and vpass==v_pass:
            print("Login Successfull ^_^")
            voter_header()
            print(f"Welcome ^_^ {vname}")
            first_screen(cn,vid)
        else:
            print("Login Failed.-_-!!")
    else:
        print("Invalid Voter Info...!!!")
            
        
def first_screen(cn,vid):
    #try:
    while True:
        lst=['To Vote','Get Result','exit']
        for no,opt in enumerate(lst,1):
            print(f"{no}) {opt}")
        choice=int(input("Enter Choice:- "))
        if choice>=1 and choice<=len(lst):
            if choice ==1:
               
                candidate=get_candidate(cn)
                print("Press:- ")
                for candidate_name in candidate:
                    print(candidate_name)
                choice=int(input("Vote To:- "))
                
                chance_remain=chance_vote(cn,vid)
                for ch in chance_remain:
                #print(chance_remain)
                    if ch == '1':
                        cand=get_candidate_count(cn,choice)
                        cn.execute(f"UPDATE candidates set count=count+1 WHERE can_id={choice}")
                        cn.commit()
                        
                        cn.execute(f"UPDATE voter set chance_vote={vote} WHERE vid={vid}")
                        cn.commit()
                        print("Voted Successfully..")
                        
                        
                    else:
                        print("Already Voted Cannot Vote Again *_*!")
       
                    
                        
            elif choice ==2:
                #candidate=get_candidate(cn)
                cand=get_result(cn)
                #for candidate_name in candidate:
                for cand1 in cand:
                    print(f"{cand1}")
                
                
            elif choice==3:
                print(m_101)
                return
        else:
            print(e_101)
            
    
    