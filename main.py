#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
form = open("Input/Letters/starting_letter.txt")
names = open("Input/Names/invited_names.txt")
letter = form.read()


for n in names:
    name = n.strip()
    new_text = letter.replace("[name]", name)
    print(new_text)
    
    with open(f"Output/ReadyToSend/{name}.txt", 'w') as n:
        n.write(new_text)


form.close()
names.close()
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp