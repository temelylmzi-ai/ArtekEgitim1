class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    
    def checkAnswer(self,answer):
       return self.answer==answer
    
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):

        question=self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for choice in question.choices:
            print(f"- {choice}")

        answer = input("cevap: ")
        self.guess(answer)

    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        print(f"Puaniniz {self.score * 20}")

q1 = Question("Turkiyenin baskenti neresidir?",["Bursa","Istanbul","Ankara","Izmir","Nevsehir"],"Ankara")
q2 = Question("Turkiyede kac tane bolge vardir?",[1,9,5,3,7],7)
q3 = Question("Turkiyenin en kalabalik sehri hangisidir?",["Bursa","Istanbul","Ankara","Izmir","Nevsehir"],"Istanbul")
questions = [q1,q2,q3]         

quiz = Quiz(questions)
quiz.displayQuestion()

