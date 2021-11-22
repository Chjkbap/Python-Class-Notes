from guizero import App, Text, PushButton
def greet():
    print("Greetings")

app = App("First GUI", bg="red")

label = Text(app, "GUI")
btnGreet = PushButton(app,text="Greet", command=greet)

btnGoodbye = PushButton(app,text="Bye", command=app.destroy )
app.display()