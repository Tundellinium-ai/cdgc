class Questions:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Student:
    def __init__(self, name, matric):
        self.name = name
        self.matric = matric

class CBTApp():
    def __init__(self):
        self.questions = [
            Questions("    What is the common name for the condition where the eye's natural lens becomes cloudy, causing blurry vision, a major cause of blindness in Nigeria? \n", ["Glaucoma \n",    "Cataract \n", "Conjunctivitis \n"], 1), Questions("    In Nigeria, 'Apollo' is a popular local name for a highly contagious eye infection causing redness and discharge. What is its medical term? \n", ["Blepharitis \n", "Trachoma \n", "Viral Conjunctivitis\n"], 2)
        ]
        self.student = None

    def home(self):
        while True:
            print('''
            1. Enter Student Info
            2. Start Test
            3. Exit
            ''')
            choice = int(input("    Enter your choice: "))
            if choice == 1:
                self.student_info()
            elif choice == 2:
                self.start_test()
            elif choice == 3:
                print("\n Thank you!")
                break
            else:
                print("    Invalid choice number. Try again.\n")
    
    def student_info(self):
        print("\n    Fill in your student details below:")
        name = str(input("\n    Enter your full name: "))
        matric = input("\n    Enter your matric number: ")
        self.student = Student(name, matric)
        print("\n    Your student information has been captured. You can now proceed to take the test. \n")
    
    def start_test(self):
        if not self.student:
            print("\n    Please enter your student info first before taking the test.")
            return
        
        print("\n   Welcome Start the Test\n")
        score = 0
        for index, q in enumerate(self.questions, 1):
            print(f"    {index}. {q.prompt}")
            for i, opt in enumerate(q.options, 1):
                print(f"    {i}. {opt}")
            try: 
                ans = int(input("    Your answer: ")) - 1
            except:
                print("    Invalid option.\n")
                continue
            if ans == q.answer:
                print("\n    Correct answer") 
                score += 1
            else:
                print(f"    Wrong answer\n")
        print(f"\n    Thank you {self.student.name}! You have completed the test\n")
        self.show_score(score)
    
    def show_score(self, score):
        total = len(self.questions)
        percent = (score/total) * 100
        if percent >= 70:
            grade = "A"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C"
        elif percent >= 45:
            grade = "D"
        else:
            grade = "F"

        print(f"     Student: {self.student.name}\n")
        print(f"    Matric Number: {self.student.matric}\n")
        print(f"    Score: {score} / {total}\n")
        print(f"    Percentage: {percent:.2f}%\n")
        print(f"    Grade: {grade}\n")


app = CBTApp()
app.home()