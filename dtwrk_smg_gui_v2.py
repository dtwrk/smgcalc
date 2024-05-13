import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow_for_dtwrk_smg_gui_v2 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_mix.clicked.connect(self.butt_swap)
        self.ui.pushButton_calculate.clicked.connect(self.butt_calculate)
        

    def butt_swap(self): # для кнопки "Размешать ->"
        value_entry_bank1_l = str_to_float(self.ui.entry_bank1_l.text())
        value_entry_bank2_l = str_to_float(self.ui.entry_bank2_l.text())
        value_entry_bank1_perc = str_to_float(self.ui.entry_bank1_perc.text())
        value_entry_bank2_perc = str_to_float(self.ui.entry_bank2_perc.text())
        value_for_entry_value_perc = round(((value_entry_bank1_l * value_entry_bank1_perc)+(value_entry_bank2_l * value_entry_bank2_perc))/(value_entry_bank1_l + value_entry_bank2_l),3)
        
        self.ui.entry_value_perc.setText(str(value_for_entry_value_perc))
        value_for_entry_value_l = round((value_entry_bank1_l + value_entry_bank2_l),3)
        self.ui.entry_value_l.setText(str(value_for_entry_value_l))

        #в 1 версии я очищал (код ниже). Надо вспомнить зачем 
        #pos_3_0.delete(0, END) #очищаю поле Entry
        #pos_3_1.delete(0, END) #очищаю поле Entry

    def butt_calculate(self): # для кнопки "Рассчитать"
        value_entry_value_perc = str_to_float(self.ui.entry_value_perc.text())
        value_entry_value_l = str_to_float(self.ui.entry_value_l.text())
        value_for_label_value_abssp_l = round((value_entry_value_l * value_entry_value_perc / 100.0), 3)
        value_for_label_value_addwater_l = round(((value_for_label_value_abssp_l / 0.2) - value_entry_value_l), 3)
        value_for_label_all_in_tank = round((value_entry_value_l + value_for_label_value_addwater_l), 3)

        self.ui.label_value_abssp_l.setText(str(value_for_label_value_abssp_l))
        self.ui.label_value_addwater_l.setText(str(value_for_label_value_addwater_l))
        self.ui.label_all_in_tank.setText(str(value_for_label_all_in_tank))


def str_to_float(a_value):
    if a_value == "":
        out_value = float(0)
    else:
        out_value = a_value.replace(",", ".")
        out_value = float(out_value)
    return(out_value)  

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())