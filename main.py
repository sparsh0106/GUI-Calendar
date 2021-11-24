# IMPORTING THE DIFFERENT LIBRARIES
from tkinter import *
import calendar
import pywhatkit



def showCal():

	def sparsh_agarwal():
		print(pywhatkit.sendwhatmsg_instantly('+91 9312422987', 'Hi, I want to raise some errors regarding the calendar app you have made. Kindly note my errors : \n 1. <error1> \n 2. <error2> \n 3. <error3> \n I hope you look into the errors carefully and fix them. \n Thanking you \n <NAME>'))


	new_gui = Tk()

	new_gui.title("CALENDER")
	fetch_year = int(year_field.get())
	cal_content = calendar.calendar(fetch_year)
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 20)

	RAISE_COMPLAINT_BUTTON = Button(new_gui, text = "Raise Complaint!", bg = 'red', fg = 'blue', activebackground = 'yellow', command = sparsh_agarwal).grid()


	new_gui.mainloop()



if __name__ == "__main__" :


	gui = Tk()
	gui.config(background = "white")
	gui.title("CALENDER")
	gui.geometry("250x140")
	cal = Label(gui, text = "CALENDAR", bg = "dark gray", font = ("times", 28, 'bold'))
	year = Label(gui, text = "Enter Year", bg = "light green")
	year_field = Entry(gui)
	Show = Button(gui, text = "Show Calendar", fg = "Black", bg = "Red", command = showCal)
	cal.grid(row = 1, column = 1)
	year.grid(row = 2, column = 1)
	year_field.grid(row = 3, column = 1)
	Show.grid(row = 4, column = 1)




	gui.mainloop()
