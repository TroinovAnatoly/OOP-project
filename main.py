import sys
from asyncio import create_task

import datetime as dt
from calendar import month
from traceback import print_tb
from webbrowser import Error

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QWidget, QPushButton, QDialog

from abc import ABC


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Календарь Эйзенхаэра")

        self.task_create_button = QPushButton("Создать задачу")
        self.task_create_button.setFixedSize(150, 70)
        self.task_create_button.setStyleSheet('QPushButton {background-color: black; '
                                              'color: white;'
                                              'border-radius: 10px;'
                                              'margin: 0px}')

        self.task_delete_button = QPushButton("Удалить задачу")
        self.task_delete_button.setFixedSize(150, 70)
        self.task_delete_button.setStyleSheet('QPushButton {background-color: black; '
                                              'color: red;'
                                              'border-radius: 10px;'
                                              'margin: 0px;}')

        self.window_menu = QLabel()
        self.window_menu.setFixedSize(200, 500)
        self.window_menu.setStyleSheet('QLabel {background-color: #111111; '
                                       'border-radius: 20px;}')

        self.window_tasks = QLabel()
        self.window_tasks.setFixedSize(880, 500)
        self.window_tasks.setStyleSheet('QLabel {background-color: #111111; '
                                        'border-radius: 20px;}')

        self.layout = QGridLayout()

        self.layout.addWidget(self.window_menu, 0, 0, 1, 1)
        self.layout.addWidget(self.window_tasks, 0, 1, 1, 1)
        self.layout.addWidget(self.task_create_button, 1, 0, 2, 2, Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.task_delete_button, 1, 2, 2, 2, Qt.AlignmentFlag.AlignRight)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        self.task_create_button.clicked.connect(self.go_to_task)

    def go_to_task(self, event):
        tm = TaskManager()
        tm.create_task()
        tm.exec()


class Priority(ABC):
    def __init__(self, name, level, date, complexity):
        self.priorities = {1: "Важно и Срочно",
                           2: "Важно, но не срочно",
                           3: "Не важно,но срочно",
                           4: "Не важно и Не срочно"}
        self.complexities = {1: "Невероятно сложно",
                             2: "Сложно",
                             3: "Средне",
                             4: "Легко",
                             5: "Элементарно"}
        self.name = name
        self.level = level
        self.date = date
        self.complexity = complexity

    def checking_the_logic(self):
        if self.level == 4:
            otvet = input("Возмжно ли делигировать задачу?")

    def configuration(self):
        pass

    def manual_of_priority(self):
        print("1 - Важно и Срочно | 4 ")


class TaskStandard:
    def __init__(self):
        pass

    def minimum_param_ret(self):
        level = "Важно и Срочно"
        date = dt.datetime.now() + dt.timedelta(days=1)
        complexity = "Сложно"
        return (f"Ошибка!!! Не переданы нужные параметры \n"
                f"Установлены параметры по умолчанию \n"
                f"Логика: {level} | Дедлайн: {date.strftime("%d.%m.%y / Время: %H:%M")} | Сложность: {complexity}")


class OutOfRangeList(Exception):
    pass


class Tasks:
    def __init__(self):
        self.tasks = []

    def append_element(self, task):
        self.tasks.append(task)

    def __getitem__(self, item):
        return self.tasks[item]

    def __setitem__(self, key, value):
        self.tasks[key] = value


class Task(Priority):

    def ret_params(self):
        self.checking_the_logic()
        if (self.level not in self.priorities) or (self.complexity not in self.complexities):
            raise OutOfRangeList("------------------------------------------ \n"
                                 "Кря!!! Переданы не верные параметры!!! \n"
                                 "------------------------------------------ \n"
                                 "Внимательно введите значение и соблюдайте условия \n"
                                 "------------------------------------------ \n")
        else:
            __level = self.priorities[self.level]
            __date = dt.datetime.now() + dt.timedelta(days=self.date)
            __complexity = self.complexities[self.complexity]
            return (f"Название задачи: {self.name} \n"
                    f"Дедлайн: {__date.strftime("%d.%m.%y / Время: %H:%M")} \n"
                    f"Логика: {__level} | Сложность: {__complexity}")

    def __str__(self):
        __level = self.priorities[self.level]
        __date = dt.datetime.now() + dt.timedelta(days=self.date)
        __complexity = self.complexities[self.complexity]
        return (f"Название задачи: {self.name} <-- То, что вы хотите сделать\n"
                f"Дедлайн: {__date.strftime("%d.%m.%y / Время: %H:%M")} <-- Для данной строки, нужно ввести количество дней на выполнение задачи(в примере дано 3 дня) \n"
                f"Логика: {__level} <-- Логика по матрице Эйзенхауэра, от 1 до 4 | Сложность: {__complexity} <-- Уровень сложности, от 1 до 5")

    def __repr__(self):
        __level = self.priorities[self.level]
        __date = dt.datetime.now() + dt.timedelta(days=self.date)
        __complexity = self.complexities[self.complexity]
        return (f"Название задачи: {self.name} \n"
                f"Дедлайн: {__date.strftime("%d.%m.%y / Время: %H:%M")} \n"
                f"Логика: {__level} | Сложность: {__complexity}")


class TaskManagerGUI(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.setFixedSize(500, 300)
        self.setStyleSheet('QDialog {background-color: #111111;}')


class TaskManager:
    def __init__(self):
        pass

    def create_task(self, name, level, date, complexity):
        task1 = Task(name, level, date, complexity)
        print(task1.ret_params())

    def delete_task(self):
        pass

    def change_task(self):
        pass


class ThemeChange:
    def __init__(self):
        pass


class StandInput:
    def __init__(self, question):
        print(f"Актуальное время: {dt.datetime.now().strftime("%d.%m.%y %H:%M")}")
        self.__shablon_flag = True
        self.check_the_answer(question)

    def check_the_answer(self, question):
        if question.lower() == "да":
            if self.__shablon_flag == True and input("Нужен шаблон? (Да/Нет) - ").lower() == "да":
                example_tasks = self.get_exapmle_tasks()
                for i in example_tasks:
                    print("---------------------")
                    print(i)
                    print("---------------------")

                self.__shablon_flag = False
                self.check_the_answer(input("Создать задачу?(Да/Нет) - "))
            else:
                try:
                    self.create_new_task()
                except ValueError as val:
                    print(self.get_value_error())
                    self.create_new_task()
                except OutOfRangeList as inv:
                    print(f"{inv}")
                finally:
                    self.check_the_answer(input("Создать еще одну задачу?(Да/Нет) - "))

        else:
            print("Пока пока!")
            exit()

    def get_exapmle_tasks(self):
        return [Task("Пример очень сложной, важной и срочной задачи задачи/Шаблон", 1, 3, 1),
         Task("Пример сложной и важной, но не срочной задачи задачи/Шаблон", 2, 3, 2),
         Task("Пример средней и срочной, но не важной задачи задачи/Шаблон", 3, 3, 3),
         Task("Пример легкой, не важной и  не срочной задачи задачи/Шаблон", 4, 3, 4),
         Task("Пример элементарной, не важной и не срочной задачи задачи/Шаблон", 4, 3, 5)]

    def get_value_error(self):
        return ("Значение приоритета может быть только числом \n"
                "Все строки должны быть заполнены \n"
                "Пожалуйста, попробуйте снова \n"
                "-----------------------------------------------")

    def create_new_task(self):
        tasks = TaskManager()
        tasks.create_task(input("Название задачи: "), int(input("Значение приоритета задачи, от 1 до 4: ")),
                          int(input("Количество дней, для выполнения задачи: ")),
                          int(input("Значение сложности задачи, от 1 до 5: ")))


first_input = StandInput(input("Создать задачу?(Да/Нет) - "))

app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(1100, 600)
window.setStyleSheet('QMainWindow {background-color: #222222;}')
window.show()

app.exec()
