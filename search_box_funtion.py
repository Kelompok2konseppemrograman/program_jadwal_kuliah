from tkinter import *
from window import myWindow
import library.List as List

#search box function
def box():
    input_ = entry_1.get().upper()
    display = ""
    sunken = ""
    if input_ == "SENIN":
    	sunken +="JADWAL HARI SENIN"
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

    #exception hendling
    try:
        input_ = str(entry_1.get().upper())
        if (input_ == "SABTU"):
            raise NameError ("hari yang anda masukan tidak memiliki jadwal")
        elif (input_ == "MINGGU"):
        	raise NameError ("hari yang anda masukan tidak memiliki jadwal")
    except NameError:
        display += "myWindow, text=hari yang anda masukan tidak memiliki jadwal, font=none 14).pack()"
        raise    
    	
    sunken_label['text'] = sunken # update label 
    message['text'] = display     # update label
    entry_1.delete(0, END)        # clear entry
entry_1 = Entry(myWindow)
button_1 = Button(myWindow, text="cari jadwal", command=box)
entry_1.pack()
button_1.pack()
sunken_label = Label(myWindow, text="", font="none 16", relief="sunken")
sunken_label.pack()
message = Label(myWindow, text="", font="none 14")
message.pack()