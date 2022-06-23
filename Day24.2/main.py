#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get names from file
with open("Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.readlines()

# Open starting letter


for name in names:
    # Read starting letter
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter_file:
        starting_letter = starting_letter_file.read()

    # Write name
    new_letter_text = starting_letter.replace("[name]", f"{name.strip()}")

    # Save new letter
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="a") as new_letter:
        new_letter.write(new_letter_text)

starting_letter_file.close()



