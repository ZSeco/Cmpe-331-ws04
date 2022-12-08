# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YquoZ02Qo48jc-F45k1KnSXj36WJpme2
"""

"""
    Stage: Development-02
    @author: Deniz Kuzey, 119202077
    @author: Zafer Sercan Yıldız, 119202037
"""

import tkinter as tk


class LoginWindow:
  
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        window.title("Ecommerce Login")
        self.lbl01 = tk.Label(text="Ecommerce Username")
        self.lbl02 = tk.Label(text="User Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Login")

        self.btn01.bind("<Button-1>", self.handle_click)
        


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)

    def create_ecommerce_window(self):
        self.after_login_window = tk.Tk()
        self.after_login_window.geometry("640x480")
        self.after_login_window.title('ecommerce')

    def validate_and_login_user(self, event):
        username = self.txt01.get()
        password = self.txt02.get()
        if(username == test_login_username and password == test_login_password):
          # After a successful login, we create a new 'page' or a window to show the ecommerce. 
          self.create_ecommerce_window()
          # Login window can now be destroyed
          self.window.destroy()
          # Start the after login window main loop
          self.after_login_window.mainloop()



    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        pass



# main method for testing the application
if __name__ == "__main__":
    LoginWindow()