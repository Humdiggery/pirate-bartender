#Pirate Bartending Project 

#Use version control on github. Push final project to github and share with mentor

#Setup
#neccessary parameters

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#questions to determine customer taste
#identify ingredients that match that taste

def customer_pref():
    preference={}
    for key in questions:
        answer=input(questions[key])
        if answer.lower() == 'y' or answer.lower() == 'yes':
            preference[key]=True
        else:
            preference[key]=False
    #answers can be boolean values
    return preference

output=customer_pref()
print(output)
    
#write a function that requests what style the customer wants
#function should ask all questions in the question dictionary
#utilize input(). Error exceptions for things that don't exist. 

#def create_drink():
#write a function to construct a drink
#create an empty list to represent the drink
#append corresponding ingredients from the dictionary for each ingredients
    #the customer said they liked
#use random.choice() to select a random ingredient

#Provide a main function to call function 1 & 2 in order and passing
#the list of drink preferences to the drink creation function
#if __name__=='__main__':
    #customer_pref()
    #create_drink()





