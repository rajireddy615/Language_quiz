import random
words = [
    {"Telugu": "ఎం చేస్తున్నావ్", "english": "What are you doing"},
    {"Telugu": "ఎక్కడున్నావ్", "english": "Where are you"},
    {"Telugu": "మీరు ఎలా ఉన్నారు", "english": "How are you"},
    {"Telugu": "నువ్వు ఎక్కడ నుంచి వచ్చావు", "english": "Where are you from"},
    {"Telugu": "నీ పేరు ఏమిటి", "english": "What is your name"},
    {"Telugu": "మీరు ఇక్కడ ఉంటున్నారా", "english": "Do you live here"},
    {"Telugu": "ధన్యవాదాలు", "english": "Thank you"},
    {"Telugu": "శుభోదయం", "english": "Good morning"},
    {"Telugu": "మీ వృత్తి ఏమిటి", "english": "What is your occupation"},
    {"Telugu": "మీ వయస్సు ఎంత", "english": "How old are you"},
    {"Telugu": "తర్వాత కలుద్దాం", "english": "See you later"},
    {"Telugu": "ఇది ఎంత", "english": "How much is this"},
    {"Telugu": "మీరు ఇంగ్లీష్ మాట్లాడతారా", "english": "Do you speak English"},
    {"Telugu": "క్షమించండి", "english": "Sorry"},

]

def quiz_user(words):
    random.shuffle(words)
    score = 0
    for word in words:
        print(f"What is the English translation of '{word['Telugu']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
