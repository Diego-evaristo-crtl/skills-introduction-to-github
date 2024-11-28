from PySide6.QtWidgets import QApplication
from calculator import Calculator
import sys

if len(sys.argv) == 2:
    if sys.argv[1] == "-e" or sys.argv[1] == "--error" or sys.argv[1] == "--ERROR" or sys.argv[1] == "-E":
        print("ERROR_01: ZerDivisionError \n " + 
              "Occurs when the evaluation of self.txt has a division by 0" + 
              "such as \'(2 + 3) / 0\'\n"
              )
        print("ERROR_02: SyntaxError \n" + 
              "Occurs when the equal_button_connect method is called and the self.txt attribute has" +
              " a sequence of symbols that cannot be evaluated, such as \' 2 + + 0 \' \n")
        print("ERROR_03: TypeError \n" +
              "Occurs when the equal_button_connect method is called and the self.txt attribute has" +
              " a letter or symbol that does not have a mathematical meaning supported by the Calculator class\n")
        print("ERROR_04: Error \n" +
              "an error that is not specifically handled by the equal_button_connect method" +
              " , any error that is not from the TypeError, SyntaxError, or ZeroDvisionError classes")
        sys.exit()
    

app = QApplication(sys.argv)

calc = Calculator()
calc.show()

app.exec()
