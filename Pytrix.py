##programa hecho por Abdul Hamid Achik López

from tkinter import *
from sympy import *

matrices = list()
diccionario = dict()
root = Tk()
f = Frame(root,height = 600, width = 820)
f.pack()
titulo = Label(f,text ="Programa Pytrix", fg="blue",font=('Arial',20))
titulo.place(x = 330, y = 5)

gBotones = LabelFrame(f,text="Menu ",padx=5,pady=5)
gBotones.place(x = 695,y = 50)
gText = LabelFrame(f,text="Texto",padx=5,pady=5)
gText.place(x=20,y=50)
gLista = LabelFrame(f,text="Matrices Creadas",padx=5,pady=5)
gLista.place(x = 695,y=280)
gMenu = LabelFrame(f,text="Operaciones", padx=5,pady=5)
gMenu.place(x=695,y=380)
t = Text(gText, height = 30,width=80)
t.pack()
bMult = Button(gMenu, text="x", width = 10,
               command = lambda:Multiplicacion(lstMatrices.get(lstMatrices.curselection())))
bMult.pack(padx=5,pady=5)
bSum = Button(gMenu, text="+", width = 10,
              command = lambda:Suma(lstMatrices.get(lstMatrices.curselection())))
bSum.pack(padx=5,pady=5)
bRes = Button(gMenu, text="-", width = 10,
              command = lambda:Resta(lstMatrices.get(lstMatrices.curselection())))
bRes.pack(padx=5,pady=5)
bInv = Button(gMenu, text="Inversa", width = 10,\
              command=lambda:Inversa(lstMatrices.get(lstMatrices.curselection())))

bInv.pack(padx=5,pady=10)
bInit = Button(gBotones, text ="Crear Matriz",width = 10,\
               command = lambda:init())
bInit.pack(padx=5,pady=5)
bGauss = Button(gBotones, text ="Gauss",width = 10,\
                command =lambda:\
                gauss(lstMatrices.get(lstMatrices.curselection())))
bGauss.pack(padx=5,pady=5)
bDeter = Button(gBotones,text = "Determinante",width = 10,\
                command = lambda:\
                determinante(lstMatrices.get(lstMatrices.curselection())))
bDeter.pack(padx=5,pady=5)

bEigVals = Button(gBotones,text = "Eigenvalores",\
                  command=lambda:\
                  eigVal(lstMatrices.get(lstMatrices.curselection())))
bEigVals.pack(padx=5,pady=5)
bEigVects = Button(gBotones,text = "Eigenvectores",\
                   command=lambda:\
                   eigVect(lstMatrices.get(lstMatrices.curselection())))
bEigVects.pack(padx=5,pady=5)


scrlMatrices = Scrollbar(gLista)
lstMatrices = Listbox(gLista,yscrollcommand=scrlMatrices,exportselection=0)

lstMatrices.config(height=3,width=10)
lstMatrices.grid(row =0,column =0)


scrlMatrices.grid(row = 0, column =1)
scrlMatrices.config(command=lstMatrices.yview)

def init():
    
    fn = Toplevel()
    lbColumna = Label(fn,text="Columnas",font=('Arial',9))
    lbColumna.grid(row=0,column=0,padx=5,pady=10)
    lbFila = Label(fn,text="Filas",font=('Arial',9))
    lbFila.grid(row=0,column=1,padx=5,pady=10)

    entColumna = Entry(fn,textvariable=1,width = 10)
    entColumna.grid(row=1,column=0,padx=5,pady=10)
    entFila = Entry(fn,textvariable=2,width =10)
    entFila.grid(row=1,column=1,padx=5,pady=10)

    btnCrear = Button(fn, text="Crear",width = 10,\
                      command = lambda:\
                      crearMatriz(int(Entry.get(entFila)),\
                                  int(Entry.get(entColumna))))
    btnCrear.grid(row=2,column=1)
    


    def crearMatriz(fila, columna):
        entFila.delete(0,END)
        entColumna.delete(0,END)
        fn.destroy()
        fx = Toplevel()
        
        Svar = list()
        cmpLb = LabelFrame(fx,text = "Matriz")
        cmpLb.pack()
        cmpBt = LabelFrame(fx,text="Nombre de la matriz")
        cmpBt.pack()
        
        
        for i in range(0,fila):
            b = list()
            
            for j in range(0,columna):
                b.insert(j,StringVar())
                entDt = Entry(cmpLb, \
                              textvariable = b[j],width=5)
                entDt.grid(row = i, column = j)
                

            Svar.insert(j,b)
        entNombre = Entry(cmpBt,textvariable=4,width=10)
        entNombre.grid(row=0,column = 0)
        btn = Button(cmpBt, text="Aceptar",\
                     command = lambda:Aceptar(Svar,Entry.get(entNombre)))
        btn.grid(row = 0,column = 1 )

        def Aceptar(Svar,Nombre):
            entNombre.delete(0,END)
            global matrices
            global diccionario
            for i in range(0,fila):

                for j in range(0,columna):
                    
                    Svar[i][j] = Svar[i][j].get()
                
            matrices.append(Svar)
        
            lstMatrices.insert(END,Nombre)
            diccionario[Nombre]=matrices[-1]
            
            fx.destroy()
            
            t.insert(END,"Matriz creada exitosamente!\n\n")
            
def mostrar(Matriz,Nombre):
    
    try:
        t.insert(END,(Nombre + " = \n"))
        for i in range(0,len(Matriz)):
            t.insert(END,"\t")
            t.insert(END,Matriz[i])
            t.insert(END,"\n")
    except TypeError:
        t.insert(END,(Nombre + "="))
        t.insert(END,"\t")
        t.insert(END, Matriz)
        t.insert(END,"\n")
            
          
    

def onSelect(evt):
    
    if (lstMatrices.size()== 0):
        try:
            t.insert(END,"no hay nada en la lista seleccionado\n")
        except Exception:
            t.insert(END, "hubo un Error \n")
        pass
    else:
        fn=Toplevel()
        lb=Label(fn,text ="Mostrar matriz en pantalla")
        lb.pack(padx=5,pady=5)
        btnSi = Button(fn,text="Si",command = lambda: si() )
        btnSi.pack(side = LEFT,padx=5,pady=5)
        btnNo = Button(fn,text ="No",command = lambda: no())
        btnNo.pack(side=RIGHT,padx=5,pady=5)
    def no():
        fn.destroy()
        fx = Toplevel()
        string = "Matriz " + lstMatrices.get(lstMatrices.curselection())+\
                 " seleccionada"
        lb = Label(fx,text =string)
        lb.pack(padx =5,pady=5)
        btn = Button(fx,text="Ok",command=lambda:fx.destroy())
        btn.pack(padx=5,pady=5)
        lstMatrices.get(lstMatrices.curselection())  
    def si():
        
        mostrar(diccionario[lstMatrices.get(lstMatrices.curselection())],\
                    lstMatrices.get(lstMatrices.curselection()))
        fn.destroy()

lstMatrices.bind('<<ListboxSelect>>',onSelect)

def gauss(Nombre):
    fila = len(diccionario[Nombre])
    columna = len(diccionario[Nombre][0])
    if((fila + 1) == columna):
    
        t.insert(END,"\n")
        m = Matrix(diccionario[Nombre])
        res = m.rref()
        t.insert(END, "Resultado = \n")
        c = trans(res[0])
        nuevoNombre="ans("+Nombre+")"
        mostrar(c,Nombre)
        guardar(c,Nombre,nuevoNombre)
    else:
        t.insert(END, "La matriz fue resuelta pero no tiene un resultado util \n")

def determinante(Nombre):
    if(len(diccionario[Nombre]) ==len(diccionario[Nombre][0])):
        t.insert(END,"\n")
        m = Matrix(diccionario[Nombre])
        res = m.det()
        nuevoNombre = "det("+Nombre+" = "
        guardar(res,nuevoNombre)
        
        t.insert(END,"Determinante = \t")
        t.insert(END,res)
        t.insert(END,"\n")
    else:
        t.insert(END,"La matriz no es cuadrada \n")

def eigVal(Nombre):
    fila = len(diccionario[Nombre])
    columna = len(diccionario[Nombre][0])
    if(columna== fila):
        t.insert(END,"\n")
        m = Matrix(diccionario[Nombre])
        res = m.eigenvals()
        nuevoNombre = "EigenValor("+Nombre+")"
        t.insert(END,"Eigen Valores = \t")
        t.insert(END,res)
        t.insert(END,"\n")
    else:
        t.insert(END,"La matriz no es cuadrada \n")
   

def eigVect(Nombre):
    fila = len(diccionario[Nombre])
    columna = len(diccionario[Nombre][0])
    if(columna== fila):
        t.insert(END,"\n")
        m = Matrix(diccionario[Nombre])
        res = m.eigenvects()
        t.insert(END,"Eigen Valores = \n")
        t.insert(END,res)
        t.insert(END,"\n")
        nuevoNombre = "EigVector("+Nombre+")"
        guardar(m,nuevoNombre)
    else:
        t.insert(END,"La matriz no es cuadrada \n")
    

def Inversa(Nombre):
    m = Matrix(diccionario[Nombre])
    try:
        res = m.inv()
    except:
        t.insert(END,"det = 0, la matriz no tiene inversa")
    c = trans(res)
    t.insert(END,"\n")
    t.insert(END,"Resultado de la inversa = \t")
    t.insert(END,"\n")
    nuevoNombre= Nombre + "^-1"
    mostrar(c,nuevoNombre)
    guardar(c,nuevoNombre)
    
def Suma(Nombre):
    m = Matrix(diccionario[Nombre])
    f = Toplevel()
    scrl = Scrollbar(f )
    l = Listbox(f,yscrollcommand=scrl)
    l.grid(row =1, column =0)
    scrl.config(command=l.yview)
    scrl.grid(row=1,column=1)
    btn = Button(f, text="Sumar", command = lambda: Operacion(m,l.get(l.curselection()),Nombre))
    btn.grid(row=2,column=0)
    l.bind('<<ListboxSelect>>',onSelect)
    for item in diccionario:
        l.insert(END, item)

    def Operacion(m, Nombre2,Nombre):
        m2 = Matrix(diccionario[Nombre2])
        
        res = m + m2
        c = trans(res)
           
        nuevoNombre = Nombre +" + "  + Nombre2 
        
        mostrar(c,nuevoNombre)
        t.insert(END,"\n")
        guardar(c,nuevoNombre)
        f.destroy()
    t.insert(END,"\n")
def Resta(Nombre):
    m = Matrix(diccionario[Nombre])
    f = Toplevel()
    scrl = Scrollbar(f )
    l = Listbox(f,yscrollcommand=scrl)
    l.grid(row =1, column =0)
    scrl.config(command=l.yview)
    scrl.grid(row=1,column=1)
    btn = Button(f, text="Restar", command = lambda: Operacion(m,l.get(l.curselection()),Nombre))
    btn.grid(row=2,column=0)
    l.bind('<<ListboxSelect>>',onSelect)
    for item in diccionario:
        l.insert(END, item)

    def Operacion(m, Nombre2,Nombre):
        m2 = Matrix(diccionario[Nombre2])
        res = m - m2
        c = trans(res)
        nuevoNombre = Nombre +" - "  + Nombre2 
        mostrar(c,nuevoNombre)
        t.insert(END,"\n")
        guardar(c,nuevoNombre)
        f.destroy()
    t.insert(END,"\n")
def Multiplicacion(Nombre):
    m = Matrix(diccionario[Nombre])
    f = Toplevel()
    scrl = Scrollbar(f )
    l = Listbox(f,yscrollcommand=scrl)
    l.grid(row =1, column =0)
    scrl.config(command=l.yview)
    scrl.grid(row=1,column=1)
    btn = Button(f, text="Multiplicar", command = lambda: Operacion(m,l.get(l.curselection()),Nombre))
    btn.grid(row=2,column=0)
    l.bind('<<ListboxSelect>>',onSelect)
    for item in diccionario:
        l.insert(END, item)

    def Operacion(m, Nombre2,Nombre):
        m2 = Matrix(diccionario[Nombre2])
        res = m * m2
        c = trans(res)
           
        nuevoNombre = Nombre +" x "  + Nombre2 
        
        mostrar(c,nuevoNombre)
        t.insert(END,"\n")
        guardar(c,nuevoNombre)
        f.destroy()
    t.insert(END,"\n")
def trans(m):
    row = list()
    col = list()
    contador = 1
    j =0
    for i in range(0,len(m)):
          
        col.insert(contador,m[i])
        if(contador == (len(m.row(0)))):
            row.insert(j,col)
            col = list()
            j+=1

            contador = 0      
        contador += 1
    return row
def guardar(matrix,Nombre):
    matrices.append(matrix)
    diccionario[Nombre]=matrices[-1]
    lstMatrices.insert(END,Nombre)
    
root.mainloop()    
