# 4. Creating tabbed widgets:
#The tabbed widgets are called Notebooks in Tkinter, It manages a collection of windows and displays on a single window.
#Syntax:
#Tab_name=ttk.Notebook(options)
#The options used in tabbed widgets are
#Height – Height of the widget.
#Width – Width of the widget.
#Padding – Space around the outside of tab.

#Ok, let’s Create a simple tabbed widget contained window.

#Adding widgets in the tabs, Example
from tkinter import ttk
import tkinter as tk
from  datetime import date
import sqlite3
import datetime
from tkinter import messagebox




#def create():
#    
#    conn = sqlite3.connect("customers.db")
#    c = conn.cursor()
#    
#    #01234567
#    c.execute("CREATE TABLE IF NOT EXISTS plus2_invoice_dtl (item TEXT,qty_stock INT,total_gzzi INT,total_shyach INT,qty_shyach INT,credits INT,wechi INT,profit INT)")
#    
#    
#    conn.commit()
#    conn.close()








########################################################################


    #
    
    #############
    
profit,iid=0,0

def my_add():
    
    
    
    itemvars=itemvar.get()
    qtyvars=qtyvar.get()
    pricevars=pricegzzivar.get()
    
    
    profit=pricevars*qtyvars
    
    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
    
    
    
    conn = sqlite3.connect("customers.db")
    table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (item TEXT,qty_stock INT,total_gzzi INT,total_shyach INT,qty_shyach INT,credits INT,wechi INT,profit INT)
            '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO Student_Data (item, qty_stock, total_gzzi, 
            total_shyach, qty_shyach, credits, wechi, profit) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
    
    data_insert_tuple = (itemvars,qtyvars,pricevars,'4','5','6','7',profit)
    
    
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
    
    print("success")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    global iid
    iid=iid+1  # Serial number to display 
    profit=round(qtyvar.get()*pricegzzivar.get(),2) # row wise total 
    trv.insert("", 'end',iid=iid, values =(itemvar.get(),qtyvar.get(),pricegzzivar.get(),"09",'66','','87',profit))
    
    my_upd(trv)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ################
    
    
    
    
    
    
    
#profit,iid=0,0
#def my_add():    
#    global iid
#    
#    iid=iid+1
#    
#    profit=round(qtyvar.get()*pricegzzivar.get(),2)
#    
#    #profit=round(((float(trv.item["values"][4]),2/trv.item["values"][5]))-(( float(trv.item["values"][3]),2/trv.item["values"][2])))
#        
#    trv.insert("", 'end',iid=iid, values =(itemvar.get(),qtyvar.get(),pricegzzivar.get(),"09",'66','','87',profit))
#    
#    my_upd(trv)





def my_upd(trv):
    global profit
    profit,tot_profit=0,0
    for child in trv.get_children():
        tot_profit=round(tot_profit+float(trv.item(child)["values"][7]),2)
        
    l16.config(text=str(tot_profit)) # shows sub total 
    #tax=round(0.1*sub_total,2)  # 10 % tax rate,update here
#    l8.config(text=str(tax))  # tax amount is displayed 
#    total=round(sub_total+tax,2) # tax added to sub total 
#    l10.config(text=str(total))  # Final price is displayed
#    
    itemvar.set('') # reset the combobox 
    qtyvar.set('')  # reset quantity to 1
    pricegzzivar.set('')






#pluss2 code


#def my_upd(trv):
#    #global total 
#    total,sub_total=0,0
#    for child in trv.get_children():
#        sub_total=round(sub_total+float(trv.item(child)["values"][6]),2)
#    l6.config(text=str(sub_total)) # shows sub total 
#    tax=round(0.1*sub_total,2)  # 10 % tax rate, update here
#    l8.config(text=str(tax))  # tax amount is displayed 
#    total=round(sub_total+tax,2) # tax added to sub total 
#    l10.config(text=str(total))  # Final price is displayed
#    
#    itemvar.set('') # reset the combobox 
#    qtyvar.set('')  # reset quantity to 1
#    pricegzzivar.set('')
    
    
    
 
 
 
 
 
 
    
def my_select(self):
    b2.config(state='active') # Delete button is active now 
def data_delete():
    p_id = trv.selection()[0] # collect selected row id
    trv.delete(p_id)  # remove the selected row from Treeview
    b2['state']='disabled' # disable the button 
    my_upd(trv) # Update the total 
def my_reset():
    for item in trv.get_children():
        trv.delete(item) # remove row 
    global total
    total=0
    
    
    
    itemvar.set('') # reset the combobox 
    qtyvar.set('')  # reset quantity to 1
    pricegzzivar.set('')
    #pricevar.set('')
#    namevar.set('')
#    phonevar.set('')
#    creditvar.set('')
#    accountvar.set('')
#    totalvar.set('')
    
    l16.config(text='0')  # Update display sub total
    #l8.config(text='0')  # Update display for tax
#    l10.config(text='0') # Update display for total

################################################################################################################################################


#child=0

def insert_data():
    #global total
#    #global items
#    global child
#    child=child + 1
#    for child in trv.get_children():
#        items=(trv.item(child)["values"][1])
#        qty_stock=(trv.item(child)["values"][2])
#        total_gzzi=(trv.item(child)["values"][3])
#        total_shyach=(trv.item(child)["values"][4])
#        qty_shyach=(trv.item(child)["values"][5])
#        credits=(trv.item(child)["values"][6])
#        wechi=(trv.item(child)["values"][7])
#        profit=(trv.item(child)["values"][8])
#        
#        
#    conn = sqlite3.connect("customers.db")
#    c = conn.cursor()
#        
#    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#    c.execute("INSERT INTO plus2_invoice_dtl (item,qty_stock,total_gzzi,total_shyach,qty_shyach,credits,wechi,profit) VALUES ( ?, ? , ?, ?, ? ,?, ?,?)",(items,qty_stock,total_gzzi,total_shyach,qty_shyach,credits,wechi,profit))
#    conn.commit()
#    conn.close()
#    print("success")
#    my_upd(trv)
#        
        
        
        
##############################################################################################################################    
        
        
        
        
        
        
        
        
        #conn = sqlite3.connect("customers.db")
#        c = conn.cursor()
#        
#        date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#        c.execute("INSERT INTO plus2_invoice_dtl (item,qty_stock,total_gzzi,total_shyach,qty_shyach,credits,wechi,profit) VALUES ( ?, ? , ?, ?, ? ,?, ?,?)",(item(child)["values"][1],trv.item(child)["values"][2],trv.item(child)["values"][3],trv.item(child)["values"][4],trv.item(child)["values"][5],trv.item(child)["values"][6],trv.item(child)["values"][7],trv.item(child)["values"][8]))
#        
#        
#        conn.commit()
#        conn.close()
#        print("success")






#def insert_data():
#    #global total
#    
#    #for child in trv.get_children():
#    conn = sqlite3.connect("customers.db")
#    c = conn.cursor()
#    
#    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#    c.execute("INSERT INTO plus2_invoice_dtl (item,qty_stock,total_gzzi,total_shyach,qty_shyach,credits,wechi,profit) VALUES ( ?, ? , ?, ?, ? ,?, ?,?)",(trv.item[1],'hey','hey','hey','hey','hey','hey','hey',))
#    
#    
#    conn.commit()
#    conn.close()
#    print("success")















    
    #dt = date.today() # Today's date 
#    data=(total,dt) # Data for parameterized query
#    query="INSERT INTO plus2_invoice ( total, dt) values(?,?)"
    #print(query)
    #id=conn.execute(query,data)
#    inv_id=id.lastrowid # get the bill or invoice number after adding data
    
    #query="INSERT INTO  plus2_invoice_dtl where price=total"
#    my_data=[] # list to store multiple rows of data
#    # In all rows inventory id is same
#    #for line in trv.get_children():
#        my_list=trv.item(line)['values']
#        my_data.append([id,my_list[0],my_list[1],my_list[2],my_list[3]])
#    id=conn.execute(query,my_data) # adding list of products to table
#    #print("Rows Added  = ",id.rowcount)
#    l_msg.config(text='Bill No:'+str(id)+',Products:'+str(id.rowcount))

    
    l_msg.after(3000, lambda: l_msg.config(text='') )
    
    
    my_reset() # reset function 
















font1=['Times',7,'normal'] # font size and style 
font2=['Times',7,'normal']
 
labelframe =tk.Tk()
labelframe.geometry('640x300')
labelframe.title('IoT4Begineers')
 
tabs = ttk.Notebook(labelframe)
first = ttk.Frame(tabs)
tabs.add(first, text='First')



second = ttk.Frame(tabs)
tabs.add(second, text='Second')

##########
#a = Button(first, text='Hello There This is 1st Tab', bg='Red')
#a.pack()
#########
item_label=tk.Label(first, text="item")
item_label.grid(row=6, column=0,sticky='w')

qty_label=tk.Label(first, text='QTY')
qty_label.grid(row=7, column=0,sticky='w')


price_gzzi_label=tk.Label(first, text="gzi br")
price_gzzi_label.grid(row=8, column=0,sticky='w')




#p_list=['Moniter','Mouse','Keyboard','Pen Drive','CPU','Power Unit'] # product list
#itemvar=tk.StringVar(my_w)
#itemscombo = ttk.Combobox(my_w, values=p_list,textvariable=itemvar,width=13,placeholder="items")
#itemscombo.grid(row=9,column=1)





itemvar=tk.StringVar()
itementry= tk.Entry(first, textvariable=itemvar,width=8,placeholder="items")
itementry.grid(row=6,column=1,sticky='w')


qtyvar=tk.IntVar(value="")
quantityentry = tk.Entry(first, textvariable=qtyvar,width=8,placeholder="item qty")
quantityentry.grid(row=7,column=1,sticky='w')



pricegzzivar=tk.DoubleVar(value="")
pricegzzientry= tk.Entry(first, textvariable=pricegzzivar,width=8,placeholder="gzi birr")
pricegzzientry.grid(row=8,column=1,sticky='w')







#totalvar=tk.IntVar(value="")
#totalentry = tk.Entry(my_w, textvariable=totalvar,width=15,placeholder="total")
#totalentry.grid(row=12,column=1)



#accountvar=tk.IntVar(value="")
#totalentry = tk.Entry(my_w, textvariable=accountvar,width=15,placeholder="account")
#totalentry.grid(row=13,column=1)

#creditvar=tk.IntVar(value="")
#creditentry = tk.Entry(my_w, textvariable=creditvar,width=15,placeholder="credit")
#creditentry.grid(row=14,column=1)




##
style = ttk.Style(first) 
style.theme_use("clam") # set theam to clam
style.configure("Treeview", background="azure2", 
                fieldbackground="lightyellow", foreground="black",font=font1)
style.configure('Treeview.Heading', background="PowderBlue") 
# Using treeview widget
trv = ttk.Treeview(first, selectmode ='browse')
trv.grid(row=2,column=0,columnspan=10,rowspan=2,padx=10,pady=10)
# number of columns
trv["columns"] = ("1", "2", "3","4","5","6","7","8")
trv['show'] = 'headings'

#trv.column("1", width = 50, anchor ='c') # width & alignment
trv.column("1", width = 250, anchor ='w')


trv.column("2", width = 150, anchor ='c')
trv.column("3", width = 150, anchor ='e')
trv.column("4", width = 200, anchor ='e')

trv.column("5", width = 200, anchor ='e')
trv.column("6", width = 150, anchor ='e')
trv.column("7", width = 150, anchor ='e')
trv.column("8", width = 150, anchor ='e')

#trv.heading("1", text ="no") # Heading text 
trv.heading("1", text ="item")



trv.heading("2", text ="qty_stock")
trv.heading("3", text ="tot_gzzi")  
trv.heading("4", text ="tot_shyach")  
trv.heading("5", text ="qty_shyach")
trv.heading("6", text ="credits")
trv.heading("7", text ="wechi")
trv.heading("8", text ="profit")



#trv.heading("1", text ="Sl No") # Heading text 
#trv.heading("2", text ="Product")
#trv.heading("3", text ="Quantity")
#trv.heading("4", text ="Rate")  
#trv.heading("5", text ="Total")  
#trv.heading("6", text ="Total")
#trv.heading("7", text ="Total")
#trv.heading("8", text ="Total")





l1=tk.Label(first,text='|item_bzat|',fg='red',font=font1,anchor='e')
l1.grid(row=4,column=1,sticky='w')
l2=tk.Label(first,text='0',fg='red',font=font1,anchor='w')
l2.grid(row=5,column=1,sticky='w')

l3=tk.Label(first,text='|stock_qty|',fg='red',font=font2,anchor='e')
l3.grid(row=4,column=2,sticky='w')
l4=tk.Label(first,text='0',fg='red',font=font2,anchor='e')
l4.grid(row=5,column=2,pady=20,sticky='w')



l5=tk.Label(first,text="|tot_gzzi|",fg='red',font=font2,anchor='e')
l5.grid(row=4,column=3,sticky='w')
l6=tk.Label(first,text='0',fg='red',font=font2,anchor='e')
l6.grid(row=5,column=3,sticky='w')


l7=tk.Label(first,text='|tot_shyach|',fg='red',font=font2,anchor='e')
l7.grid(row=4,column=4,sticky='w')
l8=tk.Label(first,text='0',fg='red',font=font2,anchor='e')
l8.grid(row=5,column=4,sticky='w')


l9=tk.Label(first,text='|qty_shiyach|',fg='red',font=font2,anchor='e')
l9.grid(row=4,column=5,sticky='w')
l10=tk.Label(first,text="0",fg='red',font=font2,anchor='e')
l10.grid(row=5,column=5,sticky='w')

l11=tk.Label(first,text="|credits|",fg='red',font=font2,anchor='e')
l11.grid(row=4,column=6,sticky='w')
l12=tk.Label(first,text='0',fg='red',font=font2,anchor='e')
l12.grid(row=5,column=6,sticky='w')


l13=tk.Label(first,text='|wechi|',fg='red',font=font2,anchor='e')
l13.grid(row=4,column=7,sticky='w')
l14=tk.Label(first,text='0',fg='red',font=font2,anchor='e')
l14.grid(row=5,column=7,sticky='w')


l15=tk.Label(first,text='|profit|',fg='blue',font=font2,anchor='e')
l15.grid(row=4,column=8,sticky='w')
l16=tk.Label(first,text='0',fg='blue',font=font2,anchor='e')
l16.grid(row=5,column=8,sticky='w')


#l9=tk.Label(my_w,text='Total :',fg='red',font=font2,anchor='e')
#l9.grid(row=5,column=3)

#l5=tk.Label(my_w,text='profit',fg='green',font=font1,anchor='e')
#l5.grid(row=4,column=9)
#l6=tk.Label(my_w,text='0',fg='blue',font=font1,anchor='e')
#l6.grid(row=5,column=9)





##
b1=tk.Button(first,text='Add',font=font2,width=3,command=lambda:my_add())
b1.grid(row=6,column=2,sticky='w')
b2=tk.Button(first,text='Delete',state='disabled',width=3,command=lambda:data_delete())
b2.grid(row=6,column=3,sticky='w')
b3=tk.Button(first,text='Del All',width=3,command=lambda:my_reset())
b3.grid(row=7,column=3,padx=1,sticky='w')
b4=tk.Button(first,text='Confirm',font=font2,bg='gray',width=3,command=lambda:insert_data())
b4.grid(row=7,column=2,sticky='w')

l_msg=tk.Label(first,text='',fg='red',font=1)
l_msg.grid(row=11,column=0,columnspan=2)


  
    # reset function 
trv.bind("<<TreeviewSelect>>", my_select)  # User selection of row




########################################################################################################################################################################################################################################################################################################################################################################





#

############################################################################################################################################################################################################################################################################################################################################################################################



########################################################################################################################################################################################################################################################################################






####################################################################################################################################################################################



namevar=tk.StringVar()

nameentry= tk.Entry(second,textvariable=namevar,width=15,placeholder="name")

nameentry.grid(row=7,column=1)


phonevar=tk.StringVar()
phoneentry= tk.Entry(second, textvariable=phonevar,width=15,placeholder="phone")

phoneentry.grid(row=8,column=1)




p_list=['Moniter','Mouse','Keyboard','Pen Drive','CPU','Power Unit'] # product list
itemvar=tk.StringVar()
itemscombo = ttk.Combobox(second, values=p_list,textvariable=itemvar,width=13,placeholder="items")
itemscombo.grid(row=9,column=1)

qtyvar=tk.IntVar()
quantityentry = tk.Entry(second, textvariable=qtyvar,width=15,placeholder="qty")
quantityentry.grid(row=10,column=1)



pricevar=tk.DoubleVar()
priceentry= tk.Entry(second, textvariable=pricevar,width=15,placeholder="price")
priceentry.grid(row=11,column=1)

#totalvar=tk.IntVar()
#totalentry = tk.Entry(my_w, textvariable=totalvar,width=15,placeholder="total")
#totalentry.grid(row=1,column=1)

creditvar=tk.IntVar()
creditentry = tk.Entry(second, textvariable=creditvar,width=15,placeholder="credit")
creditentry.grid(row=12,column=1)




##
style = ttk.Style(second) 
style.theme_use("clam") # set theam to clam
style.configure("Treeview", background="azure2", 
                fieldbackground="lightyellow", foreground="black",font=font1)
style.configure('Treeview.Heading', background="PowderBlue") 
# Using treeview widget
trv = ttk.Treeview(second, selectmode ='browse')
trv.grid(row=2,column=0,columnspan=9,rowspan=2,padx=10,pady=10)
# number of columns
trv["columns"] = ("1", "2", "3","4","5","6","7","8")
trv['show'] = 'headings'
trv.column("1", width = 50, anchor ='c') # width & alignment
trv.column("2", width = 250, anchor ='w')
trv.column("3", width = 150, anchor ='c')
trv.column("4", width = 150, anchor ='e')
trv.column("5", width = 150, anchor ='e')

trv.column("6", width = 150, anchor ='e')
trv.column("7", width = 150, anchor ='e')
trv.column("8", width = 150, anchor ='e')

trv.heading("1", text ="no") # Heading text 
trv.heading("2", text ="name")
trv.heading("3", text ="phone")
trv.heading("4", text ="item")  
trv.heading("5", text ="qty")  
trv.heading("6", text ="price")
trv.heading("7", text ="total")

trv.heading("8", text ="credit")



#trv.heading("1", text ="Sl No") # Heading text 
#trv.heading("2", text ="Product")
#trv.heading("3", text ="Quantity")
#trv.heading("4", text ="Rate")  
#trv.heading("5", text ="Total")  
#trv.heading("6", text ="Total")
#trv.heading("7", text ="Total")
#trv.heading("8", text ="Total")





l5=tk.Label(second,text='Total :',fg='blue',font=font1,anchor='e')
l5.grid(row=4,column=5)
l6=tk.Label(second,text='0',fg='blue',font=font1,anchor='e')
l6.grid(row=4,column=6)
l7=tk.Label(second,text='Tax 10 % :',fg='blue',font=font1,anchor='e')
l7.grid(row=5,column=5)
l8=tk.Label(second,text='0',fg='blue',font=font1,anchor='e')
l8.grid(row=5,column=6)
l9=tk.Label(second,text='Total :',fg='red',font=font2,anchor='e')
l9.grid(row=6,column=5)
l10=tk.Label(second,text='0',fg='red',font=font2,anchor='e')
l10.grid(row=6,column=6,pady=20)


##
b1=tk.Button(second,text='Add',font=font2,command=lambda:my_add())
b1.grid(row=4,column=0)
    
b2=tk.Button(second,text='Delete',state='disabled',command=lambda:data_delete())
b2.grid(row=6,column=0)
b3=tk.Button(second,text='Del All',command=lambda:my_reset())
b3.grid(row=6,column=1,padx=1)
b4=tk.Button(second,text='Confirm ',font=font2,bg='gray',command=lambda:insert_data())
b4.grid(row=4,column=1)
l_msg=tk.Label(second,text='',fg='red',font=1)
l_msg.grid(row=2,column=0,columnspan=2)


    





#l5=tk.Label(my_w,text='Total :',fg='blue',font=font1,anchor='e')
#l5.grid(row=4,column=4)
#l6=tk.Label(my_w,text='0',fg='blue',font=font1,anchor='e')
#l6.grid(row=4,column=5)
#l7=tk.Label(my_w,text='Tax 10 % :',fg='blue',font=font1,anchor='e')
#l7.grid(row=5,column=4)
#l8=tk.Label(my_w,text='0',fg='blue',font=font1,anchor='e')
#l8.grid(row=5,column=5)
#l9=tk.Label(my_w,text='Total :',fg='red',font=font2,anchor='e')
#l9.grid(row=6,column=4)
#l10=tk.Label(my_w,text='0',fg='red',font=font2,anchor='e')
#l10.grid(row=6,column=5,pady=20)
#    
#b2=tk.Button(my_w,text='Delete',state='disabled',command=lambda:data_delete())
#b2.grid(row=3,column=0)
#b3=tk.Button(my_w,text='Del All',command=lambda:my_reset())
#b3.grid(row=4,column=0,padx=1)
#b4=tk.Button(my_w,text='Confirm ',font=font2,bg='lightyellow',command=lambda:insert_data())
#b4.grid(row=5,column=0)
#l_msg=tk.Label(my_w,text='',fg='red',font=1)
#l_msg.grid(row=6,column=0,columnspan=2)

#total,iid=0,0

#def my_add():
#    global iid
#    iid=iid+1  # Serial number to display 
#    total=round(qty.get()*prc.get(),2) # row wise total 
#    trv.insert("", 'end',iid=iid, values =(iid,product.get(),qty.get(),prc.get(),total))
#    my_upd(trv)



total,iid=0,0

def my_add():
    
    
    
    namevars=namevar.get()
    phonevars=phonevar.get()
    itemvars=itemvar.get()
    qtyvars=qtyvar.get()
    pricevars=pricevar.get()
    creditvars=creditvar.get()
    
    total=pricevars*qtyvars
    
    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
    
    
    
    conn = sqlite3.connect("customers.db")
    table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (date INT,name TEXT,phone TEXT,item TEXT,quantity INT,price INT,total INT,credit INT)
            '''
    conn.execute(table_create_query)
    
    # Insert Data
    data_insert_query = '''INSERT INTO Student_Data (date, name, phone, 
            item, quantity, price, total, credit) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
    
    data_insert_tuple = (date,namevars,phonevars,itemvars,qtyvars,pricevars,total,creditvars)
    
    
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
    
    print("success")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    global iid
    iid=iid+1  # Serial number to display 
    total=round(qtyvar.get()*pricevar.get(),2) # row wise total 
    trv.insert("", 'end',iid=iid, values =(iid,namevar.get(),phonevar.get(),itemvar.get(),qtyvar.get(),pricevar.get(),total,creditvar.get()))
    my_upd(trv)









def my_upd(trv):
    global total 
    total,sub_total=0,0
    for child in trv.get_children():
        sub_total=round(sub_total+float(trv.item(child)["values"][6]),2)
    l6.config(text=str(sub_total)) # shows sub total 
    tax=round(0.1*sub_total,2)  # 10 % tax rate, update here
    l8.config(text=str(tax))  # tax amount is displayed 
    total=round(sub_total+tax,2) # tax added to sub total 
    l10.config(text=str(total))  # Final price is displayed
    itemvar.set('') # reset the combobox 
    qtyvar.set(1)  # reset quantity to 1
    pricevar.set(0.0) # reset price to 0.0 
    
    
def my_select(self):
    b2.config(state='active') # Delete button is active now 
def data_delete():
    p_id = trv.selection()[0] # collect selected row id
    trv.delete(p_id)  # remove the selected row from Treeview
    b2['state']='disabled' # disable the button 
    my_upd(trv) # Update the total 
def my_reset():
    for item in trv.get_children():
        trv.delete(item) # remove row 
    global total
    total=0
    itemvar.set('') # reset combobox
    qtyvar.set(1) # Update quantity to 1 
    pricevar.set(0.0) # Update price to 0.0
    l6.config(text='0')  # Update display sub total
    l8.config(text='0')  # Update display for tax
    l10.config(text='0') # Update display for total





    
def insert_data():
    #
    #namevars=namevar.get()
#    phonevars=phonevar.get()
#    itemvars=itemvar.get()
#    qtyvars=qtyvar.get()
#    pricevars=pricevar.get()
#    creditvars=creditvar.get()
#    
#    total=pricevars*qtyvars
#    
#    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#    
#    
#    
#    conn = sqlite3.connect("customers.db")
#    table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
#                    (date INT,name TEXT,phone TEXT,item TEXT,quantity INT,price INT,total INT,credit INT)
#            '''
#    conn.execute(table_create_query)
#    
#    # Insert Data
#    data_insert_query = '''INSERT INTO Student_Data (date, name, phone, 
#            item, quantity, price, total, credit) VALUES 
#            (?, ?, ?, ?, ?, ?, ?, ?)'''
#    
#    data_insert_tuple = (date,namevars,phonevars,itemvars,qtyvars,pricevars,total,creditvars)
#    
#    
#    cursor = conn.cursor()
#    cursor.execute(data_insert_query, data_insert_tuple)
#    conn.commit()
#    conn.close()
#    
#    print("success")
#    
    
    
    
    
    
    
    
    #global total
#    
#    conn = sqlite3.connect("customers.db")
#    c = conn.cursor()
#    
#    for child in trv.get_children():
#        #totals=qtyvar.get()*pricevar.get()
#        date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#        c.execute("INSERT INTO plus2_invoice_dtl (date,name,phone,item,quantity,price,total,credit) VALUES ( ?, ? , ?, ?, ? ,?, ?,?)",(date,trv.item(child)["values"][1],trv.item(child)["values"][2],trv.item(child)["values"][3],trv.item(child)["values"][4],trv.item(child)["values"][5],trv.item(child)["values"][6],trv.item(child)["values"][7]))
#    
#    
#    
#    conn.commit()
#    conn.close()
#    print("success")


#    global total
#    
#    conn = sqlite3.connect("customers.db")
#    c = conn.cursor()
#    

#    date=datetime.datetime.now().strftime("%d-%m-%y || %H-%M-%S-")
#    c.execute("INSERT INTO plus2_invoice_dtl (date,name,phone,item,quantity,price,total,credit) VALUES ( ?, ? , ?, ?, ? ,?, ?,?)",(date,namevar.get(),phonevar.get(),itemvar.get(),qtyvar.get(),pricevar.get(),total,creditvar.get()))
#    
#    
#    
#    conn.commit()
#    conn.close()
#    print("success")








    
    #dt = date.today() # Today's date 
#    data=(total,dt) # Data for parameterized query
#    query="INSERT INTO plus2_invoice ( total, dt) values(?,?)"
    #print(query)
    #id=conn.execute(query,data)
#    inv_id=id.lastrowid # get the bill or invoice number after adding data
    
    #query="INSERT INTO  plus2_invoice_dtl where price=total"
#    my_data=[] # list to store multiple rows of data
#    # In all rows inventory id is same
#    #for line in trv.get_children():
#        my_list=trv.item(line)['values']
#        my_data.append([id,my_list[0],my_list[1],my_list[2],my_list[3]])
#    id=conn.execute(query,my_data) # adding list of products to table
#    #print("Rows Added  = ",id.rowcount)
#    l_msg.config(text='Bill No:'+str(id)+',Products:'+str(id.rowcount))

    
    l_msg.after(3000, lambda: l_msg.config(text='') )
    
    
    my_reset() # reset function 
    
trv.bind("<<TreeviewSelect>>", my_select)  # User selection of row
















def my_open():
    my_w_child=tk.Toplevel(second)
    my_w_child.geometry("500x500")
    my_w_child.title('www.plus2net.com')
    my_w_child.config(bg="gray")
    my_str1=tk.StringVar()
    l1=tk.Label(my_w_child,text='Your name' ,textvariable=my_str1)
    l1.grid(row=1,column=0)
    e1=tk.Entry(my_w_child, bg='yellow')
    e1.grid(row=1,column=1)
    
    b2=tk.Button(my_w_child,text='Submit',
    command=lambda:l1_str.set(e1.get()))
    b2.grid(row=4,column=0)
    
    my_str1.set('Your Name')
    
    l3=tk.Label(my_w_child,text=e2.get())
    l3.grid(row=6,column=0)




#########
#b = Button(second, text='Hello There This is 2nd Tab',bg = 'coral')
#b.pack()
########


tabs.pack(expand=1, fill="both")
labelframe.mainloop()
#-First Tab has a button color Red and second tab has a button color coral
#Well, that’s about it. Now go create something more fun, and I hope my tutorial has helped you out somewhat.