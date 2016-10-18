def start(choice):
    
    if choice == "No":
        print "Ok. Go home then."
        return "finished"
    elif choice == "Yes":
        return "opening"
    else:
        print "This is a Yes or No question."
        return "start"