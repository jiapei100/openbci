# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obci_window.ui'
#
# Created: Fri Aug  8 22:19:07 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OBCILauncher(object):
    def setupUi(self, OBCILauncher):
        OBCILauncher.setObjectName(_fromUtf8("OBCILauncher"))
        OBCILauncher.resize(716, 606)
        OBCILauncher.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        OBCILauncher.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(OBCILauncher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QtCore.QSize(40, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scenarios = QtGui.QTreeWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.scenarios.sizePolicy().hasHeightForWidth())
        self.scenarios.setSizePolicy(sizePolicy)
        self.scenarios.setObjectName(_fromUtf8("scenarios"))
        self.scenarios.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_4.addWidget(self.scenarios)
        self.store_checkBox = QtGui.QCheckBox(self.groupBox)
        self.store_checkBox.setObjectName(_fromUtf8("store_checkBox"))
        self.verticalLayout_4.addWidget(self.store_checkBox)
        self.store_container = QtGui.QWidget(self.groupBox)
        self.store_container.setObjectName(_fromUtf8("store_container"))
        self.verticalLayout = QtGui.QVBoxLayout(self.store_container)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setSpacing(3)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_7 = QtGui.QLabel(self.store_container)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.store_container)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.store_file = QtGui.QLineEdit(self.store_container)
        self.store_file.setObjectName(_fromUtf8("store_file"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.store_file)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.store_dir = QtGui.QLineEdit(self.store_container)
        self.store_dir.setObjectName(_fromUtf8("store_dir"))
        self.horizontalLayout_7.addWidget(self.store_dir)
        self.store_dir_chooser = QtGui.QToolButton(self.store_container)
        self.store_dir_chooser.setObjectName(_fromUtf8("store_dir_chooser"))
        self.horizontalLayout_7.addWidget(self.store_dir_chooser)
        self.formLayout_4.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.store_ts_checkBox = QtGui.QCheckBox(self.store_container)
        self.store_ts_checkBox.setToolTip(_fromUtf8(""))
        self.store_ts_checkBox.setStatusTip(_fromUtf8(""))
        self.store_ts_checkBox.setWhatsThis(_fromUtf8(""))
        self.store_ts_checkBox.setChecked(True)
        self.store_ts_checkBox.setObjectName(_fromUtf8("store_ts_checkBox"))
        self.verticalLayout.addWidget(self.store_ts_checkBox)
        self.store_local_checkBox = QtGui.QCheckBox(self.store_container)
        self.store_local_checkBox.setEnabled(False)
        self.store_local_checkBox.setCheckable(False)
        self.store_local_checkBox.setChecked(False)
        self.store_local_checkBox.setObjectName(_fromUtf8("store_local_checkBox"))
        self.verticalLayout.addWidget(self.store_local_checkBox)
        self.verticalLayout_4.addWidget(self.store_container)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontalLayout.addWidget(self.stop_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.parameters_of = QtGui.QGroupBox(self.splitter)
        self.parameters_of.setMinimumSize(QtCore.QSize(0, 0))
        self.parameters_of.setObjectName(_fromUtf8("parameters_of"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.parameters_of)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scenarioTab = QtGui.QTabWidget(self.parameters_of)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scenarioTab.sizePolicy().hasHeightForWidth())
        self.scenarioTab.setSizePolicy(sizePolicy)
        self.scenarioTab.setObjectName(_fromUtf8("scenarioTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.info = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setMinimumSize(QtCore.QSize(0, 0))
        self.info.setWordWrap(True)
        self.info.setIndent(-1)
        self.info.setOpenExternalLinks(True)
        self.info.setObjectName(_fromUtf8("info"))
        self.verticalLayout_5.addWidget(self.info)
        self.parameters = QtGui.QTreeWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameters.sizePolicy().hasHeightForWidth())
        self.parameters.setSizePolicy(sizePolicy)
        self.parameters.setMinimumSize(QtCore.QSize(390, 192))
        self.parameters.setObjectName(_fromUtf8("parameters"))
        self.parameters.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_5.addWidget(self.parameters)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.details_label = QtGui.QLabel(self.tab)
        self.details_label.setObjectName(_fromUtf8("details_label"))
        self.horizontalLayout_4.addWidget(self.details_label)
        self.details_mode = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_mode.sizePolicy().hasHeightForWidth())
        self.details_mode.setSizePolicy(sizePolicy)
        self.details_mode.setObjectName(_fromUtf8("details_mode"))
        self.horizontalLayout_4.addWidget(self.details_mode)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.scenarioTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.scenarioTab.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.scenarioTab)
        self.verticalLayout_3.addWidget(self.splitter)
        OBCILauncher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OBCILauncher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        OBCILauncher.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OBCILauncher)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OBCILauncher.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(OBCILauncher)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        OBCILauncher.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave_as = QtGui.QAction(OBCILauncher)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesaveas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave_as.setIconVisibleInMenu(True)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave = QtGui.QAction(OBCILauncher)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(OBCILauncher)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAdd_to_sidebar = QtGui.QAction(OBCILauncher)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_add-bookmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_to_sidebar.setIcon(icon3)
        self.actionAdd_to_sidebar.setIconVisibleInMenu(True)
        self.actionAdd_to_sidebar.setObjectName(_fromUtf8("actionAdd_to_sidebar"))
        self.actionExit = QtGui.QAction(OBCILauncher)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRemove_from_sidebar = QtGui.QAction(OBCILauncher)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/stock_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_from_sidebar.setIcon(icon5)
        self.actionRemove_from_sidebar.setIconVisibleInMenu(True)
        self.actionRemove_from_sidebar.setObjectName(_fromUtf8("actionRemove_from_sidebar"))
        self.actionConnect = QtGui.QAction(OBCILauncher)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon6)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionSelectAmplifier = QtGui.QAction(OBCILauncher)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/filefind.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectAmplifier.setIcon(icon7)
        self.actionSelectAmplifier.setObjectName(_fromUtf8("actionSelectAmplifier"))
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionRemove_from_sidebar)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelectAmplifier)

        self.retranslateUi(OBCILauncher)
        self.scenarioTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OBCILauncher)

    def retranslateUi(self, OBCILauncher):
        OBCILauncher.setWindowTitle(_translate("OBCILauncher", "OBCI Launcher", None))
        self.groupBox.setTitle(_translate("OBCILauncher", "Experiment scenarios", None))
        self.store_checkBox.setText(_translate("OBCILauncher", "store EEG signal and tags", None))
        self.label_7.setText(_translate("OBCILauncher", "Directory", None))
        self.label_8.setText(_translate("OBCILauncher", "File name", None))
        self.store_file.setText(_translate("OBCILauncher", "test1", None))
        self.store_dir.setText(_translate("OBCILauncher", "~/", None))
        self.store_dir_chooser.setText(_translate("OBCILauncher", "...", None))
        self.store_ts_checkBox.setText(_translate("OBCILauncher", "Append timestamp to file name", None))
        self.store_local_checkBox.setText(_translate("OBCILauncher", "Store data locally", None))
        self.start_button.setText(_translate("OBCILauncher", "Start", None))
        self.stop_button.setText(_translate("OBCILauncher", "Stop", None))
        self.parameters_of.setTitle(_translate("OBCILauncher", "Scenario data", None))
        self.info.setText(_translate("OBCILauncher", "asjdn asjklndjk naskljdh jka", None))
        self.details_label.setText(_translate("OBCILauncher", "Details mode:", None))
        self.scenarioTab.setTabText(self.scenarioTab.indexOf(self.tab), _translate("OBCILauncher", "Tab 1", None))
        self.scenarioTab.setTabText(self.scenarioTab.indexOf(self.tab_2), _translate("OBCILauncher", "Tab 2", None))
        self.menuMenu.setTitle(_translate("OBCILauncher", "File", None))
        self.toolBar.setWindowTitle(_translate("OBCILauncher", "toolBar", None))
        self.actionSave_as.setText(_translate("OBCILauncher", "Save as...", None))
        self.actionSave_as.setShortcut(_translate("OBCILauncher", "Ctrl+Shift+S", None))
        self.actionSave.setText(_translate("OBCILauncher", "Save", None))
        self.actionSave.setShortcut(_translate("OBCILauncher", "Ctrl+S", None))
        self.actionOpen.setText(_translate("OBCILauncher", "Import...", None))
        self.actionOpen.setShortcut(_translate("OBCILauncher", "Ctrl+O", None))
        self.actionAdd_to_sidebar.setText(_translate("OBCILauncher", "Add to sidebar", None))
        self.actionAdd_to_sidebar.setShortcut(_translate("OBCILauncher", "Ctrl+B", None))
        self.actionExit.setText(_translate("OBCILauncher", "Exit", None))
        self.actionExit.setShortcut(_translate("OBCILauncher", "Ctrl+Q", None))
        self.actionRemove_from_sidebar.setText(_translate("OBCILauncher", "Remove from sidebar", None))
        self.actionRemove_from_sidebar.setShortcut(_translate("OBCILauncher", "Ctrl+Shift+D", None))
        self.actionConnect.setText(_translate("OBCILauncher", "Connect...", None))
        self.actionConnect.setToolTip(_translate("OBCILauncher", "Connect to another machine", None))
        self.actionConnect.setShortcut(_translate("OBCILauncher", "Ctrl+Shift+C", None))
        self.actionSelectAmplifier.setText(_translate("OBCILauncher", "Select Amplifier ...", None))
        self.actionSelectAmplifier.setToolTip(_translate("OBCILauncher", "Search for available amplifiers and select one", None))
        self.actionSelectAmplifier.setShortcut(_translate("OBCILauncher", "Ctrl+Shift+A", None))

import resources_rc