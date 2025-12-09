print("    __A Simple Quiz Application (Using Zip Class)")
number_of_students = int(input("How many students will take this quiz: "))
score = 0
student_answers = []
students = []
pass_mark = 50

Questions = ["    1. What is the common name for the condition where the eye's natural lens becomes cloudy, causing blurry vision, a major cause of blindness in Nigeria? \n    (A) Glaucoma \n    (B) Cataract \n    (C) Conjunctivitis", "    2. In Nigeria, 'Apollo' is a popular local name for a highly contagious eye infection causing redness and discharge. What is its medical term? \n    (A) Blepharitis \n    (B) Trachoma \n    (C) Viral Conjunctivitis", "    3. Which of these is a common symptom of Computer Vision Syndrome, often experienced by young Nigerians who spend long hours on digital devices? \n    (A) Eye Twitching \n    (B) Eye Strain and Dryness \n    (C) Sudden Floaters", "    4. What is the primary function of the Optometrist in the Nigerian healthcare system? \n    (A) To perform eye surgery \n    (B) To prescribe glasses and contact lenses and diagnose eye  \n    (C) To dispense and sell medications for all body ailments", "    5. Which eye condition is often called the 'silent thief of sight' because it can cause permanent vision loss without early symptoms and is a major concern in Nigeria? \n    (A) Diabetic Retinopathy \n    (B) Glaucoma  \n    (C) Macular Degeneration", "    6. What is the Nigerian term often used for the refractive error where one can see nearby objects clearly but distant objects appear blurry? \n    (A) Long-sight \n    (B) Short-sight  \n    (C) Astigmatism", "    7. Which of these is a recommended practice to protect your eyes from the intense ultraviolet (UV) rays of the Nigerian sun? \n    (A) Wearing a face cap \n    (B) Wearing sunglasses with UV protection  \n    (C) Washing your eyes with clean water", "    8. What is the name of the transparent front part of the eye that covers the iris and pupil? \n    (A) Retina \n    (B) Sclera  \n    (C) Cornea", "    .9. For a child in Nigeria struggling to see the blackboard in school, which eye care professional should they see first for a comprehensive eye examination? \n    (A) An Ophthalmologist \n    (B) An Optician  \n    (C) An Optometrist", "    10. Which vitamin deficiency is a leading cause of childhood blindness in developing countries like Nigeria and is linked to poor nutrition? \n    (A) Vitamin A Deficiency \n    (B) Vitamin C Deficiency  \n    (C) Vitamin D Deficiency"]

Answers = ["B", "C", "B", "B", "B", "B", "B", "C", "C", "A"]

for number in range(number_of_students):
    print(f"You are student no: {number + 1}")
    surname = input("    What is your surname: ").strip()
    mat_num = input("    What is your matric number: ").strip()
for Question, Answer in zip(Questions, Answers):
    print(Question)
    ans = input("    Your answer (A/B/C): ").strip().upper()
    if len(ans) == 1 and ans == Answer:
        score += 1
        student_answers.append(ans)

percent = (score/len(Questions)) * 100
passed = percent >= pass_mark
students.append({
    "surname": surname,
    "matric": mat_num,
    "score": score,
    "percent": percent,
    "passed": passed
})

print("    ==Your Result==")
for s in students:
    print(f"    Thank you for taking this simple quiz {s['surname']}-{s['matric']}. You scored: {s['score']} out of {len(Questions)} ({s['percent']}%). This mens that you {'Passed the quiz' if s['passed'] else 'You failed the quiz'}")


min_score = min(s['score'] for s in students)
max_score = max(s['score'] for s in students)

avg_score = sum(s['score'] for s in students) / len(students)
avg_percent = (avg_score / len(Questions)) * 100

print(f"The average score: {avg_score}/{len(Questions)} ({avg_percent}%)")

