from PySide6.QtWidgets import QApplication, QWidget, QCalendarWidget, QDialog

from PySide6 import QtGui, QtCore

from PySide6.QtGui import QDoubleValidator

from PySide6.QtCore import QDate


from views.ui_datecalc import *


from model import main_model


import json

import re

from datetime import datetime

from dateutil import relativedelta



class MainController(QWidget):

    def __init__(self, tempDire):

        super().__init__()

        self.ui = Ui_date_mode_widget()

        self.ui.setupUi(self)
        
        

        self.initialiseVariables()

        self.initialiseData()

        self.manageDateCombobox()

        self.manageButtons()

        self.manageDateChanged()
        

        


    def initialiseData(self):

        # complet date_category_cb combobox

        date_combo_items = ["Difference between dates", "Add or subtract days"]

        self.ui.date_category_cb.addItems(date_combo_items)
        

        # create a list of numbers in range of 0 to 1000

        numbers = [str(i) for i in range(0,1000)]

        # add that numbers in all years month and days combo
        

        self.ui.date_years_combo.addItems(numbers)

        self.ui.date_month_combo.addItems(numbers)

        self.ui.date_days_combo.addItems(numbers)
        
        

        # set the current date to all current date buttons

        self.ui.initial_dateEdit.setDate(self.__initial_date)

        self.ui.date_to_label_date.setDate(self.__final_date)
    

    def manageDateCombobox(self):

        def manageStacks(text:str):

            """manage stacked widget current widget change"""

            if text == "Difference between dates":

                self.ui.date_main_stackedWidget.setCurrentWidget(

                    self.ui.date_difference_widget)

                pass

            elif text == "Add or subtract days":

                self.ui.date_main_stackedWidget.setCurrentWidget(

                    self.ui.date_add_soubstract_widget)

                pass 

        def changeYears(years:str):

            # calculate the date add os sub

            self.calculateAddSubDate()

            pass

        def changeMonths(months:str):

            # calculate the date add os sub

            self.calculateAddSubDate()

            pass

        def changeDays(days:str):

            # calculate the date add os sub

            self.calculateAddSubDate()

            pass

        # initialise the stacked widget by getting the current value of the date combo

        current_date_text = self.ui.date_category_cb.currentText()

        manageStacks(text=current_date_text)

        # if combobox selection change change the stacked widget 

        self.ui.date_category_cb.currentTextChanged.connect(manageStacks)
        

        # if dates (years, months, days ) combobox selection change the value of variables

        self.ui.date_years_combo.currentTextChanged.connect(changeYears)

        self.ui.date_month_combo.currentTextChanged.connect(changeMonths)

        self.ui.date_days_combo.currentTextChanged.connect(changeDays)
    

    def initialiseVariables(self):

        self.__initial_date = QDate.currentDate()

        self.__final_date = QDate.currentDate()
        

        self.__years = 0

        self.__months = 0

        self.__days = 0

        self.__new_date = ""

        self.__operation = "Addition"


    def manageDateChanged(self):

        def onInitialDateChanged(date):
            self.__initial_date = date

            # calculate the difference of date

            self.calculateDifference()

            # calculate the date add os sub

            self.calculateAddSubDate()

        def onFinalDateChanged(date):
            self.__final_date = date

            # calculate the difference of date

            self.calculateDifference()

            # calculate the date add os sub

            self.calculateAddSubDate()

        # manage initial date change

        self.ui.initial_dateEdit.dateChanged.connect(onInitialDateChanged)

        self.ui.date_to_label_date.dateChanged.connect(onFinalDateChanged)
        

    def manageButtons(self):

        # manage radio buttons action

        self.ui.date_add_radioButton.clicked.connect(lambda:self.setOperator("Addition"))

        self.ui.dare_substract_radioButton.clicked.connect(lambda:self.setOperator("subtract"))    
    

    def setOperator(self,operation:str=None):

        if operation == None:

            self.__operation = self.__operation

            self.calculateAddSubDate()

        else:

            self.__operation = operation

            self.calculateAddSubDate()
            

    def calculateAddSubDate(self):

        # get the current initial date
        current_date = self.__initial_date

        # transform all dates into python dates for operation

        py_initial_date = self.__initial_date.toPython()

        # get current value of all combo

        self.__years = int(self.ui.date_years_combo.currentText())

        self.__months = int(self.ui.date_month_combo.currentText())

        self.__days = int(self.ui.date_days_combo.currentText())
        

        if self.__operation == "Addition":

            def additionOperation():

                # check if the year is different of 0

                self.__new_date = py_initial_date + relativedelta.relativedelta(years = self.__years)

                self.__new_date = self.__new_date + relativedelta.relativedelta(months =self.__months )

                self.__new_date = self.__new_date + relativedelta.relativedelta(months =self.__days)
                

            additionOperation()

        elif self.__operation == "subtract":

            def subtractOperation():

                # check if the year is different of 0

                self.__new_date = py_initial_date + relativedelta.relativedelta(years = self.__years)

                self.__new_date = self.__new_date + relativedelta.relativedelta(months =self.__months )

                self.__new_date = self.__new_date + relativedelta.relativedelta(months =self.__days)
                

                pass

            subtractOperation()

        self.ui.date_result_label.setText(str(self.__new_date))

        pass
    

    def calculateDifference(self):

        # transform all dates into python dates for operation

        py_initial_date = self.__initial_date.toPython()

        py_final_date = self.__final_date.toPython()
    

        # calculate the difference for days

        difference = py_initial_date - py_final_date

        difference_days = abs(difference.days)
        

        # calculate differences for weeks

        difference_weeks_float = float(difference_days/7)       

        difference_weeks_int = difference_days//7 
        if difference_weeks_float == difference_weeks_int:

            rest_of_days_week = 0

        else:

            rest_of_days_week = (difference_weeks_float - difference_weeks_int)*7

            rest_of_days_week = round(rest_of_days_week)

        # calculate the difference for months

        difference_months = (py_initial_date.year - py_final_date.year)*12 - (py_initial_date.month - py_final_date.month)
        

        # calculate the difference for year

        difference_years = py_initial_date.year - py_final_date.year

        # get the delta value of the difference

        delta = relativedelta.relativedelta(py_final_date, py_initial_date)
        # print the difference on the label

        str_days = f""

        str_weeks = f""

        str_months = f""

        str_years = f""

        if int(delta.days) != 0 :

            if int(delta.days) == 1:

                str_days = f"{int(delta.days)-(int(delta.weeks)*7)} day"

            else:

                str_days = f"{int(delta.days)-(int(delta.weeks)*7)} days"

        else:

            str_days == f""

        if int(delta.weeks) != 0 :

            if int(delta.weeks) == 1:

                str_weeks = f"{delta.weeks} week ,"

            else:

                str_weeks = f"{delta.weeks} weeks ,"

        else:

            str_weeks == f""

        if int(delta.months) != 0 :

            if int(delta.months) == 1:

                str_months = f"{delta.months} month ,"

            else:

                str_months = f"{delta.months} months ,"

        else:

            str_months == f""

        if int(delta.years) != 0 :

            if int(delta.years) == 1:

                str_years = f"{delta.years} year ,"

            else:

                str_years = f"{delta.years} years ,"

        else:

            str_years == f""
        

        final_str = f"{str_years} {str_months} {str_weeks} {str_days}"

        final_str = final_str.strip()
        

        self.ui.date_difference_label.setText(final_str)

        if int(difference_days) == 1:

            self.ui.all_days.setText(f"{difference_days} day")

        elif int(difference_days) == 0:

            self.ui.all_days.setText(f"")

        else:

            self.ui.all_days.setText(f"{difference_days} days")
        
        pass