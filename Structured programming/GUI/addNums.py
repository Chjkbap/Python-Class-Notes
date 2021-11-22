from guizero import App, Text, TextBox, PushButton
app = App(title="Add two numbers", bg="yellow")

instruction1 = Text(app, text="Enter  first number")
enterNum1 = TextBox(app)

instruction2 = Text(app, text="Enter second number")
enterNum2 = TextBox(app)

displayAnswer = Text(app,text="Answer will be displaye here")

def addNums():
    num1 = enterNum1.value
    num2 = enterNum2.value
    answer = int(num1) + int(num2)
    displayAnswer.value = answer

displayAddedNums = PushButton(app, command=addNums, text="Add")

app.display()