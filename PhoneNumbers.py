# Benjamin Readman
# Phone_Numbers

phone_book = {"Will Smith":"(555)-555-5555", "Billy Bob":"1-(800)-ALABAMA", "Chicken Little":"(123)-123-1234", "Lucas Sadoulet":"(215-FRIENDS)", "Police":"911"}
cont = 'y'
while cont == 'y':
    look_up = input("Enter the person who's phone number you would like to find: ")
    if phone_book[look_up] == look_up:
        print(look_up,"'s number is ", )