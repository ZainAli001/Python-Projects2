import pyttsx3
data = input("Enter Your Data : ")
with open("Mydata.txt", "w") as f:
    f.write(data)

with open("Mydata.txt", "r") as f:
    book_text = f.readlines()

engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
