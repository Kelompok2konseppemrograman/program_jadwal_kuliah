from tkinter import *
from window import myWindow
from datetime import date
import library.dictionary as dicti

#Main function
#fungsi module datetime
detect_date = date.today()			#Menampilkan tanggal dengan format YY-MM-DD
hari = detect_date.strftime("%A")	#Menampilkan Hari dengan format bahasa inggris

def main():
	display = ""
	if (hari == "Monday"):
		display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["a"], dicti.dict_mapel["a"], dicti.dict_waktu["a"], dicti.dict_kelas["b"], dicti.dict_dosen["a"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["b"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["b"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["c"], dicti.dict_waktu["c"], dicti.dict_kelas["k"], dicti.dict_dosen["c"])
	elif(hari == "Tuesday"):
		display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["b"], dicti.dict_mapel["d"], dicti.dict_waktu["a"], dicti.dict_kelas["i"], dicti.dict_dosen["d"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["b"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["b"])
	elif(hari == "Wednesday"):
		display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["c"], dicti.dict_mapel["d"], dicti.dict_waktu["a"], dicti.dict_kelas["i"], dicti.dict_dosen["d"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["e"], dicti.dict_waktu["b"], dicti.dict_kelas["a"], dicti.dict_dosen["e"])
	elif(hari == "Thursday"):
		display +="\n{}\n{} | {} | {}\n{}".format(dicti.dict_hari["d"], dicti.dict_mapel["g"], dicti.dict_waktu["b"], dicti.dict_kelas["f"], dicti.dict_dosen["g"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}".format(dicti.dict_mapel["f"], dicti.dict_waktu["a"], dicti.dict_kelas["g"], dicti.dict_dosen["f"])
		display +="\n--------------------------------------------"
		display +="\n{} | {} | {}\n{}\n".format(dicti.dict_mapel["k"], dicti.dict_waktu["d"], dicti.dict_kelas["e"], dicti.dict_dosen["k"])
	elif(hari == "Friday"):
		display +="JADWAL kosong"
	elif(hari == "Saturday"):
		display +="JADWAL KOSONG"
	elif(hari == "Sunday"):
		display +="JADWAL KOSONG"

	message['text'] = display  
Label(myWindow, text="JADWAL HARI INI", font="none 16", relief="sunken").pack()
message = Label(myWindow, text="", font="none 14")
message.pack()