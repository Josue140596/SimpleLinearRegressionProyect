# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:26:10 2020

@author: Puro código
"""


from tkinter import *
from tkinter import ttk, filedialog, messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class SimpleLinearRegression:
    
    def __init__(self, root):
        self.root = root
        root.title('Simple Linear Regression')
        root.geometry('840x600')
        root.config(bg='grey')
        
        
        
        
        
        
        #Fisrt FrameWork
        frameWork = LabelFrame(self.root)
        frameWork.grid(row=0, column=0, sticky=(W,E) )
      
        label = Label(frameWork, text = 'Simple Linear Regression')
        
        label.pack(anchor = CENTER)
        label.config(fg='blue', bg = 'gray', font=('helvetica', 55))
        
        
        #Second FrameWork
        frameWorkTwo = LabelFrame(self.root, text = 'Machine Learning')
        frameWorkTwo.grid(row=1, column=0, sticky=(W, E) )
        frameWorkTwo.config(fg = 'white' ,bg = 'black')
        
        
        
        #Button choose file
        self.btnChoose= ttk.Button( frameWorkTwo ,text = 'Choose File', command= lambda:[self.getFiles(), self.askVariableInd(), self.askVariableDep()]).grid(row= 0, column=1)
        
        
        
        
    
        #choose file
        self.file = Entry(frameWorkTwo)
        self.file.config( width = 100)
        self.file.grid(row = 0, column=0 , padx=5, pady=5)
        
        
        
        
        
        
        #Table
        table=Label(root,text=" X \t\t y \t\t Xy \t\t X^2 \t\t y^2\t\t\t predict values y ")
        table.grid(row=2, sticky=(W, E))
        table.config(fg='white', bg='black')
        
        
        
    def askVariableInd(self):
        self.edit_windI = Toplevel()
        self.edit_windI.title('Choose variable I')
        self.edit_windI.geometry("200x100")
        
        
        
        Label(self.edit_windI ,text="choose the independent variable").grid(row= 0)
        
        
        variables = list(self.dataSet)
        
        self.valI= IntVar()
        valI = 0
        for x in variables:
            valI+=1
            RIndependent =Radiobutton(self.edit_windI, text=x, command = lambda: [ self.selecVariableI(), self.edit_windI.destroy()],  value=valI, variable=self.valI ).grid(row=valI, column=0)
        
    
    def askVariableDep(self):
        self.edit_windD = Toplevel()
        self.edit_windD.title('Choose variable Dependent')
        self.edit_windD.geometry("200x100")
        
        
        Label(self.edit_windD ,text="choose the dependent variable").grid(row= 0)
        
        self.valD= IntVar()
        variables = list(self.dataSet)
        valD= 0
        for x in variables:
            valD  +=1
            RDependent = Radiobutton(self.edit_windD, text=x,command= lambda: [self.selecVariableD(), self.edit_windD.destroy(), self.regressionSimple()], value= valD, variable= self.valD).grid(row=valD, column=0)
            
        
 
        
        
    def selecVariableI(self):
        RIndependent =self.valI.get()
        dataSet = self.dataSet
        self.variableDivI = dataSet.iloc[:, RIndependent-1].values
        
        
       
        
    def selecVariableD(self):
        RDependent =self.valD.get()
        dataSet = self.dataSet
        self.variableDivD = dataSet.iloc[:, RDependent-1].values
     
    
        
    def regressionSimple(self):
        variableInde = self.variableDivI.reshape(-1, 1)
        variableDep  = self.variableDivD.reshape(-1, 1)
        
        times = variableInde * variableDep
        squareX = variableInde **2 
        squarey = variableDep **2
        meanX = np.mean( variableInde)
        meany = np.mean( variableDep )
        
        
        #Regresión lineal

        regression = LinearRegression().fit(variableInde, variableDep)

        predict = regression.predict(variableInde)
        
        rSquare = regression.score(variableInde, variableDep)
        
        
        
        
        val=2
        for i in range(len(variableInde)):
            val+=1
            Label(root,text="  {}\t\t   {}\t\t   {}\t\t   {}\t\t   {} \t\t\t {}".format(variableInde[i], variableDep[i], times[i], squareX[i], squarey[i], predict[i])).grid(row=val , sticky=(W, E))
            
        
        suma= Label(root,text=" Σ={}  \t\t  Σ={}  \t\t  Σ={}   \t\t   Σ={}   \t   Σ={}".format(sum(variableInde), sum(variableDep), sum(times), sum(squareX), sum(squarey)))
        suma.grid(row=val+1 , sticky=(W, E))
        suma.config(bg='yellow')
        
        means =Label(root,text=" mean x̄ =  {}  \t  mean y = {} \t R^2= {} ".format(meanX, meany, rSquare))
        means.grid(row=val+2) 
        means.config(bg='sky blue')
        
        
        #plots
        plt.scatter(variableInde, variableDep, color="red")
        plt.plot(variableInde, predecir, color="blue")
        plt.show()
        
        
            
    def getFiles(self):
        
        file_path = filedialog.askopenfile(title = 'Select a file', filetypes = (('csv files', '*.csv'),('xlsx files', '*.xlsx')))
        self.dataSet = pd.read_csv(file_path)
        self.file.insert(0, file_path.name)
        
        messagebox.showinfo("alert!", "choose the Independent variable first")
        
        
    
        




if __name__ == '__main__':  
    root = Tk()
    app = SimpleLinearRegression(root)
    
    root.mainloop()



