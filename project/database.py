import sqlite3

def create_connection():
    db=sqlite3.connect("DATA.db")
    return db
def create_table(cn):

    #cn.execute("drop table constitution")
    
    
    tbl1='''CREATE TABLE IF NOT EXISTS constitution
        (cid INTEGER PRIMARY KEY AUTOINCREMENT,
         constitution_name  TEXT   UNIQUE,
         date_start      TEXT  NOT NULL,
         time_start       TEXT  NOT NULL,
         end_date         TEXT  NOT NULL,
         end_time         TEXT   NOT NUll)'''
    
    tbl2='''CREATE TABLE IF NOT EXISTS voter
        (vid INTEGER PRIMARY KEY AUTOINCREMENT,
         voter_name TEXT NOT NULL,
         voter_consistency   TEXT   NOT NULL,
         voter_dob     TEXT     NOT NULL,
         voter_age  INT NOT NULL,
         voter_paswd   TEXT  NOT NULL,
         chance_vote    INT   NOT NULL)'''
    
    tbl3='''CREATE TABLE IF NOT EXISTS admin_login
        (aid INTEGER PRIMARY KEY AUTOINCREMENT,
         admin_name     TEXT   NOT NULL,
         paswd          TEXT   NOT NULL)'''


    tbl4='''CREATE TABLE IF NOT EXISTS candidates
            (can_id  INTEGER PRIMARY KEY AUTOINCREMENT,
             candidate_name TEXT NOT NULL,
             can_dob     TEXT     NOT NULL,
             party_name   TEXT    NOT NULL,
             can_constitution   TEXT   NOT NULL,
             count INT  NOT NULL)'''
    
    for tbl in [tbl1,tbl2,tbl3,tbl4]:
        cn.execute(tbl)

#def admin_login(cn,a_name,pswd):
    
#    tbl3=(f"INSERT INTO admin_login (admin_name,paswd) VALUES ('akash','1234')")
#    cn.execute(tbl3)
    
def insert_tbl1(cn, cname,vote_start,start_time,vote_end,end_time):
    try:
        cursor = cn.execute(f"SELECT constitution_name FROM constitution WHERE constitution_name = ('{cname}')")
        con_exists = cursor.fetchone()
        if con_exists is None:
            cn.execute(f"INSERT INTO constitution (constitution_name,date_start,time_start,end_date,end_time) VALUES ('{cname}','{vote_start}','{start_time}','{vote_end}','{end_time}')")
            cn.commit()
            print("Data Inserted")
        else:
            print("Election details is Already present for this consistency...")
   
    except NameError:
        print("Error During Inserting Data")


def insert_tbl2(cn,voter_name,const,birthdate,age,pswd,chance):
    try:
        cons_name=const[0][0]
        cn.execute(f"INSERT INTO voter (voter_name,voter_consistency,voter_dob,voter_age,voter_paswd,chance_vote) VALUES ('{voter_name}','{cons_name}','{birthdate}',{age},'{pswd}',{chance})")
        cn.commit()
        print("Data Stored --^_^--")
    except NameError:
        print("Error During Entering name...!!")

def insert_tbl4(cn,candidate_name,dob,pname,constitution_name,count):
    try:
        cons=constitution_name[0][0]
        cn.execute(f"INSERT INTO candidates (candidate_name,can_dob,party_name,can_constitution,count) VALUES ('{candidate_name}','{dob}','{pname}','{cons}',{count})")
        cn.commit()
    except NameError:
        print("Error Occured -_-!!")
        
def update_voter(cn,vid,vname):
    cn.execute(f"UPDATE voter set voter_name='{vname}' WHERE vid={vid}")
    cn.commit()
    
def update_dob(cn,vid,dob):
    cn.execute(f"UPDATE voter set voter_dob='{dob}' WHERE vid={vid}")
    cn.commit()
    
def update_constitution(cn,vid,cname):
    const=cname[0][0]
    cn.execute(f"UPDATE voter set voter_consistency='{const}' WHERE vid={vid}")
    cn.commit()
    
def get_consist(cn):
    tbl1=f"SELECT cid,constitution_name FROM constitution"
    cursor=cn.execute(tbl1)
    return [f'{row[0]}. {row[1]}' for row in cursor]

def get_candidate(cn):
    tbl4=f"SELECT can_id,candidate_name,party_name FROM candidates"
    cursor=cn.execute(tbl4)
    return [f'{row[0]}. Candidate Name:- {row[1]}  Party:- {row[2]}' for row in cursor]

def chance_vote(cn,vid):
    tbl2=f"SELECT chance_vote FROM voter WHERE vid={vid}"
    cursor=cn.execute(tbl2)
    return [f'{row[0]}'for row in cursor]
    
def get_candidate_count(cn,choice):
    tbl4=f"SELECT count FROM candidates WHERE can_id={choice}"
    cursor=cn.execute(tbl4)
    return [f'{row[0]}' for row in cursor]

def get_result(cn):
    tbl4=f"SELECT candidate_name,party_name,count FROM candidates"
    cursor=cn.execute(tbl4)
    return [f'Candidate:- {row[0]}  Party:- {row[1]}  Total Votes:- {row[2]}'for row in cursor]