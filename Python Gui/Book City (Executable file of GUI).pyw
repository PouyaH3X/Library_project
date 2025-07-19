import pymssql as sql
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

class main:
    def __init__(self):
        server = sql.connect(host="127.0.0.1", port="6144", database="Book_City")
        self.server = server

    def root_app(self,root):
        self.root = root
        root.title("Book city")
        root.geometry("700x400")
        root.minsize(300,200)
 
    def main_page(self):
        self.root.geometry("419x419")
        self.root.resizable(False,False)
        fr11 = ctk.CTkFrame(self.root,width=419)
        fr12 = ctk.CTkFrame(self.root,width=419)
        fr11.pack()
        fr12.pack()
        fr1 = ctk.CTkButton(fr11,width=200,height=200,text = 'Books list',corner_radius=30,border_width=1,border_color='gray',font=("Calibri ", 30),fg_color='transparent',hover_color='#FFBF00',command=self.f1)
        fr2 = ctk.CTkButton(fr11,width=200,height=200,text = 'Add books',corner_radius=30,border_width=1,border_color='gray',font=("Calibri ", 30),fg_color='transparent',command=self.add_b)
        fr4 = ctk.CTkButton(fr12,width=400,height=200,text = 'Search & Edit & Delete',corner_radius=30,border_width=1,border_color='gray',font=("Calibri ", 30),fg_color='transparent',hover_color='#228B22',command=self.search)
        fr1.grid(row=0,column=0,padx=5,pady=5)
        fr2.grid(row=0,column=1,padx=5,pady=5)
        fr4.grid(row=1,padx=5,pady=5)

    def empty_find(self,x):
        if x==None or x=="" or x==" ":
            return "----"
        else:
            return x
    
    def space_rem(self,x):
        return x.replace(" ","")

    def f1(self):
        cursor1 = self.server.cursor()
        cursor1.execute("SELECT * FROM book")
        cursor1_result = cursor1.fetchall()
        window1=ctk.CTkToplevel(self.root)
        window1.title("List of all the books")
        window1.grab_set()
        window1.resizable(False,True)
        self.books_list(cursor1_result,window1,400)

    def books_list(self,cursor1_result,window1,h):
        books_list  = ctk.CTkScrollableFrame(window1,width=1310,height=h, scrollbar_button_hover_color='#FFBF00')
        books_list.grid(row=0,column=0,sticky="W")
        
        f0 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f1 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f2 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f3 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f4 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f5 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f6 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f7 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)
        f8 = ctk.CTkFrame(books_list,border_width=1,border_color='white',corner_radius=1)

        f0.grid(row=0,column=8,pady=2,padx=3)
        f1.grid(row=0,column=7,pady=2,padx=3)
        f2.grid(row=0,column=6,pady=2,padx=3)
        f3.grid(row=0,column=5,pady=2,padx=3)
        f4.grid(row=0,column=4,pady=2,padx=3)
        f5.grid(row=0,column=3,pady=2,padx=3)
        f6.grid(row=0,column=2,pady=2,padx=3)
        f7.grid(row=0,column=1,pady=2,padx=3)
        f8.grid(row=0,column=0,pady=2,padx=3)
    
        f10 = ctk.CTkFrame(f0,border_width=2,border_color='white',width=10)
        f11 = ctk.CTkFrame(f1,border_width=2,border_color='white')
        f12 = ctk.CTkFrame(f2,border_width=2,border_color='white')
        f13 = ctk.CTkFrame(f3,border_width=2,border_color='white')
        f14 = ctk.CTkFrame(f4,border_width=2,border_color='white')
        f15 = ctk.CTkFrame(f5,border_width=2,border_color='white')
        f16 = ctk.CTkFrame(f6,border_width=2,border_color='white')
        f17 = ctk.CTkFrame(f7,border_width=2,border_color='white')
        f18 = ctk.CTkFrame(f8,border_width=2,border_color='white',width=30)

        f10.pack()
        f11.pack()
        f12.pack()
        f13.pack()
        f14.pack()
        f15.pack()
        f16.pack()
        f17.pack()
        f18.pack()

        l0 = ctk.CTkLabel(f10,text='ردیف',font=('b titr',15))
        l1 = ctk.CTkLabel(f11,text='کد شابک',font=('b titr',15))
        l2 = ctk.CTkLabel(f12,text='عنوان کتاب',font=('b titr',15))
        l3 = ctk.CTkLabel(f13,text='نویسنده',font=('b titr',15))
        l4 = ctk.CTkLabel(f14,text='نویسنده دوم',font=('b titr',15))
        l5 = ctk.CTkLabel(f15,text='موضوع کتاب',font=('b titr',15))
        l6 = ctk.CTkLabel(f16,text='قیمت',font=('b titr',15))
        l7 = ctk.CTkLabel(f17,text='ناشر',font=('b titr',15))
        l8 = ctk.CTkLabel(f18,text='نوبت چاپ',font=('b titr',15))

        l0.pack(pady=2,ipadx=35)
        l1.pack(pady=2,ipadx=35)
        l2.pack(pady=2,ipadx=90)
        l3.pack(pady=2,ipadx=60)
        l4.pack(pady=2,ipadx=30)
        l5.pack(pady=2,ipadx=30)
        l6.pack(pady=2,ipadx=60)
        l7.pack(pady=2,ipadx=40)
        l8.pack(pady=2,ipadx=30)

        for i,j in enumerate(cursor1_result):
            if i%2==0:
                col="gray"
            else:
                col="transparent"

            f20 = ctk.CTkLabel(f0,text=i+1,bg_color=col)
            f21 = ctk.CTkLabel(f1,text=j[0],bg_color=col)
            f22 = ctk.CTkLabel(f2,text=j[1],bg_color=col,font=('b nazanin',15))
            f23 = ctk.CTkLabel(f3,text=j[2],bg_color=col,font=('b nazanin',15))
            f24 = ctk.CTkLabel(f4,text=self.empty_find(j[3]),bg_color=col,font=('b nazanin',15))
            f25 = ctk.CTkLabel(f5,text=j[4],bg_color=col,font=('b nazanin',15))
            f26 = ctk.CTkLabel(f6,text=self.space_rem(j[5]),bg_color=col)
            f27 = ctk.CTkLabel(f7,text=j[6],bg_color=col,font=('b nazanin',15))
            f28 = ctk.CTkLabel(f8,text=self.space_rem(j[7]),bg_color=col)

            f20.pack(padx=2,pady=3,ipadx=36)
            f21.pack(padx=2,pady=3,ipadx=30)
            f22.pack(padx=2,pady=3,ipadx=70)
            f23.pack(padx=2,pady=3,ipadx=40)
            f24.pack(padx=2,pady=3,ipadx=40)
            f25.pack(padx=2,pady=3,ipadx=42)
            f26.pack(padx=2,pady=3,ipadx=50)
            f27.pack(padx=2,pady=3,ipadx=30)
            f28.pack(padx=2,pady=3,ipadx=40)

    def add_b(self):
        h = 0
        self.h = h
        self.add_a_book("Add a book to library","Add")

    def add_a_book(self,x,y):
        window2=ctk.CTkToplevel(self.root)
        window2.title(x)
        window2.grab_set()
        self.window2=window2
        frame2=ctk.CTkFrame(window2)
        frame2.grid(row=0,column=0)
        shbq_var=ctk.StringVar()
        title_var=ctk.StringVar()
        author1_var=ctk.StringVar()
        author2_var=ctk.StringVar()
        subject_var=ctk.StringVar()
        price_var=ctk.StringVar()
        publisher_var=ctk.StringVar()
        pubdate_var=ctk.StringVar()
        shbq_lab=ctk.CTkLabel(frame2,text='Shabaq Code')
        title_lab=ctk.CTkLabel(frame2,text='Title')
        author1_lab=ctk.CTkLabel(frame2,text='Main writer')
        author2_lab=ctk.CTkLabel(frame2,text='Additional Writer')
        subject_lab=ctk.CTkLabel(frame2,text='SUbject')
        price_lab=ctk.CTkLabel(frame2,text='Price')
        publisher_lab=ctk.CTkLabel(frame2,text='Publisher')
        pubdate_lab=ctk.CTkLabel(frame2,text='Publish Date')

        shbq_ent=ctk.CTkEntry(frame2,width=300,textvariable=shbq_var,font=('calibri',15),text_color='#FFBF00',placeholder_text="xx-xxxx",placeholder_text_color='#228B22')
        title_ent=ctk.CTkEntry(frame2,width=300,textvariable=title_var,font=('b nazanin',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        author1_ent=ctk.CTkEntry(frame2,width=300,textvariable=author1_var,font=('b nazanin',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        author2_ent=ctk.CTkEntry(frame2,width=300,textvariable=author2_var,font=('b nazanin',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        subject_ent=ctk.CTkEntry(frame2,width=300,textvariable=subject_var,font=('b nazanin',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        price_ent=ctk.CTkEntry(frame2,width=300,textvariable=price_var,font=('calibri',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        publisher_ent=ctk.CTkEntry(frame2,width=300,textvariable=publisher_var,font=('b nazanin',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')
        pubdate_ent=ctk.CTkEntry(frame2,width=300,textvariable=pubdate_var,font=('calibri',15),text_color='#FFBF00',placeholder_text='xx-xxxx (x must be a number)',placeholder_text_color='#228B22')

        if self.h !=0 : 
            shbq_ent.insert(0,self.outp[0])
            title_ent.insert(0,self.outp[1])
            author1_ent.insert(0,self.outp[2])
            author2_ent.insert(0,self.outp[3])
            subject_ent.insert(0,self.outp[4])
            price_ent.insert(0,self.outp[5])
            publisher_ent.insert(0,self.outp[6])
            pubdate_ent.insert(0,self.outp[7])
        shbq_lab.grid(row=0,column=0,padx=10,pady=10)
        shbq_ent.grid(row=0,column=1,padx=10,pady=10)
        
        title_lab.grid(row=1,column=0,padx=10,pady=10)
        title_ent.grid(row=1,column=1,padx=10,pady=10)

        author1_lab.grid(row=2,column=0,padx=10,pady=10)
        author1_ent.grid(row=2,column=1,padx=10,pady=10)

        author2_lab.grid(row=3,column=0,padx=10,pady=10)
        author2_ent.grid(row=3,column=1,padx=10,pady=10)
        subject_lab.grid(row=4,column=0,padx=10,pady=10)
        subject_ent.grid(row=4,column=1,padx=10,pady=10)
        price_lab.grid(row=5,column=0,padx=10,pady=10)
        price_ent.grid(row=5,column=1,padx=10,pady=10)
        publisher_lab.grid(row=6,column=0,padx=10,pady=10)
        publisher_ent.grid(row=6,column=1,padx=10,pady=10)
        pubdate_lab.grid(row=7,column=0,padx=10,pady=10)
        pubdate_ent.grid(row=7,column=1,padx=10,pady=10)

        lis=[]
        self.lis=lis
        lis.extend([shbq_ent,title_ent,author1_ent,author2_ent,subject_ent,price_ent,publisher_ent,pubdate_ent])

        button01 = ctk.CTkButton(window2,width=200,text=y,command=self.add_book_Validation)
        button01.grid(row=1,column=0,pady=10)

    def add_book_Validation(self):
        value=[]
        self.value = value
        for i,j in enumerate(self.lis):
            val=j.get()
            if i==0:
                if len(val)!=7:
                    messagebox.showerror("Error","Shabaq code must be 7 charecters!")
                    break
                num="0123456789-"
                for nu in val:
                    if nu not in num:
                        messagebox.showerror("Error","Shabaq code must be numberic (xx-xxxx)!")
                        break
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Shabaq code of the book must not be empty!")
                    break
            if i==1:
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Title of the book must not be empty!")
                    break
            if i==2:
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Main Writer of the book must not be empty!")
                    break
            if i==4:
                if val==None or val==" " or val=="":
                    messagebox.showerror("Error","Subject of the book must not be empty!")
                    break
            if i==5:
                try:
                    numbr = float(val)
                except:
                    messagebox.showerror("Error","Price must be a number!")
                    break
                if numbr<0:
                    messagebox.showerror("Error","Price can not be negetive!")
                    break
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Price of the book must not be empty!")
                    break
            if i==6:
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Someone must have published the book!")
                    break
            if i==7:
                try:
                    numb=int(val)
                except:
                    messagebox.showerror("Error","Publish Date must be an intiger!")
                    break
                if len(val)!=4:
                    messagebox.showerror("Error","Publish Date must be a year (yyyy like 1380)!")
                    break
                if val==None or val==" "or val=="":
                    messagebox.showerror("Error","Publish Date of the book must not be empty!")
                    break
            value.append(val)
        else:
            if self.h == 0 :
                self.add_b1()
            else:
                self.upd()

    def add_b1(self):
        try:
            curs=self.server.cursor()
            curs.execute("INSERT INTO book VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",self.value)
            self.server.commit()
            messagebox.showinfo("Succesfull","The book was successfully added to library.")
        except:
            messagebox.showerror("Error","Unexpected error, please try again later.")

    def upd(self):
        x = self.value
        try:
            curs=self.server.cursor()
            curs.execute("UPDATE book SET shbq=%s, title=%s, author1=%s, author2=%s, subject=%s, price=%s, publisher=%s, pub_date#=%s WHERE book.shbq = %s AND book.title = %s",(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], self.outp[0], self.outp[1]))
            self.server.commit()
            messagebox.showinfo("Succesfull","The book was successfully edited to library.")
        except:
            messagebox.showerror("Error","Unexpected error, please try again later.")

    def search(self):
        window4 = ctk.CTkToplevel(self.root)
        window4.title("Searching a book in library")
        self.window4 = window4
        window4.grab_set()
        window4.geometry("1300x500")
        window4.resizable(False,True)
        ent_var = ctk.StringVar()
        search_ent = ctk.CTkEntry(window4,font=('b nazanin',30),height=30,placeholder_text='???',textvariable=ent_var)
        self.search_ent=search_ent
        search_ent.pack(fill='x',padx=5,pady=5)
        butt = ctk.CTkButton(window4,text="Search",state="disabled",hover_color='#E32227',height = 30,bg_color='transparent',fg_color='transparent',command=self.search_b)
        butt.pack(fill='x',padx=40)
        search_ent.wait_variable(ent_var)
        butt.configure(state="normal",fg_color="gray")
        c = False
        self.c=c
    
    def search_b(self):
        if self.c:
            self.fr1.destroy()
            self.fr2.destroy()
        x = self.search_ent.get()
        cursor1 = self.server.cursor()
        cursor1.execute("SELECT * FROM book")
        cursor1_result = cursor1.fetchall()
        output=[]
        for i,j in enumerate(cursor1_result):
            for k in j:
                if k==None or k=="" or k==" ":
                    continue
                if (x == k or x in k) and (j not in output):
                    output.append(j)
        self.output=output
        if len(output)>0 and output[0] != "":
            self.c = True
            fr1 = ctk.CTkFrame(self.window4)
            self.fr1 = fr1
            fr1.pack(fill='x')
            self.books_list(output,fr1,200)
            fr2 = ctk.CTkFrame(self.window4)
            self.fr2=fr2
            fr2.pack(fill='x',pady=40)
            fr3 = ctk.CTkFrame(fr2,width=400)
            fr3.grid(row=0,column=2,padx=20)
            ent_var1 = ctk.StringVar()
            ent = ctk.CTkEntry(fr3,font=('b nazanin',30),height=30,width=60,placeholder_text='???',textvariable=ent_var1)
            self.ent = ent
            ent.grid(row=0,column=0,padx=10)
            edit_butt = ctk.CTkButton(fr2,text="Edit",state="disabled",hover_color='#E32227',height = 30,bg_color='transparent',fg_color='transparent',command=self.edit_rec)
            edit_butt.grid(row=0,column=0,padx=20)
            del_butt = ctk.CTkButton(fr2,text="Delete",state="disabled",hover_color='#E32227',height = 30,bg_color='transparent',fg_color='transparent',command=self.del_rec)
            del_butt.grid(row=0,column=1,padx=20)
            lab1 = ctk.CTkLabel(fr3,text = "برای ویرایش هر کدام از گزینه ها، شماره ردیف را در کادر مقابل وارد کنید",font=('b nazanin',20))
            lab1.grid(row=0,column=3,padx=20)
            ent.wait_variable(ent_var1)
            edit_butt.configure(state="normal",fg_color="#228B22")
            del_butt.configure(state="normal",fg_color="#E32227")
        else:
            messagebox.showinfo("Nothing","We found nothing in our library whith the result you want.")
    
    def del_rec(self):
        k = True
        q = self.ent.get()
        try:
            q = int(q)
        except:
            messagebox.showerror("Error","You have to enter a number in the id box.")
            k = False
        if len(self.output)<q:
            messagebox.showerror("Error","The id must be in resault list.")
            k = False
        k = messagebox.askokcancel("Warning",f"Are you sure you want to delete {self.output[q-1][1]} by {self.output[q-1][2]}")
        if k:
            tmp1 = self.output[q-1][0]
            tmp2 = self.output[q-1][1]
            cursor2 = self.server.cursor()
            cursor2.execute("DELETE FROM book WHERE book.shbq = (%s) AND book.title = (%s)",(tmp1,tmp2))
            self.server.commit()
            messagebox.showinfo("Sucess","The record sucessfuly deleted!")
    def edit_rec(self):
        k = True
        q = self.ent.get()
        try:
            q = int(q)
        except:
            messagebox.showerror("Error","You have to enter a number in the id box.")
            k = False
        if len(self.output)<q:
            messagebox.showerror("Error","The id must be in resault list.")
            k = False
        k = messagebox.askokcancel("Warning",f"Are you sure you want to edit {self.output[q-1][1]} by {self.output[q-1][2]}")
        if k:
            outp = self.output[q-1]
            print(outp)
            self.outp = outp
            h = 1
            self.h = h
            self.add_a_book("Editting a book in library","Edit")
a = main()
root = ctk.CTk()
a.root_app(root)
a.main_page()
root.mainloop()