# -*-coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from userview import user
import pymysql
#from main import main


class Login(object):

    def __init__(self, master):
        self.root = master  # 定义内部变量root
        # self.root.withdraw()
        self.root.geometry('300x180')  # 设置窗口大小
        self.Win = Frame(self.root)  # 创建Frame

        self.username = StringVar()
        self.password = StringVar()

        self.bookID=StringVar()
        self.bookname=StringVar()
        self.bookpublishtime=StringVar()
        self.bookauthor=StringVar()
        self.stock=IntVar()

        self.roomID=StringVar()
        self.numlimit=StringVar()
        self.services=StringVar()

        self.Win2 = master
        self.Win3 = master

        self.createWindow()

    def createWindow(self):

        self.Win.pack()
        Label(self.Win).grid(row=0, stick=W)
        Label(self.Win, text='请选择登陆类型 ').grid(row=1, stick=W, pady=10)
 #       Entry(self.Win, textvariable=self.username).grid(row=1, column=1, stick=E)
 #       Label(self.Win, text='密码: ').grid(row=2, stick=W, pady=10)
 #       Entry(self.Win, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.Win, text='管理员', command=self.loginCheck1).grid(row=2, stick=W, pady=10)
        Button(self.Win, text='用户', command=user).grid(row=2, stick=E, pady=10)
        # Button(self.Win, text='用户', command=self.loginCheck2).grid(row=2,column=1, stick=E)
        # Button(self.Win, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.Win, text='退出', command=self.Win.quit).grid(row=3, column=1, stick=E)


    def loginCheck1(self):
        Win=Tk()
        Win.title("login")
        Win.geometry('250x250')
        Label(Win).grid(row=0, stick=W)
        Label(Win, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(Win, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(Win, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(Win, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(Win, text='登陆', command=self.loginCheck2).grid(row=3, stick=W, pady=10)
        Button(Win, text='退出', command=Win.quit).grid(row=3, column=1, stick=E)
        Win.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0));
    def loginCheck2(self):
        self.win=Tk()
        self.win.title("管理员操作")
        self.win.geometry("200x200")
        btn1=Button(self.win,text="研讨间",command=self.roomf)
        btn2=Button(self.win,text="图书与用户",command=self.bookf)
        # btn3=Button(self.win,text="用户")
        btn1.grid(column=3,row=1)
        btn2.grid(column=6,row=1)
        # btn3.grid(column=9,row=1)
     # def loginCheck2(self):
    #     user(self.root)

    def bookf(self):

        self.Win2=Toplevel()
        Label(self.Win2, text="bookID").place(relx=0, rely=0.05, relwidth=0.1)
        Label(self.Win2, text="书名：").place(relx=0.5, rely=0.05, relwidth=0.1)
        Label(self.Win2, text="作者：").place(relx=0, rely=0.1, relwidth=0.1)
        Label(self.Win2, text="馆藏量").place(relx=0.5, rely=0.1, relwidth=0.1)
        Label(self.Win2, text="出版时间").place(relx=0, rely=0.15, relwidth=0.1)
        Label(self.Win2, text="出版社：").place(relx=0.5, rely=0.15, relwidth=0.1)
        Label(self.Win2, text="版次").place(relx=0, rely=0.2, relwidth=0.1)


        # Label(self.Win2, text="出版时间").place(relx=0, rely=0.15, relwidth=0.1)

        Entry(self.Win2, textvariable=self.bookID).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookname).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookauthor).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.stock).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookpublishtime).place(relx=0.1, rely=0.15, relwidth=0.37, height=25)
        Entry(self.Win2).place(relx=0.6, rely=0.15, relwidth=0.37, height=25)
        Entry(self.Win2).place(relx=0.1, rely=0.2, relwidth=0.37, height=25)

        Button(self.Win2, text="显示所有图书", command=self.showAllBooks).place(relx=0.15, rely=0.25, width=80)
        Button(self.Win2, text="查询图书", command=self.searchBook).place(relx=0.3, rely=0.25, width=80)
        Button(self.Win2, text="修改图书", command=self.modifyBook).place(relx=0.45, rely=0.25, width=80)
        Button(self.Win2, text="添加图书", command=self.addBook).place(relx=0.6, rely=0.25, width=80)
        Button(self.Win2, text="删除图书", command=self.deleteBook).place(relx=0.75, rely=0.25, width=80)
        Button(self.Win2, text="所有用户", command=self.allusers).place(relx=0.9, rely=0.25, width=80)

        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        # # 表格
        # self.tree = ttk.Treeview(self.Win2, show='headings', column=('isbn', 'name', 'author', 'publisher', 'price'))
        # self.tree.column('isbn', width=150, anchor="center")
        # self.tree.column('name', width=150, anchor="center")
        # self.tree.column('author', width=150, anchor="center")
        # self.tree.column('publisher', width=150, anchor="center")
        # self.tree.column('price', width=150, anchor="center")
        #
        # self.tree.heading('isbn', text='ISBN')
        # self.tree.heading('name', text='书名')
        # self.tree.heading('author', text='作者')
        # self.tree.heading('publisher', text='出版社')
        # self.tree.heading('price', text='价格')
        #
        # self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        # 按钮


    #    self.showAllBooks()

    def allusers(self):
         # 表格
        self.treeu = ttk.Treeview(self.Win2, show='headings', column=('UserID', 'name', 'password', 'email', 'phone'))
        self.treeu.column('UserID', width=150, anchor="center")
        self.treeu.column('name', width=150, anchor="center")
        self.treeu.column('password', width=150, anchor="center")
        self.treeu.column('email', width=150, anchor="center")
        self.treeu.column('phone', width=150, anchor="center")

        self.treeu.heading('UserID', text='编号')
        self.treeu.heading('name', text='姓名')
        self.treeu.heading('password', text='密码')
        self.treeu.heading('email', text='邮箱')
        self.treeu.heading('phone', text='电话号码')

        self.treeu.place(rely=0.35, relwidth=1, relheight=0.6)

        x = self.treeu.get_children()
        for item in x:
            self.tree.delete(item)
        con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
        cur = con.cursor()#获取游标
        cur.execute("select * from users")
        lst = cur.fetchall()
        # treeview的插入方法
        for item in lst:
            self.treeu.insert("", 1, text="line1", values=item)
        cur.close()
        con.close()
    # 查询所有书籍信息
    def showAllBooks(self):
        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
        cur = con.cursor()#获取游标
        cur.execute("select * from book")
        lst = cur.fetchall()
        # treeview的插入方法
        for item in lst:
            self.tree.insert("", 1, text="line1", values=item)
        cur.close()
        con.close()

    # 添加书籍信息
    def addBook(self):
        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        if self.bookID.get() == "" or self.bookname.get() == "" or self.stock.get() == "":
            showerror(title='提示', message='请输入完整信息！')
        else:
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()


            # 检验ISBN是否已经存在
            sqlSearch = "select * from book where bookID = %s"
            result = cur.execute(sqlSearch, self.bookID.get())
            if result > 0:
                showerror(title="提示", message="bookID已存在！")
            else:
                sql = "insert into book (bookID,name,author,stock) values(%s,%s,%s,%s)"
                cur.execute(sql, (self.bookID.get(),self.bookname.get(), self.bookauthor.get(), self.stock.get()))
                con.commit()
                cur.execute("select * from book")
                lst = cur.fetchall()
                for item in lst:
                    self.tree.insert("", 1, text="line1", values=item)
            cur.close()
            con.close()

    # 删除书籍信息
    def deleteBook(self):
        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        if self.bookID.get() == '':
            showerror(title='提示', message='请输入ISBN')
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            line = cur.execute("delete from book where bookID = %s", self.bookID.get())
            if line == 0:
                showerror(title="提示", message="删除失败，请检查bookID")
            else:
                showinfo(title="提示", message="删除成功！")
                con.commit()
            cur.close()
            con.close()
            self.showAllBooks()

    # 查询书籍信息
    def searchBook(self):
        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        # 针对书名进行查询并显示
        if self.bookname.get() == "":
            showerror(title='提示', message='请输入书籍名称进行查询')
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            # 对模糊查询的%进行转移
            sqlname = "select * from book where name like '%%%%%s%%%%'"
            sqlname = sqlname % (self.bookname.get())
            result = cur.execute(sqlname)
            if result < 1:
                showerror(title='提示', message='未找到相关图书')
            else:
                # 清除原有Treeview数据
                x = self.tree.get_children()
                for item in x:
                    self.tree.delete(item)
                lst = cur.fetchall()
                for item in lst:
                    self.tree.insert("", 1, text="line1", values=item)

            cur.close()
            con.close()

    # 修改书籍信息
    def modifyBook(self):
        # 表格
        self.tree = ttk.Treeview(self.Win2, show='headings', column=('bookID', 'name', 'publisher', 'publishtime', 'edition','author','stock'))
        self.tree.column('bookID', width=150, anchor="center")
        self.tree.column('name', width=150, anchor="center")
        self.tree.column('publisher', width=150, anchor="center")
        self.tree.column('publishtime', width=150, anchor="center")
        self.tree.column('edition', width=150, anchor="center")
        self.tree.column('author', width=150, anchor="center")
        self.tree.column('stock', width=150, anchor="center")

        # self.tree.column('price', width=150, anchor="center")

        self.tree.heading('bookID', text='bookID')
        self.tree.heading('name', text='书名')

        self.tree.heading('publisher', text='出版社')
        self.tree.heading('publishtime', text='publishtime')
        self.tree.heading('edition', text='edition')
        self.tree.heading('author', text='作者')
        self.tree.heading('stock', text='stock')
        # self.tree.heading('price', text='价格')

        self.tree.place(rely=0.35, relwidth=1, relheight=0.6)
        if self.bookID.get() == "" or self.bookname.get() == "" or self.bookauthor.get() == "" :
            showerror(title='提示', message='请输入完整信息！')
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            # sql = 'update books set name=' + self.name.get() + ',' + 'author=' + self.author.get() + ',' \
            #       + 'publisher=' + self.publisher.get() + ',' + 'price=' + self.price.get() + ' where isbn=' + self.isbn.get()
            # result = cur.execute(sql, (
            #     self.name.get(), self.author.get(), self.publisher.get(), self.price.get(), self.isbn.get()))
            sql = 'update book set name=%s, author=%s where bookID=%s'%(self.bookID.get())
            # result = cur.execute(sql)
            result = cur.execute(sql)
            print(sql)
            print(result)
            if result > 0:
                showinfo(title='提示', message='修改成功！')
                con.commit()
                self.showAllBooks()
            else:
                showerror(title="提示", message="修改失败！")
            cur.close()
            con.close()
#            self.Win.mainloop()
    def roomf(self):

        self.Win3.title("all rooms")
        self.Win3.geometry("400x400+200+50")
   #     self.Win3 = Frame(self.Win3)

    #    self.Win3.pack()

        Label(self.Win3, text="roomID").place(relx=0, rely=0.05, relwidth=0.1)
        Label(self.Win3, text="numlimit").place(relx=0.5, rely=0.05, relwidth=0.1)
        Label(self.Win3, text="services").place(relx=0, rely=0.1, relwidth=0.1)


        Entry(self.Win3, textvariable=self.roomID).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win3, textvariable=self.numlimit).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win3, textvariable=self.services).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)


        # 表格
        self.tree2 = ttk.Treeview(self.Win3, show='headings', column=('roomID', 'numlimit', 'services'))
        self.tree2.column('roomID', width=150, anchor="center")
        self.tree2.column('numlimit', width=150, anchor="center")
        self.tree2.column('services', width=150, anchor="center")


        self.tree2.heading('roomID', text='roomID')
        self.tree2.heading('numlimit', text='numlimit')
        self.tree2.heading('services', text='services')


        self.tree2.place(rely=0.35, relwidth=1, relheight=0.6)
        # 按钮
        Button(self.Win3, text="显示所有研讨间", command=self.showAllrooms).place(relx=0.15, rely=0.25, width=80)
        Button(self.Win3, text="查询研讨间", command=self.searchBook).place(relx=0.3, rely=0.25, width=80)
        Button(self.Win3, text="修改研讨间", command=self.modifyBook).place(relx=0.45, rely=0.25, width=80)
        Button(self.Win3, text="添加研讨间", command=self.addroom).place(relx=0.6, rely=0.25, width=80)
        Button(self.Win3, text="删除研讨间", command=self.deleteBook).place(relx=0.75, rely=0.25, width=80)

    def addroom(self):
        if self.roomID.get() == "" or self.numlimit.get() == "" or self.services.get() == "" :
            showerror(title='提示', message='请输入完整信息！')
        else:
            x = self.tree2.get_children()
            for item in x:
                self.tree2.delete(item)

            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()

            roomID = self.roomID.get()
            numlimit = self.numlimit.get()
            services = self.services.get()

            # 检验ISBN是否已经存在
            sqlSearch = "select * from room where roomID = %s"
            result = cur.execute(sqlSearch, roomID)
            if result > 0:
                showerror(title="提示", message="room已存在！")
            else:
                sql = "insert into room values(%s,%s,%s)"
                cur.execute(sql, (roomID,numlimit,services))
                con.commit()
                cur.execute("select * from room")
                lst = cur.fetchall()
                for item in lst:
                    self.tree2.insert("", 1, text="line1", values=item)
            cur.close()
            con.close()
        self.showAllrooms()
    def showAllrooms(self):
        x = self.tree2.get_children()
        for item in x:
            self.tree2.delete(item)
        con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
        cur = con.cursor()#获取游标
        cur.execute("select * from room")
        lst = cur.fetchall()
        # treeview的插入方法
        for item in lst:
            self.tree2.insert("", 1, text="line1", values=item)
        cur.close()
        con.close()

