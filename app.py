import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("First project")
root.iconbitmap("favicon.ico")
img1 = PhotoImage(file="uet.png")

# image mai nearest sy image k pixels set hoty hain 
# antialiasing tkinter sy khtm ho chuka hia

frame = LabelFrame(
    root,
    text="ECAT app...",
    padx=50,
    pady=50,
    background="#007875",
    width=1300,
    height=760
)
frame.pack(padx=5, pady=5)
frame.pack_propagate(False)

questions = [
    "Which one is not a branch of physical sciences?",
    "Which branch of science plays an important role in the development of technology and engineering?",
    "The number of categories in which physical quantities are divided are?",
    "How many types of units are in SI?",
    "In scientific notation numbers are expressed in",
    "Random errors can be reduced by taking?",
    "The uncertainty in a measurement may occur due to",
    "Preftix deca represents",
    "The error in measurement may occur due to?",
    "1024 can be written in scientific notation as?",
]

answers_choice = [
    ["A. chemistry", "B. astronomy", "C. geology", "D. biology"],
    ["A. chemistry", "B. physics", "C. geology", "D. biology"],
    ["one", "two", "three", "four"],
    ["one", "two", "three", "four"],
    ["power of 10", "power of 2", "reciprocal", "decimal"],
    ["average", "difference", "sum", "product"],
    ["limitation of an instrument", "natural variation of the object to be measured", "inadequate of technique",
     "all given in a , b and c"],
    ["10 Raised to power 1", "10 Raised to power 2", "10 Raised to power 3", "10 Raised to power -1"],
    ["inexperience of a person", "the faulty apparantus", "inappropriate method", "due to all reasons in a, b and c"],
    ["1.024x103", "2 Raised to power 10", "0.000976", "1/0.00097"],
]

#widgets created

def login():
    username = entry1.get()
    password = entry2.get()
    if username == "" and password == "":
        messagebox.showerror("Login", "Please enter username and password")
    elif username == "admin" and password == "root":
        messagebox.showinfo("Login", "Login successful")
        label1.destroy()
        label2.destroy()
        label3.destroy()
        entry1.destroy()
        entry2.destroy()
        button.destroy()
        # Show quiz interface
        create_widgets()   
    else:
        messagebox.showerror("Login", "Login failed")

# labels mai user interaction include nahi hota widgets mai hota hai        

label1 = Label(
    root, 
    text="Login Page", 
    font=("Comic Sans MS", 30), 
    background="#007875", 
    fg="black"
)
label1.place(x=500, y=20)    

label2 = Label(
    root, 
    text="Username: ", 
    font=("Comic Sans MS", 20), 
    background="#007875", 
    fg="black"
)
label2.place(x=400, y=190)

label3 = Label(
    root, 
    text="Password: ", 
    font=("Comic Sans MS", 20), 
    background="#007875", 
    fg="black"
)
label3.place(x=400, y=340)

entry1 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black"
)
entry1.place(x=600, y=200)

entry2 = Entry(
    root, 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
    show="."
)
entry2.place(x=600, y=350)

button = Button(
    root, 
    text="Login", 
    font=("Comic Sans MS", 20), 
    background="white", 
    fg="black",
    command=login
)
button.place(x=550, y=500)

def create_widgets():
    global label_image, label_text, btn_start, lbl_instruction, lbl_rules

    create_header()
    create_instruction_label()
    create_start_button()
    create_rules_label()

def start_timer():
    global timer_seconds
    if timer_seconds > 0:
        timer_label.config(text=f"Time left: {timer_seconds} seconds")
        timer_seconds -= 1
        timer_label.after(1000, start_timer)  # Update every second
    else:
        messagebox.showinfo("Timer", "Time's up!")
        root.destroy()

def create_header():
    global label_image, label_text
    label_image = Label(
        frame,
        image=img1,
        background="#007875"
    )
    label_image.pack()

    label_text = Label(
        frame,
        text="Welcome to UET ECAT",
        font=("Comic Sans MS", 24, "bold"),
        bg="#007875"
    )
    label_text.pack(pady=(40, 0))

def create_instruction_label():
    global lbl_instruction
    lbl_instruction = Label(
        frame,
        text="Read the rules\nClick start when you are ready",
        bg="#007875",
        font=("Comic Sans MS", 14),
        justify="center"
    )
    lbl_instruction.pack(pady=(10, 0))

def create_start_button():
    global btn_start
    btn_start = Button(
        frame,
        text="Start",
        command=startButtonPressed, 
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_start.pack(pady=(20, 5))

def create_rules_label():
    global lbl_rules
    lbl_rules = Label(
        frame,
        text="You will get 20 minutes to solve the quiz",
        width=100,
        font=("Times", 14),
        background="#007875",
        foreground="#FACA2F"
    )
    lbl_rules.pack(pady=(10, 0))

def create_skip_submit_buttons():
    global btn_skip, btn_submit
    btn_skip = Button(
        frame,
        text="Skip",
        command=skipQuestion,
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_skip.pack(side=BOTTOM, pady=(5, 5))

    btn_submit = Button(
        frame,
        text="Submit",
        command=calc,
        relief=RAISED,
        border=2,
        background="#007875",
        font=("Comic Sans MS", 16)
    )
    btn_submit.pack(side=BOTTOM, pady=(5, 5))

def start_quiz():
    global lbl_Questions, ques
    lbl_Questions = Label(
        frame,
        text=questions[ques],
        font=("Comic Sans MS", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#007875"
    )
    lbl_Questions.pack(pady=(50, 10))

    global radio_var, r1, r2, r3, r4
    radio_var = IntVar()   # Create an IntVar object to store the selected value
    radio_var.set(-1)   # Initialize the radio button value to -1

    r1 = Radiobutton(
        frame,
        text=answers_choice[ques][0],
        font=("Comic Sans MS", 12),
        value=0,
        variable=radio_var,   # to ensure that only one radio button can be selected at a time
        command=selected,
        background="#007875"
    )
    r1.pack(pady=3)

    r2 = Radiobutton(
        frame,
        text=answers_choice[ques][1],
        font=("Comic Sans MS", 12),
        value=1,
        variable=radio_var,  # to ensure that only one radio button can be selected at a time
        command=selected,
        background="#007875"
    )
    r2.pack(pady=3)

    r3 = Radiobutton(
        frame,
        text=answers_choice[ques][2],
        font=("Comic Sans MS", 12),
        value=2,
        variable=radio_var, # to ensure that only one radio button can be selected at a time
        command=selected,
        background="#007875"
    )
    r3.pack(pady=3)

    r4 = Radiobutton(
        frame,
        text=answers_choice[ques][3],
        font=("Comic Sans MS", 12),
        value=3,
        variable=radio_var, # to ensure that only one radio button can be selected at a time
        command=selected,
        background="#007875"
    )
    r4.pack(pady=3)

def congrats_image():
    img = Image.open("congrats.png")
    img = img.resize((200, 200), Image.NEAREST)
    img = ImageTk.PhotoImage(img)

    lbl_img = Label(
        frame,
        image=img,
        background="#007875"
    )
    lbl_img.image = img
    lbl_img.pack(pady=20)

def try_again_image():
    img = Image.open("tryagain.jpg")
    img = img.resize((200, 200), Image.NEAREST)
    img = ImageTk.PhotoImage(img)

    lbl_img = Label(
        frame,
        image=img,
        background="#007875"
    )
    lbl_img.image = img
    lbl_img.pack(pady=20)    

# Different functions's implementations

def startButtonPressed():
    response = messagebox.askyesno("This is my popup", "Do you want to start the quiz?")
    if response:
        # If the user selects "Yes",start the quiz jisme questions and options honge
        label_image.destroy()
        label_text.destroy()
        btn_start.destroy()
        lbl_instruction.destroy()
        lbl_rules.destroy()
        create_skip_submit_buttons()  # Call the function to create skip and submit buttons
        start_quiz()
        start_timer()
    else:
        # If the user selects "No", close the window
        root.destroy()
 
def destroy_widgets():
    lbl_instruction.destroy()
    lbl_rules.destroy()
    btn_start.destroy()

    label_image.destroy()
    label_text.destroy()

    btn_submit.destroy()
    btn_skip.destroy()
    timer_label.destroy()

    lbl_Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

ques = 0
skipped_questions = 0
user_answer = []

def selected():
    global radio_var, lbl_Questions, r1, r2, r3, r4, user_answer, ques, skipped_questions
    x = radio_var.get() #is sy pata chale ga k user ne konsa option select kia hai
    user_answer.append(x)
    radio_var.set(-1) # is waja sy next question pe ja k user ko select krny ka option milta hai aor yha par do options select nhi ho skty

    if ques < len(questions) - 1:
        ques += 1
        lbl_Questions.config(text=questions[ques]) # it tells k labl question k text ko change krdo
        r1['text'] = answers_choice[ques][0] # ye btata hai k r1(yani first radio button) ki jga par konsa option hoga
        r2['text'] = answers_choice[ques][1]
        r3['text'] = answers_choice[ques][2]
        r4['text'] = answers_choice[ques][3]
    else:
        btn_skip.config(state=DISABLED)
        calc()

    if x == -1:  # mtlb k user ne koi option select nhi kia aor skip kr dia hai
        skipped_questions += 1 
        print("Skipped questions:", skipped_questions)
        lbl_Questions.config(text=questions[ques])  # next question display krdo

def skipQuestion():
    global skipped_questions
    skipped_questions += 1
    lbl_Questions.config(text=questions[ques])  # Display the next question

answers = [3, 1, 1, 2, 0, 0, 3, 0, 3, 0]

def calc():
    global user_answer, skipped_questions
    score = 0
    correct_answers = 0
    wrong_answers = 0

    for i in range(len(questions)):
        if i < len(user_answer):  # Ensure index is within user_answer list
            if user_answer[i] == -1:
                skipped_questions += 1
            elif user_answer[i] == answers[i]:
                score += 10
                correct_answers += 1
            else:
                wrong_answers += 1
        # else:
        #     skipped_questions += 1 
    if skipped_questions == 10:
        messagebox.showwarning("Warning", "You have skipped all the questions")
        root.destroy()
    if correct_answers >= 5:
        show_result(score, correct_answers, wrong_answers, skipped_questions)
        destroy_widgets()
        congrats_image()
    else:
        show_result(score, correct_answers, wrong_answers, skipped_questions)
        destroy_widgets()
        try_again_image()

def show_result(score, correct_answers, wrong_answers, skipped_questions):
    # Destroy existing widgets
    lbl_Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    btn_skip.destroy()
    btn_submit.destroy()

    # Display the score on the same frame
    score_label = Label(
        frame,
        text=f"Your score is: {score}\n\n"
             f"Correct Answers: {correct_answers}\n"
             f"Wrong Answers: {wrong_answers}\n"
             f"Skipped Questions: {skipped_questions}",
        font=("Comic Sans MS", 16),
        background="#007875"
    )
    score_label.pack(pady=20)

timer_seconds = 300  # 10 minutes = 600 seconds
timer_label = Label(
    frame,
    font=("Comic Sans MS", 16),
    background="#007875"
)
timer_label.pack(pady=(5, 5))


root.mainloop()