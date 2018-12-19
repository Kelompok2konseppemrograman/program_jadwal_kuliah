from tkinter import *
from window import myWindow
import library.dictionary as dicti

#search box function
def box():
    input_ = entry_1.get().upper()
    display = ""
    sunken = ""
    if input_ == "SENIN":
    	sunken +="JADWAL HARI SENIN"
    	display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["a"], dicti.dict_mapel["a"], dicti.dict_waktu["a"], dicti.dict_kelas["b"], dicti.dict_dosen["a"])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["b"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["b"])
    	display +="\n--------------------------------------------"
    	display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["c"], dicti.dict_waktu["c"], dicti.dict_kelas["j"], dicti.dict_dosen["c"])
    elif input_ == "SELASA":
        sunken +="JADWAL HARI SELASA"
        display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["b"], dicti.dict_mapel["d"], dicti.dict_waktu["a"], dicti.dict_kelas["i"], dicti.dict_dosen["d"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["b"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["b"])
    elif input_ == "RABU":
        sunken +="JADWAL HARI RABU"
        display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["c"], dicti.dict_mapel["d"], dicti.dict_waktu["a"], dicti.dict_kelas["i"], dicti.dict_dosen["d"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["e"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["e"])
    elif input_ == "KAMIS":
        sunken +="JADWAL HARI KAMIS"
        display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["d"], dicti.dict_mapel["g"], dicti.dict_waktu["b"], dicti.dict_kelas["f"], dicti.dict_dosen["g"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["f"], dicti.dict_waktu["a"], dicti.dict_kelas["g"], dicti.dict_dosen["f"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}\n".format(dicti.dict_mapel["k"], dicti.dict_waktu["d"], dicti.dict_kelas["e"], dicti.dict_dosen["k"])
    elif input_ == "JUMAT":
        sunken +="JADWAL HARI JUMAT"
        display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["e"], dicti.dict_mapel["h"], dicti.dict_waktu["a"], dicti.dict_kelas["c"], dicti.dict_dosen["h"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["i"], dicti.dict_waktu["b"], dicti.dict_kelas["c"], dicti.dict_dosen["i"])
        display +="\n--------------------------------------------"
        display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["j"], dicti.dict_waktu["d"], dicti.dict_kelas["a"], dicti.dict_dosen["j"])

    #exception hendling
    try:
        if (input_ == "SABTU"):
            raise NameError ("hari yang anda masukan tidak memiliki jadwal")
        elif (input_ == "MINGGU"):
        	raise NameError ("hari yang anda masukan tidak memiliki jadwal")
        elif (input_ == "JUMAT"):
            raise NameError ("sampai jam tiga")
    except NameError:
        display += "hari yang anda masukan tidak memiliki jadwal"
    	
    sunken_label['text'] = sunken # update label 
    message['text'] = display     # update label
    entry_1.delete(0, END)        # clear entry
#variable untuk menampung fungsi entry dan button
entry_1 = Entry(myWindow)
button_1 = Button(myWindow, text="cari jadwal", command=box)
#deklarasi variable entry dan button yg menampung fungsi entry dan button
entry_1.pack()
button_1.pack()
#variable untuk menampung fungsi label dan deklarasi variable
sunken_label = Label(myWindow, text="", font="none 16", relief="sunken")
sunken_label.pack()
#variable untuk menampung fungsi label dan deklarasi variable
message = Label(myWindow, text="", font="none 14")
message.pack()