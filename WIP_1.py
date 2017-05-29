game = input("Would you like to play a game? (Y/N) ").upper()

if game == "Y":
    print("Awesome. Let's get started.")
    print("STORYSTORYSTORY")

else:
    sure = input("Are you sure? (Y/N) ").upper()
    if sure == "Y":
        print("Okay. Have a nice day! :)")
    else:
        print("Great! Let's get started!")        
        print("STORYSTORYSTORY")
        
path_1 = "STORY PATH 1"
path_2 = "STORY PATH 2"
path_3 = "STORY PATH 3"

# I think some of the mess below could be replaced with better code, but I haven't learned enough to do that yet.

first_path = int(input("Which path do you choose? 1, 2, or 3? "))
if first_path == 1:
    print(path_1)
        continue_1 = input("Would you like to go right or left?").upper()
            if continue_1 == "LEFT":
                print("MORE STORY")
                    direction_1 = input("Now where do you want to go? Home or forward?").upper()
                    if direction_1 = "FORWARD":
                        input("Back home!")
                    else:
                        print("")
elif first_path == 2:
    print(path_2)
else:
    print(path_3)
    
