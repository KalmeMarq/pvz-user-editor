# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SelectUserDialog(object):
    def setupUi(self, SelectUserDialog):
        if not SelectUserDialog.objectName():
            SelectUserDialog.setObjectName(u"SelectUserDialog")
        SelectUserDialog.resize(379, 362)
        self.verticalLayoutWidget = QWidget(SelectUserDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 361, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.userdata_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.userdata_lineedit.setObjectName(u"userdata_lineedit")

        self.horizontalLayout.addWidget(self.userdata_lineedit)

        self.browse_btn = QPushButton(self.verticalLayoutWidget)
        self.browse_btn.setObjectName(u"browse_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_btn.sizePolicy().hasHeightForWidth())
        self.browse_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.browse_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tool_layout = QHBoxLayout()
        self.tool_layout.setObjectName(u"tool_layout")
        self.add_btn = QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName(u"add_btn")

        self.tool_layout.addWidget(self.add_btn)

        self.del_btn = QPushButton(self.verticalLayoutWidget)
        self.del_btn.setObjectName(u"del_btn")
        self.del_btn.setEnabled(False)

        self.tool_layout.addWidget(self.del_btn)

        self.dup_btn = QPushButton(self.verticalLayoutWidget)
        self.dup_btn.setObjectName(u"dup_btn")
        self.dup_btn.setEnabled(False)

        self.tool_layout.addWidget(self.dup_btn)


        self.verticalLayout.addLayout(self.tool_layout)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sel_btn = QPushButton(self.verticalLayoutWidget)
        self.sel_btn.setObjectName(u"sel_btn")

        self.horizontalLayout_3.addWidget(self.sel_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.rel_btn = QPushButton(self.verticalLayoutWidget)
        self.rel_btn.setObjectName(u"rel_btn")

        self.horizontalLayout_3.addWidget(self.rel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(SelectUserDialog)

        QMetaObject.connectSlotsByName(SelectUserDialog)
    # setupUi

    def retranslateUi(self, SelectUserDialog):
        SelectUserDialog.setWindowTitle(QCoreApplication.translate("SelectUserDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SelectUserDialog", u"User data folder:", None))
        self.browse_btn.setText(QCoreApplication.translate("SelectUserDialog", u"Browse", None))
        self.add_btn.setText(QCoreApplication.translate("SelectUserDialog", u"Add", None))
        self.del_btn.setText(QCoreApplication.translate("SelectUserDialog", u"Delete", None))
        self.dup_btn.setText(QCoreApplication.translate("SelectUserDialog", u"Duplicate", None))
        self.sel_btn.setText(QCoreApplication.translate("SelectUserDialog", u"OK", None))
        self.rel_btn.setText(QCoreApplication.translate("SelectUserDialog", u"Reload", None))
    # retranslateUi

