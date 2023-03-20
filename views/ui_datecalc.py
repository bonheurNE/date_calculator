# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datecalc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
from model.icons import icon_rc

class Ui_date_mode_widget(object):
    def setupUi(self, date_mode_widget):
        if not date_mode_widget.objectName():
            date_mode_widget.setObjectName(u"date_mode_widget")
        date_mode_widget.resize(400, 503)
        date_mode_widget.setStyleSheet(u"QLabel{\n"
"background-color:transparent;\n"
"color:rgb(122, 122, 122);}\n"
"QLabel:hover{\n"
"background-color:rgb(38, 38, 38);\n"
"color:rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"color:rgb(122, 122, 122);\n"
"border:none;}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border:1px solid rgb(255, 170, 0);\n"
"border-left:none;\n"
"border-right:none;\n"
"border-top:none\n"
"}\n"
"QWidget{\n"
"background-color:rgb(32, 32, 32);}")
        self.verticalLayout = QVBoxLayout(date_mode_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.date_header_frame = QFrame(date_mode_widget)
        self.date_header_frame.setObjectName(u"date_header_frame")
        self.date_header_frame.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border:1px solid darkgrey;\n"
"}\n"
"QLabel{\n"
"color:skyblue;}\n"
"QLabel:hover{\n"
"color:rgb(0, 85, 127);\n"
"border:2px solid rgb(0, 58, 0);\n"
"	border-top-color: transparent;\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"}")
        self.date_header_frame.setFrameShape(QFrame.StyledPanel)
        self.date_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.date_header_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.DateManasIconpushButton = QPushButton(self.date_header_frame)
        self.DateManasIconpushButton.setObjectName(u"DateManasIconpushButton")
        self.DateManasIconpushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/MANAS_ICON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DateManasIconpushButton.setIcon(icon)
        self.DateManasIconpushButton.setIconSize(QSize(100, 100))

        self.horizontalLayout_15.addWidget(self.DateManasIconpushButton)

        self.date_title_label = QLabel(self.date_header_frame)
        self.date_title_label.setObjectName(u"date_title_label")

        self.horizontalLayout_15.addWidget(self.date_title_label, 0, Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.date_header_frame)

        self.date_category_frame = QFrame(date_mode_widget)
        self.date_category_frame.setObjectName(u"date_category_frame")
        font = QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        self.date_category_frame.setFont(font)
        self.date_category_frame.setStyleSheet(u"")
        self.date_category_frame.setFrameShape(QFrame.StyledPanel)
        self.date_category_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.date_category_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.from_date_calendar_btn = QPushButton(self.date_category_frame)
        self.from_date_calendar_btn.setObjectName(u"from_date_calendar_btn")
        font1 = QFont()
        font1.setPointSize(12)
        self.from_date_calendar_btn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.from_date_calendar_btn.setIcon(icon1)
        self.from_date_calendar_btn.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.from_date_calendar_btn, 6, 2, 1, 1)

        self.date_from_label = QLabel(self.date_category_frame)
        self.date_from_label.setObjectName(u"date_from_label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.date_from_label.setFont(font2)

        self.gridLayout_4.addWidget(self.date_from_label, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 1, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 4, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 5, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 6, 4, 1, 1)

        self.date_category_cb = QComboBox(self.date_category_frame)
        self.date_category_cb.setObjectName(u"date_category_cb")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.date_category_cb.setFont(font3)
        self.date_category_cb.setStyleSheet(u"background-color:transparent;\n"
"color:rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.date_category_cb, 0, 0, 1, 5)

        self.initial_dateEdit = QDateEdit(self.date_category_frame)
        self.initial_dateEdit.setObjectName(u"initial_dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.initial_dateEdit.sizePolicy().hasHeightForWidth())
        self.initial_dateEdit.setSizePolicy(sizePolicy)
        self.initial_dateEdit.setFont(font1)
        self.initial_dateEdit.setStyleSheet(u"color:skyblue;\n"
"border:none;")
        self.initial_dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.initial_dateEdit.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.initial_dateEdit, 6, 0, 1, 1)


        self.verticalLayout.addWidget(self.date_category_frame)

        self.date_main_frame = QFrame(date_mode_widget)
        self.date_main_frame.setObjectName(u"date_main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.date_main_frame.sizePolicy().hasHeightForWidth())
        self.date_main_frame.setSizePolicy(sizePolicy1)
        self.date_main_frame.setFrameShape(QFrame.StyledPanel)
        self.date_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.date_main_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.date_main_stackedWidget = QStackedWidget(self.date_main_frame)
        self.date_main_stackedWidget.setObjectName(u"date_main_stackedWidget")
        self.date_difference_widget = QWidget()
        self.date_difference_widget.setObjectName(u"date_difference_widget")
        self.horizontalLayout_17 = QHBoxLayout(self.date_difference_widget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame = QFrame(self.date_difference_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.date_to_label = QLabel(self.frame)
        self.date_to_label.setObjectName(u"date_to_label")
        self.date_to_label.setFont(font2)

        self.gridLayout_3.addWidget(self.date_to_label, 0, 0, 1, 1)

        self.date_to_calendar_btn = QPushButton(self.frame)
        self.date_to_calendar_btn.setObjectName(u"date_to_calendar_btn")
        self.date_to_calendar_btn.setIcon(icon1)
        self.date_to_calendar_btn.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.date_to_calendar_btn, 2, 1, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_9 = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_18, 8, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 57, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 3, 0, 1, 1)

        self.date_difference_title_label = QLabel(self.frame)
        self.date_difference_title_label.setObjectName(u"date_difference_title_label")
        self.date_difference_title_label.setFont(font2)

        self.gridLayout_3.addWidget(self.date_difference_title_label, 4, 0, 1, 1, Qt.AlignLeft)

        self.date_difference_label = QLabel(self.frame)
        self.date_difference_label.setObjectName(u"date_difference_label")
        font4 = QFont()
        font4.setFamilies([u"Calibri Light"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.date_difference_label.setFont(font4)

        self.gridLayout_3.addWidget(self.date_difference_label, 6, 0, 1, 2)

        self.date_to_label_date = QDateEdit(self.frame)
        self.date_to_label_date.setObjectName(u"date_to_label_date")
        font5 = QFont()
        font5.setPointSize(14)
        self.date_to_label_date.setFont(font5)
        self.date_to_label_date.setStyleSheet(u"color:skyblue;\n"
"border:none;")
        self.date_to_label_date.setFrame(True)
        self.date_to_label_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.date_to_label_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_to_label_date.setCalendarPopup(True)
        self.date_to_label_date.setCurrentSectionIndex(0)

        self.gridLayout_3.addWidget(self.date_to_label_date, 2, 0, 1, 1)

        self.all_days = QLabel(self.frame)
        self.all_days.setObjectName(u"all_days")
        self.all_days.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.all_days, 7, 0, 1, 1)


        self.horizontalLayout_17.addWidget(self.frame)

        self.date_main_stackedWidget.addWidget(self.date_difference_widget)
        self.date_add_soubstract_widget = QWidget()
        self.date_add_soubstract_widget.setObjectName(u"date_add_soubstract_widget")
        self.horizontalLayout_18 = QHBoxLayout(self.date_add_soubstract_widget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.date_sum_diff_frame = QFrame(self.date_add_soubstract_widget)
        self.date_sum_diff_frame.setObjectName(u"date_sum_diff_frame")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(9)
        self.date_sum_diff_frame.setFont(font6)
        self.date_sum_diff_frame.setStyleSheet(u"\n"
"QRadioButton{\n"
"background-color:transparent;\n"
"color:rgb(122, 122, 122);\n"
"border:none;}\n"
"QRadioButton:hover{\n"
"background-color:transparent;\n"
"color:rgb(255, 255, 255);\n"
"border:none;}\n"
"QComboBox{\n"
"background-color:rgb(32, 32, 32);\n"
"color:rgb(255, 255, 255);\n"
"border:1px solid rgb(159, 159, 159);\n"
"}\n"
"QComboBox:hover{\n"
"background-color:rgb(32, 32, 32);\n"
"color:rgb(255, 255, 255);\n"
"border:1px solid skyblue;\n"
"border-radius:2px;\n"
"}")
        self.date_sum_diff_frame.setFrameShape(QFrame.StyledPanel)
        self.date_sum_diff_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.date_sum_diff_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.dare_substract_radioButton = QRadioButton(self.date_sum_diff_frame)
        self.dare_substract_radioButton.setObjectName(u"dare_substract_radioButton")
        self.dare_substract_radioButton.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dare_substract_radioButton.setIcon(icon2)

        self.gridLayout_5.addWidget(self.dare_substract_radioButton, 0, 2, 1, 1)

        self.date_years_label = QLabel(self.date_sum_diff_frame)
        self.date_years_label.setObjectName(u"date_years_label")
        self.date_years_label.setFont(font6)

        self.gridLayout_5.addWidget(self.date_years_label, 2, 0, 1, 1)

        self.date_month_label = QLabel(self.date_sum_diff_frame)
        self.date_month_label.setObjectName(u"date_month_label")
        self.date_month_label.setFont(font6)

        self.gridLayout_5.addWidget(self.date_month_label, 2, 2, 1, 1)

        self.date_add_radioButton = QRadioButton(self.date_sum_diff_frame)
        self.date_add_radioButton.setObjectName(u"date_add_radioButton")
        self.date_add_radioButton.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.date_add_radioButton.setIcon(icon3)

        self.gridLayout_5.addWidget(self.date_add_radioButton, 0, 0, 1, 1)

        self.date_years_combo = QComboBox(self.date_sum_diff_frame)
        self.date_years_combo.setObjectName(u"date_years_combo")
        self.date_years_combo.setMinimumSize(QSize(0, 30))
        self.date_years_combo.setMaxVisibleItems(15)
        self.date_years_combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.date_years_combo.setMinimumContentsLength(0)
        self.date_years_combo.setFrame(False)

        self.gridLayout_5.addWidget(self.date_years_combo, 4, 0, 1, 1)

        self.date_month_combo = QComboBox(self.date_sum_diff_frame)
        self.date_month_combo.setObjectName(u"date_month_combo")
        self.date_month_combo.setMinimumSize(QSize(0, 30))

        self.gridLayout_5.addWidget(self.date_month_combo, 4, 2, 1, 1)

        self.date_days_combo = QComboBox(self.date_sum_diff_frame)
        self.date_days_combo.setObjectName(u"date_days_combo")
        self.date_days_combo.setMinimumSize(QSize(60, 30))

        self.gridLayout_5.addWidget(self.date_days_combo, 4, 4, 1, 1)

        self.date_result_title_label = QLabel(self.date_sum_diff_frame)
        self.date_result_title_label.setObjectName(u"date_result_title_label")
        self.date_result_title_label.setFont(font2)

        self.gridLayout_5.addWidget(self.date_result_title_label, 7, 0, 1, 1)

        self.date_days_label = QLabel(self.date_sum_diff_frame)
        self.date_days_label.setObjectName(u"date_days_label")
        self.date_days_label.setFont(font6)

        self.gridLayout_5.addWidget(self.date_days_label, 2, 4, 1, 1)

        self.date_result_label = QLabel(self.date_sum_diff_frame)
        self.date_result_label.setObjectName(u"date_result_label")
        font7 = QFont()
        font7.setFamilies([u"Calibri"])
        font7.setPointSize(18)
        font7.setBold(True)
        self.date_result_label.setFont(font7)
        self.date_result_label.setStyleSheet(u"color:rgb(243, 243, 243)")

        self.gridLayout_5.addWidget(self.date_result_label, 9, 0, 1, 5)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 3, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 7, 2, 1, 3)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_17, 6, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_16, 8, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 5, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 4, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 4, 3, 1, 1)


        self.horizontalLayout_18.addWidget(self.date_sum_diff_frame)

        self.date_main_stackedWidget.addWidget(self.date_add_soubstract_widget)

        self.horizontalLayout_16.addWidget(self.date_main_stackedWidget)


        self.verticalLayout.addWidget(self.date_main_frame)


        self.retranslateUi(date_mode_widget)
        self.from_date_calendar_btn.clicked.connect(self.initial_dateEdit.setFocus)
        self.date_to_calendar_btn.clicked.connect(self.date_to_label_date.setFocus)
        self.date_main_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(date_mode_widget)
    # setupUi

    def retranslateUi(self, date_mode_widget):
        date_mode_widget.setWindowTitle(QCoreApplication.translate("date_mode_widget", u"Form", None))
        self.DateManasIconpushButton.setText("")
        self.date_title_label.setText(QCoreApplication.translate("date_mode_widget", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600; color:skyblue;\">Date Calculation</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.from_date_calendar_btn.setToolTip(QCoreApplication.translate("date_mode_widget", u"show calendar", None))
#endif // QT_CONFIG(tooltip)
        self.from_date_calendar_btn.setText("")
        self.date_from_label.setText(QCoreApplication.translate("date_mode_widget", u"From", None))
        self.date_category_cb.setCurrentText("")
        self.initial_dateEdit.setSpecialValueText("")
        self.initial_dateEdit.setDisplayFormat(QCoreApplication.translate("date_mode_widget", u"dd/MM/yyyy", None))
        self.date_to_label.setText(QCoreApplication.translate("date_mode_widget", u"To", None))
        self.date_to_calendar_btn.setText("")
        self.date_difference_title_label.setText(QCoreApplication.translate("date_mode_widget", u"Difference", None))
        self.date_difference_label.setText(QCoreApplication.translate("date_mode_widget", u"Difference Date", None))
        self.all_days.setText("")
#if QT_CONFIG(tooltip)
        self.dare_substract_radioButton.setToolTip(QCoreApplication.translate("date_mode_widget", u"substract", None))
#endif // QT_CONFIG(tooltip)
        self.dare_substract_radioButton.setText(QCoreApplication.translate("date_mode_widget", u"Substract", None))
        self.date_years_label.setText(QCoreApplication.translate("date_mode_widget", u"Years", None))
        self.date_month_label.setText(QCoreApplication.translate("date_mode_widget", u"Months", None))
#if QT_CONFIG(tooltip)
        self.date_add_radioButton.setToolTip(QCoreApplication.translate("date_mode_widget", u"add", None))
#endif // QT_CONFIG(tooltip)
        self.date_add_radioButton.setText(QCoreApplication.translate("date_mode_widget", u"Add", None))
#if QT_CONFIG(tooltip)
        self.date_years_combo.setToolTip(QCoreApplication.translate("date_mode_widget", u"input years", None))
#endif // QT_CONFIG(tooltip)
        self.date_years_combo.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.date_month_combo.setToolTip(QCoreApplication.translate("date_mode_widget", u"input month", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.date_days_combo.setToolTip(QCoreApplication.translate("date_mode_widget", u"input days", None))
#endif // QT_CONFIG(tooltip)
        self.date_result_title_label.setText(QCoreApplication.translate("date_mode_widget", u"Date", None))
        self.date_days_label.setText(QCoreApplication.translate("date_mode_widget", u"Days", None))
        self.date_result_label.setText(QCoreApplication.translate("date_mode_widget", u"Final Date", None))
    # retranslateUi

