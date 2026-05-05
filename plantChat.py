import pandas as pd

df = pd.read_csv('plant_whispers.csv')

print("Plantwhisperer: Hello 🌱 I am your plant assistant. Type 'quit' to exit.")

while True:
    user_text = input("\nYou: ").lower()

    if user_text == "quit":
        print("Plantwhisperer: Goodbye! 🌿")
        break

    if not user_text.strip():
        print("Plantwhisperer: Please type something 🌱")
        continue

    found_answer = False

    for index, row in df.iterrows():
        keywords_list = str(row['Keywords']).split(',')

        for word in keywords_list:
            clean_word = word.strip().lower()

            if clean_word in user_text.split():
                print("Plantwhisperer:", row['Response'])
                found_answer = True
                break

        if found_answer:
            break

    if not found_answer:
        print("Plantwhisperer: Sorry, I don't understand. Try asking something else 🌱")