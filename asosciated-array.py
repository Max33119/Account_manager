#creation of accounts list
accounts = []

#password creation, and login
password = input("please create a password: ")
guess = ""
attempt_number = 0
attempt_limit = 3
out_of_attempts = False

while guess != password and not(out_of_attempts):
  if attempt_number < attempt_limit:
    guess = input("\nInput a password for the account: ")
    attempt_number += 1
  else:
    out_of_attempts = True

if out_of_attempts:
    print("\nFraud detected.")
    exit()
else:
    print("\nWelcome to your password manager")



def main():
  # Main Program Loop
  loop = True
  while loop:
    selection = getMenuSelection()

    if selection == "1":
      option1()
    elif selection == "2":
      print("1: add a program")
      print("2: remove a program")
      second_menu = input("please make a menu selection: ")
      if second_menu == "1":
        add_item()
      elif second_menu == "2":
        remove_item()
    elif selection == "3":
      option3()
    elif selection == "4":
      option4()
    elif selection == "5":
      option5()
    elif selection == "6":
      print("Exit")
      loop = False

# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: View accounts in account manager")
  print("2: Add or remove an account")
  print("3: Search for date")
  print("4: Search for service")
  print("5: Random account")
  print("6: Exit")
  return input("Enter menu selection:")

# option 1
def option1():
  if input("Please enter your password to view accounts: ") == password:
    for items in accounts:
      print(items)
  else:
    ("wrong password")

#add
def add_item():
  user = input("please enter a username: ")
  code = input("please enter a password: ")
  service = input("please enter the name of the service: ")
  date = int(input("please enter year(number) of account creation: "))
  
  add(user, code, service, date)

#remove
def remove_item():
  user = input("please enter the username: ")
  code = input("please enter the password: ")
  service = input("please enter the name of the service: ")
  date = int(input("please enter the year(number) of account creation: "))
  
  remove(user, code, service, date)

#option 3(by date)
def option3():
  search = int(input("please enter the date you wish to search by: "))
  date_lookup(search)

#option 4(Search by service)
def option4():

  search = input("please enter the service you wish to look for: ")
  
  lookup(search)

#option 5(random)
def option5():
  import random
  length = 0
  length += int(len(accounts))
  print(length)
  length -= 1
  if length < 0:
    print("nothing is in the account list")
  else:
    print(accounts[random.randint(0, length)])


  

#global functions
def add(name, code, service, date):
  for items in accounts:
    if items["username"] == name and items["service"] == service:
      items["password"] = code
      items["date"] = date
      print("\naccount already exists with this name for this service, but date and password have been updated")
      print("\nnew password is: " + code)
      print("\nnew date is: " + date)
      return

  accounts.append({"username": name, "password": code, "service": service, "date": int(date)})

def remove(name, code, service, date):
  for items in accounts:
    if items["username"] == name and items["service"] == service and items["password"] == code and items["date"] == date:
      print("\naccount with these details removed")
      accounts.remove(items)
      return
    

  print("\naccount with these credentials does not exist")

def lookup(service):
  for items in accounts:
    if items["service"] == service:
      print(items)

def date_lookup(date):
  for items in accounts:
    if items["date"] == date:
      print(items)




main()