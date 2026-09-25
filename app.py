# Study Chatbot - Made by Sonu Tagde from Nagpur
print("Hello! I am your Study Chatbot 🤖")

while True:
    question = input("\nAapka sawal puchho (exit likhne par band hoga): ")
    
    if question.lower() == "exit":
        print("Bye Bye! Padhte raho! 📚")
        break
    
    if "python" in question.lower():
        print("Python ek programming language hai, bahut easy hai!")
    elif "github" in question.lower():
        print("GitHub par hum apna code save karte hain!")
    else:
        print(f"Aapne pucha: {question} | Iska jawab mai jald sikhunga!")
