#rizky jelek

#rizky ganteng
from tkinter import *
from window import myWindow
import this_day_schadule as tds
import search_box_funtion as sbf


#title
myWindow.title("Jadwal Kuliah")

#This day schadule
tds.main()

#search_box_funtion
sbf.box()

#Ukuran window yang ditampilkan     
myWindow.geometry("900x900")

#Main window
myWindow.mainloop()
