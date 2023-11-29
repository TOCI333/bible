
import tkinter
import customtkinter
from xml.dom import minidom

doc=minidom.parse("C:\Users\Alumno\Desktop\Nueva carpeta\Reina-Valera 1960.xml")
book=doc.getElementsbyTagname("b")
print(book)
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  
app.geometry("400x240")
app.title("Biblia") 

def button_function():
    #print("button pressed")
  label = customtkinter.CTkLabel(master=app, text="Biblia")
  label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
  label.grid(row=1, column=0, padx=20, pady=20, sticky="ew")  

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="MOSTRAR", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



app.mainloop()
