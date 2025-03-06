""" Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"""



#solution:
JOKE=" Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"


Sorry="Sorry, I can only tell jokes"
def bot():
    user_input = input("what do u want? ")
   
    if "joke" in user_input:
        print(JOKE)
    else:
        print(f"{Sorry} ")   

bot()