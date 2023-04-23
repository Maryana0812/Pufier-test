from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QApplication, QWidget,
  QHBoxLayout, QVBoxLayout, 
  QGroupBox, QRadioButton, 
  QPushButton, QLabel, QListWidget, QLineEdit)

from instr import*
from final_win import*

# class second_win

class TestWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_apper() # устанавливает, как будет выглядеть окно
    self.initUI() # создаёт и настраивает графические элементы
    self.connects() # устанавливает связи между элелентами
    self.show() # старт, сделать окно видимым
  def set_appear(self):
    self.setWindoTitle(txt_title) # добавить название окна
    self.resize(win_width, win_height) # изменить размерв окна
    self.move(win_x, win_y) # появление окна в указанной точке
  def initUI(self):
    # описание элементов интерфейса
    '''создание графических элементов'''
    pass
  def connects(self):
    pass
  def next_click(self):
    self.hide()
    self.tw = TestWin()
