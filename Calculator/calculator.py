from PySide6.QtWidgets import (
QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
QLabel, QMainWindow, QWidget,  
)
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize
import csv
            
class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculator")
        
        self.button0 = QPushButton("0") 
        self.button1 = QPushButton("1")       
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        
        self.plus_button = QPushButton("+")
        self.minus_button = QPushButton("-")
        self.mult_button = QPushButton("*")
        self.div_button = QPushButton("/")
        self.dot_button = QPushButton(".")
        self.par1_button = QPushButton("(")
        self.par2_button = QPushButton(")")
        self.equal_button = QPushButton("=")
        
        self.textHolder = QLabel()
        self._txt = ""
        
        self.button0.clicked.connect(self.button_0_connect)
        self.button1.clicked.connect(self.button_1_connect)
        self.button2.clicked.connect(self.button_2_connect)
        self.button3.clicked.connect(self.button_3_connect)
        self.button4.clicked.connect(self.button_4_connect)
        self.button5.clicked.connect(self.button_5_connect)
        self.button6.clicked.connect(self.button_6_connect)
        self.button7.clicked.connect(self.button_7_connect)
        self.button8.clicked.connect(self.button_8_connect)
        self.button9.clicked.connect(self.button_9_connect)
        
        self.plus_button.clicked.connect(self.button_plus_connect)
        self.minus_button.clicked.connect(self.button_minus_connect)
        self.mult_button.clicked.connect(self.button_mult_connect)
        self.div_button.clicked.connect(self.button_div_connect)
        self.dot_button.clicked.connect(self.dot_button_connect)
        self.par1_button.clicked.connect(self.par1_button_connect)
        self.par2_button.clicked.connect(self.par2_button_connect)
        self.equal_button.clicked.connect(self.button_equal_connect)
        self.equal_button.setMinimumSize(QSize(25,25))
        self.textHolder.setMinimumSize(QSize(50,25))
        
        
        menuBar = self.menuBar()
        config_menu = menuBar.addMenu("Configuration")
        
        quit_action = config_menu.addAction("quit")
        quit_action.triggered.connect(quit)
        
        
        Bh1_layout = QHBoxLayout()
        Bh1_layout.addWidget(self.textHolder)
        
        Bh2_layout = QHBoxLayout()
        Bh2_layout.addWidget(self.button7)
        Bh2_layout.addWidget(self.button8)
        Bh2_layout.addWidget(self.button9)
        Bh2_layout.addWidget(self.minus_button)
            
        Bh3_layout = QHBoxLayout()
        Bh3_layout.addWidget(self.button4)
        Bh3_layout.addWidget(self.button5)
        Bh3_layout.addWidget(self.button6)
        Bh3_layout.addWidget(self.plus_button)
            
        Bh4_layout = QHBoxLayout()
        Bh4_layout.addWidget(self.button1)
        Bh4_layout.addWidget(self.button2)
        Bh4_layout.addWidget(self.button3)
        Bh4_layout.addWidget(self.mult_button)
            
        Bh5_layout = QHBoxLayout()
        Bh5_layout.addWidget(self.button0)
        Bh5_layout.addWidget(self.dot_button)
        Bh5_layout.addWidget(self.equal_button)
        Bh5_layout.addWidget(self.div_button)
            
        BVmain_layout = QVBoxLayout()
        BVmain_layout.addLayout(Bh1_layout)
        BVmain_layout.addLayout(Bh2_layout)
        BVmain_layout.addLayout(Bh3_layout)
        BVmain_layout.addLayout(Bh4_layout)
        BVmain_layout.addLayout(Bh5_layout)
            
        self.Button_Layout = QWidget()
        self.Button_Layout.setLayout(BVmain_layout)
        self.setCentralWidget(self.Button_Layout)
            
        
        
        
    def button_0_connect(self):
        self.txt += "0"      
    def button_1_connect(self):
        self.txt += "1" 
    def button_2_connect(self):
        self.txt += "2" 
    def button_3_connect(self):
        self.txt += "3" 
    def button_4_connect(self):
        self.txt += "4" 
    def button_5_connect(self):
        self.txt += "5" 
    def button_6_connect(self):
        self.txt += "6" 
    def button_7_connect(self):
        self.txt += "7" 
    def button_8_connect(self):
        self.txt += "8" 
    def button_9_connect(self):
        self.txt += "9" 
        
    def button_plus_connect(self):
        self.txt += " + "  
    def button_minus_connect(self):
        self.txt += " - " 
    def button_mult_connect(self):
        self.txt += " * " 
    def button_div_connect(self):
        self.txt += " / "     
    def dot_button_connect(self):
        self.txt += "."         
    def par1_button_connect(self):
        self.txt += "("
    def par2_button_connect(self):
        self.txt += ")"
        
    
    def button_equal_connect(self):
        try:
            self.txt = str(eval(self.txt))
            self.textHolder.setText(self.txt)
        except ZeroDivisionError:  
            self.textHolder.setText(f"ERROR_01 - Attempted to divide by zero - {self.txt}")
            self.txt = ""
        except SyntaxError:
            self.textHolder.setText(f"ERROR_02 - Invalid expression - {self.txt}")
            self.txt = ""
        except TypeError:
            self.textHolder.setText(f"ERROR_03 - invalid expression - {self.txt}")
            self.txt = ""
        except:
            self.textHolder.setText(f"ERROR_04 - undentified error - {self.txt}")
                
    @property
    def txt(self):
        return self._txt
    
    @txt.setter
    def txt(self, new):
        self._txt = new
        self.textHolder.setText(self.txt)
            
         
        