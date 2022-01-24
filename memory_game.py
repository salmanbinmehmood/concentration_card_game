from tkinter import *
import time
from pygame import mixer
import random
from PIL import ImageTk, Image


root=Tk()



cards=[['2C','AH','9C','2S','3C','9H','3H','3S','10H'],['4D','7H','4S',
       '5C','AC','5H','5S','6C','6D'],['6H','6S','7C','7D','4H','7S',
       '8C','8D','8H'],['QD','2H','9D','3D','9S','10C','JD','4C','10S'],
       ['5D','AD','2D','AS','KC','KD','KH','joker','JC'],['10D','JH','JS',
       'QC','8s','QH','QS','joker','KS']]

card_back=[['card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back'],['card_back','card_back','card_back',
       'card_back','card_back','card_back','card_back','card_back','card_back'],['card_back','card_back','card_back','card_back','card_back','card_back',
       'card_back','card_back','card_back'],['card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back'],
       ['card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back','card_back'],['card_back','card_back','card_back',
       'card_back','card_back','card_back','card_back','card_back','card_back']]

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)
card_height=100
if screen_height>768:
    card_height = 150

card_setup=0

after_setup=0
print(len(cards))
# root.geometry(f"{screen_width}x{screen_height}")

root.attributes('-fullscreen',True)
after_paly_again=0
pgl=0
r,c=0,0
list=[]
list2=[]
list3=[]
calls=0
term_count=1
player1_score=0
player2_score=0
# f1=Frame(root,bg="gray")
# f1.pack()
f=Frame(root)
f.pack(pady=20,side=LEFT)

cards_counter=0
list4=[]
list5=[]
checks=0
coco=0
heading2=Label(root,text="", font=("", 14, "bold"), bg="gray10",
                               fg="gray80")
heading2.place(x=1050, y=150)


sec = StringVar()

mins= StringVar()

hrs= StringVar()

times=0
fp=StringVar()
sp=StringVar()
gm_over=False
f0=Frame(root,bg="gray10")
f0.pack(fill="both", expand = True)
# f2=Frame(root)
# f2.pack(side=RIGHT)
mixer.init()
bolean=False
# heading=Label()
heading = Label(root, text="", font=("", 16, "bold"), background="gray10", foreground="gray80")
heading.place(x=1100, y=50)





b_arror=Button()
heading1=Label(root,text="", font=("", 14, "bold"), bg="gray10",fg="gray80")

after_clicks=0
heading1.place(x=1050,y=100)
gr_frame_limit=0
pe1=Entry()
pe2=Entry()

random.shuffle(cards)
print(cards)

player1_cards=False
player2_cards=False
# print(3%2,"==")
db_frame=Frame(root,bg="gray10")
gr_frame=Frame()
heading_container=0
db_l=Label()
db_l2=Label()
db_l3=Label()
db_btn=Button()

# def game_over():
#     global card_back
#     result = all(element == 'empty_card2' for element in card_back)
#     if (result):
#         # print("all are same")
#         root.destroy()
#     else:
#         print("all are not same")


def game_tules():
    f0.destroy()
    global gr_frame
    global gr_frame_limit


    gr_frame = Frame(root)
    gr_frame.pack(anchor=W,fill=BOTH,expand=True)

    gr_heading=Label(gr_frame,text="Concentration Game Rules",font=("","22","bold"),fg="royal blue")
    gr_heading.pack(pady=10)
    gr_back_btn=Button(gr_frame,text="back",command=page1).pack(anchor=W)
    text_widget =Text(gr_frame, height=5, width=40,font=("","16",""),fg="midnight blue")

    scroll_bar = Scrollbar(gr_frame)

    scroll_bar.pack(side=RIGHT,fill=BOTH)

    text_widget.pack(side=LEFT,fill=BOTH,expand=True,pady=20,padx=20)

    with open("rules.txt") as f:
        text = f.read()

    text_widget.insert(END, text)
    gr_frame_limit+=1
    text_widget.configure(state='disabled')

def playagain():
    global player1_score
    global player2_score
    global heading_container
    global fp
    global sp
    global gm_over
    global card_setup
    global after_setup
    global coco
    global cards_counter
    # global db_frame
    db_frame.destroy()
    global f0
    global term_count
    global calls
    global bolean
    global after_clicks
    global f
    global list
    global list2

    f = Frame(root, bg="springGreen4")
    f.pack(pady=20, side=LEFT)
    f0 = Frame(root, bg="gray10")
    f0.pack(fill="both", expand=True)
    player1_score = 0
    cards_counter=0
    player2_score = 0
    heading_container = 0
    gm_over = False
    bolean = False
    card_setup=0
    after_setup=0
    term_count=1
    after_clicks=0
    calls=0
    list.clear()
    list2.clear()
    fp.set("")
    sp.set("")
    coco +=1
    page1()

def dashboard():
    global f0
    global db_frame
    global fp
    global sp
    global card_back
    global db_l
    global db_l2
    global db_l3
    global db_btn
    global coco
    global player1_score
    global player2_score
    db_frame = Frame(root, bg="gray10")
    db_frame.pack(fill="both", expand=True)
    db_frame2 = Frame(db_frame, bg="dark slate gray")
    db_frame2.pack(fill="y", expand=True)
    db_l=Label(db_frame2,fg="gray80",text=f"{fp.get()[:10]}                      {player1_score}",font=("","20","bold"),bg="dark slate gray")
    db_l2=Label(db_frame2,fg="gray80",text=f"{sp.get()[:10]}                     {player2_score}",font=("","20","bold"),bg="dark slate gray")
    db_l3=Label(db_frame2,text="Game Over",font=("","50","bold"),fg="gray80",bg="dark slate gray")
    if player1_score>player2_score:
        db_l0=Label(db_frame2,fg="cyan",text=f"{fp.get()[:10]} is win",font=("","20","bold"),bg="dark slate gray")
        db_l0.grid(row=2, column=2)

    elif player1_score==player2_score:
        db_l0=Label(db_frame2,fg="cyan",text="The match is tied",font=("","20","bold"),bg="dark slate gray")
        db_l0.grid(row=2, column=2)

    else:
        db_l0= Label(db_frame2, fg="cyan", text=f"{sp.get()[:10]} is win",font=("", "20", "bold"), bg="dark slate gray")
        db_l0.grid(row=2, column=2)

    db_l3.grid(row=1,column=2,sticky="new",padx=10)
    db_l.grid(row=3,column=2)
    db_l2.grid(row=4,column=2)

    db_frame2.rowconfigure(0, weight=1)

    db_frame2.rowconfigure(1, weight=1)

    db_frame2.rowconfigure(2, weight=1)

    db_frame2.rowconfigure(3, weight=1)
    db_frame2.rowconfigure(4, weight=1)
    db_frame2.rowconfigure(5, weight=1)
    db_frame2.rowconfigure(6, weight=1)
    db_frame2.rowconfigure(7, weight=1)

    db_frame2.columnconfigure(0, weight=1)

    db_frame2.columnconfigure(1, weight=1)

    db_frame2.columnconfigure(2, weight=1)

    db_frame2.columnconfigure(3, weight=1)

    db_frame2.columnconfigure(4, weight=1)
    db_frame2.columnconfigure(5, weight=1)
    db_frame2.columnconfigure(6, weight=1)


    try_image = Image.open(f"cards\\try_again.png")

    try_image = try_image.resize((150, 200))

    try_img = ImageTk.PhotoImage(try_image)

    try_btn = Button(db_frame2, image=try_img, borderwidth=0, bg="dark slate gray",fg="dark slate gray", activebackground="dark slate gray",
                       command=playagain)

    try_btn.grules_image = try_img
    try_btn.grid(row=5,column=2,sticky=S)

    ex_image = Image.open(f"cards\\exit.png")

    ex_image = ex_image.resize((150, 200))

    ex_img = ImageTk.PhotoImage(ex_image)

    ex_btn = Button(db_frame2, image=ex_img, borderwidth=0, bg="dark slate gray", fg="dark slate gray",
                     activebackground="dark slate gray",
                     command=root.destroy)

    ex_btn.grules_image = ex_img
    ex_btn.grid(row=6, column=2,sticky=N)
    # coco=0


    for i in range(6):
        for j in range(9):
            # cards[][]=cards
            card_back[i][j] = 'card_back'
    root.update()


# def back():
#     global coco
#
#
#     f.destroy()
#     f0.destroy()
#     coco+=1
#     page2()

def click2(b_row,b_col):
       global fp
       global sp
       global heading
       # global heading1
       global heading2
       global bolean
       global term_count
       global player2_score
       global player1_score
       global list3
       global calls
       global checks

       global card_back
       global list
       global list2
       global player1_cards
       global player2_cards
       global cards_counter
       global gm_over
       global cards
       global after_clicks
       global list4
       global list5


       if card_back[b_row][b_col]!="empty_card2":
              mixer.music.load("take.mp3")
              # Start playing the song
              mixer.music.play()
              calls += 1
              after_clicks += 1

              if len(list)!=2:
                     list.append(b_row)
                     list.append(b_col)
              elif len(list2)!=2 and (list[0]!=b_row or list[1]!=b_col):

                     list2.append(b_row)

                     list2.append(b_col)
                     print(list2[0])
                     print(list2[1])


              image = Image.open(f"cards\\{cards[b_row][b_col]}.jpg")
              image = image.resize((100, card_height))
              img = ImageTk.PhotoImage(image)

              l = Button(f, image=img, activebackground='red', background="gray10")
              l.image = img
              l.grid(row=b_row, column=b_col, sticky='ns', pady=5, padx=5)


              kk=cards[list[0]][list[1]]
              kk = tuple(kk)
              print(list[0],"pehli")
              print(list[1],"dosri")




              for i in range(len(list2)):
                     if len(list) == 2 and len(list2) == 2 :

                            if cards[list2[0]][list2[1]].startswith(kk):
                                   #
                                   # card_back[list[0]][list[1]] = "empty_card2"
                                   # card_back[list2[0]][list2[1]] = "empty_card2"
                                   print(card_back)

                                   bolean=True

                                   mixer.music.load("correct.mp3")
                                   mixer.music.play()


                            else:
                                   print("no")

                                   mixer.music.load("buzz2.wav")

                                   mixer.music.play()



       if calls == 2:


              if(term_count==1):
                     # calls=0
                     if(bolean):

                            image = Image.open(f"cards\\empty_card2.jpg")
                            image = image.resize((100, card_height))
                            img = ImageTk.PhotoImage(image)

                            l = Button(f, image=img, activebackground='red', background="gray10")
                            l.image = img
                            l.grid(row=list[0], column=list[1], sticky='ns', pady=5, padx=5)

                            image = Image.open(f"cards\\empty_card2.jpg")
                            image = image.resize((100, card_height))
                            img = ImageTk.PhotoImage(image)

                            l = Button(f, image=img, activebackground='red', background="gray10")
                            l.image = img
                            l.grid(row=list2[0], column=list2[1], sticky='ns', pady=5, padx=5)

                            list.clear()
                            list2.clear()


                            heading.config(text=f"{fp.get()[:10]}")
                            player1_score+=1
                            print("player 1 score is ",player1_score)
                            heading1.config(text=f"{fp.get()[:10]}")
                            score1_label = Label(root, text=f"{player1_score}",font=("","14","bold"), bg="gray10", fg="gray80").place(x=1190,
                                                                                                                y=100)
                            bolean=False
                            calls = 0
                            term_count=1
                            cards_counter+=2
                            after_clicks =0

                     else:

                            calls = 0
                            term_count = 2
                            heading.config(text=f"{sp.get()[:10]}")


              elif (term_count ==2):
                     # calls=0
                     if (bolean):

                            image = Image.open(f"cards\\empty_card2.jpg")
                            image = image.resize((100, card_height))
                            img = ImageTk.PhotoImage(image)

                            l = Button(f, image=img,activebackground='red', background="gray10")
                            l.image = img
                            l.grid(row=list[0], column=list[1], sticky='ns', pady=5, padx=5)

                            image = Image.open(f"cards\\empty_card2.jpg")
                            image = image.resize((100, card_height))
                            img = ImageTk.PhotoImage(image)

                            l = Button(f, image=img, activebackground='red', background="gray10")
                            l.image = img
                            l.grid(row=list2[0], column=list2[1], sticky='ns', pady=5, padx=5)
                            list.clear()
                            list2.clear()

                            heading.config(text=f"{sp.get()[:10]}")
                            player2_score += 1
                            print("player 2 score is ",player2_score)
                            heading2.config(text=f"{sp.get()[:10]}")
                            score2_label = Label(root, text=f"{player2_score}",font=("","14","bold"), bg="gray10", fg="gray80").place(x=1190,
                                                                                                                y=150)
                            bolean = False
                            calls = 0
                            after_clicks=0
                            cards_counter += 2
                            term_count = 2

                     else:

                            calls = 0
                            term_count = 1
                            heading.config(text=f"{fp.get()[:10]}")


       root.update()
       if cards_counter==54:
           f.destroy()
           f0.destroy()

           dashboard()


       if after_clicks == 2 and bolean==False:
           # list.clear()
           # list2.clear()

           root.after(400, click1)


def page2():
       global pgl
       global ff
       global f0
       global fp
       global sp
       global pe1
       if pgl>0:
              f0.destroy()
              f0 = Frame(root, bg="gray10")
              f0.pack(fill="both", expand=True)
       pgl+=1

       image22 = Image.open(f"cards\\start-button.png")

       image22 = image22.resize((150, 150))

       img22 = ImageTk.PhotoImage(image22)

       image = Image.open(f"cards//casino8.jpg")
       image = image.resize((screen_width, screen_height))
       img = ImageTk.PhotoImage(image)
       background_label = Label(f0, image=img)
       background_label.image=img
       background_label.place(x=0, y=0, relwidth=1, relheight=1)

       first_name=Label(background_label, text="player 1:", font=("", 22, "bold"), fg="gray80",bg='gray6',borderwidth=0)
       first_name.place(x=10,y=100)
       second_name=Label(background_label, text="player 2:", font=("", 22, "bold"),  fg="gray80",bg='gray6',borderwidth=0)
       second_name.place(x=1000,y=100)
       pe1 = Entry(background_label, textvariable=fp,relief=RIDGE, bd=2).place(x=140, y=110)
       pe2 = Entry(background_label, textvariable=sp,relief=RIDGE,bd=2).place(x=1130, y=110)
       btn = Button(background_label, image=img22, borderwidth=0, bg="black", activebackground="black",command=lambda :[click1(),countdowntimer()])
       btn.image22=img22
       btn.place(x=screen_width-300, y=screen_height-200)
       root.update()


def click1():
    global heading
    global times
    global gm_over
    global sec
    global mins
    global heading2
    global coco
    global card_back
    global f
    global fp
    global heading_container

    global card_setup
    global list
    global list2
    global after_setup
    global after_clicks
    global sp
    if gm_over == False:

        f.columnconfigure(0, weight=1)

        f.columnconfigure(1, weight=1)

        f.columnconfigure(2, weight=1)

        f.columnconfigure(3, weight=1)

        f.columnconfigure(4, weight=1)
        f.columnconfigure(5, weight=1)
        f.columnconfigure(6, weight=1)
        f.columnconfigure(7, weight=1)
        f.columnconfigure(8, weight=1)
        f.columnconfigure(9, weight=0)

        f.rowconfigure(0, weight=1)

        f.rowconfigure(1, weight=1)

        f.rowconfigure(2, weight=1)

        f.rowconfigure(3, weight=1)
        f.rowconfigure(4, weight=1)
        f.rowconfigure(5, weight=1)
        root.config(bg="gray10")
        f.config(bg="springGreen4")


        print("wow")

        ex_image = Image.open("cards\\exit.png")
        ex_image = ex_image.resize((100, 200))
        ex_img = ImageTk.PhotoImage(ex_image)
        ex_btn = Button(root, image=ex_img, activebackground="gray10",background="gray10", borderwidth=0,command=root.destroy)

        ex_btn.image = ex_img
        ex_btn.place(x=1100, y=screen_height-200)

        f0.destroy()

        # if coco>0:
        #     print("frame baqi hai")
        #
        #     # f.destroy()
        #     f = Frame(root,bg="springGreen4")
        #     f.pack(pady=20, side=LEFT)
        #           #
        #
        #     f.columnconfigure(0, weight=1)
        #
        #     f.columnconfigure(1, weight=1)
        #
        #     f.columnconfigure(2, weight=1)
        #
        #     f.columnconfigure(3, weight=1)
        #
        #     f.columnconfigure(4, weight=1)
        #     f.columnconfigure(5, weight=1)
        #     f.columnconfigure(6, weight=1)
        #     f.columnconfigure(7, weight=1)
        #     f.columnconfigure(8, weight=1)
        #     f.columnconfigure(9, weight=0)
        #
        #     f.rowconfigure(0, weight=1)
        #
        #     f.rowconfigure(1, weight=1)
        #
        #     f.rowconfigure(2, weight=1)
        #
        #     f.rowconfigure(3, weight=1)
        #     f.rowconfigure(4, weight=1)
        #     f.rowconfigure(5, weight=1)


        if heading_container==0:
                score1_label=Label(root,text=f"{player1_score}",bg="gray10",font=("","14","bold"),fg="gray80").place(x=1190,y=100)
                score2_label = Label(root, text=f"{player2_score}",font=("","14","bold"), bg="gray10", fg="gray80").place(x=1190, y=150)
                heading1.config(text=(f"{fp.get()[:10]}"))

                heading2.config(text=f"{sp.get()[:10]}")
                heading.config(text=f"{fp.get()[:10]}")

        heading_container+=1

        for i in range(6):
            for j in range(9):
                # global r,c
                # r,c=i,j

                image = Image.open(f"cards\\card_back.jpg")
                image = image.resize((100, card_height))
                img = ImageTk.PhotoImage(image)

                l=Button(f,image=img,activebackground='red',background="gray10", command=lambda row=i, column=j:click2(row,column))
                l.image = img
                if card_setup == 0 :
                    l.grid(row=i,column=j,sticky='ns',pady=5,padx=5)
    card_setup = 1

    if len(list)==2 and len(list2)==2 and gm_over==False:

        image = Image.open(f"cards\\card_back.jpg")
        image = image.resize((100, card_height))
        img = ImageTk.PhotoImage(image)

        l = Button(f, image=img, activebackground='red', background="gray10",
                          command=lambda row=list[0], column=list[1]: click2(row, column))
        l.image = img
        l.grid(row=list[0], column=list[1], sticky='ns', pady=5, padx=5)

        image = Image.open(f"cards\\card_back.jpg")
        image = image.resize((100, card_height))
        img = ImageTk.PhotoImage(image)

        l = Button(f, image=img, activebackground='red', background="gray10",
                          command=lambda row=list2[0], column=list2[1]: click2(row, column))
        l.image = img
        l.grid(row=list2[0], column=list2[1], sticky='ns', pady=5, padx=5)
    list.clear()
    list2.clear()

    after_clicks=0
    root.update()


bolean2=False

root.update()

def countdowntimer():
    global card_back
    global sec
    global gm_over
    global mins
    global f
    global cards
    global heading_container
    global f0
    global fp
    global sp
    global player1_score
    global player2_score
    global heading2
    l1 = Label(root, textvariable=sec, width=2, font='Helvetica 20 bold',bg="gray10",fg="gray80").place(x=1140, y=300)
    l2 = Label(root, textvariable=mins, width=2, font='Helvetica 20 bold',bg="gray10",fg="gray80").place(x=1100, y=300)
    sec.set('59')

    mins.set('00')

    times = int(int(mins.get())*60 + int(sec.get()))
    while times > -1:

       minute,second = (times // 60 , times % 60)
       sec.set(second)
       mins.set(minute)
       try:
          root.update()
       except Exception as e:
          print("the application has been closed")
          exit()

       time.sleep(1)
       if(times == 0):

          sec.set('00')
          mins.set('00')
          time.sleep(1)
          f.destroy()
          f0.destroy()
          gm_over =True
          dashboard()

       times -= 1




def page1():
       global f0
       global gr_frame
       global gr_frame_limit
       gr_frame.destroy()
       if gr_frame_limit>0:
           f0 = Frame(root, bg="gray10")
           f0.pack(fill="both", expand=True)


       heading1.config(text="")

       next_image = Image.open(f"cards\\next.png")

       next_image = next_image.resize((150, 200))

       next_img = ImageTk.PhotoImage(next_image)

       grules_image = Image.open(f"cards\\game_rules.png")

       grules_image = grules_image.resize((150, 200))

       grules_img = ImageTk.PhotoImage(grules_image)

       exit_image = Image.open(f"cards\\exit.png")

       exit_image = exit_image.resize((150, 200))

       exit_img = ImageTk.PhotoImage(exit_image)


       next_btn=Button(f0, image=next_img, borderwidth=0, bg="gray10", activebackground="gray10",
             command=page2)

       next_btn.next_image=next_img

       next_btn.grid(row=2,column=5,sticky="ns")

       rules_btn = Button(f0, image=grules_img, borderwidth=0, bg="gray10", activebackground="gray10",
             command=game_tules)

       rules_btn.grules_image= grules_img
       rules_btn.grid(row=3, column=5, sticky="ns")

       exit_btn = Button(f0, image=exit_img, borderwidth=0, bg="gray10", activebackground="gray10",
             command=root.destroy)
       exit_btn.exit_image = exit_img
       exit_btn.grid(row=4, column=5, sticky="ns")

       image = Image.open("cards\\casino.png")

       image = image.resize((500, 500))
       img = ImageTk.PhotoImage(image)

       l = Label(f0, image=img,bg="gray10")
       l.image = img
       l.grid(row=1,column=5,sticky="new")
       gr_frame_limit=0


       f0.rowconfigure(0, weight=1)

       f0.rowconfigure(1, weight=1)

       f0.rowconfigure(2, weight=1)

       f0.rowconfigure(3, weight=1)
       f0.rowconfigure(4, weight=1)
       f0.rowconfigure(5, weight=1)
       f0.rowconfigure(6, weight=1)
       f0.rowconfigure(7, weight=1)

       f0.columnconfigure(0, weight=1)

       f0.columnconfigure(1, weight=1)

       f0.columnconfigure(2, weight=1)

       f0.columnconfigure(3, weight=1)

       f0.columnconfigure(4, weight=1)
       f0.columnconfigure(5, weight=1)
       f0.columnconfigure(6, weight=1)
       f0.columnconfigure(7, weight=1)
       f0.columnconfigure(8, weight=1)
       f0.columnconfigure(9, weight=1)

# f.columnconfigure(0, weight=1)
#
# f.columnconfigure(1, weight=1)
#
# f.columnconfigure(2, weight=1)
#
# f.columnconfigure(3, weight=1)
#
# f.columnconfigure(4, weight=1)
# f.columnconfigure(5, weight=1)
# f.columnconfigure(6, weight=1)
# f.columnconfigure(7, weight=1)
# f.columnconfigure(8, weight=1)
# f.columnconfigure(9, weight=0)
#
#
# f.rowconfigure(0, weight=1)
#
# f.rowconfigure(1, weight=1)
#
# f.rowconfigure(2, weight=1)
#
# f.rowconfigure(3, weight=1)
# f.rowconfigure(4, weight=1)
# f.rowconfigure(5, weight=1)
# root.config(bg="gray10")
# f.config(bg="springGreen4")



page1()
root.mainloop()




