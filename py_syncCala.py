import tkinter as tk

from math import *

End_Str="Python"+"\n"+"End Project"+"\n"+" Scientific"+"\n"+"Calculatur Made"+"\n"+" By Shaked"



ColorGrey="#505050"
ColorDarkGrey="#1c1c1c"
ColorOrange='#ff9500'


buttons = {

    'padx': 16,

    'pady': 1,

    'bd': 4,

    'fg': 'white',

    'bg': ColorGrey,

    'font': ('arial', 18),

    'width': 2,

    'height': 2,

    'relief': 'flat',

    'activebackground': ColorGrey

}

#----------------------------------------------------------------------------------------------------------
def fsin(arg):

    return sin(arg * 1)

#----------------------------------------------------------------------------------------------------------
    
def fcos(arg):

    return cos(arg * 1)

#----------------------------------------------------------------------------------------------------------
    
def ftan(arg):

    return tan(arg * 1)

#----------------------------------------------------------------------------------------------------------

class Calculator:


    def __init__(self, master):
        
        self.calculation = ""
        
        self.recall = ""
       
        self.sum = ""
		
        self.text_input = tk.StringVar()
        
        self.master = master
        
        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg=ColorGrey)

        top_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg=ColorGrey)

        bottom_frame.pack(side=tk.BOTTOM)
        
        txt_display = tk.Entry(top_frame, font=('arial', 36), relief='flat',

                               bg=ColorGrey, fg='white', textvariable=self.text_input, width=60, bd=4, justify='right')

        txt_display.pack()

#----------------------------------------------------------------------------------------------------------
      
       
        self.btn_0 = tk.Button(bottom_frame, buttons, text="0", command=lambda: self.btn_click(0))

        self.btn_0.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey, width=7, bd=5)

        self.btn_0.grid(row=4, column=4, columnspan=2)
        
#----------------------------------------------------------------------------------------------------------        
        self.btn_1 = tk.Button(bottom_frame, buttons, text="1", command=lambda: self.btn_click(1))

        self.btn_1.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_1.grid(row=3, column=4)

#----------------------------------------------------------------------------------------------------------       
        self.btn_2 = tk.Button(bottom_frame, buttons, text="2", command=lambda: self.btn_click(2))

        self.btn_2.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_2.grid(row=3, column=5)

#----------------------------------------------------------------------------------------------------------
        self.btn_3 = tk.Button(bottom_frame, buttons, text="3", command=lambda: self.btn_click(3))

        self.btn_3.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_3.grid(row=3, column=6)
        
#----------------------------------------------------------------------------------------------------------        
        self.btn_4 = tk.Button(bottom_frame, buttons, text="4", command=lambda: self.btn_click(4))

        self.btn_4.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_4.grid(row=2, column=4)

#----------------------------------------------------------------------------------------------------------      
        self.btn_5 = tk.Button(bottom_frame, buttons, text="5", command=lambda: self.btn_click(5))

        self.btn_5.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_5.grid(row=2, column=5)

#----------------------------------------------------------------------------------------------------------       
        self.btn_6 = tk.Button(bottom_frame, buttons, text="6", command=lambda: self.btn_click(6))

        self.btn_6.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_6.grid(row=2, column=6)
        
#----------------------------------------------------------------------------------------------------------      
        self.btn_7 = tk.Button(bottom_frame, buttons, text="7", command=lambda: self.btn_click(7))

        self.btn_7.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_7.grid(row=1, column=4)

#----------------------------------------------------------------------------------------------------------        

        self.btn_8 = tk.Button(bottom_frame, buttons, text="8", command=lambda: self.btn_click(8))

        self.btn_8.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_8.grid(row=1, column=5)

#----------------------------------------------------------------------------------------------------------       
        self.btn_9 = tk.Button(bottom_frame, buttons, text="9", command=lambda: self.btn_click(9))

        self.btn_9.configure(activebackground=ColorDarkGrey, bg=ColorDarkGrey)

        self.btn_9.grid(row=1, column=6)
        
#----------------------------------------------------------------------------------------------------------        

        self.btn_clear = tk.Button(bottom_frame, buttons, text="C", command=self.btn_clear_all)
        
        self.btn_clear.configure(bg=ColorOrange, activebackground=ColorOrange, width=7)

        self.btn_clear.grid(row=1, column=7,columnspan=2)
        
#----------------------------------------------------------------------------------------------------------
        self.btn_del = tk.Button(bottom_frame, buttons, text="del", command=self.Del)
        
        self.btn_del.configure(width=7)

        self.btn_del.grid(row=0, column=7,columnspan=2)
        
#----------------------------------------------------------------------------------------------------------
        self.btn_left_brack = tk.Button(bottom_frame, buttons, text="(", command=lambda: self.btn_click('('))

        self.btn_left_brack.grid(row=2, column=7)
#----------------------------------------------------------------------------------------------------------

        self.btn_right_brack = tk.Button(bottom_frame, buttons, text=")", command=lambda: self.btn_click(')'))

        self.btn_right_brack.grid(row=2, column=8)       
#----------------------------------------------------------------------------------------------------------        
        self.btn_pi = tk.Button(bottom_frame, buttons, text="π", command=lambda: self.btn_click('pi'))

        self.btn_pi.grid(row=3, column=2)        
        
#----------------------------------------------------------------------------------------------------------
        self.btn_abs = tk.Button(bottom_frame, buttons, text="abs", command=lambda: self.btn_click('abs' + '('))

        self.btn_abs.grid(row=2, column=2)
        
#----------------------------------------------------------------------------------------------------------        

        self.btn_ans = tk.Button(bottom_frame, buttons, text="ans", command=self.answer)

        self.btn_ans.grid(row=0, column=6)
        
#----------------------------------------------------------------------------------------------------------        

        self.btn_MC = tk.Button(bottom_frame, buttons, text="MC", command=self.memory_clear)

        self.btn_MC.grid(row=0, column=5)
        
#----------------------------------------------------------------------------------------------------------        

        self.btn_MR = tk.Button(bottom_frame, buttons, text="MR", command=self.memory_recall)

        self.btn_MR.grid(row=0, column=4)
        
#----------------------------------------------------------------------------------------------------------        
        self.btn_M_plus = tk.Button(bottom_frame, buttons, text="M+", command=self.memory_add)

        self.btn_M_plus.grid(row=0, column=3)

#----------------------------------------------------------------------------------------------------------        
     
        self.btn_log = tk.Button(bottom_frame, buttons, text="log", command=lambda: self.btn_click('log('))

        self.btn_log.grid(row=2, column=3)

#----------------------------------------------------------------------------------------------------------        
        self.btn_ln = tk.Button(bottom_frame, buttons, text="ln", command=lambda: self.btn_click('ln('))

        self.btn_ln.grid(row=3, column=3)

#----------------------------------------------------------------------------------------------------------

        self.btn_sin = tk.Button(bottom_frame, buttons, text="sin", command=lambda: self.btn_click('sin('))

        self.btn_sin.grid(row=1, column=3)
        
#----------------------------------------------------------------------------------------------------------

        self.btn_cos = tk.Button(bottom_frame,buttons, text="cos", command=lambda: self.btn_click('cos('))

        self.btn_cos.grid(row=1, column=2)
        
#----------------------------------------------------------------------------------------------------------

        self.btn_tan = tk.Button(bottom_frame, buttons, text="tan", command=lambda: self.btn_click('tan('))

        self.btn_tan.grid(row=1, column=1)

#----------------------------------------------------------------------------------------------------------        

        self.btn_fact = tk.Button(bottom_frame, buttons, text="n!", command=lambda: self.btn_click('factorial('))

        self.btn_fact.grid(row=2, column=1)

#----------------------------------------------------------------------------------------------------------

        self.btn_sqr = tk.Button(bottom_frame, buttons, text=u"x\u00B2", command=lambda: self.btn_click('**2'))

        self.btn_sqr.grid(row=0, column=1)
        
#----------------------------------------------------------------------------------------------------------

        self.cube = tk.Button(bottom_frame, buttons, text=u"x\u00B3", command=lambda: self.btn_click('**3'))

        self.cube.grid(row=0, column=2)
        
#----------------------------------------------------------------------------------------------------------        

        self.btn_power = tk.Button(bottom_frame, buttons, text="x^y", command=lambda: self.btn_click('**'))

        self.btn_power.grid(row=4, column=2)

#----------------------------------------------------------------------------------------------------------

        self.btn_sqrt = tk.Button(bottom_frame, buttons, text="sqrt", command=lambda: self.btn_click('sqrt('))

        self.btn_sqrt.grid(row=3, column=1)

#----------------------------------------------------------------------------------------------------------
     

        self.btn_div = tk.Button(bottom_frame, buttons, text="/", command=lambda: self.btn_click('/'))

        self.btn_div.grid(row=4, column=7)
        
#---------------------------------------------------------------------------------------------------------
        self.btn_mult = tk.Button(bottom_frame, buttons, text="x", command=lambda: self.btn_click('*'))

        self.btn_mult.grid(row=4, column=8)
        
#----------------------------------------------------------------------------------------------------------

        self.btnSub = tk.Button(bottom_frame, buttons, text="-", command=lambda: self.btn_click('-'))

        self.btnSub.grid(row=3, column=8)
        
#----------------------------------------------------------------------------------------------------------

        self.btn_add = tk.Button(bottom_frame, buttons, text="+", command=lambda: self.btn_click('+'))

        self.btn_add.grid(row=3, column=7)
        
#----------------------------------------------------------------------------------------------------------

        self.btn_eq = tk.Button(bottom_frame, buttons, text="=", command=self.btn_equal)

        self.btn_eq.configure(bg=ColorOrange, activebackground=ColorOrange)

        self.btn_eq.grid(row=4, column=6)
        
#----------------------------------------------------------------------------------------------------------

        self.btn_dec = tk.Button(bottom_frame, buttons, text=".", command=lambda: self.btn_click('.'))

        self.btn_dec.grid(row=4, column=3)
        
#----------------------------------------------------------------------------------------------------------        
        
        self.text=tk.Label(bottom_frame,text=End_Str)
        self.text.configure(bg=ColorGrey,fg= ColorOrange)
        
        self.text.grid(row=4, column=1)
        
#----------------------------------------------------------------------------------------------------------

    def btn_click(self, calculation_val):

        if len(self.calculation) >= 23:

            self.calculation = self.calculation

            self.text_input.set(self.calculation)

        else:

            self.calculation = self.calculation + str(calculation_val)


            self.text_input.set(self.calculation)

#--------------------------------------------------------------------------------------------------------
    def Del(self):

        self.calculation = self.calculation[:-1]

        self.text_input.set(self.calculation)

#----------------------------------------------------------------------------------------------------------
    def memory_clear(self):

        self.recall = ""
 
#----------------------------------------------------------------------------------------------------------

    def memory_add(self):

        self.recall = self.recall + '+' + self.calculation

#----------------------------------------------------------------------------------------------------------

    def answer(self):

        self.answer = self.sum

        self.calculation = self.calculation + self.answer

        self.text_input.set(self.calculation)

#----------------------------------------------------------------------------------------------------------
    def memory_recall(self):

        if self.calculation == "":

            self.text_input.set('0' + self.calculation + self.recall)

        else:

            self.text_input.set(self.calculation + self.recall)
            
#----------------------------------------------------------------------------------------------------------

    def btn_clear_all(self):

        self.calculation = ""

        self.text_input.set("")

#----------------------------------------------------------------------------------------------------------


    def btn_equal(self):
        self.sum = float(str(eval(self.calculation)))

        self.text_input.set(self.sum)

        self.calculation = self.sum
        
#----------------------------------------------------------------------------------------------------------

app = tk.Tk()

Calculator(app)

app.title("Shaked Scientific Calculator")

app.geometry("605x470")

app.resizable(False, False)

app.mainloop()