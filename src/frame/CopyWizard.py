'''

Created on 2010-04-27

@author:  Mathieu Gagnon
@contact: mathieu.gagnon.10@ulaval.ca
@organization: Universite Laval

@license

 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
'''

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CopyWizard.ui'
#
# Created: Tue Apr 27 15:45:07 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from model.baseVarModel import GeneratorBaseModel

class Ui_Dialog(object):
    '''
    This class is an automatically generated python file using the pyuic4 program and .ui file generated by Qt_Designer
    This class is meant to allow the user to copy data in baseVarModel from a profile to another profile
    '''
    def __init__(self,parent,copyLabel, profileLabel):
        '''
        @summary Constructor
        @param parent : ProfileManager window
        @param copyLabel : String(Simulation Variables or Accept Function)
        @param profileLabel : profile from which the data is going to be copied
        '''
        self.parent = parent
        self.copyLabel = copyLabel
        self.profileLabel = profileLabel
        self.baseModel = GeneratorBaseModel()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 361, 291))
        self.listWidget.setObjectName("listView")
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 25, 361, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        for elements in self.baseModel.getProfilesList():
            newListWidgetItem = QtGui.QListWidgetItem(elements,self.listWidget)
            newListWidgetItem.setCheckState(QtCore.Qt.Unchecked)
            if elements == self.profileLabel:
                newListWidgetItem.setHidden(True)
                
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"),self.checkCopy)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Copy Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", self.profileLabel+"'s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", self.copyLabel, None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "to :", None, QtGui.QApplication.UnicodeUTF8))

    def checkCopy(self):
        '''
        @summary If the user selected profiles in self.listWidget, perform copy
        Else, show message
        '''
        for i in range(0,self.listWidget.count()):
            if self.listWidget.item(i).data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                self.accept()
                return
        QtGui.QMessageBox.information(self, "Invalid Copy", "Choose Profiles in which you want the "+self.copyLabel+" to be replaced or press Cancel")
        
                
