from secrets import choice
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pip import main

# Use a service account
cred = credentials.Certificate('firestore.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})
def print_team():
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

def new_entry():
    print("Type your first initial and last name. For example, Matt Smith becomes msmith'.")
    user = input()
    print("Type your first name")
    first = input()
    print("Type your middle name")
    middle = input()
    print("Type your last name")
    last = input()
    print("when when you born?")
    born = input()
    doc_ref = db.collection(u'users').document(user)
    doc_ref.set({
        u'first': first,
        u'middle': middle,
        u'last': last,
        u'born': born})

def delete_entry():
    print("Delete which entry?")
    print_team()
    choice = input()
    db.collection(u'users').document(choice).delete()

def update_entry():
    # select teammate to be changed
    print("which teammate do you want to update? (type the document id that is to the far left.)")
    print_team()
    teammate = input()
    doc_ref = db.collection(u'users').document(teammate)
    # select what needs to be changed
    print("What needs to be changed?")
    print("A: first name")
    print("B: middle name")
    print("C: last name")
    print("D: when you were born")
    letter = input()
    # change the first name
    if letter == 'a':
        print("what is your new first name?")
        first = input()
        doc_ref.update({
            u'first': first
        })
    # change the middle name
    elif letter =='b':
        print("what is your new middle name?")
        middle = input()
        doc_ref.update({
            u'middle': middle
        })
    # change the last name
    elif letter == 'c':
        print("what is your new last name?")
        last = input()
        doc_ref.update({
            u'last': last
        })
    # change the date of birth
    elif letter == 'd':
        print("what is your date of birth?")
        birth_date = input()
        doc_ref.update({
            u'born': birth_date
        })


def main():
    run = True
    while run == True:
        print("Hello, Welcome to your team database!")
        print("What would you like to do?")
        print("A: add a teammate")
        print("B: delete a teammate")
        print("C: print teammates")
        print("D: upate entry")
        print("E: quit")
        letter = input()
        if letter == 'a':
            new_entry()
        elif letter =='b':
            delete_entry()
        elif letter == 'c':
            print_team()  
        elif letter == 'd':
            update_entry()
        elif letter == 'e':
            run = False

main()
    


