from tkinter import *
from window import myWindow
from datetime import date
import library.List as List


#Main function
#fungsi module datetime
detect_date = date.today()
hari = detect_date.strftime("%A")

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
		Label(myWindow, text="{} | {} | {}\n{}\n".format(List.list_mapel[10], List.list_waktu[3], List.list_kelas[4], List.list_dosen[10]), font="none 14").pack()
	elif(hari == "Friday"):
		Label(myWindow, text="{}\n{} | {} | {}\n{}".format(List.list_hari[4], List.list_mapel[7], List.list_waktu[0], List.list_kelas[2], List.list_dosen[7]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[8], List.list_waktu[1], List.list_kelas[2], List.list_dosen[8]), font="none 14").pack()
		Label(myWindow, text="--------------------------------------------", font="none 14").pack()
		Label(myWindow, text="{} | {} | {}\n{}".format(List.list_mapel[9], List.list_waktu[3], List.list_kelas[0], List.list_dosen[9]), font="none 14").pack()


#fungsi exception
def exception():
	try:
		input_ = str(entry_1.get().upper())
		if input_ == "SABTU":
			raise NameError ("hari yang anda masukan tidak memiliki jadwal")
	except NameError:
		Label(myWindow, text="hari yang anda masukan tidak memiliki jadwal", font="none 14").pack()
		raise
