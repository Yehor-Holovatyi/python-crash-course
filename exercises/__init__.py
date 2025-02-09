print ("Hi world")

print ("Hi man! How are you ?")

while True:
    user_input = input()

    if user_input.lower() == "good": 
        print ("Great!!!")
        print ("this is the end of my dialogue")
        break
    
    elif user_input.lower() == "bad":
       print ("it's horrible") 
       print ("this is the end of my dialogue")
    break