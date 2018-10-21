import random

from tkinter import *
from tkinter import ttk

from questions import questions

root = Tk()
root.title("Викторина")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


def get_question():
    unanswered_questions = [q for q in questions if 'answered' not in q]
    if len(unanswered_questions) == 0:
        return None
    question = random.choice(unanswered_questions)
    return question


def play():
    for widget in mainframe.winfo_children():
        widget.destroy()

    question = get_question()
    if question is None:
        ttk.Label(mainframe, text='Край!').grid(column=1, columnspan=2, sticky=(W, E))
        return

    choosed_answer = StringVar()
    result = StringVar()

    def submit_answer():
        if choosed_answer.get() == question['answer']:
            result.set('Вярно!')
        else:
            result.set('Грешно!')
        question['answered'] = True
        button_next.configure(state=NORMAL)

    ttk.Label(mainframe, text=question['question']).grid(column=1, columnspan=2, sticky=(W, E))

    for answer in question['answers']:
        ttk.Radiobutton(mainframe, text=answer, variable=choosed_answer , value=answer)\
            .grid(column=1, sticky=W)

    ttk.Button(mainframe, text="Отговори", command=submit_answer)\
        .grid(column=2, sticky=W)

    ttk.Label(mainframe, textvariable=result).grid(column=1, sticky=(W, E))
    button_next = ttk.Button(mainframe, text="Следващ", command=play, state=DISABLED)
    button_next.grid(column=2, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

play()
root.mainloop()