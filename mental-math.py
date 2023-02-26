# Mia Scarpati
# Mental Math Game

# Levels:
# 1. Easy - clean whole numbers addition/subtraction/multiplication/division only, more addition/subtraction
# 2. Medium - less clean whole numbers addition/subtraction/multiplication/division with square roots
# 3. Hard - simple fractions/decimals addition/subtraction/multiplication/division, some square roots
# 4. Expert - tougher fractions/decimals addition/subtraction/multiplication/division, some square roots

import random
import time
import sys
import datetime as dt

class MentalMath():
    def __init__(self):
        """
        Constructor, reset score
        """
        self.score = 0
    
    def StartGame(self):
        level = self.PromptUser()
        print("How many questions? 10, 20, 30, or 50")
        while True:
            try:
                numQ = input()
                if numQ == '10' or numQ == '20' or numQ == '30' or numQ == '50': 
                    numQ = int(numQ)
                    break
                if numQ == '$': sys.exit()
            except ValueError:
                print("Please enter valid input.")
        tempQ = numQ
        if level == '1':
            start = time.time()
            while numQ > 0:
                self.Easy()
                numQ-=1
            end = time.time()
        elif level == '2':
            start = time.time()
            while numQ > 0:
                self.Medium()
                numQ-=1
            end = time.time()
    
        scores = self.GetWeightedScore(self.score, tempQ, round(end-start), int(level))
        print("Time:", round(end-start, 2), "seconds")
        print("Score:", self.score, "/", tempQ)
        print("Weighted score:", scores[0], "%")
        print("Ideal time:", scores[1], "seconds")

    def GetWeightedScore(self, numCorrect, numQ, time, level):
        if level == 1:
            stdTime = numQ * 2.4
            stdScore = numQ * stdTime
            #weightedScore = round((1-(((numCorrect*time)-stdScore)/stdScore))*100, 2)
            weightedScore2 = round(numCorrect/numQ*100 - (time-stdTime)/stdTime*100, 2)
        elif level == 2:
            stdTime = numQ * 3.6
            weightedScore2 = round(numCorrect/numQ*100 - (time-stdTime)/stdTime*100, 2)
        
        return [weightedScore2, stdTime]
    
    def PromptUser(self):
        print("What level? 1-4")
        try:
            level = input()
            if level == '1' or level == '2' or level == '3' or level == '4': return level
        except ValueError:
            print("Please enter valid input.")
            self.PromptUser()
    
    def GetAns(self):
        answer = input()
        try:
            if answer == '$':
                sys.exit()
            else:
                answer = float(answer)
        except ValueError:
            print("Please enter a valid input.")
            self.GetAns()
        return answer

    def Addition(self, upperBound):
        num1 = random.randint(2, upperBound)
        num2 = random.randint(2, upperBound)
        print(num1, "+", num2)
        return num1+num2

    def Subtraction(self, upperBound):
        num1 = random.randint(2, upperBound)
        num2 = random.randint(num1, upperBound)
        print(num2, "-", num1)
        return num2-num1
    
    def Multiplication(self, upperBound):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, upperBound)
        print(num1, "*", num2)
        return num1*num2
    
    def Division(self, upperBound):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, upperBound)
        num3 = num1*num2
        
        whichAns = random.randint(0, 1)
        if whichAns == 0:
            print(num3, "/", num1)
            return num3/num1
        else:
            print(num3, "/", num2)
            return num3/num2
   
    def Power(self, upperBound, expBound):
        num1 = random.randint(2, upperBound)
        num2 = random.randint(2, expBound)
        print(num1, "^", num2)
        return num1**num2
    
    def Easy(self):
        operator = random.randint(0, 5)

        if operator == 0 or operator == 4:
            trueAns = self.Addition(99)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
            
        elif operator == 1 or operator == 5:
            trueAns = self.Subtraction(99)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1

        elif operator == 2:
            trueAns = self.Multiplication(99)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1

        elif operator == 3:
            trueAns = self.Division(99)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1

    
    def Medium(self):
        operator = random.randint(0,4)
        if operator == 0:
            trueAns = self.Addition(499)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
        elif operator == 1:
            trueAns = self.Subtraction(499)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
        elif operator == 2:
            trueAns = self.Multiplication(499)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
        elif operator == 3:
            trueAns = self.Division(199)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
        elif operator == 4:
            trueAns = self.Power(29, 4)
            ans = self.GetAns()
            if trueAns == ans: self.score+=1
    
    #def Hard(self):

    #def Expert(self):

MM = MentalMath()
MM.StartGame()   
