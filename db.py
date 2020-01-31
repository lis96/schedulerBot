from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, qApp, QAction
from PyQt5.QtCore import QSize

# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
		# Переопределяем конструктор класса
		def __init__(self, title, width, height):
			# Обязательно нужно вызвать метод супер класса
			QMainWindow.__init__(self)

			self.setMinimumSize(QSize(width, height))			# Устанавливаем размеры
			self.setWindowTitle(title)							# Устанавливаем заголовок окна
			central_widget = QWidget(self)						# Создаём центральный виджет
			self.setCentralWidget(central_widget)				# Устанавливаем центральный виджет

			grid_layout = QGridLayout(self)						# Создаём QGridLayout
			central_widget.setLayout(grid_layout)				# Устанавливаем данное размещение в центральный виджет

			title = QLabel("Hello World on the PyQt5", self)	# Создаём лейбл
			title.setAlignment(QtCore.Qt.AlignCenter)			# Устанавливаем позиционирование текста
			grid_layout.addWidget(title, 0, 0)					# и добавляем его в размещение

			exit_action = QAction("&Exit", self)				# Создаём Action с помощью которого будем выходить из приложения
			exit_action.setShortcut('Ctrl+Q')					# Задаём для него хоткей
				# Подключаем сигнал triggered к слоту quit у qApp.
				# синтаксис сигналов и слотов в PyQt5 заметно отличается от того,
				# который используется Qt5 C++
			exit_action.triggered.connect(qApp.quit)
				# Устанавливаем в панель меню данный Action.
				# Отдельного меню создавать пока не будем.
			file_menu = self.menuBar()
			file_menu.addAction(exit_action)


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)

	mw = MainWindow(
		title = 'Hello, World',
		width = 600,
		height = 300
	)
	mw.show()

	sys.exit(app.exec())