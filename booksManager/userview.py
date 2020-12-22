# -*-coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import pymysql
class user(object):
    def __init__(self):
        # self.root = Tk()# 定义内部变量root
        # self.root.title("user view")
        # self.root.geometry('300x300')

        self.sid=StringVar()
        self.password = StringVar()

        self.name=StringVar()
        self.email=StringVar()
        self.phone=StringVar()

        self.bookID=StringVar()
        self.bookname=StringVar()
        self.bookpublishtime=StringVar()
        self.bookauthor=StringVar()
        self.usercheck()
    def usercheck(self):
        win = Toplevel()  # 创建Frame

        Label(win).grid(row=0, stick=W)
        Label(win, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(win, textvariable=self.sid).grid(row=1, column=1, stick=E)
        Label(win, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(win, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(win, text='注册', command=self.rig).grid(row=3, column=2, stick=E)
        Button(win, text='登陆', command=self.use).grid(row=3, stick=W, pady=10)
        Button(win, text='退出', command=win.quit).grid(row=3, column=1, stick=E)
    def use(self):
        con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
        cur = con.cursor()
        sql="select* from users where UsersID=%s and password=%s"
        result=cur.execute(sql,(self.sid.get(),self.password.get()))
        if result<1:
            showerror(title="id or password is wrong")
        else:
            self.main()

    def rig(self):
        win0=Toplevel()
        # win0.pack()
        # win0.title("注册")
        # win0.geometry('400x400')

        Label(win0, text='学号: ').grid(row=0, stick=W, pady=10)
        Entry(win0, textvariable=self.sid).grid(row=0, column=1, stick=E)
        Label(win0, text='姓名: ').grid(row=1, stick=W, pady=10)
        Entry(win0, textvariable=self.name).grid(row=1, column=1, stick=E)
        Label(win0, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(win0, textvariable=self.password).grid(row=2, column=1, stick=E)
        Label(win0, text='emial: ').grid(row=4, stick=W, pady=10)
        Entry(win0, textvariable=self.email).grid(row=4, column=1, stick=E)
        Label(win0, text='phone ').grid(row=3, stick=W, pady=10)
        Entry(win0, textvariable=self.phone).grid(row=3, column=1, stick=E)
        Button(win0, text='注册', command=self.view).grid(row=5, stick=W, pady=10)
        Button(win0, text='退出', command=win0.quit).grid(row=5, column=1, stick=E)

    def view(self):
        if self.sid.get()==""or self.name.get()=="" or self.password.get()=="":
                showerror(title='提示', message='请输入完整信息！')
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            # 检验ISBN是否已经存在
            sqlSearch = "select * from users where UsersID = %s"
            result = cur.execute(sqlSearch, self.sid.get())
            if result > 0:
                showerror(title="提示", message="sid已存在！")
            else:
                sql = "insert into users values(%s,%s,%s,%s,%s)"
                cur.execute(sql, (self.sid.get(),self.name.get(),self.password.get(),self.email.get(),self.phone.get()))
                con.commit()
            cur.close()
            con.close()
            self.use()
    def main(self):
        self.Win2=Toplevel()
        self.Win2.geometry("1800x600")
        Label(self.Win2, text="bookID").place(relx=0, rely=0.05, relwidth=0.1)
        Label(self.Win2, text="书名：").place(relx=0.5, rely=0.05, relwidth=0.1)
        Label(self.Win2, text="作者：").place(relx=0, rely=0.1, relwidth=0.1)
        Label(self.Win2, text="出版社：").place(relx=0.5, rely=0.1, relwidth=0.1)
        # Label(self.Win2, text="出版时间").place(relx=0, rely=0.15, relwidth=0.1)

        Entry(self.Win2, textvariable=self.bookID).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookname).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookauthor).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
        Entry(self.Win2, textvariable=self.bookpublishtime).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)
        # Entry(self.Win2, textvariable=self.price).place(relx=0.1, rely=0.15, relwidth=0.37, height=25)

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
        # 按钮
        Button(self.Win2, text="借阅图书", command=self.lendbook).place(relx=0.15, rely=0.25, width=80)
        Button(self.Win2, text="查询图书", command=self.searchBook).place(relx=0.3, rely=0.25, width=80)
        Button(self.Win2, text="我的借阅记录", command=self.record).place(relx=0.45, rely=0.25, width=80)
        Button(self.Win2, text="还书", command=self.returnbook).place(relx=0.6, rely=0.25, width=80)
        Button(self.Win2, text="退出", command=self.Win2.quit).place(relx=0.75, rely=0.25, width=80)
    def searchBook(self):
        # 针对书名进行查询并显示
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
    def lendbook(self):
        if self.bookID.get()=="":
            showerror(title="提示",message="请输入bookid")
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            sql1 = "insert into borrowbook (bookID,borrowtime,shouldbacktime,Infactbacktime,backyon,breakyon,sid)\
            values('%s',curdate(),date_add(curdate(),interval 30 day),NULL,'否','否',%s)"%(self.bookID.get(),self.sid.get())#调用sql内部时间函数，随机生成顺序数borrowid，表内插入sid
            sql2 = 'update book set stock=stock-1 where bookID="%s"'%(self.bookID.get())
            cur.execute(sql1)
            con.commit()
            cur.execute(sql2)
            con.commit()
            showinfo(message="借书成功")
        cur.close()
        con.close()
    def returnbook(self):
        if self.bookID.get()=="":
            showerror(title="tishi",message="bookid")
        else:
            con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
            cur = con.cursor()
            sql1="update book set stock=stock+1 where bookID='%s';"%(self.bookID.get())
            cur.execute(sql1)
            con.commit()
            sql2="update Borrowbook set backyon='是' where bookID='%s'and sid='%s';" %(self.bookID.get(),self.sid.get())
            cur.execute(sql2)
            con.commit()
            sql3="update Borrowbook set breakyon='是' where bookID='%s' and shouldbacktime<CURDATE();" %(self.bookID.get())
            cur.execute(sql3)
            con.commit()
            sql4="update Borrowbook set Infactbacktime= DATE_FORMAT(CURDATE(),'%%yy%%m%%d');"

            cur.execute(sql4)
            con.commit()
            showinfo(message="归还成功")
        cur.close()
        con.close()
    #    self.showAllBooks()
    def record(self):
        self.treer = ttk.Treeview(self.Win2, show='headings', column=('bookID','shouldbacktime','backyon'))
        self.treer.column('bookID', width=150, anchor="center")
        self.treer.column('shouldbacktime', width=150, anchor="center")
        self.treer.column('backyon', width=150, anchor="center")


        # self.treer.column('price', width=150, anchor="center")

        self.treer.heading('bookID', text='bookID')
        self.treer.heading('shouldbacktime', text='应还时间')

        self.treer.heading('backyon', text='是否归还')


        self.treer.place(rely=0.35, relwidth=1, relheight=0.6)
        con = pymysql.connect(user='root', password='root', database='books', charset='utf8')
        cur = con.cursor()
        sqlname = "SELECT bookID,shouldbacktime,backyon FROM borrowbook WHERE sid= %s"
        sqlname = sqlname % (self.sid.get())
        result = cur.execute(sqlname)
        if result < 1:
            showerror(title='提示', message='未找到相关记录')
        else:
            # 清除原有treerview数据
            x = self.treer.get_children()
            for item in x:
                self.treer.delete(item)
            lst = cur.fetchall()
            for item in lst:
                self.treer.insert("", 1, text="line1", values=item)

        cur.close()
        con.close()


