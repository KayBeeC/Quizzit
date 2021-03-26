import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Quizzit.settings')

import django
django.setup()
from quizzit_app.models import Register_User, Category, Quiz, Question, Record

def populate():
    reg_user_list = [
        {'username': 'Alice',
         'email': 'alice@gmail.com',
         'password': 'alice1234',
         'admin': False},

        {'username': 'Bob',
         'email': 'bob@gmail.com',
         'password': 'bob1234',
         'admin': False},

        {'username': 'Charlie',
         'email': 'charlie@gmail.com',
         'password': 'charlie1234',
         'admin': False},
    ]

    for user in reg_user_list:
        u = add_reg_user(user['username'], user['email'], user['password'], user['admin'])

        print(f'- added User: {u}')



    cate_list = [
        {'name': 'History',},
        {'name': 'Geography',},
        {'name': 'Sport',},
        {'name': 'Mathematics',},
        {'name': 'Biology',},
        {'name': 'Business',},
        {'name': 'Physics',},
        {'name': 'Movies',},
        {'name': 'TV Shows',},
        {'name': 'Chemistry',},
    ]

    for cate in cate_list:
        c = add_cate(cate['name'])

        print(f'- added Cate: {c}')



    quiz_list = [
        {'name': 'Quiz 1',
         'difficulty': 'Easy',
         'category': 'History',
         'views': 20,
         'questions': [
             {'index': 1,
              'text': 'When',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 2,
              'text': 'Who',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 3,
              'text': 'Where',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
         ],},

        {'name': 'Quiz 2',
         'difficulty': 'Medium',
         'category': 'History',
         'views': 10,
         'questions': [
             {'index': 1,
              'text': 'When',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 2,
              'text': 'Who',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 3,
              'text': 'Where',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
         ],},

        {'name': 'Quiz 3',
         'difficulty': 'Hard',
         'category': 'Geography',
         'views': 20,
         'questions': [
             {'index': 1,
              'text': 'When',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 2,
              'text': 'Who',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
 
             {'index': 3,
              'text': 'Where',
              'choiceA': 'A: something',
              'choiceB': 'B: something',
              'choiceC': 'C: something',
              'choiceD': 'D: something',
              'answer': 'A',},
         ],},
    ]

    # this is the global question id
    question_id = 1
    for i,quiz in enumerate(quiz_list):
        cate_obj = Category.objects.get(name=quiz['category'])
        q = add_quiz(i+1, quiz['name'], quiz['difficulty'], cate_obj, quiz['views']) 

        print(f'- added Quiz: {q}')

        for question in quiz['questions']:
            que = add_question(question_id, question['index'], question['text'],
                               question['choiceA'], question['choiceB'], question['choiceC'], 
                               question['choiceD'], question['answer'], q)
            question_id += 1
            print(f'- added Question: {que} to {q}')

    
    # record_list = [
    #     {'user': 'Alice',
    #      'quiz': 1,
    #      'score': 10},
    #     {'user': 'Bob',
    #      'quiz': 2,
    #      'score': 20},
    #     {'user': 'Charlie',
    #      'quiz': 3,
    #      'score': 30},
    # ]

    # for record in record_list:
    #     reg_user_obj = Register_User.objects.get(username=record['username'])
    #     quiz_obj = Quiz.objects.get(quizID=record['quizID'])
    #     r = add_record(reg_user_obj, quiz_obj, record['score'])

    #     print(f'- added Record: {r}')



def add_reg_user(username, email, password, admin=False):
    reg_user = Register_User.objects.get_or_create(username=username)[0]
    reg_user.email = email
    reg_user.password = password
    reg_user.admin = admin

    reg_user.save()
    return reg_user



def add_cate(name):
    cate = Category.objects.get_or_create(name=name)[0]

    cate.save()
    return cate



def add_quiz(id, name, difficulty, category, views):
    quiz = Quiz.objects.get_or_create(id=id, difficulty = difficulty, category=category)[0]
    quiz.name = name
    quiz.views = views
    quiz.save()
    return quiz



def add_question(id, index, question_text, choiceA, choiceB, choiceC, choiceD, answer, quiz):
    question = Question.objects.get_or_create(id=id, quiz=quiz)[0]
    question.index = index
    question.question_text = question_text
    question.choiceA = choiceA
    question.choiceB = choiceB
    question.choiceC = choiceC
    question.choiceD = choiceD
    question.answer = answer

    question.save()
    return question



def add_record(user, quiz, score=0):
    record = Record.objects.get_or_create(user=user, quiz=quiz)[0]
    record.score = score

    record.save()
    return record



def test():
    quiz_obj = Quiz.objects.get(id=1)
    print('--', quiz_obj)

    # cate_obj = Category.objects.get(name='History').quiz_set.all()

    print('--', Category.objects.get(name='History').quiz_set.all())
    print('--', Quiz.objects.filter(category__name='History', difficulty='Easy'))

    print('--', Quiz.objects.get(id=1).question_set.all())
    print('--', Quiz.objects.get(id=2).question_set.all())



# Start execution here!
if __name__ == '__main__':
    print('Starting quizzit_app population script...')
    populate()
    # test()



    


