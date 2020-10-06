""" Qt based Pseudonymisation GUI
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtpseudonymise.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# skipping pylint because this was generated code.
# pyuic5 could use some improvement
# pylint: skip-file

from PyQt5 import QtCore, QtWidgets


class Ui_qtpseudo_main_window(object):
    def setupUi(self, qtpseudo_main_window):
        qtpseudo_main_window.setObjectName("qtpseudo_main_window")
        qtpseudo_main_window.resize(849, 482)
        self.central_widget = QtWidgets.QWidget(qtpseudo_main_window)
        self.central_widget.setObjectName("central_widget")
        self.group_box = QtWidgets.QGroupBox(self.central_widget)
        self.group_box.setGeometry(QtCore.QRect(20, 50, 761, 341))
        self.group_box.setTitle("")
        self.group_box.setObjectName("group_box")
        self.select_input_button = QtWidgets.QPushButton(self.group_box)
        self.select_input_button.setGeometry(QtCore.QRect(0, 30, 111, 25))
        self.select_input_button.setObjectName("select_input_button")
        self.plain_text_edit_input_files = QtWidgets.QPlainTextEdit(self.group_box)
        self.plain_text_edit_input_files.setGeometry(QtCore.QRect(0, 60, 731, 141))
        self.plain_text_edit_input_files.setObjectName("plain_text_edit_input_files")
        self.select_output_button = QtWidgets.QPushButton(self.group_box)
        self.select_output_button.setGeometry(QtCore.QRect(0, 220, 111, 25))
        self.select_output_button.setObjectName("select_output_button")
        self.text_edit_output_directory = QtWidgets.QTextEdit(self.group_box)
        self.text_edit_output_directory.setGeometry(QtCore.QRect(0, 250, 731, 31))
        self.text_edit_output_directory.setObjectName("text_edit_output_directory")
        self.pseudonymise_button = QtWidgets.QPushButton(self.group_box)
        self.pseudonymise_button.setGeometry(QtCore.QRect(250, 290, 177, 41))
        self.pseudonymise_button.setObjectName("pseudonymise_button")
        self.label_output_directory = QtWidgets.QLabel(self.group_box)
        self.label_output_directory.setGeometry(QtCore.QRect(250, 220, 121, 17))
        self.label_output_directory.setObjectName("label_output_directory")
        self.label_input_files = QtWidgets.QLabel(self.group_box)
        self.label_input_files.setGeometry(QtCore.QRect(220, 30, 161, 17))
        self.label_input_files.setObjectName("label_input_files")
        self.rb_input_directory_only = QtWidgets.QRadioButton(self.central_widget)
        self.rb_input_directory_only.setGeometry(QtCore.QRect(20, 10, 171, 23))
        self.rb_input_directory_only.setObjectName("rb_input_directory_only")
        self.check_box_disable_gender_keyword = QtWidgets.QCheckBox(self.central_widget)
        self.check_box_disable_gender_keyword.setGeometry(
            QtCore.QRect(220, 10, 151, 23)
        )
        self.check_box_disable_gender_keyword.setChecked(True)
        self.check_box_disable_gender_keyword.setObjectName(
            "check_box_disable_gender_keyword"
        )
        qtpseudo_main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(qtpseudo_main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 849, 22))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")
        qtpseudo_main_window.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(qtpseudo_main_window)
        self.status_bar.setObjectName("status_bar")
        qtpseudo_main_window.setStatusBar(self.status_bar)
        self.exit_select = QtWidgets.QAction(qtpseudo_main_window)
        self.exit_select.setObjectName("exit_select")
        self.menu_file.addAction(self.exit_select)
        self.menu_bar.addAction(self.menu_file.menuAction())

        self.retranslateUi(qtpseudo_main_window)
        QtCore.QMetaObject.connectSlotsByName(qtpseudo_main_window)

    def retranslateUi(self, qtpseudo_main_window):
        _translate = QtCore.QCoreApplication.translate
        qtpseudo_main_window.setWindowTitle(
            _translate("qtpseudo_main_window", "MainWindow")
        )
        self.select_input_button.setText(
            _translate("qtpseudo_main_window", "Select Input")
        )
        self.select_output_button.setText(
            _translate("qtpseudo_main_window", "Select Output")
        )
        self.pseudonymise_button.setText(
            _translate("qtpseudo_main_window", "Pseudonymise")
        )
        self.label_output_directory.setText(
            _translate("qtpseudo_main_window", "Output Directory")
        )
        self.label_input_files.setText(
            _translate("qtpseudo_main_window", "Input Files or Directory")
        )
        self.rb_input_directory_only.setText(
            _translate("qtpseudo_main_window", "Input Directory Only")
        )
        self.check_box_disable_gender_keyword.setText(
            _translate("qtpseudo_main_window", "Ignore PatientSex")
        )
        self.menu_file.setTitle(_translate("qtpseudo_main_window", "File"))
        self.exit_select.setText(_translate("qtpseudo_main_window", "Exit"))