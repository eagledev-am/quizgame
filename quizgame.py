# quiz game using trivia api 
# fetch one question from api
import requests as req
import json
import pprint
import random
import html
url = "https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"
check_end_game = ""
score = 0
number_correct_answers = 0
print("Correct answer = 2 points")
print("Wrong answer = -1 point")
print("********** quiz game **********")
print("_______________________________________")
while(check_end_game != "yes"):
    print()
    getApi = req.get(url)
    if getApi.status_code != 200:
        check_end_game = input("Sorry ,there is a problem if you want to continue press yes!")
        print("_______________________________________")
    else:
        api = json.loads(getApi.text)
        question = api['results'][0]['question']
        answers = api['results'][0]['incorrect_answers']
        correct_answer = api['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print(html.unescape(question))
        answer_number = 1
        for answer in answers:
            print(str(answer_number) + "- " + html.unescape(answer))
            answer_number += 1
        choice_answer = int(input("Enter the number of correct answer : "))
        if(correct_answer == answers[choice_answer-1]):
            print("Good Work")
            score += 2
            number_correct_answers += 1
        else:
            print("Sorry The correct answer is " + correct_answer)
            if(score != 0):
                score -= 1
        check_end_game = input("Do you want to end game yes/no? ").lower()
        print("_______________________________________\n")
print("You have answer " + str(number_correct_answers) + " questions")
print("Your score = "  + str(score))
print("\n********** quiz game **********")