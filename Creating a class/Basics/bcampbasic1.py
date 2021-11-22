class Bcamp: #class
    def __init__(self, name, course,ratings):
        self.name = name 
        self.course = course
        self.ratings = ratings
    
    def calAverage(self):
        numofR = len(self.ratings) #  accessing instance member using self dot
        averageR = sum(self.ratings)/numofR
        print(f"The average raing for {self.course} is {averageR} ")
  
learner1 = Bcamp(
name= input("Enter your name: "),
course=input("Enter your course: "),
ratings = [1,2,3,4,5] #int(input("Enter a rating")) # [1,2,3,4,5]
)
# learner1.course ="DB"
print(f"My name is {learner1.name} and I am enrolled on {learner1.course} and my rating is {learner1.ratings}")

# learner2 = Bcamp("John", "Python")
# print(f"My name is {learner2.name} and I am enrolled on {learner2.course}  {learner1.course} ")


# learner3 = Bcamp("Anna", "CSS")
# print(f"My name is {learner3.name} and I am enrolled on {learner3.course} {learner1.course} ")
        
        
