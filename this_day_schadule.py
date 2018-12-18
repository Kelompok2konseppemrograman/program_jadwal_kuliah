from tkinter import *
from window import myWindow
from datetime import date
import library.List as List


#Main function
#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")

def main():
	display = ""
	if (hari == "Monday"):
		display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[0], List.list_mapel[0], List.list_waktu[0], List.list_kelas[1], List.list_dosen[0])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[2], List.list_waktu[2], List.list_kelas[9], List.list_dosen[2])
	elif(hari == "Tuesday"):
		display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[1], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[1], List.list_waktu[1], List.list_kelas[0], List.list_dosen[1])
	elif(hari == "Wednesday"):
		display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[2], List.list_mapel[3], List.list_waktu[0], List.list_kelas[8], List.list_dosen[3])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[4], List.list_waktu[1], List.list_kelas[0], List.list_dosen[4])
	elif(hari == "Thursday"):
		display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[3], List.list_mapel[6], List.list_waktu[1], List.list_kelas[5], List.list_dosen[6])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[5], List.list_waktu[0], List.list_kelas[6], List.list_dosen[5])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}\n".format(List.list_mapel[10], List.list_waktu[3], List.list_kelas[4], List.list_dosen[10])
	elif(hari == "Friday"):
		display +="\n{}\n{} | {} | {}\n{}".format(List.list_hari[4], List.list_mapel[7], List.list_waktu[0], List.list_kelas[2], List.list_dosen[7])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[8], List.list_waktu[1], List.list_kelas[2], List.list_dosen[8])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(List.list_mapel[9], List.list_waktu[3], List.list_kelas[0], List.list_dosen[9])
	elif(hari == "Saturday"):
		display +="JADWAL KOSONG"
	elif(hari == "Sunday"):
		display +="JADWAL KOSONG"

	message['text'] = display  
Label(myWindow, text="JADWAL HARI INI", font="none 16", relief="sunken").pack()
message = Label(myWindow, text="", font="none 14")
message.pack()