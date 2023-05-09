from tkinter import *
from textblob import TextBlob


def check_spelling():
    
    a = TextBlob(spell_check.get())
    spell = Label(window, text="The Correct Spelling is : ", font=("Arial", 30, "bold"), bg="grey")
    spell.pack()
    correct_text = Label(window, text=str(a.correct()), font=("Arial", 45, "bold"), bg="lightpink")
    correct_text.pack()


window = Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background="beige")

text_heading = Label(window, text="Spelling Checker", font=("Arial", 50, "bold"), bg="darkcyan", fg="black")
text_heading.pack()

text_check = Label(window, text="Enter the Spelling", font=("Arial", 35, "bold"), bg="burlywood", fg="midnightblue")
text_check.pack()

spell_check = Entry(window, font=("Arial", 45, "bold"), width=500, bg="lightblue")
spell_check.pack()

check_button = Button(window, text="Check!!", font=("Arial", 30, "bold"), bg="crimson", fg="white", command=check_spelling)
check_button.pack()

window.mainloop()
