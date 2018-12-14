from tkinter import *
from window import myWindow
import lib
import this_day_schadule as tds
import search_box_funtion as sbf


#title
myWindow.title("Jadwal Kuliah")

pilihan = 0
while (pilihan < 3):
    pilihan = lib.option()
    print(pilihan)
    if(pilihan==3 | pilihan==0):
        break
    elif(pilihan==1):
        tds.main()
        break
    elif(pilihan==2):
        sbf.box()
        break

#This day schadule
#tds.main()

#search_box_funtion
#sbf.box()

#Ukuran window yang ditampilkan		
myWindow.geometry("900x900")

#Main window
myWindow.mainloop()
