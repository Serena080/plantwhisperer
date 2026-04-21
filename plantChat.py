import pandas as pd

# load your data into a dataframe
df = pd.read_csv('plant_whispers.csv')

# print(df)

print("Plantwhisperer:Hello I am your plant assistant.How can I help you today?")

while True:
    
    # 1.    Get the user input and store the same into a variable
    user_text = input(" \n You: ").lower()

    #2.    Check if the user whats to exit the chat
    if user_text == "quit":
        print("Plantwhisperer: Goodbye! Nice to have been of service to you and your plant.")
        break

    # Create a variable which will store the details structured in the csv file
    found_answer = False

    # Come up with a loop that loops through the entire dataframe created before
    for index,row in df.iterrows():
        # Clean up the keywords from the csv row
        keywords_list = str(row['Keywords']).split(',')

        # print("The words inside the variable list:",keywords_list)

        # Below we check ever keyword in that given row (keywords)
        for word in keywords_list:
            clean_word = word.strip().lower()
            
            # If the keyword is of the user sentence
            if clean_word in user_text:
                print("Plantwhisperer:",row['Response'])
                found_answer = True
                break #Stop looking at other keywords

            if found_answer:
                break #Stop looking at other anwers since we already found a match

        # 4. If we went through the entire csv file and we dont find a match for the keyword, we will display a message to the user
        if not found_answer:
            print("Plantwhisperer: Sorry I don't understand. Try asking something else.")