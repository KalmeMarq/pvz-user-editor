# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.save = QPushButton(self.centralwidget)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)

        self.reload = QPushButton(self.centralwidget)
        self.reload.setObjectName(u"reload")

        self.horizontalLayout_2.addWidget(self.reload)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_16 = QGridLayout(self.tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.g_name = QLineEdit(self.tab)
        self.g_name.setObjectName(u"g_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.g_name.sizePolicy().hasHeightForWidth())
        self.g_name.setSizePolicy(sizePolicy2)
        self.g_name.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.g_name)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.g_level = QComboBox(self.tab)
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.addItem("")
        self.g_level.setObjectName(u"g_level")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.g_level.sizePolicy().hasHeightForWidth())
        self.g_level.setSizePolicy(sizePolicy3)
        self.g_level.setMaxVisibleItems(10)

        self.horizontalLayout_9.addWidget(self.g_level)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_22.addWidget(self.label_10)

        self.g_completed = QSpinBox(self.tab)
        self.g_completed.setObjectName(u"g_completed")
        self.g_completed.setMaximum(2147483647)

        self.horizontalLayout_22.addWidget(self.g_completed)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_22.addWidget(self.label_18)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_23.addWidget(self.label_8)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_23.addWidget(self.label_20)

        self.g_money = QSpinBox(self.tab)
        self.g_money.setObjectName(u"g_money")
        self.g_money.setMinimumSize(QSize(125, 0))
        self.g_money.setMaximum(999990)
        self.g_money.setSingleStep(10)
        self.g_money.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_23.addWidget(self.g_money)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.g_minigames_unlocked = QCheckBox(self.tab)
        self.g_minigames_unlocked.setObjectName(u"g_minigames_unlocked")

        self.verticalLayout.addWidget(self.g_minigames_unlocked)

        self.g_puzzle_unlocked = QCheckBox(self.tab)
        self.g_puzzle_unlocked.setObjectName(u"g_puzzle_unlocked")

        self.verticalLayout.addWidget(self.g_puzzle_unlocked)

        self.g_taco = QCheckBox(self.tab)
        self.g_taco.setObjectName(u"g_taco")

        self.verticalLayout.addWidget(self.g_taco)


        self.gridLayout_16.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_19 = QGridLayout(self.groupBox_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_24.addWidget(self.label_11)

        self.g_slots = QSpinBox(self.groupBox_7)
        self.g_slots.setObjectName(u"g_slots")
        self.g_slots.setMinimum(6)
        self.g_slots.setMaximum(10)

        self.horizontalLayout_24.addWidget(self.g_slots)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)

        self.g_roof_cleaner = QCheckBox(self.groupBox_7)
        self.g_roof_cleaner.setObjectName(u"g_roof_cleaner")

        self.horizontalLayout_25.addWidget(self.g_roof_cleaner)

        self.g_pool_cleaner = QCheckBox(self.groupBox_7)
        self.g_pool_cleaner.setObjectName(u"g_pool_cleaner")

        self.horizontalLayout_25.addWidget(self.g_pool_cleaner)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_66 = QLabel(self.groupBox_7)
        self.label_66.setObjectName(u"label_66")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy4)

        self.horizontalLayout_65.addWidget(self.label_66)

        self.g_rake_uses = QSpinBox(self.groupBox_7)
        self.g_rake_uses.setObjectName(u"g_rake_uses")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.g_rake_uses.sizePolicy().hasHeightForWidth())
        self.g_rake_uses.setSizePolicy(sizePolicy5)
        self.g_rake_uses.setMaximum(999999999)

        self.horizontalLayout_65.addWidget(self.g_rake_uses)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_65)

        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_17 = QGridLayout(self.groupBox_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.g_plants_8 = QCheckBox(self.groupBox_8)
        self.g_plants_8.setObjectName(u"g_plants_8")

        self.gridLayout_18.addWidget(self.g_plants_8, 2, 1, 1, 1)

        self.g_plants_7 = QCheckBox(self.groupBox_8)
        self.g_plants_7.setObjectName(u"g_plants_7")

        self.gridLayout_18.addWidget(self.g_plants_7, 2, 0, 1, 1)

        self.g_plants_3 = QCheckBox(self.groupBox_8)
        self.g_plants_3.setObjectName(u"g_plants_3")

        self.gridLayout_18.addWidget(self.g_plants_3, 0, 2, 1, 1)

        self.g_plants_4 = QCheckBox(self.groupBox_8)
        self.g_plants_4.setObjectName(u"g_plants_4")

        self.gridLayout_18.addWidget(self.g_plants_4, 1, 0, 1, 1)

        self.g_plants_5 = QCheckBox(self.groupBox_8)
        self.g_plants_5.setObjectName(u"g_plants_5")

        self.gridLayout_18.addWidget(self.g_plants_5, 1, 1, 1, 1)

        self.g_plants_1 = QCheckBox(self.groupBox_8)
        self.g_plants_1.setObjectName(u"g_plants_1")

        self.gridLayout_18.addWidget(self.g_plants_1, 0, 0, 1, 1)

        self.g_plants_2 = QCheckBox(self.groupBox_8)
        self.g_plants_2.setObjectName(u"g_plants_2")

        self.gridLayout_18.addWidget(self.g_plants_2, 0, 1, 1, 1)

        self.g_plants_10 = QCheckBox(self.groupBox_8)
        self.g_plants_10.setObjectName(u"g_plants_10")

        self.gridLayout_18.addWidget(self.g_plants_10, 3, 0, 1, 1)

        self.g_plants_6 = QCheckBox(self.groupBox_8)
        self.g_plants_6.setObjectName(u"g_plants_6")

        self.gridLayout_18.addWidget(self.g_plants_6, 1, 2, 1, 1)

        self.g_plants_9 = QCheckBox(self.groupBox_8)
        self.g_plants_9.setObjectName(u"g_plants_9")

        self.gridLayout_18.addWidget(self.g_plants_9, 2, 2, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_8)


        self.gridLayout_19.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_22 = QGridLayout(self.tab_2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_48 = QLabel(self.tab_2)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_9.addWidget(self.label_48)

        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_9.addWidget(self.listWidget)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.zg_add_plant = QPushButton(self.tab_2)
        self.zg_add_plant.setObjectName(u"zg_add_plant")

        self.horizontalLayout_45.addWidget(self.zg_add_plant)

        self.zg_del_plant = QPushButton(self.tab_2)
        self.zg_del_plant.setObjectName(u"zg_del_plant")
        self.zg_del_plant.setEnabled(False)

        self.horizontalLayout_45.addWidget(self.zg_del_plant)

        self.zg_dup_plant = QPushButton(self.tab_2)
        self.zg_dup_plant.setObjectName(u"zg_dup_plant")
        self.zg_dup_plant.setEnabled(False)

        self.horizontalLayout_45.addWidget(self.zg_dup_plant)


        self.verticalLayout_9.addLayout(self.horizontalLayout_45)

        self.groupBox_11 = QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setEnabled(False)
        self.gridLayout_23 = QGridLayout(self.groupBox_11)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_37 = QLabel(self.groupBox_11)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_37.addWidget(self.label_37)

        self.comboBox_2 = QComboBox(self.groupBox_11)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_37.addWidget(self.comboBox_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_38 = QLabel(self.groupBox_11)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_38.addWidget(self.label_38)

        self.comboBox_3 = QComboBox(self.groupBox_11)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_38.addWidget(self.comboBox_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_39 = QLabel(self.groupBox_11)
        self.label_39.setObjectName(u"label_39")
        sizePolicy4.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy4)

        self.horizontalLayout_39.addWidget(self.label_39)

        self.spinBox_25 = QSpinBox(self.groupBox_11)
        self.spinBox_25.setObjectName(u"spinBox_25")

        self.horizontalLayout_39.addWidget(self.spinBox_25)

        self.label_40 = QLabel(self.groupBox_11)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)

        self.horizontalLayout_39.addWidget(self.label_40)

        self.spinBox_26 = QSpinBox(self.groupBox_11)
        self.spinBox_26.setObjectName(u"spinBox_26")

        self.horizontalLayout_39.addWidget(self.spinBox_26)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_41 = QLabel(self.groupBox_11)
        self.label_41.setObjectName(u"label_41")
        sizePolicy4.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy4)

        self.horizontalLayout_40.addWidget(self.label_41)

        self.spinBox_27 = QSpinBox(self.groupBox_11)
        self.spinBox_27.setObjectName(u"spinBox_27")

        self.horizontalLayout_40.addWidget(self.spinBox_27)

        self.label_42 = QLabel(self.groupBox_11)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_40.addWidget(self.label_42)


        self.verticalLayout_8.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_45 = QLabel(self.groupBox_11)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_42.addWidget(self.label_45)

        self.dateEdit_4 = QDateEdit(self.groupBox_11)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setWrapping(False)
        self.dateEdit_4.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_4.setAccelerated(False)
        self.dateEdit_4.setProperty("showGroupSeparator", False)
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_42.addWidget(self.dateEdit_4)

        self.checkBox_88 = QCheckBox(self.groupBox_11)
        self.checkBox_88.setObjectName(u"checkBox_88")

        self.horizontalLayout_42.addWidget(self.checkBox_88)


        self.verticalLayout_8.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_43 = QLabel(self.groupBox_11)
        self.label_43.setObjectName(u"label_43")
        sizePolicy4.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy4)

        self.horizontalLayout_41.addWidget(self.label_43)

        self.spinBox_28 = QSpinBox(self.groupBox_11)
        self.spinBox_28.setObjectName(u"spinBox_28")

        self.horizontalLayout_41.addWidget(self.spinBox_28)

        self.label_44 = QLabel(self.groupBox_11)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_41.addWidget(self.label_44)


        self.verticalLayout_8.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_46 = QLabel(self.groupBox_11)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_43.addWidget(self.label_46)

        self.dateEdit_5 = QDateEdit(self.groupBox_11)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setWrapping(False)
        self.dateEdit_5.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit_5.setAccelerated(False)
        self.dateEdit_5.setProperty("showGroupSeparator", False)
        self.dateEdit_5.setCalendarPopup(True)
        self.dateEdit_5.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_43.addWidget(self.dateEdit_5)

        self.checkBox_89 = QCheckBox(self.groupBox_11)
        self.checkBox_89.setObjectName(u"checkBox_89")

        self.horizontalLayout_43.addWidget(self.checkBox_89)


        self.verticalLayout_8.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_47 = QLabel(self.groupBox_11)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_44.addWidget(self.label_47)

        self.comboBox_4 = QComboBox(self.groupBox_11)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_44.addWidget(self.comboBox_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_44)


        self.gridLayout_23.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_11)


        self.gridLayout_22.addLayout(self.verticalLayout_9, 0, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_26.addWidget(self.label_12)

        self.zg_mg1_date = QDateEdit(self.tab_2)
        self.zg_mg1_date.setObjectName(u"zg_mg1_date")
        self.zg_mg1_date.setEnabled(False)
        self.zg_mg1_date.setWrapping(False)
        self.zg_mg1_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.zg_mg1_date.setAccelerated(False)
        self.zg_mg1_date.setProperty("showGroupSeparator", False)
        self.zg_mg1_date.setCalendarPopup(True)
        self.zg_mg1_date.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_26.addWidget(self.zg_mg1_date)

        self.zg_mg1_never = QCheckBox(self.tab_2)
        self.zg_mg1_never.setObjectName(u"zg_mg1_never")
        self.zg_mg1_never.setChecked(True)

        self.horizontalLayout_26.addWidget(self.zg_mg1_never)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_27.addWidget(self.label_14)

        self.zg_mg2_date = QDateEdit(self.tab_2)
        self.zg_mg2_date.setObjectName(u"zg_mg2_date")
        self.zg_mg2_date.setEnabled(False)
        self.zg_mg2_date.setWrapping(False)
        self.zg_mg2_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.zg_mg2_date.setAccelerated(False)
        self.zg_mg2_date.setProperty("showGroupSeparator", False)
        self.zg_mg2_date.setCalendarPopup(True)
        self.zg_mg2_date.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_27.addWidget(self.zg_mg2_date)

        self.zg_mg2_never = QCheckBox(self.tab_2)
        self.zg_mg2_never.setObjectName(u"zg_mg2_never")
        self.zg_mg2_never.setChecked(True)

        self.horizontalLayout_27.addWidget(self.zg_mg2_never)


        self.verticalLayout_7.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_28.addWidget(self.label_16)

        self.zg_mg3_date = QDateEdit(self.tab_2)
        self.zg_mg3_date.setObjectName(u"zg_mg3_date")
        self.zg_mg3_date.setEnabled(False)
        self.zg_mg3_date.setWrapping(False)
        self.zg_mg3_date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.zg_mg3_date.setAccelerated(False)
        self.zg_mg3_date.setProperty("showGroupSeparator", False)
        self.zg_mg3_date.setCalendarPopup(True)
        self.zg_mg3_date.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_28.addWidget(self.zg_mg3_date)

        self.zg_mg3_never = QCheckBox(self.tab_2)
        self.zg_mg3_never.setObjectName(u"zg_mg3_never")
        self.zg_mg3_never.setChecked(True)

        self.horizontalLayout_28.addWidget(self.zg_mg3_never)


        self.verticalLayout_7.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.zg_golden_can = QCheckBox(self.tab_2)
        self.zg_golden_can.setObjectName(u"zg_golden_can")

        self.horizontalLayout_31.addWidget(self.zg_golden_can)

        self.zg_phonograph = QCheckBox(self.tab_2)
        self.zg_phonograph.setObjectName(u"zg_phonograph")

        self.horizontalLayout_31.addWidget(self.zg_phonograph)

        self.zg_glove = QCheckBox(self.tab_2)
        self.zg_glove.setObjectName(u"zg_glove")

        self.horizontalLayout_31.addWidget(self.zg_glove)


        self.verticalLayout_7.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_35 = QLabel(self.tab_2)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_34.addWidget(self.label_35)

        self.zg_fertilizer = QSpinBox(self.tab_2)
        self.zg_fertilizer.setObjectName(u"zg_fertilizer")
        self.zg_fertilizer.setEnabled(False)

        self.horizontalLayout_34.addWidget(self.zg_fertilizer)

        self.zg_fertilizer_np = QCheckBox(self.tab_2)
        self.zg_fertilizer_np.setObjectName(u"zg_fertilizer_np")
        self.zg_fertilizer_np.setChecked(True)

        self.horizontalLayout_34.addWidget(self.zg_fertilizer_np)


        self.verticalLayout_7.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_36 = QLabel(self.tab_2)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_35.addWidget(self.label_36)

        self.zg_bugspray = QSpinBox(self.tab_2)
        self.zg_bugspray.setObjectName(u"zg_bugspray")
        self.zg_bugspray.setEnabled(False)

        self.horizontalLayout_35.addWidget(self.zg_bugspray)

        self.zg_bugspray_np = QCheckBox(self.tab_2)
        self.zg_bugspray_np.setObjectName(u"zg_bugspray_np")
        self.zg_bugspray_np.setChecked(True)

        self.horizontalLayout_35.addWidget(self.zg_bugspray_np)


        self.verticalLayout_7.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.zg_mushroom_g = QCheckBox(self.tab_2)
        self.zg_mushroom_g.setObjectName(u"zg_mushroom_g")

        self.horizontalLayout_36.addWidget(self.zg_mushroom_g)

        self.zg_aquarium_g = QCheckBox(self.tab_2)
        self.zg_aquarium_g.setObjectName(u"zg_aquarium_g")

        self.horizontalLayout_36.addWidget(self.zg_aquarium_g)

        self.zg_wheelbarrow = QCheckBox(self.tab_2)
        self.zg_wheelbarrow.setObjectName(u"zg_wheelbarrow")

        self.horizontalLayout_36.addWidget(self.zg_wheelbarrow)


        self.verticalLayout_7.addLayout(self.horizontalLayout_36)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.zg_snail_purchased = QCheckBox(self.groupBox_10)
        self.zg_snail_purchased.setObjectName(u"zg_snail_purchased")

        self.verticalLayout_6.addWidget(self.zg_snail_purchased)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_22 = QLabel(self.groupBox_10)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_29.addWidget(self.label_22)

        self.zg_snail_lawoken = QDoubleSpinBox(self.groupBox_10)
        self.zg_snail_lawoken.setObjectName(u"zg_snail_lawoken")
        self.zg_snail_lawoken.setEnabled(False)
        self.zg_snail_lawoken.setDecimals(1)

        self.horizontalLayout_29.addWidget(self.zg_snail_lawoken)

        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_29.addWidget(self.label_24)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_30.addWidget(self.label_26)

        self.zg_snail_lchoco = QDoubleSpinBox(self.groupBox_10)
        self.zg_snail_lchoco.setObjectName(u"zg_snail_lchoco")
        self.zg_snail_lchoco.setEnabled(False)
        self.zg_snail_lchoco.setDecimals(1)

        self.horizontalLayout_30.addWidget(self.zg_snail_lchoco)

        self.label_28 = QLabel(self.groupBox_10)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_30.addWidget(self.label_28)

        self.zg_snail_lchoco_never = QCheckBox(self.groupBox_10)
        self.zg_snail_lchoco_never.setObjectName(u"zg_snail_lchoco_never")
        self.zg_snail_lchoco_never.setChecked(True)

        self.horizontalLayout_30.addWidget(self.zg_snail_lchoco_never)


        self.verticalLayout_6.addLayout(self.horizontalLayout_30)


        self.verticalLayout_7.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_21 = QGridLayout(self.groupBox_9)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.zg_food_purchased = QCheckBox(self.groupBox_9)
        self.zg_food_purchased.setObjectName(u"zg_food_purchased")

        self.gridLayout_20.addWidget(self.zg_food_purchased, 1, 0, 1, 1)

        self.zg_tree_purchased = QCheckBox(self.groupBox_9)
        self.zg_tree_purchased.setObjectName(u"zg_tree_purchased")

        self.gridLayout_20.addWidget(self.zg_tree_purchased, 0, 0, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_30 = QLabel(self.groupBox_9)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_32.addWidget(self.label_30)

        self.zg_tree_height = QSpinBox(self.groupBox_9)
        self.zg_tree_height.setObjectName(u"zg_tree_height")

        self.horizontalLayout_32.addWidget(self.zg_tree_height)

        self.label_32 = QLabel(self.groupBox_9)
        self.label_32.setObjectName(u"label_32")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy6)

        self.horizontalLayout_32.addWidget(self.label_32)


        self.gridLayout_20.addLayout(self.horizontalLayout_32, 0, 1, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_34 = QLabel(self.groupBox_9)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_33.addWidget(self.label_34)

        self.zg_tree_food = QSpinBox(self.groupBox_9)
        self.zg_tree_food.setObjectName(u"zg_tree_food")
        self.zg_tree_food.setEnabled(False)

        self.horizontalLayout_33.addWidget(self.zg_tree_food)


        self.gridLayout_20.addLayout(self.horizontalLayout_33, 1, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_9)


        self.gridLayout_22.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_15 = QGridLayout(self.tab_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_14.setVerticalSpacing(4)
        self.a_1 = QCheckBox(self.tab_3)
        self.a_1.setObjectName(u"a_1")

        self.gridLayout_14.addWidget(self.a_1, 0, 0, 1, 1)

        self.a_2 = QCheckBox(self.tab_3)
        self.a_2.setObjectName(u"a_2")

        self.gridLayout_14.addWidget(self.a_2, 0, 1, 1, 1)

        self.a_3 = QCheckBox(self.tab_3)
        self.a_3.setObjectName(u"a_3")

        self.gridLayout_14.addWidget(self.a_3, 1, 0, 1, 1)

        self.a_4 = QCheckBox(self.tab_3)
        self.a_4.setObjectName(u"a_4")

        self.gridLayout_14.addWidget(self.a_4, 1, 1, 1, 1)

        self.a_5 = QCheckBox(self.tab_3)
        self.a_5.setObjectName(u"a_5")

        self.gridLayout_14.addWidget(self.a_5, 2, 0, 1, 1)

        self.a_6 = QCheckBox(self.tab_3)
        self.a_6.setObjectName(u"a_6")

        self.gridLayout_14.addWidget(self.a_6, 2, 1, 1, 1)

        self.a_7 = QCheckBox(self.tab_3)
        self.a_7.setObjectName(u"a_7")

        self.gridLayout_14.addWidget(self.a_7, 3, 0, 1, 1)

        self.a_8 = QCheckBox(self.tab_3)
        self.a_8.setObjectName(u"a_8")

        self.gridLayout_14.addWidget(self.a_8, 3, 1, 1, 1)

        self.a_9 = QCheckBox(self.tab_3)
        self.a_9.setObjectName(u"a_9")

        self.gridLayout_14.addWidget(self.a_9, 4, 0, 1, 1)

        self.a_10 = QCheckBox(self.tab_3)
        self.a_10.setObjectName(u"a_10")

        self.gridLayout_14.addWidget(self.a_10, 4, 1, 1, 1)

        self.a_11 = QCheckBox(self.tab_3)
        self.a_11.setObjectName(u"a_11")

        self.gridLayout_14.addWidget(self.a_11, 5, 0, 1, 1)

        self.a_12 = QCheckBox(self.tab_3)
        self.a_12.setObjectName(u"a_12")

        self.gridLayout_14.addWidget(self.a_12, 5, 1, 1, 1)

        self.a_13 = QCheckBox(self.tab_3)
        self.a_13.setObjectName(u"a_13")

        self.gridLayout_14.addWidget(self.a_13, 6, 0, 1, 1)

        self.a_14 = QCheckBox(self.tab_3)
        self.a_14.setObjectName(u"a_14")

        self.gridLayout_14.addWidget(self.a_14, 6, 1, 1, 1)

        self.a_15 = QCheckBox(self.tab_3)
        self.a_15.setObjectName(u"a_15")

        self.gridLayout_14.addWidget(self.a_15, 7, 0, 1, 1)

        self.a_16 = QCheckBox(self.tab_3)
        self.a_16.setObjectName(u"a_16")

        self.gridLayout_14.addWidget(self.a_16, 7, 1, 1, 1)

        self.a_17 = QCheckBox(self.tab_3)
        self.a_17.setObjectName(u"a_17")

        self.gridLayout_14.addWidget(self.a_17, 8, 0, 1, 1)

        self.a_18 = QCheckBox(self.tab_3)
        self.a_18.setObjectName(u"a_18")

        self.gridLayout_14.addWidget(self.a_18, 8, 1, 1, 1)

        self.a_19 = QCheckBox(self.tab_3)
        self.a_19.setObjectName(u"a_19")

        self.gridLayout_14.addWidget(self.a_19, 9, 0, 1, 1)

        self.a_20 = QCheckBox(self.tab_3)
        self.a_20.setObjectName(u"a_20")

        self.gridLayout_14.addWidget(self.a_20, 9, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.a_all = QPushButton(self.tab_3)
        self.a_all.setObjectName(u"a_all")

        self.horizontalLayout_21.addWidget(self.a_all)

        self.a_invert = QPushButton(self.tab_3)
        self.a_invert.setObjectName(u"a_invert")

        self.horizontalLayout_21.addWidget(self.a_invert)

        self.a_none = QPushButton(self.tab_3)
        self.a_none.setObjectName(u"a_none")

        self.horizontalLayout_21.addWidget(self.a_none)


        self.verticalLayout_5.addLayout(self.horizontalLayout_21)


        self.gridLayout_15.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.c_surv_1 = QSpinBox(self.groupBox_4)
        self.c_surv_1.setObjectName(u"c_surv_1")
        self.c_surv_1.setMinimum(0)
        self.c_surv_1.setMaximum(5)

        self.horizontalLayout_5.addWidget(self.c_surv_1)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.c_surv_3 = QSpinBox(self.groupBox_4)
        self.c_surv_3.setObjectName(u"c_surv_3")
        self.c_surv_3.setMaximum(5)

        self.horizontalLayout_7.addWidget(self.c_surv_3)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 0, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.c_surv_2 = QSpinBox(self.groupBox_4)
        self.c_surv_2.setObjectName(u"c_surv_2")
        self.c_surv_2.setMaximum(5)

        self.horizontalLayout_6.addWidget(self.c_surv_2)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.c_surv_4 = QSpinBox(self.groupBox_4)
        self.c_surv_4.setObjectName(u"c_surv_4")
        self.c_surv_4.setMaximum(5)

        self.horizontalLayout_8.addWidget(self.c_surv_4)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 3, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.c_surv_5 = QSpinBox(self.groupBox_4)
        self.c_surv_5.setObjectName(u"c_surv_5")
        self.c_surv_5.setMaximum(5)

        self.horizontalLayout_10.addWidget(self.c_surv_5)


        self.gridLayout_8.addLayout(self.horizontalLayout_10, 0, 4, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(9, 5, -1, 5)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.c_survhard_1 = QSpinBox(self.groupBox_5)
        self.c_survhard_1.setObjectName(u"c_survhard_1")
        self.c_survhard_1.setMaximum(10)

        self.horizontalLayout_11.addWidget(self.c_survhard_1)


        self.gridLayout_10.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.c_survhard_3 = QSpinBox(self.groupBox_5)
        self.c_survhard_3.setObjectName(u"c_survhard_3")
        self.c_survhard_3.setMaximum(10)

        self.horizontalLayout_12.addWidget(self.c_survhard_3)


        self.gridLayout_10.addLayout(self.horizontalLayout_12, 0, 2, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.c_survhard_2 = QSpinBox(self.groupBox_5)
        self.c_survhard_2.setObjectName(u"c_survhard_2")
        self.c_survhard_2.setMaximum(10)

        self.horizontalLayout_13.addWidget(self.c_survhard_2)


        self.gridLayout_10.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.c_survhard_4 = QSpinBox(self.groupBox_5)
        self.c_survhard_4.setObjectName(u"c_survhard_4")
        self.c_survhard_4.setMaximum(10)

        self.horizontalLayout_14.addWidget(self.c_survhard_4)


        self.gridLayout_10.addLayout(self.horizontalLayout_14, 0, 3, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_15.addWidget(self.label_23)

        self.c_survhard_5 = QSpinBox(self.groupBox_5)
        self.c_survhard_5.setObjectName(u"c_survhard_5")
        self.c_survhard_5.setMaximum(10)

        self.horizontalLayout_15.addWidget(self.c_survhard_5)


        self.gridLayout_10.addLayout(self.horizontalLayout_15, 0, 4, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_5)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_17.addWidget(self.label_27)

        self.c_survend = QSpinBox(self.groupBox)
        self.c_survend.setObjectName(u"c_survend")
        self.c_survend.setMaximum(2147483647)

        self.horizontalLayout_17.addWidget(self.c_survend)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)


        self.gridLayout_7.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.c_mg_4 = QCheckBox(self.groupBox_2)
        self.c_mg_4.setObjectName(u"c_mg_4")

        self.gridLayout.addWidget(self.c_mg_4, 0, 3, 1, 1)

        self.c_mg_15 = QCheckBox(self.groupBox_2)
        self.c_mg_15.setObjectName(u"c_mg_15")

        self.gridLayout.addWidget(self.c_mg_15, 2, 4, 1, 1)

        self.c_mg_6 = QCheckBox(self.groupBox_2)
        self.c_mg_6.setObjectName(u"c_mg_6")

        self.gridLayout.addWidget(self.c_mg_6, 1, 0, 1, 1)

        self.c_mg_13 = QCheckBox(self.groupBox_2)
        self.c_mg_13.setObjectName(u"c_mg_13")

        self.gridLayout.addWidget(self.c_mg_13, 2, 2, 1, 1)

        self.c_mg_12 = QCheckBox(self.groupBox_2)
        self.c_mg_12.setObjectName(u"c_mg_12")

        self.gridLayout.addWidget(self.c_mg_12, 2, 1, 1, 1)

        self.c_mg_3 = QCheckBox(self.groupBox_2)
        self.c_mg_3.setObjectName(u"c_mg_3")

        self.gridLayout.addWidget(self.c_mg_3, 0, 2, 1, 1)

        self.c_mg_1 = QCheckBox(self.groupBox_2)
        self.c_mg_1.setObjectName(u"c_mg_1")

        self.gridLayout.addWidget(self.c_mg_1, 0, 0, 1, 1)

        self.c_mg_11 = QCheckBox(self.groupBox_2)
        self.c_mg_11.setObjectName(u"c_mg_11")

        self.gridLayout.addWidget(self.c_mg_11, 2, 0, 1, 1)

        self.c_mg_16 = QCheckBox(self.groupBox_2)
        self.c_mg_16.setObjectName(u"c_mg_16")

        self.gridLayout.addWidget(self.c_mg_16, 3, 0, 1, 1)

        self.c_mg_18 = QCheckBox(self.groupBox_2)
        self.c_mg_18.setObjectName(u"c_mg_18")

        self.gridLayout.addWidget(self.c_mg_18, 3, 2, 1, 1)

        self.c_mg_14 = QCheckBox(self.groupBox_2)
        self.c_mg_14.setObjectName(u"c_mg_14")

        self.gridLayout.addWidget(self.c_mg_14, 2, 3, 1, 1)

        self.c_mg_17 = QCheckBox(self.groupBox_2)
        self.c_mg_17.setObjectName(u"c_mg_17")

        self.gridLayout.addWidget(self.c_mg_17, 3, 1, 1, 1)

        self.c_mg_10 = QCheckBox(self.groupBox_2)
        self.c_mg_10.setObjectName(u"c_mg_10")

        self.gridLayout.addWidget(self.c_mg_10, 1, 4, 1, 1)

        self.c_mg_5 = QCheckBox(self.groupBox_2)
        self.c_mg_5.setObjectName(u"c_mg_5")

        self.gridLayout.addWidget(self.c_mg_5, 0, 4, 1, 1)

        self.c_mg_2 = QCheckBox(self.groupBox_2)
        self.c_mg_2.setObjectName(u"c_mg_2")

        self.gridLayout.addWidget(self.c_mg_2, 0, 1, 1, 1)

        self.c_mg_9 = QCheckBox(self.groupBox_2)
        self.c_mg_9.setObjectName(u"c_mg_9")

        self.gridLayout.addWidget(self.c_mg_9, 1, 3, 1, 1)

        self.c_mg_8 = QCheckBox(self.groupBox_2)
        self.c_mg_8.setObjectName(u"c_mg_8")

        self.gridLayout.addWidget(self.c_mg_8, 1, 2, 1, 1)

        self.c_mg_19 = QCheckBox(self.groupBox_2)
        self.c_mg_19.setObjectName(u"c_mg_19")

        self.gridLayout.addWidget(self.c_mg_19, 3, 3, 1, 1)

        self.c_mg_20 = QCheckBox(self.groupBox_2)
        self.c_mg_20.setObjectName(u"c_mg_20")

        self.gridLayout.addWidget(self.c_mg_20, 3, 4, 1, 1)

        self.c_mg_7 = QCheckBox(self.groupBox_2)
        self.c_mg_7.setObjectName(u"c_mg_7")

        self.gridLayout.addWidget(self.c_mg_7, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.c_pz_1 = QCheckBox(self.groupBox_3)
        self.c_pz_1.setObjectName(u"c_pz_1")

        self.gridLayout_5.addWidget(self.c_pz_1, 0, 0, 1, 1)

        self.c_pz_13 = QCheckBox(self.groupBox_3)
        self.c_pz_13.setObjectName(u"c_pz_13")

        self.gridLayout_5.addWidget(self.c_pz_13, 2, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.c_pz_10 = QSpinBox(self.groupBox_3)
        self.c_pz_10.setObjectName(u"c_pz_10")
        self.c_pz_10.setMaximum(2147483647)

        self.horizontalLayout_3.addWidget(self.c_pz_10)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 4, 1, 1)

        self.c_pz_4 = QCheckBox(self.groupBox_3)
        self.c_pz_4.setObjectName(u"c_pz_4")

        self.gridLayout_5.addWidget(self.c_pz_4, 0, 3, 1, 1)

        self.c_pz_7 = QCheckBox(self.groupBox_3)
        self.c_pz_7.setObjectName(u"c_pz_7")

        self.gridLayout_5.addWidget(self.c_pz_7, 1, 1, 1, 1)

        self.c_pz_2 = QCheckBox(self.groupBox_3)
        self.c_pz_2.setObjectName(u"c_pz_2")

        self.gridLayout_5.addWidget(self.c_pz_2, 0, 1, 1, 1)

        self.c_pz_6 = QCheckBox(self.groupBox_3)
        self.c_pz_6.setObjectName(u"c_pz_6")

        self.gridLayout_5.addWidget(self.c_pz_6, 1, 0, 1, 1)

        self.c_pz_14 = QCheckBox(self.groupBox_3)
        self.c_pz_14.setObjectName(u"c_pz_14")

        self.gridLayout_5.addWidget(self.c_pz_14, 2, 3, 1, 1)

        self.c_pz_9 = QCheckBox(self.groupBox_3)
        self.c_pz_9.setObjectName(u"c_pz_9")

        self.gridLayout_5.addWidget(self.c_pz_9, 1, 3, 1, 1)

        self.c_pz_3 = QCheckBox(self.groupBox_3)
        self.c_pz_3.setObjectName(u"c_pz_3")

        self.gridLayout_5.addWidget(self.c_pz_3, 0, 2, 1, 1)

        self.c_pz_12 = QCheckBox(self.groupBox_3)
        self.c_pz_12.setObjectName(u"c_pz_12")

        self.gridLayout_5.addWidget(self.c_pz_12, 2, 1, 1, 1)

        self.c_pz_8 = QCheckBox(self.groupBox_3)
        self.c_pz_8.setObjectName(u"c_pz_8")

        self.gridLayout_5.addWidget(self.c_pz_8, 1, 2, 1, 1)

        self.c_pz_11 = QCheckBox(self.groupBox_3)
        self.c_pz_11.setObjectName(u"c_pz_11")

        self.gridLayout_5.addWidget(self.c_pz_11, 2, 0, 1, 1)

        self.c_pz_5 = QCheckBox(self.groupBox_3)
        self.c_pz_5.setObjectName(u"c_pz_5")

        self.gridLayout_5.addWidget(self.c_pz_5, 0, 4, 1, 1)

        self.c_pz_15 = QCheckBox(self.groupBox_3)
        self.c_pz_15.setObjectName(u"c_pz_15")

        self.gridLayout_5.addWidget(self.c_pz_15, 2, 4, 1, 1)

        self.c_pz_16 = QCheckBox(self.groupBox_3)
        self.c_pz_16.setObjectName(u"c_pz_16")

        self.gridLayout_5.addWidget(self.c_pz_16, 3, 0, 1, 1)

        self.c_pz_17 = QCheckBox(self.groupBox_3)
        self.c_pz_17.setObjectName(u"c_pz_17")

        self.gridLayout_5.addWidget(self.c_pz_17, 3, 1, 1, 1)

        self.c_pz_18 = QCheckBox(self.groupBox_3)
        self.c_pz_18.setObjectName(u"c_pz_18")

        self.gridLayout_5.addWidget(self.c_pz_18, 3, 2, 1, 1)

        self.c_pz_19 = QCheckBox(self.groupBox_3)
        self.c_pz_19.setObjectName(u"c_pz_19")

        self.gridLayout_5.addWidget(self.c_pz_19, 3, 3, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.c_pz_20 = QSpinBox(self.groupBox_3)
        self.c_pz_20.setObjectName(u"c_pz_20")
        self.c_pz_20.setMaximum(2147483647)

        self.horizontalLayout_4.addWidget(self.c_pz_20)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 3, 4, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_11 = QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_13 = QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_33 = QLabel(self.groupBox_6)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_20.addWidget(self.label_33)

        self.l_survend_4 = QSpinBox(self.groupBox_6)
        self.l_survend_4.setObjectName(u"l_survend_4")
        self.l_survend_4.setMaximum(2147483647)

        self.horizontalLayout_20.addWidget(self.l_survend_4)


        self.gridLayout_12.addLayout(self.horizontalLayout_20, 0, 3, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_29 = QLabel(self.groupBox_6)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.l_survend_2 = QSpinBox(self.groupBox_6)
        self.l_survend_2.setObjectName(u"l_survend_2")
        self.l_survend_2.setMaximum(2147483647)

        self.horizontalLayout_18.addWidget(self.l_survend_2)


        self.gridLayout_12.addLayout(self.horizontalLayout_18, 0, 1, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_19.addWidget(self.label_31)

        self.l_survend_3 = QSpinBox(self.groupBox_6)
        self.l_survend_3.setObjectName(u"l_survend_3")
        self.l_survend_3.setMaximum(2147483647)

        self.horizontalLayout_19.addWidget(self.l_survend_3)


        self.gridLayout_12.addLayout(self.horizontalLayout_19, 0, 2, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_16.addWidget(self.label_25)

        self.l_survend_1 = QSpinBox(self.groupBox_6)
        self.l_survend_1.setObjectName(u"l_survend_1")
        self.l_survend_1.setMaximum(2147483647)

        self.horizontalLayout_16.addWidget(self.l_survend_1)


        self.gridLayout_12.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_6)

        self.groupBox_12 = QGroupBox(self.tab_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_26 = QGridLayout(self.groupBox_12)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.l_mg_1 = QCheckBox(self.groupBox_12)
        self.l_mg_1.setObjectName(u"l_mg_1")

        self.gridLayout_26.addWidget(self.l_mg_1, 0, 0, 1, 1)

        self.l_mg_2 = QCheckBox(self.groupBox_12)
        self.l_mg_2.setObjectName(u"l_mg_2")

        self.gridLayout_26.addWidget(self.l_mg_2, 0, 1, 1, 1)

        self.l_mg_3 = QCheckBox(self.groupBox_12)
        self.l_mg_3.setObjectName(u"l_mg_3")

        self.gridLayout_26.addWidget(self.l_mg_3, 0, 2, 1, 1)

        self.l_mg_4 = QCheckBox(self.groupBox_12)
        self.l_mg_4.setObjectName(u"l_mg_4")

        self.gridLayout_26.addWidget(self.l_mg_4, 0, 3, 1, 1)

        self.l_mg_5 = QCheckBox(self.groupBox_12)
        self.l_mg_5.setObjectName(u"l_mg_5")

        self.gridLayout_26.addWidget(self.l_mg_5, 0, 4, 1, 1)

        self.l_mg_6 = QCheckBox(self.groupBox_12)
        self.l_mg_6.setObjectName(u"l_mg_6")

        self.gridLayout_26.addWidget(self.l_mg_6, 1, 0, 1, 1)

        self.l_mg_7 = QCheckBox(self.groupBox_12)
        self.l_mg_7.setObjectName(u"l_mg_7")

        self.gridLayout_26.addWidget(self.l_mg_7, 1, 1, 1, 1)

        self.l_mg_8 = QCheckBox(self.groupBox_12)
        self.l_mg_8.setObjectName(u"l_mg_8")

        self.gridLayout_26.addWidget(self.l_mg_8, 1, 2, 1, 1)

        self.l_mg_9 = QCheckBox(self.groupBox_12)
        self.l_mg_9.setObjectName(u"l_mg_9")

        self.gridLayout_26.addWidget(self.l_mg_9, 1, 3, 1, 1)

        self.l_mg_10 = QCheckBox(self.groupBox_12)
        self.l_mg_10.setObjectName(u"l_mg_10")

        self.gridLayout_26.addWidget(self.l_mg_10, 1, 4, 1, 1)

        self.l_mg_11 = QCheckBox(self.groupBox_12)
        self.l_mg_11.setObjectName(u"l_mg_11")

        self.gridLayout_26.addWidget(self.l_mg_11, 2, 0, 1, 1)

        self.l_mg_12 = QCheckBox(self.groupBox_12)
        self.l_mg_12.setObjectName(u"l_mg_12")

        self.gridLayout_26.addWidget(self.l_mg_12, 2, 1, 1, 1)

        self.l_mg_13 = QCheckBox(self.groupBox_12)
        self.l_mg_13.setObjectName(u"l_mg_13")

        self.gridLayout_26.addWidget(self.l_mg_13, 2, 2, 1, 1)

        self.l_mg_14 = QCheckBox(self.groupBox_12)
        self.l_mg_14.setObjectName(u"l_mg_14")

        self.gridLayout_26.addWidget(self.l_mg_14, 2, 3, 1, 1)

        self.l_mg_15 = QCheckBox(self.groupBox_12)
        self.l_mg_15.setObjectName(u"l_mg_15")

        self.gridLayout_26.addWidget(self.l_mg_15, 2, 4, 1, 1)

        self.l_mg_16 = QCheckBox(self.groupBox_12)
        self.l_mg_16.setObjectName(u"l_mg_16")

        self.gridLayout_26.addWidget(self.l_mg_16, 3, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_25 = QGridLayout(self.tab_5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.z_license = QCheckBox(self.tab_5)
        self.z_license.setObjectName(u"z_license")

        self.horizontalLayout_46.addWidget(self.z_license)

        self.z_created_before = QCheckBox(self.tab_5)
        self.z_created_before.setObjectName(u"z_created_before")

        self.horizontalLayout_46.addWidget(self.z_created_before)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_7)


        self.gridLayout_25.addLayout(self.horizontalLayout_46, 0, 0, 1, 2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.listWidget_2 = QListWidget(self.tab_5)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy7)

        self.verticalLayout_10.addWidget(self.listWidget_2)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.pushButton_9 = QPushButton(self.tab_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy8)

        self.horizontalLayout_47.addWidget(self.pushButton_9)

        self.pushButton_11 = QPushButton(self.tab_5)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy8)

        self.horizontalLayout_47.addWidget(self.pushButton_11)

        self.pushButton_10 = QPushButton(self.tab_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy8)

        self.horizontalLayout_47.addWidget(self.pushButton_10)


        self.verticalLayout_10.addLayout(self.horizontalLayout_47)


        self.gridLayout_25.addLayout(self.verticalLayout_10, 1, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_5)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setEnabled(False)
        self.gridLayout_24 = QGridLayout(self.groupBox_13)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_55 = QLabel(self.groupBox_13)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_54.addWidget(self.label_55)

        self.comboBox_11 = QComboBox(self.groupBox_13)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.horizontalLayout_54.addWidget(self.comboBox_11)


        self.gridLayout_27.addLayout(self.horizontalLayout_54, 3, 1, 1, 1)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_51 = QLabel(self.groupBox_13)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_50.addWidget(self.label_51)

        self.comboBox_7 = QComboBox(self.groupBox_13)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_50.addWidget(self.comboBox_7)


        self.gridLayout_27.addLayout(self.horizontalLayout_50, 1, 1, 1, 1)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_64 = QLabel(self.groupBox_13)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_63.addWidget(self.label_64)

        self.comboBox_20 = QComboBox(self.groupBox_13)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.horizontalLayout_63.addWidget(self.comboBox_20)


        self.gridLayout_27.addLayout(self.horizontalLayout_63, 8, 0, 1, 1)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_53 = QLabel(self.groupBox_13)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_52.addWidget(self.label_53)

        self.comboBox_9 = QComboBox(self.groupBox_13)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_52.addWidget(self.comboBox_9)


        self.gridLayout_27.addLayout(self.horizontalLayout_52, 2, 1, 1, 1)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_56 = QLabel(self.groupBox_13)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_55.addWidget(self.label_56)

        self.comboBox_12 = QComboBox(self.groupBox_13)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.horizontalLayout_55.addWidget(self.comboBox_12)


        self.gridLayout_27.addLayout(self.horizontalLayout_55, 4, 0, 1, 1)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_61 = QLabel(self.groupBox_13)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_60.addWidget(self.label_61)

        self.comboBox_17 = QComboBox(self.groupBox_13)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.horizontalLayout_60.addWidget(self.comboBox_17)


        self.gridLayout_27.addLayout(self.horizontalLayout_60, 6, 1, 1, 1)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_57 = QLabel(self.groupBox_13)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_56.addWidget(self.label_57)

        self.comboBox_13 = QComboBox(self.groupBox_13)
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.horizontalLayout_56.addWidget(self.comboBox_13)


        self.gridLayout_27.addLayout(self.horizontalLayout_56, 4, 1, 1, 1)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_60 = QLabel(self.groupBox_13)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_59.addWidget(self.label_60)

        self.comboBox_16 = QComboBox(self.groupBox_13)
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.horizontalLayout_59.addWidget(self.comboBox_16)


        self.gridLayout_27.addLayout(self.horizontalLayout_59, 6, 0, 1, 1)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_49 = QLabel(self.groupBox_13)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_48.addWidget(self.label_49)

        self.comboBox_5 = QComboBox(self.groupBox_13)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_48.addWidget(self.comboBox_5)


        self.gridLayout_27.addLayout(self.horizontalLayout_48, 0, 0, 1, 1)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_59 = QLabel(self.groupBox_13)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_58.addWidget(self.label_59)

        self.comboBox_15 = QComboBox(self.groupBox_13)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.horizontalLayout_58.addWidget(self.comboBox_15)


        self.gridLayout_27.addLayout(self.horizontalLayout_58, 5, 1, 1, 1)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_50 = QLabel(self.groupBox_13)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_49.addWidget(self.label_50)

        self.comboBox_6 = QComboBox(self.groupBox_13)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_49.addWidget(self.comboBox_6)


        self.gridLayout_27.addLayout(self.horizontalLayout_49, 1, 0, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_54 = QLabel(self.groupBox_13)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_53.addWidget(self.label_54)

        self.comboBox_10 = QComboBox(self.groupBox_13)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_53.addWidget(self.comboBox_10)


        self.gridLayout_27.addLayout(self.horizontalLayout_53, 3, 0, 1, 1)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_63 = QLabel(self.groupBox_13)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_62.addWidget(self.label_63)

        self.comboBox_19 = QComboBox(self.groupBox_13)
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.horizontalLayout_62.addWidget(self.comboBox_19)


        self.gridLayout_27.addLayout(self.horizontalLayout_62, 7, 1, 1, 1)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_62 = QLabel(self.groupBox_13)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_61.addWidget(self.label_62)

        self.comboBox_18 = QComboBox(self.groupBox_13)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.horizontalLayout_61.addWidget(self.comboBox_18)


        self.gridLayout_27.addLayout(self.horizontalLayout_61, 7, 0, 1, 1)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_65 = QLabel(self.groupBox_13)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_64.addWidget(self.label_65)

        self.comboBox_21 = QComboBox(self.groupBox_13)
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.horizontalLayout_64.addWidget(self.comboBox_21)


        self.gridLayout_27.addLayout(self.horizontalLayout_64, 8, 1, 1, 1)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_58 = QLabel(self.groupBox_13)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_57.addWidget(self.label_58)

        self.comboBox_14 = QComboBox(self.groupBox_13)
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.horizontalLayout_57.addWidget(self.comboBox_14)


        self.gridLayout_27.addLayout(self.horizontalLayout_57, 5, 0, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_52 = QLabel(self.groupBox_13)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_51.addWidget(self.label_52)

        self.comboBox_8 = QComboBox(self.groupBox_13)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_51.addWidget(self.comboBox_8)


        self.gridLayout_27.addLayout(self.horizontalLayout_51, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_4, 9, 1, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_27, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_13, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Player name:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Adventure Mode Level:", None))
        self.g_level.setItemText(0, QCoreApplication.translate("MainWindow", u"1-1", None))
        self.g_level.setItemText(1, QCoreApplication.translate("MainWindow", u"1-2", None))
        self.g_level.setItemText(2, QCoreApplication.translate("MainWindow", u"1-3", None))
        self.g_level.setItemText(3, QCoreApplication.translate("MainWindow", u"1-4", None))
        self.g_level.setItemText(4, QCoreApplication.translate("MainWindow", u"1-5", None))
        self.g_level.setItemText(5, QCoreApplication.translate("MainWindow", u"1-6", None))
        self.g_level.setItemText(6, QCoreApplication.translate("MainWindow", u"1-7", None))
        self.g_level.setItemText(7, QCoreApplication.translate("MainWindow", u"1-8", None))
        self.g_level.setItemText(8, QCoreApplication.translate("MainWindow", u"1-9", None))
        self.g_level.setItemText(9, QCoreApplication.translate("MainWindow", u"1-10", None))
        self.g_level.setItemText(10, QCoreApplication.translate("MainWindow", u"2-1", None))
        self.g_level.setItemText(11, QCoreApplication.translate("MainWindow", u"2-2", None))
        self.g_level.setItemText(12, QCoreApplication.translate("MainWindow", u"2-3", None))
        self.g_level.setItemText(13, QCoreApplication.translate("MainWindow", u"2-4", None))
        self.g_level.setItemText(14, QCoreApplication.translate("MainWindow", u"2-5", None))
        self.g_level.setItemText(15, QCoreApplication.translate("MainWindow", u"2-6", None))
        self.g_level.setItemText(16, QCoreApplication.translate("MainWindow", u"2-7", None))
        self.g_level.setItemText(17, QCoreApplication.translate("MainWindow", u"2-8", None))
        self.g_level.setItemText(18, QCoreApplication.translate("MainWindow", u"2-9", None))
        self.g_level.setItemText(19, QCoreApplication.translate("MainWindow", u"2-10", None))
        self.g_level.setItemText(20, QCoreApplication.translate("MainWindow", u"3-1", None))
        self.g_level.setItemText(21, QCoreApplication.translate("MainWindow", u"3-2", None))
        self.g_level.setItemText(22, QCoreApplication.translate("MainWindow", u"3-3", None))
        self.g_level.setItemText(23, QCoreApplication.translate("MainWindow", u"3-4", None))
        self.g_level.setItemText(24, QCoreApplication.translate("MainWindow", u"3-5", None))
        self.g_level.setItemText(25, QCoreApplication.translate("MainWindow", u"3-6", None))
        self.g_level.setItemText(26, QCoreApplication.translate("MainWindow", u"3-7", None))
        self.g_level.setItemText(27, QCoreApplication.translate("MainWindow", u"3-8", None))
        self.g_level.setItemText(28, QCoreApplication.translate("MainWindow", u"3-9", None))
        self.g_level.setItemText(29, QCoreApplication.translate("MainWindow", u"3-10", None))
        self.g_level.setItemText(30, QCoreApplication.translate("MainWindow", u"4-1", None))
        self.g_level.setItemText(31, QCoreApplication.translate("MainWindow", u"4-2", None))
        self.g_level.setItemText(32, QCoreApplication.translate("MainWindow", u"4-3", None))
        self.g_level.setItemText(33, QCoreApplication.translate("MainWindow", u"4-4", None))
        self.g_level.setItemText(34, QCoreApplication.translate("MainWindow", u"4-5", None))
        self.g_level.setItemText(35, QCoreApplication.translate("MainWindow", u"4-6", None))
        self.g_level.setItemText(36, QCoreApplication.translate("MainWindow", u"4-7", None))
        self.g_level.setItemText(37, QCoreApplication.translate("MainWindow", u"4-8", None))
        self.g_level.setItemText(38, QCoreApplication.translate("MainWindow", u"4-9", None))
        self.g_level.setItemText(39, QCoreApplication.translate("MainWindow", u"4-10", None))
        self.g_level.setItemText(40, QCoreApplication.translate("MainWindow", u"5-1", None))
        self.g_level.setItemText(41, QCoreApplication.translate("MainWindow", u"5-2", None))
        self.g_level.setItemText(42, QCoreApplication.translate("MainWindow", u"5-3", None))
        self.g_level.setItemText(43, QCoreApplication.translate("MainWindow", u"5-4", None))
        self.g_level.setItemText(44, QCoreApplication.translate("MainWindow", u"5-5", None))
        self.g_level.setItemText(45, QCoreApplication.translate("MainWindow", u"5-6", None))
        self.g_level.setItemText(46, QCoreApplication.translate("MainWindow", u"5-7", None))
        self.g_level.setItemText(47, QCoreApplication.translate("MainWindow", u"5-8", None))
        self.g_level.setItemText(48, QCoreApplication.translate("MainWindow", u"5-9", None))
        self.g_level.setItemText(49, QCoreApplication.translate("MainWindow", u"5-10", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Completed Adventure Mode:", None))
        self.g_completed.setSuffix("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"times", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Money:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"$", None))
        self.g_money.setPrefix("")
        self.g_minigames_unlocked.setText(QCoreApplication.translate("MainWindow", u"Mini-games unlocked", None))
        self.g_puzzle_unlocked.setText(QCoreApplication.translate("MainWindow", u"Puzzle mode unlocked", None))
        self.g_taco.setText(QCoreApplication.translate("MainWindow", u"Has Magic Taco", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Shop", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number of slots", None))
        self.g_roof_cleaner.setText(QCoreApplication.translate("MainWindow", u"Roof Cleaner", None))
        self.g_pool_cleaner.setText(QCoreApplication.translate("MainWindow", u"Pool Cleaner", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Uses of rake:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Plants", None))
        self.g_plants_8.setText(QCoreApplication.translate("MainWindow", u"Cob cannon", None))
        self.g_plants_7.setText(QCoreApplication.translate("MainWindow", u"Water Melon", None))
        self.g_plants_3.setText(QCoreApplication.translate("MainWindow", u"Cattail", None))
        self.g_plants_4.setText(QCoreApplication.translate("MainWindow", u"Gloom-shroom", None))
        self.g_plants_5.setText(QCoreApplication.translate("MainWindow", u"Spikerock", None))
        self.g_plants_1.setText(QCoreApplication.translate("MainWindow", u"Gatling Pea", None))
        self.g_plants_2.setText(QCoreApplication.translate("MainWindow", u"Twin Sunflowers", None))
        self.g_plants_10.setText(QCoreApplication.translate("MainWindow", u"Wall-nut First Aid", None))
        self.g_plants_6.setText(QCoreApplication.translate("MainWindow", u"Gold Magnet", None))
        self.g_plants_9.setText(QCoreApplication.translate("MainWindow", u"The Imitater", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Plants:", None))
        self.zg_add_plant.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.zg_del_plant.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.zg_dup_plant.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Plant Properties", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Plant Type:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Peashooter", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Sunflower", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cherry Bomb", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Wall-nut", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Potate Mine", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Twin Sunflower", None))

        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Row:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Column:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Watered:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"times", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Last watered:", None))
        self.dateEdit_4.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dddd, MMMM dd, yyyy", None))
        self.checkBox_88.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Fertilized:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"times", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Last fertilized:", None))
        self.dateEdit_5.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dddd, MMMM dd, yyyy", None))
        self.checkBox_89.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Needs for happiness:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Nothing", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Phonograph", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Bug Spray", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Marigold 1 last purchased on:", None))
        self.zg_mg1_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dddd, MMMM dd, yyyy", None))
        self.zg_mg1_never.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Marigold 2 last purchased on:", None))
        self.zg_mg2_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dddd, MMMM dd, yyyy", None))
        self.zg_mg2_never.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Marigold 3 last purchased on:", None))
        self.zg_mg3_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dddd, MMMM dd, yyyy", None))
        self.zg_mg3_never.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.zg_golden_can.setText(QCoreApplication.translate("MainWindow", u"Golden Watering can", None))
        self.zg_phonograph.setText(QCoreApplication.translate("MainWindow", u"Phonograph", None))
        self.zg_glove.setText(QCoreApplication.translate("MainWindow", u"Gardening Glove", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Fertilizer:", None))
        self.zg_fertilizer_np.setText(QCoreApplication.translate("MainWindow", u"Never Purchased", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Bug spray:", None))
        self.zg_bugspray_np.setText(QCoreApplication.translate("MainWindow", u"Never Purchased", None))
        self.zg_mushroom_g.setText(QCoreApplication.translate("MainWindow", u"Mushroom Garden", None))
        self.zg_aquarium_g.setText(QCoreApplication.translate("MainWindow", u"Aquarium Garden", None))
        self.zg_wheelbarrow.setText(QCoreApplication.translate("MainWindow", u"Wheel barrow", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Stinky the Snail", None))
        self.zg_snail_purchased.setText(QCoreApplication.translate("MainWindow", u"Purchased", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Last awoken:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"minutes ago", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Last chocolate:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"minutes ago", None))
        self.zg_snail_lchoco_never.setText(QCoreApplication.translate("MainWindow", u"Never", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Tree of Wisdom", None))
        self.zg_food_purchased.setText(QCoreApplication.translate("MainWindow", u"Purchased food", None))
        self.zg_tree_purchased.setText(QCoreApplication.translate("MainWindow", u"Purchased tree", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"feet", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Food:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Zen Garden", None))
        self.a_1.setText(QCoreApplication.translate("MainWindow", u"Home Law Security", None))
        self.a_2.setText(QCoreApplication.translate("MainWindow", u"Nobel Peas Prize", None))
        self.a_3.setText(QCoreApplication.translate("MainWindow", u"Better Off Dead", None))
        self.a_4.setText(QCoreApplication.translate("MainWindow", u"China Shop", None))
        self.a_5.setText(QCoreApplication.translate("MainWindow", u"SPUDOW!!", None))
        self.a_6.setText(QCoreApplication.translate("MainWindow", u"Explodonator", None))
        self.a_7.setText(QCoreApplication.translate("MainWindow", u"Morticulturalist", None))
        self.a_8.setText(QCoreApplication.translate("MainWindow", u"Don't Pea in the Pool", None))
        self.a_9.setText(QCoreApplication.translate("MainWindow", u"Roll Some Heads", None))
        self.a_10.setText(QCoreApplication.translate("MainWindow", u"Grounded", None))
        self.a_11.setText(QCoreApplication.translate("MainWindow", u"Zombologist", None))
        self.a_12.setText(QCoreApplication.translate("MainWindow", u"Penny Pitcher", None))
        self.a_13.setText(QCoreApplication.translate("MainWindow", u"Sunny Days", None))
        self.a_14.setText(QCoreApplication.translate("MainWindow", u"Popcorn Party", None))
        self.a_15.setText(QCoreApplication.translate("MainWindow", u"Good Morning", None))
        self.a_16.setText(QCoreApplication.translate("MainWindow", u"No Fungus Among Us", None))
        self.a_17.setText(QCoreApplication.translate("MainWindow", u"Beyond the Grave", None))
        self.a_18.setText(QCoreApplication.translate("MainWindow", u"Immortal", None))
        self.a_19.setText(QCoreApplication.translate("MainWindow", u"Towering Wisdom", None))
        self.a_20.setText(QCoreApplication.translate("MainWindow", u"Mustache Mode", None))
        self.a_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.a_invert.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.a_none.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Achievements", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Survivals", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.c_surv_1.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pool", None))
        self.c_surv_3.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Night", None))
        self.c_surv_2.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fog", None))
        self.c_surv_4.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Roof", None))
        self.c_surv_5.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.c_survhard_1.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Pool", None))
        self.c_survhard_3.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Night", None))
        self.c_survhard_2.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Fog", None))
        self.c_survhard_4.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Roof", None))
        self.c_survhard_5.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Survival Endless:", None))
        self.c_survend.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Mini-games", None))
        self.c_mg_4.setText(QCoreApplication.translate("MainWindow", u"It's Raining Seeds", None))
        self.c_mg_15.setText(QCoreApplication.translate("MainWindow", u"Whack A Zombie", None))
        self.c_mg_6.setText(QCoreApplication.translate("MainWindow", u"Invisi-ghoul", None))
        self.c_mg_13.setText(QCoreApplication.translate("MainWindow", u"Bobsled Bonanza", None))
        self.c_mg_12.setText(QCoreApplication.translate("MainWindow", u"Column Like You See' Em", None))
        self.c_mg_3.setText(QCoreApplication.translate("MainWindow", u"Slot Machine", None))
        self.c_mg_1.setText(QCoreApplication.translate("MainWindow", u"ZomBotany", None))
        self.c_mg_11.setText(QCoreApplication.translate("MainWindow", u"Portal Combat", None))
        self.c_mg_16.setText(QCoreApplication.translate("MainWindow", u"Last Stand", None))
        self.c_mg_18.setText(QCoreApplication.translate("MainWindow", u"Wall-nut Bowling 2", None))
        self.c_mg_14.setText(QCoreApplication.translate("MainWindow", u"Zombie Nimble Zombie Quick", None))
        self.c_mg_17.setText(QCoreApplication.translate("MainWindow", u"ZomBotany 2", None))
        self.c_mg_10.setText(QCoreApplication.translate("MainWindow", u"Big Trouble Little Zombie", None))
        self.c_mg_5.setText(QCoreApplication.translate("MainWindow", u"Beghouled", None))
        self.c_mg_2.setText(QCoreApplication.translate("MainWindow", u"Wall-nut Bowling", None))
        self.c_mg_9.setText(QCoreApplication.translate("MainWindow", u"Beghouled Twist", None))
        self.c_mg_8.setText(QCoreApplication.translate("MainWindow", u"Zombiquarium", None))
        self.c_mg_19.setText(QCoreApplication.translate("MainWindow", u"Pogo Party", None))
        self.c_mg_20.setText(QCoreApplication.translate("MainWindow", u"Dr. Zomboss' Revenge", None))
        self.c_mg_7.setText(QCoreApplication.translate("MainWindow", u"Seeing Stars", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Puzzles", None))
        self.c_pz_1.setText(QCoreApplication.translate("MainWindow", u"Vasebreaker", None))
        self.c_pz_13.setText(QCoreApplication.translate("MainWindow", u"Can You Dig it?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vasebreaker Endless Streak Length", None))
        self.c_pz_4.setText(QCoreApplication.translate("MainWindow", u"Chain Reaction", None))
        self.c_pz_7.setText(QCoreApplication.translate("MainWindow", u"Hokey Pokey", None))
        self.c_pz_2.setText(QCoreApplication.translate("MainWindow", u"To The Left", None))
        self.c_pz_6.setText(QCoreApplication.translate("MainWindow", u"Scary Potter", None))
        self.c_pz_14.setText(QCoreApplication.translate("MainWindow", u"Totally Nuts", None))
        self.c_pz_9.setText(QCoreApplication.translate("MainWindow", u"Ace of Vases", None))
        self.c_pz_3.setText(QCoreApplication.translate("MainWindow", u"Third Vase", None))
        self.c_pz_12.setText(QCoreApplication.translate("MainWindow", u"I, Zombie Too", None))
        self.c_pz_8.setText(QCoreApplication.translate("MainWindow", u"Another Chain Reaction", None))
        self.c_pz_11.setText(QCoreApplication.translate("MainWindow", u"I, Zombie", None))
        self.c_pz_5.setText(QCoreApplication.translate("MainWindow", u"M is for Metal", None))
        self.c_pz_15.setText(QCoreApplication.translate("MainWindow", u"Dead Zeppelin", None))
        self.c_pz_16.setText(QCoreApplication.translate("MainWindow", u"Me Smash!", None))
        self.c_pz_17.setText(QCoreApplication.translate("MainWindow", u"ZomBoogie", None))
        self.c_pz_18.setText(QCoreApplication.translate("MainWindow", u"Three Hit Wonder", None))
        self.c_pz_19.setText(QCoreApplication.translate("MainWindow", u"All your brainz r belong to us", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"I, Zombie Endless Streak Length", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Challenges", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Survival Endless", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Roof", None))
        self.l_survend_4.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Night", None))
        self.l_survend_2.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Fog", None))
        self.l_survend_3.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Day", None))
        self.l_survend_1.setSuffix(QCoreApplication.translate("MainWindow", u" flags", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Mini-games", None))
        self.l_mg_1.setText(QCoreApplication.translate("MainWindow", u"Art Challenge Wall-nut", None))
        self.l_mg_2.setText(QCoreApplication.translate("MainWindow", u"Sunny Day", None))
        self.l_mg_3.setText(QCoreApplication.translate("MainWindow", u"Unsodded", None))
        self.l_mg_4.setText(QCoreApplication.translate("MainWindow", u"Buy Time", None))
        self.l_mg_5.setText(QCoreApplication.translate("MainWindow", u"Art Challenge Sunflower", None))
        self.l_mg_6.setText(QCoreApplication.translate("MainWindow", u"Air Raid", None))
        self.l_mg_7.setText(QCoreApplication.translate("MainWindow", u"Ice Level", None))
        self.l_mg_8.setText(QCoreApplication.translate("MainWindow", u"Zen Garden", None))
        self.l_mg_9.setText(QCoreApplication.translate("MainWindow", u"High Gravity", None))
        self.l_mg_10.setText(QCoreApplication.translate("MainWindow", u"Grave Danger", None))
        self.l_mg_11.setText(QCoreApplication.translate("MainWindow", u"Can You Dig It?", None))
        self.l_mg_12.setText(QCoreApplication.translate("MainWindow", u"Dark Stormy Night", None))
        self.l_mg_13.setText(QCoreApplication.translate("MainWindow", u"Bungee Blitz", None))
        self.l_mg_14.setText(QCoreApplication.translate("MainWindow", u"Intro", None))
        self.l_mg_15.setText(QCoreApplication.translate("MainWindow", u"Tree of Wisdom", None))
        self.l_mg_16.setText(QCoreApplication.translate("MainWindow", u"Upsell", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Limbo", None))
        self.z_license.setText(QCoreApplication.translate("MainWindow", u"Accepted Zombatar License", None))
        self.z_created_before.setText(QCoreApplication.translate("MainWindow", u"Has created at least one Zombatar before", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Zombatar Properties", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Accessories color:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Clothes color:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Backdrop type:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Tidbits color:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Facial hair type:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Eyewear color:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Facial hair color:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Eyewear type:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Skin color:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Hair color:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Clothes type:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Accessories type:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Hat color:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Hat type:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Backdrop color:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Hair type:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Tidbits type:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Zombatars", None))
    # retranslateUi

