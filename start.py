#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from form_ui import Ui_Form

from funcy import partial

class Form(QtGui.QWidget, Ui_Form):
    def __init__(self):
        super(Form,self).__init__()
        self.setupUi(self)

    def setupUi(self, form):
        super(Form,self).setupUi(form)
        self.btnPush1.clicked.connect(partial(self.pushed,"1"))
        self.btnPush2.clicked.connect(partial(self.pushed,"2"))

    def pushed(self, nr):
        print "pushed", nr
    
def main():
    app = QtGui.QApplication(sys.argv)
    frm = Form()
    frm.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
