import sys

import win32con
import win32gui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                             QStackedWidget, QVBoxLayout, QWidget)
from PyQt5.uic import loadUi

from main import mainTabController


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # MainWindow 좌측 탭 설정
        mainTabController.mainTabSet(self)


def main():
    # Create an application instance
    app = QApplication(sys.argv)

    # 윈도우 설정
    window = MainWindow()
    window.setWindowIcon(QIcon('nlipAdmin/resource/img/logo/logo_lt.ico'))
    window.setWindowTitle('국토정보플랫폼 유지보수 관리자')
    window.setFixedSize(1200, 800)
    window.show()

    # 상태표시줄 로고 설정
    hwnd = win32gui.GetForegroundWindow()
    hicon = win32gui.LoadImage(win32gui.GetModuleHandle(None), 'nlipAdmin/resource/img/logo/logo_lt.ico', win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE)
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, hicon)

    # Start the event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
