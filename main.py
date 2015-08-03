#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ULIMA - Programacion Internet
Servidor que reponde texto
'''

__author__ = "Hernan Quintana"
__copyright__ = "Copyright 2015, ULIMA-PI"
__credits__ = ["Hernan Quintana"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Hernan Quintana"
__email__ = "hquintan@ulima.edu.pe"
__status__ = "Production"

import Tkinter
import httplib
import sys

class main_window(Tkinter.Tk):
    """Main screen for the app """
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # Adding textbox
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        # Adding a button
        button = Tkinter.Button(self, text=u"Go", command=self.onURLEntered)
        button.grid(column=1,row=0)

        self.entry_body = Tkinter.Text(self)
        self.entry_body.grid(column=0, row=1, columnspan=2, sticky='EWS')

        self.labelVariable = Tkinter.StringVar()
        self.state_bar = Tkinter.Label(self, textvariable=self.labelVariable,
                                        anchor="w",fg="white",bg="blue")
        self.state_bar.grid(column=0,row=2,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

        # Adding event handlers
        self.entry.bind("<Return>", self.onURLEntered)

    def onURLEntered(self, evt):
        self.entry_body.delete(1.0, Tkinter.END)
        try:
            self.labelVariable.set(u'Conectando...')
            parts = self.entry.get().split("/")
            conn = httplib.HTTPConnection(parts[0]);

            conn.request("GET", parts[1])
            response = conn.getresponse()
            data = response.read()
            conn.close()

            self.entry_body.insert(1.0, data)
            self.labelVariable.set(u'Conexión OK')
        except:
            e = sys.exc_info()[1]
            self.labelVariable.set(u'Error: %s' % e)


if __name__ == '__main__':
    app = main_window(None)
    app.title('PI-MiniBrowser')
    app.mainloop()
