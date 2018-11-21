from tkinter import *
from datetime import date


#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")

#list data
list_hari = ["Senin","Selasa", "Rabu", "Kamis", "Jum'at"]
list_mapel = ["Design Thinking"]
list_waktu = ["09:45-11:25"]
list_ruang = ["Ruang 2F"]
list_dosen = ["Arif Himawan, S.Kom., M.Eng"]

#Main window
myWindow = Tk()
myWindow.title("Jadwal Kuliah")

#Label display jadwal hari ini
Label(myWindow, text="JADWAL HARI INI", font="none 16", relief="sunken").grid(column=2, row=0)
if (hari == "Monday"):
	Label(myWindow, text=list_hari[0], font="none 14").grid(column=2, row=1)
	Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=2)
	Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=3)
elif(hari == "Tuesday"):
	Label(myWindow, text=list_hari[1], font="none 14").grid(column=2, row=1)
	Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=2)
	Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=3)
elif(hari == "Wednesday"):
	Label(myWindow, text=list_hari[2], font="none 14").grid(column=2, row=1)
	Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=2)
	Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=3)
elif(hari == "Thursday"):
	Label(myWindow, text=list_hari[3], font="none 14").grid(column=2, row=1)
	Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=2)
	Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=3)
else:
	Label(myWindow, text=list_hari[4], font="none 14").grid(column=2, row=1)
	Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=2)
	Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=3)


#Label display jadwal hari yang dicari
Label(myWindow, text=" ").grid(column=2, row=4)
def box():
	input_ = entry_1.get()
	display = "JADWAL HARI " + input_
	label_display = Label(myWindow, font="none 16", relief="sunken")
	label_display["text"] = display
	label_display.grid(column=2, row=5)
	if (input_ == "SENIN"):
		Label(myWindow, text=list_hari[0], font="none 14").grid(column=2, row=6)
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=7)
		Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=8)
	elif(input_ == "SELASA"):
		Label(myWindow, text=list_hari[1], font="none 14").grid(column=2, row=6)
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=7)
		Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=8)
	elif(input_ == "RABU"):
		Label(myWindow, text=list_hari[2], font="none 14").grid(column=2, row=6)
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=7)
		Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=8)
	elif(input_ == "KAMIS"):
		Label(myWindow, text=list_hari[3], font="none 14").grid(column=2, row=6)
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=7)
		Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=8)
	else:
		Label(myWindow, text=list_hari[4], font="none 14").grid(column=2, row=6)
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_ruang[0], font="none 14").grid(column=2, row=7)
		Label(myWindow, text=list_dosen[0], font="none 14").grid(column=2, row=8)

	myWindow.update_idletasks()

#Fungsi entry dan button
entry_1 = Entry(myWindow)
button_1 = Button(myWindow, text="cari jadwal", command=box)

#Deklarasi fungsi entry dan button
entry_1.grid(column=0, row=0)
button_1.grid(column=1,row=0)

#Ukuran window yang ditampilkan		
myWindow.geometry("600x300")

#Main window
myWindow.mainloop()
