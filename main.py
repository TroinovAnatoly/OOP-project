import sys
from asyncio import create_task

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QWidget, QPushButton, QDialog


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

class Task:
    def __init__(self, name, date, priority):
        self.__name = name
        self.__date = date
        self.__priority = priority


class TaskManager(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.setFixedSize(500, 300)
        self.setStyleSheet('QDialog {background-color: #111111;}')

    def create_task(self):
        pass

    def delete_task(self):
        pass

    def change_task(self):
        pass


class Priority:
    def __init__(self, level):
        self.level = level

    def configuration(self):
        pass

    def manual_of_priority(self):
        pass


class TaskGUI:
    def __init__(self, master):
        self.__master = master

    def visualisation(self):
        pass


class ThemeChange:
    def __init__(self):
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(1100, 600)
window.setStyleSheet('QMainWindow {background-color: #222222;}')
window.show()

app.exec()
