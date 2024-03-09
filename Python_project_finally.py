import re
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 779)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(7, 10, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Nasim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 83);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.Enter_Pragragh = QtWidgets.QTextEdit(self.centralwidget)
        self.Enter_Pragragh.setGeometry(QtCore.QRect(7, 50, 381, 231))
        self.Enter_Pragragh.setObjectName("Enter_Pragragh")
        self.Text_dict = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_dict.setGeometry(QtCore.QRect(9, 610, 381, 161))
        self.Text_dict.setObjectName("Text_dict")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 570, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Nasim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.Text_other = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_other.setGeometry(QtCore.QRect(7, 330, 381, 231))
        self.Text_other.setObjectName("Text_other")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(7, 290, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Nasim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 11, 561, 41))
        font = QtGui.QFont()
        font.setFamily("Nasim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.plot_hist = QtWidgets.QLabel(self.centralwidget)
        self.plot_hist.setGeometry(QtCore.QRect(420, 70, 541, 471))
        self.plot_hist.setText("")
        self.plot_hist.setObjectName("plot_hist")
        self.btn_Run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Run.setGeometry(QtCore.QRect(792, 590, 171, 161))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Run.setFont(font)
        self.btn_Run.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(0, 0, 83);")
        self.btn_Run.setObjectName("btn_Run")

        self.btn_Run.clicked.connect(self.Run_dict)

        self.Text_cor = QtWidgets.QTextEdit(self.centralwidget)
        self.Text_cor.setGeometry(QtCore.QRect(399, 610, 381, 161))
        self.Text_cor.setObjectName("Text_cor")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 570, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Nasim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "            Enter text tow Pragragh"))
        self.label_3.setText(_translate("MainWindow", "                   Show this Dict"))
        self.label_2.setText(_translate("MainWindow", "                   Show other Text "))
        self.label_4.setText(_translate("MainWindow", "                        Show Plot in Histogram"))
        self.btn_Run.setText(_translate("MainWindow", "Run"))
        self.label_5.setText(_translate("MainWindow", "                   Correcting words"))

    def Run_dict(self):
        text_pragragh = self.Enter_Pragragh.toPlainText()
        result_word_dict = {f"Word_{index + 1}": char for index, char in enumerate(text_pragragh)}
        result_text = '\n'.join([f'{key}: {value}' for key, value in result_word_dict.items()])
        self.Text_dict.setPlainText(result_text)
        Remove_word = re.sub(r'_|2020|are|23:20|and|is|or|!|-', " ", text_pragragh)
        matches = re.findall(r'learning|book|time|day|old|best', text_pragragh)
        # Concatenate Remove_word and matches into a single string
        result_text_1 = f"Remove_word:\n{Remove_word}\n\nMatches:\n{matches}"

        # Set the plain text in Text_cor
        self.Text_cor.setPlainText(result_text_1)

        # self.Text_cor.setPlainText(Remove_word)
        # self.Text_cor.setPlainText(matches)
        self.Text_other.setPlainText(result_text)
        word_counts = {word: matches.count(word) for word in set(matches)}
        sorted_words = sorted(word_counts.keys(), key=lambda x: word_counts[x], reverse=True)
        sorted_counts = [word_counts[word] for word in sorted_words]
        result_text = '\n'.join([f'{word}: {word_counts[word]}' for word in sorted_words])
        self.Text_other.setPlainText(result_text)

        plt.bar(sorted_words, sorted_counts, color='blue')
        plt.title("Python Library", fontdict={'family': 'serif', 'color': 'green', 'size': 25})
        plt.xlabel("Name", fontdict={'family': 'serif', 'color': 'red', 'size': 15})
        plt.ylabel("Count", fontdict={'family': 'serif', 'color': 'red', 'size': 15})
        plt.grid(color='green', linestyle='--', linewidth=0.5)
        plt.savefig('histogram.png')  # Save the plot as an image
        pixmap = QtGui.QPixmap('histogram.png')
        self.plot_hist.setPixmap(pixmap)
        self.plot_hist.setScaledContents(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
