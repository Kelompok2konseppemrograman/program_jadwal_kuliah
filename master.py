from tkinter import *
from datetime import date
import List

#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")


#Main window
myWindow = Tk()
myWindow.title("Jadwal Kuliah")


#Metode
def main():
	if (hari == "Monday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[0], List.list_mapel[0], List.list_waktu[0], List.list_kelas[1], List.list_dosen[0]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[2], List.list_waktu[2], List.list_kelas[9], List.list_dosen[2]), font="none 14").pack()
	elif(hari == "Tuesday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[1], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1]), font="none 14").pack()
	elif(hari == "Wednesday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[2], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[4], List.list_waktu[1], List.list_kelas[0], List.list_dosen[4]), font="none 14").pack()
	elif(hari == "Thursday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[3], List.list_mapel[6], List.list_waktu[1], List.list_kelas[5], List.list_dosen[6]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[5], List.list_waktu[0], List.list_kelas[6], List.list_dosen[5]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[10], List.list_waktu[3], List.list_kelas[4], List.list_dosen[10]), font="none 14").pack()
	elif(hari == "Friday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[4], List.list_mapel[7], List.list_waktu[0], List.list_kelas[2], List.list_dosen[7]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[8], List.list_waktu[1], List.list_kelas[2], List.list_dosen[8]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[9], List.list_waktu[3], List.list_kelas[0], List.list_dosen[9]), font="none 14").pack()


#Label display jadwal hari ini
Label(myWindow, text="JADWAL HARI INI", font="none 16", relief="sunken").pack()
main()

#Label display jadwal hari yang dicari
Label(myWindow, text=" ").pack()
def box():
	input_ = entry_1.get()
	display = "JADWAL HARI " + input_.upper()
	label_display = Label(myWindow, font="none 16", relief="sunken")
	label_display["text"] = display
	label_display.pack()
	if (input_.upper() == "SENIN"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[0], List.list_mapel[0], List.list_waktu[0], List.list_kelas[1], List.list_dosen[0]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[2], List.list_waktu[2], List.list_kelas[9], List.list_dosen[2]), font="none 14").pack()
	elif(input_.upper() == "SELASA"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[1], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1]), font="none 14").pack()
	elif(input_.upper() == "RABU"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[2], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[4], List.list_waktu[1], List.list_kelas[0], List.list_dosen[4]), font="none 14").pack()
	elif(input_.upper() == "KAMIS"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[3], List.list_mapel[6], List.list_waktu[1], List.list_kelas[5], List.list_dosen[6]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[5], List.list_waktu[0], List.list_kelas[6], List.list_dosen[5]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[10], List.list_waktu[3], List.list_kelas[4], List.list_dosen[10]), font="none 14").pack()
	elif(input_.upper() == "JUMAT"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[4], List.list_mapel[7], List.list_waktu[0], List.list_kelas[2], List.list_dosen[7]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[8], List.list_waktu[1], List.list_kelas[2], List.list_dosen[8]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[9], List.list_waktu[3], List.list_kelas[0], List.list_dosen[9]), font="none 14").pack()

#Fungsi entry dan button
entry_1 = Entry(myWindow)
button_1 = Button(myWindow, text="cari jadwal", command=box)


#Deklarasi fungsi entry dan button
entry_1.pack()
button_1.pack()

#Ukuran window yang ditampilkan		
myWindow.geometry("900x900")

#Main window
myWindow.mainloop()
