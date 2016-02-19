'''
Created on 2010-04-09

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

# Form implementation generated from reading ui file 'Restriction.ui'
#
# Created: Fri Apr  9 13:07:24 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

import sip
from PyQt4 import QtCore, QtGui, QtXmlPatterns
from editor.mainEditorFrame import MainEditorWindow
from model.baseVarModel import GeneratorBaseModel

class Ui_Dialog(object):
    '''
    This class is an automatically generated python file using the pyuic4 program and .ui file generated by Qt_Designer
    This class is a dialog in which the user can modify the accept function of a profile
    '''
    def __init__(self, profileName,parent=None):
        '''
        @summary Constructor
        @param profileName : current profile Name
        @param parent : population tab
        '''
        self.baseModel = GeneratorBaseModel()
        self.parent = parent
        self.profileName = profileName
        self.acceptFuncDom = None
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 600)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 560, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 551, 71))
        self.textBrowser.setObjectName("textBrowser")
        
        self.checkBoxWidget = QtGui.QRadioButton("Simple accept function",Dialog)
        self.checkBoxWidget.setGeometry(QtCore.QRect(40,100,180,28))
        self.checkBoxWidget.setChecked(False)       

        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 380, 551, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        
        self.checkBox = QtGui.QRadioButton("Accept all individuals",Dialog)
        self.checkBox.setGeometry(QtCore.QRect(40,440,170,28))
        self.checkBox.setChecked(False)
        
        self.checkBoxComplex = QtGui.QRadioButton("Complex accept function",Dialog)
        self.checkBoxComplex.setGeometry(QtCore.QRect(40,475,192,28))
        self.checkBoxComplex.setChecked(False)
        
        self.pushButtonTreeEditor = QtGui.QPushButton("Open tree editor",Dialog)
        self.pushButtonTreeEditor.setGeometry(80,510,150,28)
        
        self.widgetLayout = QtGui.QWidget(Dialog)
        
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setColumnMinimumWidth(2,120)
        self.gridLayout.setColumnMinimumWidth(3,120)
        self.gridLayout.setColumnStretch(0,1)
        
        self.widgetLayout.setLayout(self.gridLayout)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(40,140,551,230)
        self.scrollArea.setWidget(self.widgetLayout)

            
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.commitChanges)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.connect(self.checkBox,QtCore.SIGNAL("toggled(bool)"),self.restrict)
        self.connect(self.checkBoxComplex,QtCore.SIGNAL("toggled(bool)"),self.restrict)
        self.connect(self.checkBoxWidget,QtCore.SIGNAL("toggled(bool)"),self.restrict)
        self.connect(self.pushButtonTreeEditor,QtCore.SIGNAL("clicked()"),self.openTreeEditor)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "LSD - Population Definition", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here, you can choose restrictions on your variables to tell the simulator which individuals you want to keep in your population. If you want more complex possibilities, use the Open Tree Editor button.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note : Fractionnal numbers must be entered using a dot \".\", not a coma\",\".</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example : 3.25 is correct, 3,25 is wrong.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


    '''
    All functions below are used to manage the dom-layout
    '''

    def enableLineEdit(self,text):
        '''
        @summary Enables second Line Edit when between is chosen in the comboBox
        @param text: comboBox current's text, possibly between
        '''
        cellSizes = self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.sender()))
        row = cellSizes[0]
        if str(text) == "between":
            self.gridLayout.itemAtPosition(row, 3).widget().setEnabled(True)
            return
        self.gridLayout.itemAtPosition(row, 3).widget().setEnabled(False)
        
    def restrict(self,checkState):
        '''
        @summary Disable or Enable the scroll area when the user unchecks/checks the Accept all individuals checkBox
        '''
        if checkState:
            if self.sender() == self.checkBox:
                self.widgetLayout.setDisabled(True)
                self.pushButtonTreeEditor.setDisabled(True)
            elif self.sender() == self.checkBoxWidget:
                self.widgetLayout.setEnabled(True)
                self.pushButtonTreeEditor.setDisabled(True)
            else:
                #Case checkBox complex
                self.widgetLayout.setDisabled(True)
                self.pushButtonTreeEditor.setEnabled(True)
            
    def commitChanges(self):
        '''
        @summary Last action performed before leaving
        '''
        self.parseResults()
        self.accept()
        
    def addRestriction(self):
        '''
        @summary Adds a line after the line where the pushButton was pressed
        '''
        #get row of the pushButton that sent the request
        cellSizes = self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.sender()))
        row = cellSizes[0]
        newComboBox = QtGui.QComboBox()
        newComboBox.addItems(QtCore.QStringList(["","equals","<=",">=","between"]))
        self.updateLayout(row)
        self.gridLayout.addWidget(newComboBox,row+1,1)
        self.gridLayout.addWidget(QtGui.QLineEdit(),row+1,2)
        self.gridLayout.addWidget(QtGui.QLineEdit(),row+1,3)
        self.gridLayout.itemAtPosition(row+1,3).widget().setDisabled(True)
        self.gridLayout.addWidget(QtGui.QPushButton("-"),row+1,4)
        self.gridLayout.itemAtPosition(row+1, 4).widget().setFixedWidth(30)
        #First remove pushButton and then add it. Adding it without removing it first gives an unexpected behavior
        self.gridLayout.removeWidget(self.sender())
        self.gridLayout.addWidget(self.sender(),row+1,5)
        
        self.connect(newComboBox,QtCore.SIGNAL("currentIndexChanged(QString)"),self.enableLineEdit)
        self.connect(self.gridLayout.itemAtPosition(row+1, 4).widget(),QtCore.SIGNAL("clicked()"),self.removeRestriction)
        #Set PushButton_remove("-") of the precedent item. Will ensure that if item was disabled because it was the only condition of the variable, it will now be available for discard
        self.gridLayout.itemAtPosition(row, 4).widget().setEnabled(True)
        
    def removeRestriction(self):
        '''
        @summary Removes the line where a "-" psuhButton was pressed
        '''
        #get row of the psuhButton that sent the request
        cellSizes = self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.sender()))
        row = cellSizes[0]
        self.updateLayout(row,False)
        #Look if disabling the PushButton "-" is necessary
        for i in range(0,self.gridLayout.rowCount()):
            if self.gridLayout.itemAtPosition(i,0) :
                if self.gridLayout.itemAtPosition(i+1,0) or not self.gridLayout.itemAtPosition(i+1,1):
                    self.gridLayout.itemAtPosition(i,4).widget().setEnabled(False)     

    def updateLayout(self,rowFrom,rowAdded=True):
        '''
        @summary QGridLayout only provides methods to replace a widget at a certain position
        This function, although not quite efficient, allows the insertion of a row in the model, "pushing" 1 row further
        @param rowAdded: if false, allows the removal of a row in the model
        @rowFrom : row where the updateLAyout comes from
        '''
        if rowAdded:
            rowCount = self.gridLayout.rowCount()
            while rowCount > rowFrom+1:
                for i in range(0,6):
                    if self.gridLayout.itemAtPosition(rowCount-1,i):
                        self.gridLayout.addWidget(self.gridLayout.itemAtPosition(rowCount-1,i).widget(),rowCount,i)
                rowCount = rowCount-1
        else:
            #Quite complex conditions to check, so they are going to be described
            rowCount =  self.gridLayout.rowCount()
            #As long as there are rows located higher(higher is lower on the screen) than the one being deleted
            while rowFrom < rowCount:
                #for all 6 columns available(label,comboBoxCondition. 2 lines Edits, + and - push Buttons)
                for i in range(0,6):
                    #look if there is an item on the line higher
                    if self.gridLayout.itemAtPosition(rowFrom+1,i):
                        #loof if there is an item on the row currently being transformed
                        if self.gridLayout.itemAtPosition(rowFrom,i):
                            #if it's a pushButton +, send it on the line before
                            if i == 5:
                                self.gridLayout.addWidget(self.gridLayout.itemAtPosition(rowFrom,i).widget(),rowFrom-1,i)
                            #else delete this item(important)
                            else:
                                item = self.gridLayout.itemAtPosition(rowFrom,i)
                                self.gridLayout.removeItem(item)
                                item.widget().deleteLater()
                        #now u can safely take the line over the one  being transformed and transfer its widgets
                        self.gridLayout.addWidget(self.gridLayout.itemAtPosition(rowFrom+1,i).widget(),rowFrom,i)
                        
                    #if there is no object on the line above, multiple possibilities
                    else:
                        #look if there is an item on the row currently being transformed
                        if self.gridLayout.itemAtPosition(rowFrom,i):
                            #if so and we're on line 5, there is QPushButton + to move below
                            if i ==5:
                
                                self.gridLayout.addWidget(self.gridLayout.itemAtPosition(rowFrom,i).widget(),rowFrom-1,i)
                            #if there is a label, leave it there
                            elif i ==0:
                                continue
                            #else, delete objects
                            else:
                                item = self.gridLayout.itemAtPosition(rowFrom,i)
                                self.gridLayout.removeItem(item)
                                item.widget().deleteLater()
                        
                rowFrom = rowFrom+1
        #Note : other conditions are implicit: ex : since a QpushButton "-" is disabled when his line is the only condition of the variable, we don'T have to check for this case(this function will never get called) 
            
    def parseEntry(self,funcNode):
        '''
        @summary Parse funcNode and create widgets until an unknown xml node is encountered or until the node is completly parsed
        @param funcNode : the xml node to be parsed
        '''
        
        self.acceptFuncDom = funcNode
        funcDict={"Operators_IsLessOrEqual":self.parseRegular,
                  "Operators_IsGreaterOrEqual":self.parseRegular,
                  "Operators_IsEqual":self.parseRegular,
                  "Operators_IsBetween":self.parseBetween}
        indexDict ={"Operators_IsLessOrEqual":2,
                  "Operators_IsGreaterOrEqual":3,
                  "Operators_IsEqual":1,
                  "Operators_IsBetween":4}
        #Renewal of the grid Layout
        self.resetLayout()
        self.acceptFunctionPmtTree = funcNode.firstChildElement("PrimitiveTree")
        acceptFunctionNode = self.acceptFunctionPmtTree.firstChild()
        #Try to parse
        if acceptFunctionNode.nodeName() == QtCore.QString("Operators_AndComplex") :
            lAndChildList = acceptFunctionNode.childNodes()
            for i in range(0,lAndChildList.count()):
                lCurrentChildNode = lAndChildList.item(i)
                if lCurrentChildNode.nodeName() == QtCore.QString("Operators_OrComplex"):
                    sameVariable, varName = self.checkIfSameVariable(lCurrentChildNode)
                    if sameVariable:
                        lOrChildList = lCurrentChildNode.childNodes()
                        for orChilds in range(0,lOrChildList.count()):
                            lCurrentOrChild = lOrChildList.item(orChilds)             
                            if str(lCurrentOrChild.nodeName()) in funcDict.keys():
                                if funcDict[str(lCurrentOrChild.nodeName())](lCurrentOrChild,varName,indexDict[str(lCurrentOrChild.nodeName())]):
                                    continue               
                            self.checkBoxComplex.setChecked(True)
                        continue
                
                self.checkBoxComplex.setChecked(True)
            
            if not self.checkBoxComplex.isChecked():
                #Check box complex wasn't check in nested loops, hence parse was successful
                self.checkBoxWidget.setChecked(True)
               
        #look if we accept all individuals)
        
        elif acceptFunctionNode.nodeName() == QtCore.QString("Data_Value"):
            
            if acceptFunctionNode.toElement().attribute("inValue_Type") == QtCore.QString("Bool"):
                
                self.checkBox.setChecked(True)
            else:
                self.checkBoxComplex.setChecked(True)
        #Else set disabled, accept function has to be edited via Tree Editor
        else:
            self.checkBoxComplex.setChecked(True)
        #Don't forget to add the variables that weren't found in the accept Function Node
        for var in self.baseModel.getDemoVarsList(self.profileName):
            if var not in self.varList():
                numRows = self.gridLayout.rowCount()
                self.createWidgets(numRows)
                self.gridLayout.addWidget(QtGui.QLabel(var),numRows,0)
                self.gridLayout.addWidget(QtGui.QPushButton("+"),numRows,5)
                self.gridLayout.itemAtPosition(numRows, 5).widget().setFixedWidth(30)
                self.gridLayout.itemAtPosition(numRows,4).widget().setDisabled(True)
                self.connect(self.gridLayout.itemAtPosition(numRows,5).widget(),QtCore.SIGNAL("clicked()"),self.addRestriction)
        
    def parseRegular(self,domNode,varName,indexVal):
        '''
        @summary Parse the xml node of a regular expression
        @param domNode : the domNode to parse
        @param varName : the variable name of the parsed node
        @param indexVal : an int corresponding to the type of condition(IsEqual, IsGreater, etc...)
        '''
        if domNode.attributes().count() == 3:
            #inArgLeft, inArgRight and in inArgRight_Type needed
            #But we already know that inArgLeft is there since domNode successfully went through checkIfSameVariable function
            if domNode.toElement().hasAttribute("inArgRight") and domNode.toElement().hasAttribute("inArgRight_Type"):
                numRows = self.gridLayout.rowCount()
                self.createWidgets(numRows)
                self.gridLayout.itemAtPosition(numRows,1).widget().setCurrentIndex(indexVal)
                self.gridLayout.itemAtPosition(numRows,2).widget().setText(domNode.toElement().attribute("inArgRight",""))
                if not varName in self.varList():
                    self.gridLayout.addWidget(QtGui.QLabel(varName),numRows,0)
                    self.gridLayout.addWidget(QtGui.QPushButton("+"),numRows,5)
                    self.gridLayout.itemAtPosition(numRows, 5).widget().setFixedWidth(30)
                    self.gridLayout.itemAtPosition(numRows,4).widget().setDisabled(True)
                    self.connect(self.gridLayout.itemAtPosition(numRows,5).widget(),QtCore.SIGNAL("clicked()"),self.addRestriction)
                else:
                    self.gridLayout.addWidget(self.gridLayout.itemAtPosition(numRows-1,5).widget(),numRows,5)
                    self.gridLayout.itemAtPosition(numRows-1,4).widget().setEnabled(True)
               
                return True
            
        return False
    
    def parseBetween(self,domNode,varName,indexVal):
        '''
        @summary Parse the xml node of a between expression
        @param dmoNode : the domNode to parse
        @param varName : the variable name of the parsed node
        @param indexVal : an int corresponding to the type of condition(IsEqual, IsGreater, etc...)
        '''
        if domNode.attributes().count() == 5:
            #inArgLeft, inArgRight and in inArgRight_Type needed
            #But we already know that inArgLeft is there since domNode successfully went through checkIfSameVariable function
            if domNode.toElement().hasAttribute("inArgRight") and domNode.toElement().hasAttribute("inArgRight_Type") and domNode.toElement().hasAttribute("inArgLeft") and domNode.toElement().hasAttribute("inArgLeft_Type"):
                numRows = self.gridLayout.rowCount()
                self.createWidgets(numRows)
                self.gridLayout.itemAtPosition(numRows,1).widget().setCurrentIndex(indexVal)
                self.gridLayout.itemAtPosition(numRows,2).widget().setText(domNode.toElement().attribute("inArgLeft",""))
                self.gridLayout.itemAtPosition(numRows,3).widget().setEnabled(True)
                self.gridLayout.itemAtPosition(numRows,3).widget().setText(domNode.toElement().attribute("inArgRight",""))
                if not varName in self.varList():
                    self.gridLayout.addWidget(QtGui.QLabel(varName),numRows,0)
                    self.gridLayout.addWidget(QtGui.QPushButton("+"),numRows,5)
                    self.gridLayout.itemAtPosition(numRows, 5).widget().setFixedWidth(30)
                    self.gridLayout.itemAtPosition(numRows,4).widget().setDisabled(True)
                    self.connect(self.gridLayout.itemAtPosition(numRows,5).widget(),QtCore.SIGNAL("clicked()"),self.addRestriction)
                else:
                    self.gridLayout.addWidget(self.gridLayout.itemAtPosition(numRows-1,5).widget(),numRows,5)
                    self.gridLayout.itemAtPosition(numRows-1,4).widget().setEnabled(True)
                    
                return True
            
        return False
    
    def varList(self):
        '''
        @summary return the variables present in the grid
        '''
        vars = []
        rows = self.gridLayout.rowCount()
        for i in range(0,rows):
            if self.gridLayout.itemAtPosition(i,0):
                vars.append(self.gridLayout.itemAtPosition(i,0).widget().text())
        return vars
    
    
    def createWidgets(self,numRows):
        '''
        @summary Creates the widget before they are customized by parse function
        @param numRows : row of the widget to create
        '''
        self.gridLayout.addWidget(QtGui.QComboBox(),numRows,1)
        self.gridLayout.itemAtPosition(numRows,1).widget().addItems(QtCore.QStringList(["","equals","<=",">=","between"]))
        self.gridLayout.addWidget(QtGui.QLineEdit(),numRows,2)
        self.gridLayout.addWidget(QtGui.QLineEdit(),numRows,3)
        self.gridLayout.itemAtPosition(numRows,3).widget().setDisabled(True)
        self.gridLayout.addWidget(QtGui.QPushButton("-"),numRows,4)
        self.gridLayout.itemAtPosition(numRows, 4).widget().setFixedWidth(30)
        self.connect(self.gridLayout.itemAtPosition(numRows, 4).widget(),QtCore.SIGNAL("clicked()"),self.removeRestriction)
        self.connect(self.gridLayout.itemAtPosition(numRows, 1).widget(),QtCore.SIGNAL("currentIndexChanged(QString)"),self.enableLineEdit)
        
    def checkIfSameVariable(self,domNode):
        '''
        @summary Security function
        @Make sure there is only one variable listed in a Or 
        '''
        variableQuery = QtXmlPatterns.QXmlQuery()
        parsedXML = QtCore.QString()
        newTextStream = QtCore.QTextStream(parsedXML)
        domNode.save(newTextStream,2)
        queryBuffer = QtCore.QBuffer()
        queryBuffer.setData(parsedXML.toUtf8())
        queryBuffer.open(QtCore.QIODevice.ReadOnly)
        variableQuery.bindVariable("varSerializedXML", queryBuffer)
        #Here is a big limit, we consider dependencies can be all found in attributes ending with the word label or Label
        variableQuery.setQuery("for $x in doc($varSerializedXML)/Operators_OrComplex/*/@inArgLeft[starts-with(data(.),'@')] return substring-after(data($x),'@')")
        variables = QtCore.QStringList()
        variableQuery.evaluateTo(variables)
        #If dom nodes i Operators_IsBetween, then check inVakue instead of inArgLeft
        variableQuery.setQuery("for $x in doc($varSerializedXML)/Operators_OrComplex/Operators_IsBetween/@inValue[starts-with(data(.),'@')] return substring-after(data($x),'@')")

        variableQuery.evaluateTo(variables)
        if len(set([str(item) for item in variables])) == 1:
            if len(list(variables)) == domNode.childNodes().count():
                return True, str(variables[0])

        return False, None
    
    def parseResults(self):
        '''
        @summary If user save the accept function, this function computes the resulting node
        '''
        if self.checkBox.isChecked():
            domNode = self.createDomNode("Data_Value","inValue_type","Bool","inValue","true")
            self.acceptFunctionPmtTree.replaceChild(domNode,self.acceptFunctionPmtTree.firstChild())
            return
        
        elif self.checkBoxComplex.isChecked():
            return
        
        domNode = self.createDomNode("Operators_AndComplex")
        i = 0
        while i < self.gridLayout.rowCount():
            if not self.gridLayout.itemAtPosition(i,0):
                i+=1
                continue
            currVar = self.gridLayout.itemAtPosition(i,0).widget()
            domNodeDict = []
            while(True):
                condition = self.gridLayout.itemAtPosition(i,1).widget().currentText()
                if not condition.isEmpty():
                    domNodeDict.append(self.writeXmlRestriction(condition, [currVar,self.gridLayout.itemAtPosition(i,2).widget(),self.gridLayout.itemAtPosition(i,3).widget()]))
                if not self.gridLayout.itemAtPosition(i+1,0) and  self.gridLayout.itemAtPosition(i+1,1):
                    i+=1
                else:
                    if domNodeDict:
                        newOrNode = domNode.appendChild(self.createDomNode("Operators_OrComplex"))
                        for item in domNodeDict:
                            newOrNode.appendChild(item)
                    i+=1
                    break
        
        self.acceptFunctionPmtTree.replaceChild(domNode,self.acceptFunctionPmtTree.firstChild())
            
    def writeXmlRestriction(self,widgetCondition,widgetList):
        '''
        @summary creates the xml subtree corresponding to one line(restriction)
        @params widgetCondition, widgetList : line condition and widgets used to create xml tree
        '''
        varName = widgetList[0].text()
        varValue = widgetList[1].text()
        if widgetCondition == QtCore.QString("equals"):
            dom = self.createDomNode("Operators_IsEqual","inArgLeft","@"+varName,"inArgRight",varValue)
            dom.setAttribute("inArgRight_Type",self.baseModel.getVarType(self.profileName,varName))
            return dom
        elif widgetCondition == QtCore.QString("<="):
            dom = self.createDomNode("Operators_IsLessOrEqual","inArgLeft",'@'+varName,"inArgRight",varValue)
            dom.setAttribute("inArgRight_Type",self.baseModel.getVarType(self.profileName,varName))
            return dom
        elif widgetCondition == QtCore.QString(">="):
            dom = self.createDomNode("Operators_IsGreaterOrEqual","inArgLeft",'@'+varName,"inArgRight",varValue)
            dom.setAttribute("inArgRight_Type",self.baseModel.getVarType(self.profileName,varName))
            return dom
        else:
            #case between
            varValue2 = widgetList[2].text()
            dom = self.createDomNode("Operators_IsBetween","inValue",'@'+varName,"inArgLeft",varValue)
            dom.setAttribute("inArgLeft_Type",self.baseModel.getVarType(self.profileName,varName))
            dom.setAttribute("inArgRight",varValue2)
            dom.setAttribute("inArgRight_Type",self.baseModel.getVarType(self.profileName,varName))
            return dom
           
    def createDomNode(self, nodeName, arg1 = QtCore.QString(), arg1Value = QtCore.QString(), arg2 = QtCore.QString(), arg2Value = QtCore.QString()):
        '''
        @summary Creates an xml node
        '''
        domNode = self.acceptFuncDom.ownerDocument().createElement(nodeName)
        if arg1:
            domNode.toElement().setAttribute(arg1,arg1Value)
        if arg2:
            domNode.toElement().setAttribute(arg2,arg2Value)
        return domNode
    
    def resetLayout(self):
        '''
        @summary Clear layout
        '''
        while [widgetItem for widgetItem in [self.gridLayout.takeAt(0)] if widgetItem]:
            widgetItem.widget().deleteLater()
        sip.delete(self.gridLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setColumnMinimumWidth(2,120)
        self.gridLayout.setColumnMinimumWidth(3,120)
        self.gridLayout.setColumnStretch(0,1)
        self.widgetLayout.setLayout(self.gridLayout)
        
    def openTreeEditor(self):
        '''
        @summary Open tree editor for more complicated accept functions
        '''
        acceptFuncParent = self.acceptFunctionPmtTree.parentNode()
        if self.scrollArea.isEnabled and self.widgetLayout.isEnabled():
            self.parseResults()
        treeEditor = MainEditorWindow(self.acceptFunctionPmtTree.firstChild(), self.parent, "AcceptFunction")
        treeEditor.exec_()
        if treeEditor.result():
            self.parseEntry(acceptFuncParent)
            