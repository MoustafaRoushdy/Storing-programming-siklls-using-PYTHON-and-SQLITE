#working with data base
import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

def commit_and_close():
    db.commit()
    db.close()
    print("connection to data base is closed")

#creating userid
uid = 1



input_message = """
what do you want to do?
"s" => show all skills
"a" => add new skill
"d" => delete a skill
"u" => update skill progress
"q" => quit the app
Choose Option:
"""
user_input =input(input_message).strip().lower()
commands_list = ['s','a','d','u','q']

def addskill():
    sk = input("Write skill name: ").strip().capitalize()
    
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")
    result = cr.fetchone()
    if result != None:
        print("Skill already exist! do you want to upate it (Y/N) ?")
        update_skill = input().strip().lower()
        if update_skill == 'y':
            prog = input("Write the new progress: ").strip()
            cr.execute(f"update skills set progress = '{prog}' where user_id = '{uid}' and name = '{sk}'")
            commit_and_close()
    else:
        prog = input("Write skill progress: ").strip()
        cr.execute(f"insert into skills(name,progress,user_id) values('{sk}','{prog}','{uid}')")
        commit_and_close()
    
def showskill():
    cr.execute("select * from skills")
    results = cr.fetchall()
    print(f"you have {len(results)} skill")
    for row in results:
        print(f"skill => {row[0]}, progress => {row[1]}%")
    commit_and_close()
    

def deleteskill():
    sk = input("Write skill name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_and_close()


def updateskill():
    sk = input("Write skill name: ").strip().capitalize()
    prog = input("Write the new progress: ").strip()
    cr.execute(f"update skills set progress = '{prog}' where user_id = '{uid}' and name = '{sk}'")
    commit_and_close()



if user_input not in commands_list:
    print("command is not found")

elif user_input == 's':
    showskill()

elif user_input == 'a':
    addskill()

elif user_input == 'd':
    deleteskill()

elif user_input == 'u':
    updateskill()

else:
    print("app is closed!")
    commit_and_close()


