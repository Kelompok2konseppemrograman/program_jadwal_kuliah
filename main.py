from tkinter import *
from window import myWindow
<<<<<<< HEAD
import lib
from this_day_schadule import main
from search_box_funtion import box
=======
import this_day_schadule as tds
import search_box_funtion as sbf
>>>>>>> 799a6f8b40cdc771beed176d3571285b3786850f


#title
myWindow.title("Jadwal Kuliah")

<<<<<<< HEAD
pilihan = 0
while (pilihan < 3):
    pilihan = lib.option()
    print(pilihan)
    if(pilihan==3 | pilihan==0):
        break
    elif(pilihan==1):
        main()
        break
    elif(pilihan==2):
        box()
        break

=======
>>>>>>> 799a6f8b40cdc771beed176d3571285b3786850f
#This day schadule
tds.main()

#search_box_funtion
sbf.box()

#Ukuran window yang ditampilkan		
myWindow.geometry("900x900")

#Main window
myWindow.mainloop()
