# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/UGMMain.ui'
#
# Created: Wed Feb 17 18:10:29 2010
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_UGMMainWidget(object):
    def setupUi(self, UGMMainWidget):
        UGMMainWidget.setObjectName("UGMMainWidget")
        UGMMainWidget.resize(400, 445)
        UGMMainWidget.setMinimumSize(QtCore.QSize(400, 208))
        UGMMainWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        UGMMainWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.mainVLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.mainVLayout.setSpacing(0)
        self.mainVLayout.setMargin(2)
        self.mainVLayout.setObjectName("mainVLayout")
        self.toolbarFrame = QtGui.QFrame(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbarFrame.sizePolicy().hasHeightForWidth())
        self.toolbarFrame.setSizePolicy(sizePolicy)
        self.toolbarFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.toolbarFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolbarFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.toolbarFrame.setLineWidth(1)
        self.toolbarFrame.setObjectName("toolbarFrame")
        self.toolbarHLayout = QtGui.QHBoxLayout(self.toolbarFrame)
        self.toolbarHLayout.setSpacing(2)
        self.toolbarHLayout.setMargin(2)
        self.toolbarHLayout.setObjectName("toolbarHLayout")
        self.sendToUgmButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendToUgmButton.sizePolicy().hasHeightForWidth())
        self.sendToUgmButton.setSizePolicy(sizePolicy)
        self.sendToUgmButton.setMaximumSize(QtCore.QSize(40, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/send_to_ugm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendToUgmButton.setIcon(icon)
        self.sendToUgmButton.setIconSize(QtCore.QSize(32, 32))
        self.sendToUgmButton.setAutoRaise(False)
        self.sendToUgmButton.setArrowType(QtCore.Qt.NoArrow)
        self.sendToUgmButton.setObjectName("sendToUgmButton")
        self.toolbarHLayout.addWidget(self.sendToUgmButton)
        self.loadButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMaximumSize(QtCore.QSize(40, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/load"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.loadButton.setIcon(icon1)
        self.loadButton.setIconSize(QtCore.QSize(32, 32))
        self.loadButton.setAutoRaise(False)
        self.loadButton.setArrowType(QtCore.Qt.NoArrow)
        self.loadButton.setObjectName("loadButton")
        self.toolbarHLayout.addWidget(self.loadButton)
        self.saveButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMaximumSize(QtCore.QSize(40, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/save"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QtCore.QSize(32, 32))
        self.saveButton.setAutoRaise(False)
        self.saveButton.setArrowType(QtCore.Qt.NoArrow)
        self.saveButton.setObjectName("saveButton")
        self.toolbarHLayout.addWidget(self.saveButton)
        self.saveAsButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveAsButton.sizePolicy().hasHeightForWidth())
        self.saveAsButton.setSizePolicy(sizePolicy)
        self.saveAsButton.setMaximumSize(QtCore.QSize(40, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons/save_as"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.saveAsButton.setIcon(icon3)
        self.saveAsButton.setIconSize(QtCore.QSize(32, 32))
        self.saveAsButton.setAutoRaise(False)
        self.saveAsButton.setArrowType(QtCore.Qt.NoArrow)
        self.saveAsButton.setObjectName("saveAsButton")
        self.toolbarHLayout.addWidget(self.saveAsButton)
        spacerItem = QtGui.QSpacerItem(8, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolbarHLayout.addItem(spacerItem)
        self.addButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMaximumSize(QtCore.QSize(36, 36))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons/add"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addButton.setIcon(icon4)
        self.addButton.setIconSize(QtCore.QSize(32, 32))
        self.addButton.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.addButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.addButton.setAutoRaise(False)
        self.addButton.setArrowType(QtCore.Qt.NoArrow)
        self.addButton.setObjectName("addButton")
        self.toolbarHLayout.addWidget(self.addButton)
        spacerItem1 = QtGui.QSpacerItem(4, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolbarHLayout.addItem(spacerItem1)
        self.addRectangleButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRectangleButton.sizePolicy().hasHeightForWidth())
        self.addRectangleButton.setSizePolicy(sizePolicy)
        self.addRectangleButton.setMaximumSize(QtCore.QSize(36, 36))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/buttons/add_rectangle"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addRectangleButton.setIcon(icon5)
        self.addRectangleButton.setIconSize(QtCore.QSize(32, 32))
        self.addRectangleButton.setAutoRaise(False)
        self.addRectangleButton.setArrowType(QtCore.Qt.NoArrow)
        self.addRectangleButton.setObjectName("addRectangleButton")
        self.toolbarHLayout.addWidget(self.addRectangleButton)
        self.addImageButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addImageButton.sizePolicy().hasHeightForWidth())
        self.addImageButton.setSizePolicy(sizePolicy)
        self.addImageButton.setMaximumSize(QtCore.QSize(36, 36))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/buttons/add_image"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addImageButton.setIcon(icon6)
        self.addImageButton.setIconSize(QtCore.QSize(32, 32))
        self.addImageButton.setAutoRaise(False)
        self.addImageButton.setArrowType(QtCore.Qt.NoArrow)
        self.addImageButton.setObjectName("addImageButton")
        self.toolbarHLayout.addWidget(self.addImageButton)
        self.addTextButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTextButton.sizePolicy().hasHeightForWidth())
        self.addTextButton.setSizePolicy(sizePolicy)
        self.addTextButton.setMaximumSize(QtCore.QSize(36, 36))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/buttons/add_text"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addTextButton.setIcon(icon7)
        self.addTextButton.setIconSize(QtCore.QSize(32, 32))
        self.addTextButton.setAutoRaise(False)
        self.addTextButton.setArrowType(QtCore.Qt.NoArrow)
        self.addTextButton.setObjectName("addTextButton")
        self.toolbarHLayout.addWidget(self.addTextButton)
        spacerItem2 = QtGui.QSpacerItem(8, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.toolbarHLayout.addItem(spacerItem2)
        self.removeButton = QtGui.QToolButton(self.toolbarFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setMaximumSize(QtCore.QSize(36, 36))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/buttons/remove"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.removeButton.setIcon(icon8)
        self.removeButton.setIconSize(QtCore.QSize(32, 32))
        self.removeButton.setAutoRaise(False)
        self.removeButton.setArrowType(QtCore.Qt.NoArrow)
        self.removeButton.setObjectName("removeButton")
        self.toolbarHLayout.addWidget(self.removeButton)
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.toolbarHLayout.addItem(spacerItem3)
        self.mainVLayout.addWidget(self.toolbarFrame)
        self.areasFrame = QtGui.QFrame(self.dockWidgetContents)
        self.areasFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.areasFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.areasFrame.setLineWidth(0)
        self.areasFrame.setObjectName("areasFrame")
        self.areasVLayout = QtGui.QVBoxLayout(self.areasFrame)
        self.areasVLayout.setSpacing(2)
        self.areasVLayout.setMargin(2)
        self.areasVLayout.setObjectName("areasVLayout")
        self.propertyList = QtGui.QTreeView(self.areasFrame)
        self.propertyList.setMinimumSize(QtCore.QSize(350, 0))
        self.propertyList.setAlternatingRowColors(True)
        self.propertyList.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.propertyList.setIndentation(12)
        self.propertyList.setRootIsDecorated(True)
        self.propertyList.setUniformRowHeights(True)
        self.propertyList.setAnimated(True)
        self.propertyList.setAllColumnsShowFocus(True)
        self.propertyList.setHeaderHidden(True)
        self.propertyList.setObjectName("propertyList")
        self.propertyList.header().setVisible(False)
        self.areasVLayout.addWidget(self.propertyList)
        self.mainVLayout.addWidget(self.areasFrame)
        UGMMainWidget.setWidget(self.dockWidgetContents)
        self.actionSave = QtGui.QAction(UGMMainWidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/buttons/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd = QtGui.QAction(UGMMainWidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/buttons/add"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon10)
        self.actionAdd.setObjectName("actionAdd")
        self.actionRemove = QtGui.QAction(UGMMainWidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/buttons/remove"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon11)
        self.actionRemove.setObjectName("actionRemove")
        self.actionAddRectangle = QtGui.QAction(UGMMainWidget)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/buttons/add_rectangle"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddRectangle.setIcon(icon12)
        self.actionAddRectangle.setObjectName("actionAddRectangle")
        self.actionAddImage = QtGui.QAction(UGMMainWidget)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/buttons/add_image"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddImage.setIcon(icon13)
        self.actionAddImage.setObjectName("actionAddImage")
        self.actionAddText = QtGui.QAction(UGMMainWidget)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/buttons/add_text"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddText.setIcon(icon14)
        self.actionAddText.setObjectName("actionAddText")
        self.actionSendToUgm = QtGui.QAction(UGMMainWidget)
        self.actionSendToUgm.setIcon(icon)
        self.actionSendToUgm.setObjectName("actionSendToUgm")
        self.actionSaveAs = QtGui.QAction(UGMMainWidget)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/buttons/save_as"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon15)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionLoad = QtGui.QAction(UGMMainWidget)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/buttons/load"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon16)
        self.actionLoad.setObjectName("actionLoad")

        self.retranslateUi(UGMMainWidget)
        QtCore.QMetaObject.connectSlotsByName(UGMMainWidget)
        UGMMainWidget.setTabOrder(self.propertyList, self.addButton)
        UGMMainWidget.setTabOrder(self.addButton, self.addRectangleButton)

    def retranslateUi(self, UGMMainWidget):
        UGMMainWidget.setWindowTitle(QtGui.QApplication.translate("UGMMainWidget", "UGM Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.sendToUgmButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.addRectangleButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.addImageButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.addTextButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("UGMMainWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("UGMMainWidget", "Zapisz", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Zapisz", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setText(QtGui.QApplication.translate("UGMMainWidget", "Dodaj", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Dodaj pole", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setText(QtGui.QApplication.translate("UGMMainWidget", "Usuń", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Usuń aktualnie zaznaczony element", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddRectangle.setText(QtGui.QApplication.translate("UGMMainWidget", "Dodaj prostokąt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddRectangle.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Dodaj prostokąt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddRectangle.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddImage.setText(QtGui.QApplication.translate("UGMMainWidget", "Dodaj obrazek", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddImage.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Dodaj obrazek", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddImage.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddText.setText(QtGui.QApplication.translate("UGMMainWidget", "Dodaj tekst", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddText.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Dodaj tekst", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddText.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendToUgm.setText(QtGui.QApplication.translate("UGMMainWidget", "Wyślij do UGMa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendToUgm.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Wyślij aktualną konfigurację do UGMa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSendToUgm.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("UGMMainWidget", "Zapisz jako", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Zapisz jako", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("UGMMainWidget", "Wczytaj", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setToolTip(QtGui.QApplication.translate("UGMMainWidget", "Wczytaj konfigurację z pliku", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setShortcut(QtGui.QApplication.translate("UGMMainWidget", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc