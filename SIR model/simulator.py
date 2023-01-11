'''
----- SIR MODEL -----
GUI Based Simulation of Infectious Disease

Created by-
Anish Kumar
'''

import numpy as np
from scipy.integrate import odeint as integrt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import tkinter.messagebox as tmsg



# COMMANDS

def value():            
    N = popvar.get()          # total population
    I_i = infectvar.get()     # initially infected
    beta = betavar.get()      
    gamma = gammavar.get()
    days = dayvar.get()

    s_i = (N-I_i)/N           # susceptible fraction of population
    i_i = 1 - s_i             # infected fraction of population
    r_i = 0                   # recovered fraction of population
    R0 = (s_i)*(beta/gamma)
    
    time = np.linspace(1, days, 100)        # array containing number of days
    ini = [s_i, i_i, r_i]                   # list of initial values
    
    def sir_equ(ini, time):                 # equations
        ds_dt = -(beta)*(ini[0])*(ini[1])
        di_dt = (beta)*(ini[0])*(ini[1]) - (gamma)*(ini[1])
        dr_dt = (gamma)*(ini[1])
        return ([ds_dt, di_dt, dr_dt])

    solutions = integrt(sir_equ, ini, time)         # solution of integral
    S, I, R = solutions[:,0], solutions[:,1], solutions[:,2]

    index, = np.where(solutions[:,1] == max(solutions[:,1]))
    max_infected_day = int(time[index])

    analysis(R0, max_infected_day)
    graphs(S, I, R, time)
    

def analysis(R0, max_infected_day):             # analysis

    Label(fr_out, text = 'Analysis :', font = 'conolas 20 bold', background="#264653", fg="#F4A261").grid(row=0, column=0, padx = 20, pady = 10, sticky='e')
    if (R0 > 1):
        output1 = Label(fr_out, text = 'Basic reproduction number is {:.3f} and it will cause an epidemic.'.format(R0), font = 'conolas 20', background="#264653", fg="#F4A261")
        output1.grid(row=1, column=1, padx = 20, pady = 10, sticky='w')

    else:
        output1 = Label(fr_out, text = 'Basic reproduction number is {:.3f} and it will not cause an epidemic.'.format(R0), font = 'conolas 20', background="#264653", fg="#F4A261")
        output1.grid(row=1, column=1, padx = 20, pady = 10, sticky='w')

    output2 = Label(fr_out, text = f'After {max_infected_day} day the number of infected will start decreasing.', font = 'conolas 20', background="#264653", fg="#F4A261")
    output2.grid(row=2, column=1, padx = 20, pady = 10, sticky='w')


def graphs(S, I, R, time):                      # graph based on data
    fig = Figure(figsize = (7, 7), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(time, S,label = 'Susceptible', color="#205CDA")
    plot1.plot(time, I,label = 'Infected', color="#EB6136")
    plot1.plot(time, R,label = 'Recovered', color="#76EA15")
    plot1.legend()
    plot1.set_title('Spread of Infection')
    plot1.set_xlabel("Days")
    plot1.set_ylabel("Fraction of Population")
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side='right', anchor='sw', fill='y', padx=50, ipadx=10, pady=7, ipady=10)



def about():
    tmsg.showinfo("About", "SIR simulation: \n To predict to what extent the infection will harm the society.")

def creator():
    tmsg.showinfo("Creators", "Anish Kumar \n Arpan Kumar \n Arunesh Pratap")    



# start of GUI

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("1340x740")
root.maxsize(screen_width, screen_height)
root.minsize(1280,720)
root.title('SIR SIMULATION')
root.configure(background="#264653")

fr_title = Frame(root, bg = '#264653')               
fr_title.pack(side='top', anchor='center', fill=X, padx=5, ipadx=10, pady=10, ipady=5)

fr_out = Frame(root, bg = '#264653')                
fr_out.pack(side='bottom', anchor='center', fill=X, padx=5, ipadx=10, pady=7, ipady=10)

fr_inp = Frame(root, bg="#264653")                     
fr_inp.pack(side='left', anchor='sw', fill='y', padx=5, ipadx=10, pady=7, ipady=10)

Label(fr_title ,text='SIR Model', font = "times 50", bg = '#264653', fg='#ffffff').pack(anchor='center')

Label(fr_inp, text = 'Total Population', font="conolas 20", background="#264653", fg="#F4A261").grid(row = 2, column = 0, padx = 30, pady = 5, sticky="W")

Label(fr_inp, text = 'Initially Infected', font="conolas 20", background="#264653", fg="#F4A261").grid(row = 3, column = 0, padx = 30, pady = 5, sticky="W")

Label(fr_inp, text = 'Transmission Rate (𝜷)', font="conolas 20", background="#264653", fg="#F4A261").grid(row = 4, column = 0, padx = 30, pady = 5, sticky="W")

Label(fr_inp, text = 'Recovery Rate (𝜸)', font="conolas 20", background="#264653", fg="#F4A261").grid(row = 5, column = 0, padx = 30, pady = 5, sticky="W")

Label(fr_inp, text = "Days of Simulation", font="conolas 20", background="#264653", fg="#F4A261").grid(row = 7, column = 0, padx = 30, pady = 5, sticky="W")

popvar = IntVar()
infectvar = IntVar()
betavar = DoubleVar()
gammavar = DoubleVar()
dayvar = IntVar()

popentry = Entry(fr_inp, textvariable = popvar)
infectentry = Entry(fr_inp, textvariable = infectvar)
betaentry = Entry(fr_inp, textvariable = betavar)
gammaentry = Entry(fr_inp, textvariable = gammavar)
dayentry = Entry(fr_inp, textvariable = dayvar)

popentry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky="E")
infectentry.grid(row = 3, column = 1, padx = 5, pady = 5, sticky="E")
betaentry.grid(row = 4, column = 1, padx = 5, pady = 5, sticky="E")
gammaentry.grid(row = 5, column = 1, padx = 5, pady = 5, sticky="E")
dayentry.grid(row = 7, column = 1, padx = 5, pady = 5, sticky="E")

submit = Button(fr_inp, text = 'Simulate', command = value)
submit.grid(row = 8, column = 1, padx = 7, pady = 7, ipadx = 5, ipady = 5)

menubar = Menu(root)
menubar.add_command(label = 'About', command = about)
menubar.add_command(label = 'Creators', command = creator)
root.config(menu = menubar)

root.mainloop()