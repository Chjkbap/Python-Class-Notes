class Bcamp: #class
    def __init__(self, name, course,ratings):
        self.name = name 
        self.course = course
        self.ratings = ratings
    
    def calAverage(self):
        numofR = len(self.ratings) #  accessing instance member using self dot
        averageR = sum(self.ratings)/numofR
        print(f"The average raing for {self.course} is {averageR} ")
        # print( averageR)
        
    def welcome(self):
        print("Welcome")

learner1 = Bcamp("Paul","HTML",[1,9,3,4,5])

# learner1 = Bcamp(
# name= input("Enter your name: "),
# course=input("Enter your course: "),
# ratings = [1,2,3,4,5]
# )

# print()
learner1.welcome()
print(f"My name is {learner1.name} and I am enrolled on {learner1.course} and my rating is {learner1.ratings}")
learner1.calAverage()
 