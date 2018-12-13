from tkinter import *
from window import myWindow
from datetime import date
import library.List as List
import library.lib as lib

#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")


#Main window
myWindow.title("Jadwal Kuliah")

#Label display jadwal hari ini
Label(myWindow, text="JADWAL HARI INI", font="none 16", relief="sunken").pack()
lib.main()

#search box function
def box():


    input_ = entry_1.get().upper()
    sunken = "JADWAL HARI " + input_.upper()
    display = ""
    if input_ == "SENIN":
        display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[0], List.list_mapel[0], List.list_waktu[0], List.list_kelas[1], List.list_dosen[0])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(List.list_mapel[2], List.list_waktu[2], List.list_kelas[9], List.list_dosen[2])
    elif input_ == "SELASA":
    	display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[1], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1])
    elif input_ == "RABU":
        display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[2], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(List.list_mapel[4], List.list_waktu[1], List.list_kelas[0], List.list_dosen[4])
    elif input_ == "KAMIS":
    	display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[3], List.list_mapel[6], List.list_waktu[1], List.list_kelas[5], List.list_dosen[6])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(List.list_mapel[5], List.list_waktu[0], List.list_kelas[6], List.list_dosen[5])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}\n".format(List.list_mapel[10], List.list_waktu[3], List.list_kelas[4], List.list_dosen[10])
    elif input_ == "JUMAT":
    	display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[4], List.list_mapel[7], List.list_waktu[0], List.list_kelas[2], List.list_dosen[7])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(List.list_mapel[8], List.list_waktu[1], List.list_kelas[2], List.list_dosen[8])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(List.list_mapel[9], List.list_waktu[3], List.list_kelas[0], List.list_dosen[9])

    try:
        input_ = str(entry_1.get().upper())
        if (input_ == "SABTU"):
            raise NameError ("hari yang anda masukan tidak memiliki jadwal")
        elif (input_ == "MINGGU"):
        	raise NameError ("hari yang anda masukan tidak memiliki jadwal")
    except NameError:
        Label(myWindow, text="hari yang anda masukan tidak memiliki jadwal", font="none 14").pack()
        raise    
    	
    sunken_label['text'] = sunken # update label 
    message['text'] = display     # update label
    entry_1.delete(0, END)        # clear entry


#entry & button
entry_1 = Entry(myWindow)
button_1 = Button(myWindow, text="cari jadwal", command=box)

#deklarasi entry & button
entry_1.pack()
button_1.pack()

#deklarasi box function 
sunken_label = Label(myWindow, text="", font="none 16", relief="sunken")
sunken_label.pack()
message = Label(myWindow, text="", font="none 14")
message.pack()

#Ukuran window yang ditampilkan		
myWindow.geometry("900x900")

#Main window
myWindow.mainloop()
