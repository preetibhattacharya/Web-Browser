from PyQt5.QtGui import QGuiApplication, QIcon,QPixmap
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtCore import*

from PyQt5.QtWebEngineWidgets import*



class WebClass(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__() #invoking the constructor of superclass "QMainWindow".
        self.setWindowTitle("Web Explorer")
        self.setWindowIcon(QIcon('icon.png'))
        self.showMaximized()

        #self.setStyleSheet("QMainWindow { font-size: 100px; }")  # Set title font size
        #self.layout().setAlignment(Qt.AlignCenter) 

        #self.setAttribute(Qt.WA_StyledBackground, True)
        #self.setStyleSheet("QMainWindow::title {background: white; padding: 50px;}")

        # Increase icon size
        #self.setWindowIconSize(QSize(50, 50))  # Adjust size as needed


        self.browser=QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('https://www.indiatoday.in/blogs-section'))
    
        

        self.menu = QToolBar()
        self.menu.setStyleSheet("QToolBar { background-color: #f0f0f0; }")
        self.addToolBar(self.menu)

        self.menu.setStyleSheet("QToolButton { background-color: #ffffff; border: 1px solid #cccccc; border-radius: 5px; }")
        self.menu.setIconSize(QSize(32, 32))  # Set icon size
        self.menu.setContentsMargins(10, 5, 10, 5)  # Set margins


        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        self.menu.addAction(back_btn)

        next_btn = QAction('Next',self)
        next_btn.triggered.connect(self.browser.forward)
        self.menu.addAction(next_btn)

        reload_btn = QAction('Refresh',self)
        reload_btn.triggered.connect(self.browser.reload)
        self.menu.addAction(reload_btn)

        
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.home_url)
        self.menu.addAction(home_btn)

        self.home_url_input = QLineEdit()  # LineEdit to input custom homepage URL
        self.home_url_input.setPlaceholderText("Enter custom homepage URL")
        self.home_url_input.returnPressed.connect(self.navigate_input)
        self.menu.addWidget(self.home_url_input)


    def home_url(self):
        self.browser.setUrl(QUrl('https://www.indiatoday.in/blogs-section'))


    def navigate_input(self):
        url = self.home_url_input.text()
        if url:
            self.browser.setUrl(QUrl(url))






WebApp = QApplication(sys.argv)
QApplication.setApplicationName("Web Explorer")
obj = WebClass()
WebApp.exec_()