#создай приложение для запоминания информации
# ПОДСКАЗКА
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
# app = QApplication([])
# main_win = QWidget()
# main_win.show()
# main_win.setWindowTitle('Определитель победителя')
# app.exec_()
#подключение библиотек
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
main_win = QWidget() 
main_win.move(900, 70) # движение окна
main_win.resize(400,200) # размер окна
main_win.setWindowTitle('Memory Card') # название окна
 # надпись


RadioGroupBox = QGroupBox('Варанты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Тут ответ')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()




layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
itog = QLabel('Тут будет верный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)
BBquestion = QLabel('Какого времени года не существует')
line1 = QHBoxLayout()
line1.addWidget(BBquestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3 = QHBoxLayout()
button = QPushButton('Ответить')
line3.addWidget(button, alignment=(Qt.AlignHCenter | Qt.AlignVCenter), stretch = 2)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')



def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == button.text():
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    BBquestion.setText(q.question)
    itog.setText(q.right_answer)
    show_question()







def show_correct(res):
    result.setText(res)
    show_result()  


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
            show_correct('Неверно')


question_list = []
q5 = Question('Какого времени года существует?', 'Веснуль', 'Зима', 'Осень', 'Лето')
q = Question('Какая из следующих професией является самой низкооплачиваемой?', 'Дворник', 'Пилот', 'Инженер', 'Тренер')
q1 = Question('Какой из этих городов является столицей Франции?', 'Париж', 'Лион', 'Марсель', 'Ницца')
q2 = Question('Что из перечисленного не является единицей измерения времени?', 'Килограмм', 'Секунда', 'Час', 'День')
q3 = Question('Какой элемент не является металлом?', 'Углерод', 'Железо', 'Золото', 'Медь')
q4 = Question('Какое животное не относится к семейству кошачьих?', 'Медведь', 'Лев', 'Волк', 'Рысь')
q6 = Question('Кто из перечисленных писателей написал роман "Война и мир"?', 'Лев Толстой', 'Александр Пушкин', 'Фёдор Достоевский', 'Михаил Лермонтов')
q7 = Question('Какой вид спорта не входит в программу Олимпийских игр?', 'Шахматы', 'Плавание', 'Легкая Атлетика', 'Гимнастика')
q8 = Question('Какой фрукт не является цитрусовым?', 'Яблоко', 'Апельсин', 'Лимон', 'Грейпфрут')
q9 = Question('Какой город не находится в России?', 'Берлин', 'Москва', 'Тюмень', 'Сургут')
q10 = Question('Какой из этих элементов не является благородным газом?', 'Водород', 'Неон', 'Криптон', 'Аргон')
question_list.append(q5)
question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)




glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)
main_win.setLayout(glav)


box = QVBoxLayout()
box.addLayout(line1)
box.addLayout(line2)
box.addLayout(line3)
def next_question():
    main_win.cur_question +=1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
    window.total += 1

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()





main_win.cur_question = -1
show_result()
next_question()
button.clicked.connect(click_ok)
main_win.show() # сделает окно видимым
app.exec_()


