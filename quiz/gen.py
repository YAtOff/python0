data = '''>>> a = 3 >>> a + 2.0
float
5.0
>>> a = a + 1.0 >>> a
float
4.0
>>> a = 3 >>> b
NoneType
None
>>> a == 5.0 >>> a
int
3
>>> b = 10 >>> c = b > 9 >>> c
bool
True
'''
template = '''
.. fillintheblank:: fill{major}_{minor}
    .. blank:: blank{major}_{minor}
        :correct: {answer}
        `{question}`'''
choices_templats = {
    'int': '''
.. mchoice:: question{major}_{minor}
    :correct: a
    :answer_a: int
    :answer_b: float
    :answer_c: str
    :answer_d: NoneType
    :answer_e: bool
    :feedback_a: Правилно!
    :feedback_b: Грешно!
    :feedback_c: Грешно!
    :feedback_d: Грешно!
    :feedback_e: Грешно!
    `{question}`''',
    'float': '''
.. mchoice:: question{major}_{minor}
    :correct: b
    :answer_a: int
    :answer_b: float
    :answer_c: str
    :answer_d: NoneType
    :answer_e: bool
    :feedback_a: Грешно!
    :feedback_b: Правилно!
    :feedback_c: Грешно!
    :feedback_d: Грешно!
    :feedback_e: Грешно!
    `{question}`''',
    'str': '''
.. mchoice:: question{major}_{minor}
    :correct: c
    :answer_a: int
    :answer_b: float
    :answer_c: str
    :answer_d: NoneType
    :answer_e: bool
    :feedback_a: Грешно!
    :feedback_b: Грешно!
    :feedback_c: Правилно!
    :feedback_d: Грешно!
    :feedback_e: Грешно!
    `{question}`''',
    'NoneType': '''
.. mchoice:: question{major}_{minor}
    :correct: d
    :answer_a: int
    :answer_b: float
    :answer_c: str
    :answer_d: NoneType
    :answer_e: bool
    :feedback_a: Грешно!
    :feedback_b: Грешно!
    :feedback_c: Грешно!
    :feedback_d: Правилно!
    :feedback_e: Грешно!
    `{question}`''',
    'bool': '''
.. mchoice:: question{major}_{minor}
    :correct: e
    :answer_a: int
    :answer_b: float
    :answer_c: str
    :answer_d: NoneType
    :answer_e: bool
    :feedback_a: Грешно!
    :feedback_b: Грешно!
    :feedback_c: Грешно!
    :feedback_d: Грешно!
    :feedback_e: Правилно!
    `{question}`'''
}
lines = data.splitlines()
questions = lines[::3]
type_answers = lines[1::3]
value_answers = lines[2::3]
major = 3
for i, (q, ta, va) in enumerate(zip(questions, type_answers, value_answers)):
    print(choices_templats[ta].format(major=major, minor=i + 1, question=q))
    print(template.format(major=major, minor=i + 1, question=q, answer=va))
