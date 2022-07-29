#-------------------------------
# ------ CALCULAR EL IVA -------
#-------------------------------

from os import preadv
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


#-------------------------
#--FUNCIONES DE LA APP----
#-------------------------

def sumar():
    i = int(x.get())*0.19
    z = int(x.get())+i
    t_resultados.insert(INSERT ," El Iva de su producto es " + x.get() + " de "  + str(i) + " es "  + str(z)+ "\n")

def borrar():
    messagebox.showinfo("borrar 1.0" , "los datos serán borrados...")
    x.set("")
    t_resultados.delete("1.0" , "end")



def salir():
     messagebox.showinfo("La appp se cerrarrá ...")
     ventana_principal.destroy()


#------------------------
#---ventana principal----
#------------------------

 # Se declara una variable que llamamos ventana_principal y que se adquiere las caracteristicas de un objeto TK 
 

ventana_principal=Tk()
#titulo de la ventana 
ventana_principal.title("iris Alviarez")

#Establecer tamaño de la venta
ventana_principal.geometry("800x500")

ventana_principal.iconbitmap("")

#deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="black")

#agregamos un widget a la ventana principal
letrero = Label(text="\n\nSistemas, La Mejor!!\n\n",bg="snow")
letrero.pack()

letrero2 = Label(text="\n\nIris Alviarez",bg="snow")
letrero2.pack()

letrero3 = Label(text="\n\nColegio San Jose de Guanenta",bg="snow")
letrero.pack()

#-------------------------
#--Variables globales----
#-------------------------

x= StringVar()
i = IntVar()
z = IntVar()




#----------------------
#----frame entrada-----
#----------------------

frame_entrada = Frame(ventana_principal) 
frame_entrada.config(bg="olive drab", width=780, height=240)
frame_entrada.place(x=10,y=10)

 #Etiqueta para el subtitulo de la app
subtitule = Label(frame_entrada, text="Especialidad de sistemas")
subtitule.config(bg="olive drab", fg="black", font=("Times New Roman", 12))
subtitule.place(x=280, y=40)

 #Etiqueta para el subtitulo2 de la app
subtitule2 = Label(frame_entrada, text="CALCULAR EL IVA")
subtitule2.config(bg="olive drab", fg="black", font=("Times New Roman", 15), anchor = CENTER)
subtitule2.place(x=270, y=70)

# Imagen - logo de la app
logo = PhotoImage(file="iva1.png")
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10 , y=10)

#Etiqueta para valor a
etiq_a = Label(frame_entrada , text=" Introduzca el valor de su producto = ")
etiq_a.config(bg="olive drab", fg="black", font=("Arial", 15), anchor = CENTER)
etiq_a.place(x=240 , y=120)

#entry para el valor a
entry_a = Entry(frame_entrada , width=4, textvariable=x)
entry_a.config(font=("Arial" , 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=590 , y=115)


frame_operaciones = Frame(ventana_principal) 
frame_operaciones.config(bg="forest green", width=780, height=120)
frame_operaciones.place(x=10,y=260)

 #Button de suma
bt_sum = PhotoImage(file="iva.png")
bt_sumar=Button(frame_operaciones ,image=bt_sum, width=105 , height=105, command=sumar)
bt_sumar.place(x=116 , y=7)


#button de salir
bt_sal = PhotoImage(file="saliva.png")
bt_salir=Button(frame_operaciones ,image=bt_sal, width=105 , height=105, command=salir)
bt_salir.place(x=558 , y=7)


#button de borrar
bt_bor = PhotoImage(file="borrar.png")
bt_borrar=Button(frame_operaciones , image=bt_bor, width=105 , height=105 , command=borrar)
bt_borrar.place(x=337 , y=7)

frame_resultados = Frame(ventana_principal) 
frame_resultados.config(bg="Blue", width=780, height=100)
frame_resultados.place(x=10,y=390)

#------------------------------
# Area de texto para resultados 
#------------------------------


t_resultados = Text(frame_resultados , width=51 , height=3)
t_resultados.config(bg="snow3" , fg="green" , font=("Courier" , 20))
t_resultados.pack()


#Se ejecuta el metodo mainloop de la clase Tk a traves de la istancia ventana principal. Este metedo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en el boton,escribir en caja de texto, ect. Cada acción del usuario se conoce como un evento. El método mainloop es bucle infinito

ventana_principal.mainloop()
 
