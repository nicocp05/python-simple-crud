from tkinter import *
from tkinter import messagebox
import sqlite3

#Funciones

def conexionBBDD():
    
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    try: 
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE_USUARIO VARCHAR (50), 
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
        ''')
        messagebox.showinfo("BBDD", "BBDD Creada con exito.")
    except:
        messagebox.showwarning("¡Atención!", "La base de datos ya existe.")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")

    if valor=="yes":
        root.destroy()

def limpiarCampos():

    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miDireccion.set("")
    miPassword.set("")
    textoComentario.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    # miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() + "', '" + miPassword.get() + "','" + miApellido.get() + "','" + miDireccion.get() + "','" + textoComentario.get("1.0", END) + "')")

    datos=miNombre.get(),miPassword.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito")

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPassword.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()    

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + "', PASSWORD='" + miPassword.get() + "', APELLIDO= '" + miApellido.get() + "', DIRECCION= '" + miDireccion.get() + "', COMENTARIOS='" + textoComentario.get("1.0", END) + "' WHERE ID=" + miID.get())
    
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con exito")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con exito")

#Tkiter

root=Tk()

root.title("Simple CRUD")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

#Fields

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPassword=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame, textvariable=miPassword)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#Labels

idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx= 10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx= 10, pady=10)

passwordLabel=Label(miFrame, text="Contraseña:")
passwordLabel.grid(row=2, column=0, padx= 10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, padx= 10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, padx= 10, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=5, column=0, padx= 10, pady=10)

#Botones

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()