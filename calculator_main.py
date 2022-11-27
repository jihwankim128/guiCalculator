import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class QPushButtonOperation(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class QPushButtonNumber(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class QLineEditText(QLineEdit):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        ######### 레이아웃 초기 설정 #########
        main_layout = QVBoxLayout()
        layout_bottom = QHBoxLayout()
        layout_equation_solution = QVBoxLayout()
        layout_top_first = QHBoxLayout()
        layout_top_second = QHBoxLayout()
        layout_bottom_first = QGridLayout()
        layout_bottom_second = QVBoxLayout()



        ######### layout_equation_solution #########
        ### later
        self.number_display = QLineEditText("")
        self.equation = QLineEditText("")
        self.solution = QLineEditText("0")
        self.equation.setAlignment(Qt.AlignRight)
        self.solution.setAlignment(Qt.AlignRight)



        ######### layout_top_first #########
        ### create widget
        button_backspace = QPushButtonOperation("<=")
        button_clear = QPushButtonOperation("C")
        button_clear_entry = QPushButtonOperation("CE")
        button_mod = QPushButtonOperation("%")

        ### addWidget ot layout_top_first
        layout_top_first.addWidget(button_mod)
        layout_top_first.addWidget(button_clear_entry)
        layout_top_first.addWidget(button_clear)
        layout_top_first.addWidget(button_backspace)

        ### function - later
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clear_entry.clicked.connect(self.button_clear_entry_clicked)
        #button_mod.clicked.connect(self.button_negate_clicked)



        ######### layout_top_second #########
        ### create widget
        button_reverse = QPushButtonOperation("¹/×")
        button_pow = QPushButtonOperation("pow")
        button_sqrt = QPushButtonOperation("sqrt")
        button_division = QPushButtonOperation("÷")

        ### addWidget ot layout_top_second
        layout_top_second.addWidget(button_reverse)
        layout_top_second.addWidget(button_pow)
        layout_top_second.addWidget(button_sqrt)
        layout_top_second.addWidget(button_division)

        ### function - later
        #button_reverse.clicked.connect(self.button_reverse_clicked)
        #button_pow.clicked.connect(self.button_pow_clicked)
        #button_sqrt.clicked.connect(self.button_sqrt_clicked)
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))



        ######### layout_bottom_first #########
        ### create widget + add widget + function
        number_button_dict = {}
        button_dot = QPushButtonNumber(".")
        button_negate = QPushButtonNumber("⁺/₋")

        layout_bottom_first.addWidget(button_negate, 3, 0)
        layout_bottom_first.addWidget(button_dot, 3, 2)

        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        #button_negate.clicked.connect(self.button_negate_clicked)

        for number in range(0, 10):
            number_button_dict[number] = QPushButtonNumber(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number:
                                                       self.number_button_clicked(num))
            if number > 0:
                x, y = int(6/number), (number-1)%3
                if number == 2:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                elif number == 1:
                    layout_bottom_first.addWidget(number_button_dict[number], 2, y)
                else :
                    layout_bottom_first.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_bottom_first.addWidget(number_button_dict[number], 3, 1)



        ######### layout_bottom_second #########
        ### create widget
        button_product = QPushButtonNumber("×")
        button_plus = QPushButtonNumber("＋")
        button_minus = QPushButtonNumber("－")
        button_equal = QPushButtonNumber("=")

        ### add widget to layout_bottom_second
        layout_bottom_second.addWidget(button_product)
        layout_bottom_second.addWidget(button_plus)
        layout_bottom_second.addWidget(button_minus)
        layout_bottom_second.addWidget(button_equal)

        ### function - later
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_equal.clicked.connect(self.button_equal_clicked)



        ######### layout_equation_solution #########
        layout_equation_solution.addWidget(self.equation, stretch = 1)
        layout_equation_solution.addWidget(self.solution, stretch = 9)


        ######### layout_bottom #########
        layout_bottom.addLayout(layout_bottom_first, stretch = 75)
        layout_bottom.addLayout(layout_bottom_second,  stretch = 25)



        ######### layout_main #########
        main_layout.addLayout(layout_equation_solution, stretch = 250)
        main_layout.addLayout(layout_top_first, stretch = 125)
        main_layout.addLayout(layout_top_second, stretch = 125)
        main_layout.addLayout(layout_bottom, stretch = 500)


        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################

        self.operand = 0
        self.result = 0
        self.operator = ""
        self.entry = ""
        self.temp = ""
        self.chkop = True
        self.ce = False
        self.inputNum = False

    def number_button_clicked(self, num):
        if self.operator != "":
            self.solution.setText("")
        self.temp+=str(num)
        print(f"num_button {self.ce}  {self.inputNum}  {self.temp}")
        if self.ce and not self.inputNum and self.chkop:
            self.equation.setText("")
            self.entry = self.operand
            self.inputNum = True

        self.operand = int(self.temp)
        self.solution.setText(self.temp)
        self.chkop = True

    def button_operation_clicked(self, operation):
        self.entry = "0" if self.entry == "" else self.entry
        self.temp = "0" if self.temp == "" else self.temp
        print(operation)
        if not self.chkop == False and self.operator == "":
            if operation == "+" :
                self.result = int(self.entry)+self.operand
                self.entry = str(self.result)
            elif operation == "-" :
                print(self.entry)
                self.result = self.operand if self.entry == "0" else int(self.entry) - self.operand
                self.entry = str(self.result)
            elif operation == "*":
                self.result = 1*self.operand
                self.entry = str(self.result)
        elif not self.chkop == False:
            if self.operator == "+" :
                self.result = int(self.entry)+self.operand
                self.entry = str(self.result)
            elif self.operator == "-" :
                print(self.entry)
                self.result = self.operand if self.entry == "0" else int(self.entry) - self.operand
                self.entry = str(self.result)
            elif self.operator == "*":
                self.result = int(self.entry)*self.operand
                self.entry = str(self.result)


        print(self.entry + " cc " + str(self.operand) + "   " + str(self.result))

        self.operator = operation
        equation = self.temp if self.equation.text() =="" else self.entry
        equation += operation
        self.equation.setText(equation)
        self.solution.setText(str(self.result))
        self.temp = ""
        self.chkop = False


    def button_equal_clicked(self):
        if self.inputNum:
            self.temp = self.entry
            self.entry = str(self.operand)
            self.operand = int(self.temp)
            self.temp = "0"
            self.ce = False
            self.inputNum = False
        else:
            self.ce = False
        equation = self.entry + self.operator + str(self.operand) + "="
        self.entry = "0" if self.entry=="" else self.entry
        if self.operator == "+":
            self.result = int(self.entry)+self.operand
        elif self.operator == "-":
            self.result = int(self.entry)-self.operand
        elif self.operator == "*":
            self.result = int(self.entry)*self.operand
        self.entry = str(self.result)
        self.equation.setText(equation)
        self.solution.setText(str(self.result))
        self.temp = ""
        self.chkop = False
        self.ce = True

        print(f"{self.entry} + {self.operator} + {self.operand} + {self.result}")


    def button_clear_clicked(self):
        self.operand = 0
        self.result = 0
        self.operator = ""
        self.entry = ""
        self.temp = ""
        self.chkop = True
        self.ce = False
        self.inputNum = False
        self.equation.setText("")
        self.solution.setText("0")

    def button_clear_entry_clicked(self):
        self.result = 0
        self.temp = ""
        self.entry = "0"
        self.chkop = True
        self.ce = True
        self.equation.setText("")
        self.solution.setText("0")

    def button_backspace_clicked(self):
        if self.chkop and not self.temp == "":
            self.operand = int(self.operand/10)
            self.temp = "" if self.operand==0 else str(self.operand)
            solution = "0" if len(self.solution.text()) == 1 else self.solution.text()[:-1]
            self.solution.setText(solution)
        else:
            self.equation.setText("")
            self.temp = self.entry

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
