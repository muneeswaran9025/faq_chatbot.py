while True:
    question = input("Ask a question: ")

    if question.lower() == "hello":
        print("Hi! How can I help you?")
    elif question.lower() == "what is python":
        print("Python is a programming language.")
    elif question.lower() == "bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't know the answer.")
        
