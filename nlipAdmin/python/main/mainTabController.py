from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QPushButton, QStackedWidget, QVBoxLayout, QWidget)
from PyQt5.uic import loadUi


def mainTabSet(self):
    # QT Designer ui 호출
    loadUi('nlipAdmin/nlipAdmin.ui', self)

    # stacked widget 생성
    self.stackedWidget = QStackedWidget()

    # 컨테이너 생성
    tabContainer = QWidget()
    tabContainer.setGeometry(0,0,120,800)
    viewContainer = QWidget()
    viewContainer.setGeometry(120,0,1080,800)
    
    # 버튼 생성
    self.tabButtonMain = QPushButton("메인")
    self.tabButtonEmap = QPushButton("바로E맵")
    self.tabButtonNlsp = QPushButton("국토조사")

    # 버튼 사이즈 조정
    self.tabButtonMain.setFixedSize(100, 50)
    self.tabButtonEmap.setFixedSize(100, 50)
    self.tabButtonNlsp.setFixedSize(100, 50)

    # Create the content widgets for each tab
    self.tab1Content = QLabel("Content of Tab 1")
    self.tab2Content = QLabel("Content of Tab 2")
    self.tab3Content = QLabel("Content of Tab 3")

    # Create a separate stacked widget for the view area
    viewStackedWidget = QStackedWidget()
    viewStackedWidget.addWidget(self.tab1Content)
    viewStackedWidget.addWidget(self.tab2Content)
    viewStackedWidget.addWidget(self.tab3Content)

    # 버튼 클릭 후 위젯 변경
    self.tabButtonMain.clicked.connect(lambda: viewStackedWidget.setCurrentIndex(0))
    self.tabButtonEmap.clicked.connect(lambda: viewStackedWidget.setCurrentIndex(1))
    self.tabButtonNlsp.clicked.connect(lambda: viewStackedWidget.setCurrentIndex(2))

    # Add buttons to a vertical layout
    buttonLayout = QVBoxLayout(tabContainer)
    buttonLayout.addWidget(self.tabButtonMain)
    buttonLayout.addWidget(self.tabButtonEmap)
    buttonLayout.addWidget(self.tabButtonNlsp)
   
    # 메인 레이아웃에 추가
    mainLayout = QVBoxLayout(self.centralwidget)
    mainLayout.addWidget(tabContainer)
    mainLayout.addWidget(viewStackedWidget)

    # Set the central widget
    self.setCentralWidget(self.centralwidget)
