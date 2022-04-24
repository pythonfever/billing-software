from tkinter import *
import math, random, os
import tkinter.messagebox as tmsg
root= Tk()
root.geometry("1350x670+0+0")
root.title("Billing Software")

# frame 1-----------------------------------------------------------------------------------------------
f1 = LabelFrame(root, bg="dark blue",borderwidth=6,relief = SUNKEN)
f1.place(x=0,y=0,width=1365,height=60)
Label(f1,text="Billing Software",fg="yellow",font = ('Bookman Old Style','30'),bg="dark blue").place(x=550,y=0)
# frame 1-----------------------------------------------------------------------------------------------

# frame 2-----------------------------------------------------------------------------------------------
f2 = LabelFrame(root, text="Customer Details",borderwidth=6,fg="yellow" ,bg="dark blue", relief=SUNKEN,
                     font = ('Bookman Old Style','12','bold','italic'))
f2.place(x=0,y=60,width=1365,height=80)

name = Label(f2, text="Customer Name",bg="dark blue",font = ('Bookman Old Style','20'),fg="yellow")
phone = Label(f2, text="Contact No.",bg="dark blue",font = ('Bookman Old Style','20'),fg="yellow")
bill = Label(f2, text="Bill No.",bg="dark blue",font = ('Bookman Old Style','20'),fg="yellow")

name.place(x=0,y=0)
phone.place(x=435,y=0)
bill.place(x=820,y=0)

namevalue = StringVar()
phonevalue = StringVar()
a = random.randint(0,10000)
billvalue = StringVar()
billvalue.set(a)

nameentry = Entry(f2, textvariable=namevalue,font="20")
phoneentry = Entry(f2, textvariable=phonevalue,font="20")
billentry = Entry(f2, textvariable=billvalue,font="20")

nameentry.place(x=230,y=0,width=170,height=40)
phoneentry.place(x=600,y=0,width=170,height=40)
billentry.place(x=920,y=0,width=150,height=40)
# frame 2-----------------------------------------------------------------------------------------------

# frame 3-----------------------------------------------------------------------------------------------
f3 = LabelFrame(root, text="Cosmetics",borderwidth=6,bg="dark blue", relief=SUNKEN,fg="yellow",
                     font = ('Bookman Old Style','15','bold','italic'))
f3.place(x=0,y=140,width=340,height=430)

item1 = Label(f3, text="Bath Soap",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item2 = Label(f3, text="Face Cream",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic') )
item3 = Label(f3, text="Face Wash",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item4 = Label(f3, text="Hair Spary",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item5 = Label(f3, text="Hair Gel",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item6 = Label(f3, text="Body Lotion",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item7 = Label(f3, text="Shampoo",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item8 = Label(f3, text="Skin Tonner",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item9 = Label(f3, text="Eye Cosmetic Kit",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item10 = Label(f3, text="Bleaching Cream",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item11 = Label(f3, text="Facial Cream",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item12 = Label(f3, text="Anti Pimple Cream",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item13 = Label(f3, text="Ayrvedic Cream",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))

#Pack text for our form
item1.place(x=0,y=0)
item2.place(x=0,y=30)
item3.place(x=0,y=60)
item4.place(x=0,y=90)
item5.place(x=0,y=120)
item6.place(x=0,y=150)
item7.place(x=0,y=180)
item8.place(x=0,y=210)
item9.place(x=0,y=240)
item10.place(x=0,y=270)
item11.place(x=0,y=300)
item12.place(x=0,y=330)
item13.place(x=0,y=360)

# Tkinter variable for storing entries
item1value = IntVar(f3)
item2value = IntVar(f3)
item3value = IntVar(f3)
item4value = IntVar(f3)
item5value = IntVar(f3)
item6value = IntVar(f3)
item7value = IntVar(f3)
item8value = IntVar(f3)
item9value = IntVar(f3)
item10value = IntVar(f3)
item11value = IntVar(f3)
item12value = IntVar(f3)
item13value = IntVar(f3)

#Entries for our form
item1entry = Entry(f3, textvariable=item1value)
item2entry = Entry(f3, textvariable=item2value)
item3entry = Entry(f3, textvariable=item3value)
item4entry = Entry(f3, textvariable=item4value)
item5entry = Entry(f3, textvariable=item5value)
item6entry = Entry(f3, textvariable=item6value)
item7entry = Entry(f3, textvariable=item7value)
item8entry = Entry(f3, textvariable=item8value)
item9entry = Entry(f3, textvariable=item9value)
item10entry = Entry(f3, textvariable=item10value)
item11entry = Entry(f3, textvariable=item11value)
item12entry = Entry(f3, textvariable=item12value)
item13entry = Entry(f3, textvariable=item13value)

# Packing the Entries
item1entry.place(x=200,y=0,height=20)
item2entry.place(x=200,y=30,height=20)
item3entry.place(x=200,y=60,height=20)
item4entry.place(x=200,y=90,height=20)
item5entry.place(x=200,y=120,height=20)
item6entry.place(x=200,y=150,height=20)
item7entry.place(x=200,y=180,height=20)
item8entry.place(x=200,y=210,height=20)
item9entry.place(x=200,y=240,height=20)
item10entry.place(x=200,y=270,height=20)
item11entry.place(x=200,y=300,height=20)
item12entry.place(x=200,y=330,height=20)
item13entry.place(x=200,y=360,height=20)

# frame 3-----------------------------------------------------------------------------------------------

# frame 4-----------------------------------------------------------------------------------------------
f4 = LabelFrame(root, text="Edibles",borderwidth=6,bg="dark blue", relief=SUNKEN,fg="yellow",
                     font = ('Bookman Old Style','15','bold','italic'))
f4.place(x=340,y=140,width=340,height=430)

item14 = Label(f4, text="Rice",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item15 = Label(f4, text="Daal",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic') )
item16 = Label(f4, text="Food Oil",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item17 = Label(f4, text="Wheat",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item18 = Label(f4, text="Sugar",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item19 = Label(f4, text="Tea",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item20 = Label(f4, text="chickpea",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item21 = Label(f4, text="Almonds",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item22 = Label(f4, text="Red Cilli Powder",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item23 = Label(f4, text="Dry Turmeric",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item24 = Label(f4, text="Black Pepper",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item25 = Label(f4, text="Salt",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item26 = Label(f4, text="Soya Sos",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))

#Pack text for our form
item14.place(x=0,y=0)
item15.place(x=0,y=30)
item16.place(x=0,y=60)
item17.place(x=0,y=90)
item18.place(x=0,y=120)
item19.place(x=0,y=150)
item20.place(x=0,y=180)
item21.place(x=0,y=210)
item22.place(x=0,y=240)
item23.place(x=0,y=270)
item24.place(x=0,y=300)
item25.place(x=0,y=330)
item26.place(x=0,y=360)

# Tkinter variable for storing entries
item14value = IntVar(f4,value="0")
item15value = IntVar(f4,value="0")
item16value = IntVar(f4,value="0")
item17value = IntVar(f4,value="0")
item18value = IntVar(f4,value="0")
item19value = IntVar(f4,value="0")
item20value = IntVar(f4,value="0")
item21value = IntVar(f4,value="0")
item22value = IntVar(f4,value="0")
item23value = IntVar(f4,value="0")
item24value = IntVar(f4,value="0")
item25value = IntVar(f4,value="0")
item26value = IntVar(f4,value="0")

#Entries for our form
item14entry = Entry(f4, textvariable=item14value)
item15entry = Entry(f4, textvariable=item15value)
item16entry = Entry(f4, textvariable=item16value)
item17entry = Entry(f4, textvariable=item17value)
item18entry = Entry(f4, textvariable=item18value)
item19entry = Entry(f4, textvariable=item19value)
item20entry = Entry(f4, textvariable=item20value)
item21entry = Entry(f4, textvariable=item21value)
item22entry = Entry(f4, textvariable=item22value)
item23entry = Entry(f4, textvariable=item23value)
item24entry = Entry(f4, textvariable=item24value)
item25entry = Entry(f4, textvariable=item25value)
item26entry = Entry(f4, textvariable=item26value)

# Packing the Entries
item14entry.place(x=200,y=0,height=20)
item15entry.place(x=200,y=30,height=20)
item16entry.place(x=200,y=60,height=20)
item17entry.place(x=200,y=90,height=20)
item18entry.place(x=200,y=120,height=20)
item19entry.place(x=200,y=150,height=20)
item20entry.place(x=200,y=180,height=20)
item21entry.place(x=200,y=210,height=20)
item22entry.place(x=200,y=240,height=20)
item23entry.place(x=200,y=270,height=20)
item24entry.place(x=200,y=300,height=20)
item25entry.place(x=200,y=330,height=20)
item26entry.place(x=200,y=360,height=20)
# frame 4-----------------------------------------------------------------------------------------------

# frame 5-----------------------------------------------------------------------------------------------
f5 = LabelFrame(root, text="Readymade Items",borderwidth=6,bg="dark blue", relief=SUNKEN,fg="yellow",
                     font = ('Bookman Old Style','15','bold','italic'))
f5.place(x=680,y=140,width=340,height=430)

item27 = Label(f5, text="Maggie",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item28 = Label(f5, text="yippee pasta",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic') )
item29 = Label(f5, text="Kurkure",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item30 = Label(f5, text="Bread",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item31 = Label(f5, text="Jam",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item32 = Label(f5, text="Amul Cheese",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item33 = Label(f5, text="yippee Noodles",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item34 = Label(f5, text="Lays Chips",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item35 = Label(f5, text="Girnar Tea",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item36 = Label(f5, text="Jainam Papad",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item37 = Label(f5, text="Celebrations Packet",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item38 = Label(f5, text="Protien-X",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))
item39 = Label(f5, text="Dabur Chavanprash",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'))

#Pack text for our form
item27.place(x=0,y=0)
item28.place(x=0,y=30)
item29.place(x=0,y=60)
item30.place(x=0,y=90)
item31.place(x=0,y=120)
item32.place(x=0,y=150)
item33.place(x=0,y=180)
item34.place(x=0,y=210)
item35.place(x=0,y=240)
item36.place(x=0,y=270)
item37.place(x=0,y=300)
item38.place(x=0,y=330)
item39.place(x=0,y=360)

# Tkinter variable for storing entries
item27value = IntVar(f5,value="0")
item28value = IntVar(f5,value="0")
item29value = IntVar(f5,value="0")
item30value = IntVar(f5,value="0")
item31value = IntVar(f5,value="0")
item32value = IntVar(f5,value="0")
item33value = IntVar(f5,value="0")
item34value = IntVar(f5,value="0")
item35value = IntVar(f5,value="0")
item36value = IntVar(f5,value="0")
item37value = IntVar(f5,value="0")
item38value = IntVar(f5,value="0")
item39value = IntVar(f5,value="0")

#Entries for our form
item27entry = Entry(f5, textvariable=item27value)
item28entry = Entry(f5, textvariable=item28value)
item29entry = Entry(f5, textvariable=item29value)
item30entry = Entry(f5, textvariable=item30value)
item31entry = Entry(f5, textvariable=item31value)
item32entry = Entry(f5, textvariable=item32value)
item33entry = Entry(f5, textvariable=item33value)
item34entry = Entry(f5, textvariable=item34value)
item35entry = Entry(f5, textvariable=item35value)
item36entry = Entry(f5, textvariable=item36value)
item37entry = Entry(f5, textvariable=item37value)
item38entry = Entry(f5, textvariable=item38value)
item39entry = Entry(f5, textvariable=item39value)

# Packing the Entries
item27entry.place(x=200,y=0,height=20)
item28entry.place(x=200,y=30,height=20)
item29entry.place(x=200,y=60,height=20)
item30entry.place(x=200,y=90,height=20)
item31entry.place(x=200,y=120,height=20)
item32entry.place(x=200,y=150,height=20)
item33entry.place(x=200,y=180,height=20)
item34entry.place(x=200,y=210,height=20)
item35entry.place(x=200,y=240,height=20)
item36entry.place(x=200,y=270,height=20)
item37entry.place(x=200,y=300,height=20)
item38entry.place(x=200,y=330,height=20)
item39entry.place(x=200,y=360,height=20)

# frame 5-----------------------------------------------------------------------------------------------

# frame 6-----------------------------------------------------------------------------------------------
f6 = LabelFrame(root,text = "Bill Area",borderwidth=6, relief=SUNKEN,font = ('Bookman Old Style','15','bold','italic'))
f6.place(x=1020,y=140,width=340,height=430)

scrollbar = Scrollbar(f6)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(f6, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)



# frame 6-----------------------------------------------------------------------------------------------

# frame 7-----------------------------------------------------------------------------------------------



f7 = LabelFrame(root, text="Overall Prices",borderwidth=6,bg="dark blue", relief=SUNKEN,fg="yellow",
                     font = ('Bookman Old Style','15','bold','italic'))
f7.place(x=0,y=570,width=1365,height=135)

cosmetic = Label(f7, text="Total Cosmetic Price",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)
edibles = Label(f7, text="Total Edibles Price",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)
readymade = Label(f7, text="Total ReadyMade Items Price",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)
cosmetic_gst = Label(f7, text="Cosmetic Tax", bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)
edibles_gst = Label(f7, text="Edibles Tax",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)
readymade_gst = Label(f7, text="Readymade Item Tax",bg="dark blue", borderwidth=6,fg="yellow",font = ('Bookman Old Style','12','bold','italic'),justify=LEFT)

#Pack text for our form
cosmetic.place(x=0,y=0)
edibles.place(x=0,y=30)
readymade.place(x=0,y=60)
cosmetic_gst.place(x=400,y=0)
edibles_gst.place(x=400,y=30)
readymade_gst.place(x=400,y=60)

# Tkinter variable for storing entries
cosmeticvalue = IntVar()
ediblevalue = IntVar()
readymadevalue = IntVar()
cosmetic_gstvalue = IntVar()
edibles_gstvalue = IntVar()
readymade_gstvalue = IntVar()

#Entries for our form
cosmeticentry = Entry(f7, textvariable=cosmeticvalue)
edibleentry = Entry(f7, textvariable=ediblevalue)
readymadeentry = Entry(f7, textvariable=readymadevalue)
cosmetic_gstentry = Entry(f7, textvariable=cosmetic_gstvalue)
edibles_gstentry = Entry(f7, textvariable=edibles_gstvalue)
readymade_gstentry = Entry(f7, textvariable=readymade_gstvalue)

# Packing the Entries
cosmeticentry.place(x=260,y=5,height=20)
edibleentry.place(x=260,y=35,height=20)
readymadeentry.place(x=260,y=65,height=20)
cosmetic_gstentry.place(x=600,y=5,height=20)
edibles_gstentry.place(x=600,y=35,height=20)
readymade_gstentry.place(x=600,y=65,height=20)

def total():
    cosmeticvalue1 = (
                     (item1value.get()*40)+
                     (item2value.get()*120)+
                     (item3value.get()*60)+
                     (item4value.get()*180)+
                     (item5value.get()*140)+
                     (item6value.get()*180)+
                     (item7value.get()*200)+
                     (item8value.get()*190)+
                     (item9value.get()*240)+
                     (item10value.get()*340)+
                     (item11value.get()*450)+
                     (item12value.get()*220)+
                     (item13value.get()*400)
                     )
    cosmeticvalue.set(f"Rs {str(cosmeticvalue1)}")

    ediblevalue1 = (
        (item14value.get()*120)+
        (item15value.get()*110)+
        (item16value.get()*150)+
        (item17value.get()*160)+
        (item18value.get()*170)+
        (item19value.get()*190)+
        (item20value.get()*190)+
        (item21value.get()*200)+
        (item22value.get()*150)+
        (item23value.get()*220)+
        (item24value.get()*250)+
        (item25value.get()*165)+
        (item26value.get()*240)
    )
    ediblevalue.set(f"Rs {str(ediblevalue1)}")

    readymadevalue1 = (
        (item27value.get()*10)+
        (item28value.get()*20)+
        (item29value.get()*10)+
        (item30value.get()*60)+
        (item31value.get()*130)+
        (item32value.get()*20)+
        (item33value.get()*20)+
        (item34value.get()*20)+
        (item35value.get()*250)+
        (item36value.get()*270)+
        (item37value.get()*300)+
        (item38value.get()*500)+
        (item39value.get()*600)
    )
    readymadevalue.set(f"Rs {str(readymadevalue1)}")

    cosmeticvalue2 = (
        (cosmeticvalue1*18)/(100)
    )
    cosmetic_gstvalue.set(f"Rs {str(cosmeticvalue2)}")

    ediblevalue2 = (
        (ediblevalue1*12)/(100)
    )
    edibles_gstvalue.set(f"Rs {str(ediblevalue2)}")

    readymadevalue2 = (
        (readymadevalue1*12)/(100)
    )
    readymade_gstvalue.set(f"Rs {str(readymadevalue2)}")
    
    global abc
    abc = (
        (cosmeticvalue1)+
        (ediblevalue1)+
        (readymadevalue1)
    )
    
    global ab
    ab = (
        (cosmeticvalue2)+
        (ediblevalue2)+
        (readymadevalue2)
    )

def welcome():
    text.delete("1.0",END)
    text.insert(END,"\tWelcome to India Retail Shop")
    text.insert(END,f"\n Bill Number: {billvalue.get()}")
    text.insert(END,f"\n Customer Name: {namevalue.get()}")    
    text.insert(END,f"\n Contact Number: {phonevalue.get()}")
    text.insert(END,"\n======================================")
    text.insert(END,f"\nProduct\t\t\tQty\tAmount")    
    text.insert(END,"\n======================================")

def bill_area():
    if abc == 0 and ab == 0 :
        tmsg.showerror("Error","Nothing Purchased!!!")
    elif namevalue.get()=="" or phonevalue.get()=="":
        tmsg.showerror("Error","Customer details are must!!!")
    else:
        print(welcome())
        if item1value.get()!=0:
            text.insert(END,f"\nBath Soap\t\t\t {item1value.get()}\t {item1value.get()*40}")
        if item2value.get()!=0:
            text.insert(END,f"\nFace Cream \t\t\t {item2value.get()}\t {item2value.get()*120}")    
        if item3value.get()!=0:
            text.insert(END,f"\nFace Wash\t\t\t {item3value.get()}\t {item3value.get()*60}")
        if item4value.get()!=0:
            text.insert(END,f"\nHair Spray\t\t\t {item4value.get()}\t {item4value.get()*180}")
        if item5value.get()!=0:
            text.insert(END,f"\nHair Gel\t\t\t {item5value.get()}\t {item5value.get()*140}")
        if item6value.get()!=0:
            text.insert(END,f"\nBody Lotion\t\t\t {item6value.get()}\t {item6value.get()*180}")
        if item7value.get()!=0:
            text.insert(END,f"\nShampoo \t\t\t {item7value.get()}\t {item7value.get()*200}")
        if item8value.get()!=0:
            text.insert(END,f"\nSkin Tonner\t\t\t {item8value.get()}\t {item8value.get()*190}")
        if item9value.get()!=0:
            text.insert(END,f"\nEye Cosmetic Kit\t\t\t {item8value.get()}\t {item8value.get()*240}")
        if item10value.get()!=0:
            text.insert(END,f"\nBleaching Cream\t\t\t {item10value.get()}\t {item10value.get()*340}")
        if item11value.get()!=0:
            text.insert(END,f"\nFacial Cream\t\t\t {item11value.get()}\t {item11value.get()*450}")
        if item12value.get()!=0:
            text.insert(END,f"\nAnti Pimple Cream\t\t\t {item12value.get()}\t {item12value.get()*220}")
        if item13value.get()!=0:
            text.insert(END,f"\nAyrvedic Cream\t\t\t {item13value.get()}\t {item13value.get()*400}")
        if item14value.get()!=0:
            text.insert(END,f"\nRice\t\t\t {item14value.get()}\t {item14value.get()*120}")
        if item15value.get()!=0:
            text.insert(END,f"\nDaal\t\t\t {item15value.get()}\t {item15value.get()*110}")
        if item16value.get()!=0:
            text.insert(END,f"\nFood Oil\t\t\t {item16value.get()}\t {item16value.get()*150}")
        if item17value.get()!=0:
            text.insert(END,f"\nWheat\t\t\t {item17value.get()}\t {item17value.get()*160}")
        if item18value.get()!=0:
            text.insert(END,f"\nSugar\t\t\t {item18value.get()}\t {item18value.get()*170}")
        if item19value.get()!=0:
            text.insert(END,f"\nTea\t\t\t {item19value.get()}\t {item19value.get()*190}")
        if item20value.get()!=0:
            text.insert(END,f"\nChickpea\t\t\t {item20value.get()}\t {item20value.get()*190}")
        if item21value.get()!=0:
            text.insert(END,f"\nAlmonds\t\t\t {item21value.get()}\t {item21value.get()*200}")
        if item22value.get()!=0:
            text.insert(END,f"\nRed Chilli Powder\t\t\t {item22value.get()}\t {item22value.get()*150}")
        if item23value.get()!=0:
            text.insert(END,f"\nDry Turmeric\t\t\t {item23value.get()}\t {item23value.get()*220}")
        if item24value.get()!=0:
            text.insert(END,f"\nBlack Pepper\t\t\t {item24value.get()}\t {item24value.get()*250}")
        if item25value.get()!=0:
            text.insert(END,f"\nSalt\t\t\t {item25value.get()}\t {item25value.get()*165}")
        if item26value.get()!=0:
            text.insert(END,f"\nSoya Sos\t\t\t {item26value.get()}\t {item26value.get()*240}")
        if item27value.get()!=0:
            text.insert(END,f"\nMaggie\t\t\t {item27value.get()}\t {item27value.get()*10}")
        if item28value.get()!=0:
            text.insert(END,f"\nYippee Pasta\t\t\t {item28value.get()}\t {item28value.get()*20}")
        if item29value.get()!=0:
            text.insert(END,f"\nKurkure\t\t\t {item29value.get()}\t {item29value.get()*10}")
        if item30value.get()!=0:
            text.insert(END,f"\nBread\t\t\t {item30value.get()}\t {item30value.get()*60}")
        if item31value.get()!=0:
            text.insert(END,f"\nJam\t\t\t {item31value.get()}\t {item31value.get()*130}")
        if item32value.get()!=0:
            text.insert(END,f"\nAmul Cheese\t\t\t {item32value.get()}\t {item32value.get()*20}")
        if item33value.get()!=0:
            text.insert(END,f"\nYippee Noodles\t\t\t {item33value.get()}\t {item33value.get()*20}")
        if item34value.get()!=0:
            text.insert(END,f"\nLays Chips\t\t\t {item34value.get()}\t {item34value.get()*20}")
        if item35value.get()!=0:
            text.insert(END,f"\nGirnar Tea\t\t\t {item35value.get()}\t {item35value.get()*250}")
        if item36value.get()!=0:
            text.insert(END,f"\nJainam Papad\t\t\t {item36value.get()}\t {item36value.get()*270}")
        if item37value.get()!=0:
            text.insert(END,f"\nCelebrations Packet\t\t\t {item37value.get()}\t {item37value.get()*300}")
        if item38value.get()!=0:
            text.insert(END,f"\nProtien-X\t\t\t {item38value.get()}\t {item38value.get()*500}")
        if item39value.get()!=0:
            text.insert(END,f"\nDabur Chavanprash\t\t\t {item39value.get()}\t {item39value.get()*600}")
    
        text.insert(END,"\n--------------------------------------")
        text.insert(END,f"\nSub Total\t\t\t\t {abc}")    
        text.insert(END,f"\nTax\t\t\t\t {ab}")    
        text.insert(END,"\n--------------------------------------")
        text.insert(END,f"\nGrand Total\t\t\t\t{abc + ab}")    
    
def save_bill():
    bill = text.get("1.0",END)
    tmsg.askyesno("save","confirm saving this data!!")
    f = open(str(namevalue.get())+".txt",'w')
    f.write(bill)
    f.close

def find(): 
    present = "no"
    for i in os.listdir("./"):
        if i.split('.')[0]==namevalue.get():
            f = open(f"{i}",'r')
            text.delete('1.0',END)
            for d in f:
                text.insert(END,d)
            f.close()
            present = "yes"
        if present=="no":
            tmsg.showinfo("Error","No such file or directory") 
def cleardata():
    namevalue.set("")
    phonevalue.set("")
    billvalue.set("")
    item1value.set(0)
    item2value.set(0)
    item3value.set(0)
    item4value.set(0)
    item5value.set(0)
    item6value.set(0)
    item7value.set(0)
    item8value.set(0)
    item9value.set(0)
    item10value.set(0)
    item11value.set(0)
    item12value.set(0)
    item13value.set(0)
    item14value.set(0)
    item15value.set(0)
    item16value.set(0)
    item17value.set(0)
    item18value.set(0)
    item19value.set(0)
    item20value.set(0)
    item21value.set(0)
    item22value.set(0)
    item23value.set(0)
    item24value.set(0)
    item25value.set(0)
    item26value.set(0)
    item27value.set(0)
    item28value.set(0)
    item29value.set(0)
    item30value.set(0)
    item31value.set(0)
    item32value.set(0)
    item33value.set(0)
    item34value.set(0)
    item35value.set(0)
    item36value.set(0)
    item37value.set(0)
    item38value.set(0)
    item39value.set(0)
    cosmeticvalue.set("Rs. 0.0")
    ediblevalue.set("Rs. 0.0")
    readymadevalue.set("Rs. 0.0")
    cosmetic_gstvalue.set("Rs. 0.0")
    edibles_gstvalue.set("Rs. 0.0")
    readymade_gstvalue.set("Rs. 0.0")

b1 = Button(f7,text="Total",font=('batang','25','bold'),command=total,bg="light blue",fg="Blue",relief=RAISED)
b1.place(x=745,y=0,width=150,height=100)

b2 = Button(f7,text="Generate Bill",font=('batang','15','bold'),command=bill_area,bg="light blue",fg="Blue",relief=RAISED)
b2.place(x=900,y=0,width=150,height=100)

b3 = Button(f7,text="Clear",font=('batang','25','bold'),command=cleardata,bg="light blue",fg="Blue",relief=RAISED)
b3.place(x=1055,y=0,width=150,height=100)

b4 = Button(f7,text="Exit",font=('batang','25','bold'),command=quit,bg="light blue",fg="Blue",relief=RAISED)
b4.place(x=1210,y=0,width=140,height=100)

b5 = Button(f2,text="Save",font=('batang','25','bold'),command=save_bill,bg="light blue",fg="Blue",relief=RAISED)
b5.place(x=1230,y=0,width=120,height=55)

b6= Button(f2,text="Search",font=('batang','25','bold'),command=find,bg="light blue",fg="Blue",relief=RAISED)
b6.place(x=1100,y=0,width=120,height=55)
# frame 7-----------------------------------------------------------------------------------------------
root.mainloop()
