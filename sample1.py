from tkinter import *
from datetime import date


#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")

#list data
list_hari = ["senin", "selasa", "rabu", "kamis", "jum'at"]
list_waktu= ["08:00-09:40", "09:45-11:25", "12:30-14:10", "13:15-16:00"]
list_kelas = ["kelas 2a", "kelas 2b", "kelas 2c", "kelas 2d", "kelas 2e", "kelas 2f", "kelas 2g", "kelas 2h",
			 "kelas 3a", "kelas 3b", "kelas 3c", "kelas 3d"]
list_dosen = ["LANDUNG SUDARMANA, S.T.,M.Kom", "SITI FIATUL HASANAH, S.Pd", "ADKHAN SHOLEH, S.Si.,M.Cs", 
			"PUJI WINAR CAHYO, S.Kom.,M.Cs", "RAGIL SURYO RAHARJO, S.Fil", "INDRATI HENDRIK, S.T.h.", "ARIF HIMAWAN, S.Kom.,M.M.,M.",
 			"ALFIRNA RIZQI LAHITANI, S..Kom.,M.Eng", "TITIK RAHMAWATI, S.T.,M.Cs", "ALI ASMU’I, S.Ag.,M.Pd", "AGUNG WIDODO, S.s., M.P.d"]
list_mapel = ["LOGIKA INFORMATIKA", "BAHASA INGGRIS I", "PRAKTIKUM APLIKASI KOMPUTER I ", "KONSEP PEMEROGRAMAN", 
			"PENDIDIKAN PANCASILA", "PENDIDIKAN AGAMA KRISTEN","DESIGN THINGKING", "PENGANTAR TEKNOLOGI INFORMASI & KOMUNIKASI", 
			"PENGANTAR REKAYASA SOFTWARE", "PENDIDIKAN AGAMA ISLAM", "PENDIDIKAN AGAMA KHATOLIK"]


#Main window
myWindow = Tk()
myWindow.title("Jadwal Kuliah")

#Metode
def main():
	if (hari == "Monday"):
		Label(myWindow, text=list_hari[0], font="none 14").pack()
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_kelas[1], font="none 14").pack()
		Label(myWindow, text=list_dosen[0], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[1] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[1], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[2] + "|" + list_waktu[2] + "|" + list_kelas[9], font="none 14").pack()
		Label(myWindow, text=list_dosen[2], font="none 14").pack()
	elif(hari == "Tuesday"):
		Label(myWindow, text=list_hari[1], font="none 14").pack()
		Label(myWindow, text=list_mapel[3] + "|" + list_waktu[0] + "|" + list_kelas[8], font="none 14").pack()
		Label(myWindow, text=list_dosen[3], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[1] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[1], font="none 14").pack()
	elif(hari == "Wednesday"):
		Label(myWindow, text=list_hari[2], font="none 14").pack()
		Label(myWindow, text=list_mapel[3] + "|" + list_waktu[0] + "|" + list_kelas[8], font="none 14").pack()
		Label(myWindow, text=list_dosen[3], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[4] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[4], font="none 14").pack()
	elif(hari == "Thursday"):
		Label(myWindow, text=list_hari[3], font="none 14").pack()
		Label(myWindow, text=list_mapel[6] + "|" + list_waktu[1] + "|" + list_kelas[5], font="none 14").pack()
		Label(myWindow, text=list_dosen[6], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[5] + "|" + list_waktu[0] + "|" + list_kelas[6], font="none 14").pack()
		Label(myWindow, text=list_dosen[5], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[10] + "|" + list_waktu[3] + "|" + list_kelas[4], font="none 14").pack()
		Label(myWindow, text=list_dosen[10], font="none 14").pack()
	elif(hari == "Friday"):
		Label(myWindow, text=list_hari[4], font="none 14").pack()
		Label(myWindow, text=list_mapel[7] + "|" + list_waktu[0] + "|" + list_kelas[2], font="none 14").pack()
		Label(myWindow, text=list_dosen[7], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[8] + "|" + list_waktu[1] + "|" + list_kelas[2], font="none 14").pack()
		Label(myWindow, text=list_dosen[8], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[9] + "|" + list_waktu[3] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[9], font="none 14").pack()


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
		Label(myWindow, text=list_hari[0], font="none 14").pack()
		Label(myWindow, text=list_mapel[0] + "|" + list_waktu[0] + "|" + list_kelas[1], font="none 14").pack()
		Label(myWindow, text=list_dosen[0], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[1] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[1], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[2] + "|" + list_waktu[2] + "|" + list_kelas[9], font="none 14").pack()
		Label(myWindow, text=list_dosen[2], font="none 14").pack()
	elif(input_.upper() == "SELASA"):
		Label(myWindow, text=list_hari[1], font="none 14").pack()
		Label(myWindow, text=list_mapel[3] + "|" + list_waktu[0] + "|" + list_kelas[8], font="none 14").pack()
		Label(myWindow, text=list_dosen[3], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[1] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[1], font="none 14").pack()
	elif(input_.upper() == "RABU"):
		Label(myWindow, text=list_hari[2], font="none 14").pack()
		Label(myWindow, text=list_mapel[3] + "|" + list_waktu[0] + "|" + list_kelas[8], font="none 14").pack()
		Label(myWindow, text=list_dosen[3], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[4] + "|" + list_waktu[1] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[4], font="none 14").pack()
	elif(input_.upper() == "KAMIS"):
		Label(myWindow, text=list_hari[3], font="none 14").pack()
		Label(myWindow, text=list_mapel[6] + "|" + list_waktu[1] + "|" + list_kelas[5], font="none 14").pack()
		Label(myWindow, text=list_dosen[6], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[5] + "|" + list_waktu[0] + "|" + list_kelas[6], font="none 14").pack()
		Label(myWindow, text=list_dosen[5], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[10] + "|" + list_waktu[3] + "|" + list_kelas[4], font="none 14").pack()
		Label(myWindow, text=list_dosen[10], font="none 14").pack()
	elif(input_.upper() == "JUMAT"):
		Label(myWindow, text=list_hari[4], font="none 14").pack()
		Label(myWindow, text=list_mapel[7] + "|" + list_waktu[0] + "|" + list_kelas[2], font="none 14").pack()
		Label(myWindow, text=list_dosen[7], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[8] + "|" + list_waktu[1] + "|" + list_kelas[2], font="none 14").pack()
		Label(myWindow, text=list_dosen[8], font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text=list_mapel[9] + "|" + list_waktu[3] + "|" + list_kelas[0], font="none 14").pack()
		Label(myWindow, text=list_dosen[9], font="none 14").pack()

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
