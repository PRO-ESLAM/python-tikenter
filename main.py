from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import random
import  os
import tempfile
import mysql.connector



# ///////////
class BillApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Computers Billing System")


#
# ====Variables===
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.categoris=StringVar()
        self.sub_catogray=StringVar()
        self.bill_no=StringVar()
        z=random.randint (1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()





#    Style pc LifeStyle
 # Product Categories list
        self.Category=["SelectOption", "Monitors", "Style PC", "Mobiles"]
# SubCatClothing
        self.SubCatClothing=["MSI","Samsung", "LG"]
        self.pant=[" Optix MAG", "Optix MAG342", "Optix MPG"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spaykar=8000
    
       

        self.T_shirt=['Odyssey', 'Samsung UR', 'Samsung S']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700
     #    LG UltraGear // LG UltraWide // LG Ergo 
        self.Shirt=['LG Ergo', 'LG UltraWide', 'LG UltraGear']
        self.price_Peter =2100
        self.price_Louis=2700
        self.price_Park=1740

     #    self.Bath_soap=['LifeBuy', 'Lux', 'Santoor', 'Pearl']
#    Bath Soap 
        self.SubCatLifStyle=['Gaming Mouse', 'Face Creame', 'Hair Oil']
        self.Bath_soap=['LifeBuy', 'Lux', 'Santoor', 'Pearl']
        self.price_life=float(20)
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=30


        self.Face_creame=['Fair&Lovely', 'Ponds', 'Olay', 'Garnier']
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30


    
        self.Hair_oil=['Parachute', 'Jashmin', 'Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30

        # SubCatMobiles
        self.SubCatMobiles=['Iphone', 'Sumsung', 'Xiome', "RealMe", "One"]
        self. Iphone= ['Iphone_X', 'Iphone_11', 'Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=['Samsung M16', 'Sumsung M12', 'Sumsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiome=['Red11', 'Redme-12', 'RedmePro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.RealMe=['RealMe 12', 'RealMe 13', 'RealMe Pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.OnePlus=['OnePlus1', 'OnePlus2', 'OnePlus3']
        self.price_one1=45000
        self.price_one12=60000
        self.price_one3=45800





 


# img 1
        img=Image.open('imges/q1.jpg')
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)
        
# img 2
        img1=Image.open('imges\q2.png')
        img1=img1.resize((500,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_img1=Label(self.root,image=self.photoimg1)
        lbl_img1.place(x=500,y=0,width=500,height=130)
     

# img 3
        img2=Image.open('imges/q3.jpg')
        img2=img2.resize((500,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=1000,y=0,width=500,height=130)

# title -------
        lbl_title=Label(self.root,text="Computers Billing System",font=("time new roman",35,"bold"),bg="#1D267D",fg="#fff")
        lbl_title.place(x=0,y=130,width=1530,height=45)


        main_F=Frame(self.root,bd=5,relief=GROOVE,bg="#fff")
        main_F.place(x=0,y=175,width=1530,height=620)

# Customer LabelFrame
        cust_F=LabelFrame(main_F,text="Customer",font=("time new roman",14,"bold"),bg="#fff",fg="#0C134F") 
        cust_F.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob=Label(cust_F,text="Mobile : " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
       
        self.entry_mob=ttk.Entry(cust_F,textvariable=self.c_phon,font=("time new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        # ===================================
        self.lbl_name=Label(cust_F,text="Name: " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)
       
        self.entry_name=ttk.Entry(cust_F,textvariable=self.c_name,font=("time new roman",12,"bold"),width=24)
        self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbl_email=Label(cust_F,text="Email : " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)
       
        self.entry_email=ttk.Entry(cust_F, textvariable=self.c_email,font=("time new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# Customer LabelFrame
        pro_F=LabelFrame(main_F,text="Product",font=("time new roman",14,"bold"),bg="#fff",fg="#0C134F") 
        pro_F.place(x=370,y=5,width=650,height=140)
        # catgray
        self.lbl_catgroy=Label(pro_F,text="Select Catogery : " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_catgroy.grid(row=0,column=0,sticky=W,padx=5,pady=2)
       
        self.com_catgroy=ttk.Combobox(pro_F,values=self.Category ,textvariable=self.categoris , font=("time new roman",12,"bold"),width=24,state="readonly" )
        self.com_catgroy.current(0)
        self.com_catgroy.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.com_catgroy.bind("<<ComboboxSelected>>",self.Categories)
        # subCatgray
        self.lbl_subcatgroy=Label(pro_F,text="Sub Catogery: " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_subcatgroy.grid(row=1,column=0,sticky=W,padx=5,pady=2)
       
        self.com_subcatgroy=ttk.Combobox(pro_F,values=[""] ,textvariable=self.sub_catogray , font=("time new roman",12,"bold"),width=24,state="readonly"  )
        self.com_subcatgroy.grid(row=1,column=1,sticky=W,padx=5,pady=2)       
        self.com_subcatgroy.bind("<<ComboboxSelected>>",self.ProductAdd)
        # productName
        self.lbl_productName=Label(pro_F,text="Product Name: " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_productName.grid(row=2,column=0,sticky=W,padx=5,pady=2)
       
        self.com_productName=ttk.Combobox(pro_F,textvariable=self.product,  font=("time new roman",12,"bold"),width=24,state="readonly"  )
        self.com_productName.grid(row=2,column=1,sticky=W,padx=5,pady=2)       
        self.com_productName.bind("<<ComboboxSelected>>",self.price)
        # price
        self.lbl_price=Label(pro_F,text="Price: " ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_price.grid(row=0,column=2,sticky=W,padx=5,pady=2)
       
        self.com_price=ttk.Combobox(pro_F, textvariable=self.prices,  font=("time new roman",12,"bold"),width=14,state="readonly"  )
        self.com_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)       
        
        #  Qty
        self.lbl_Qty=Label(pro_F,text="Qty :" ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)
       
        self.com_Qty=ttk.Entry(pro_F,  textvariable=self.qty,  font=("time new roman",12,"bold"),width=16)
        self.com_Qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)       
  
    # Moddil Frame
        middle_F=Frame(main_F,bd=10)
        middle_F.place(x=10,y=150,width=980,height=340)
  
# img 1
        img12=Image.open("imges\q4.jpg")
        img12=img12.resize((490,340),Image.ADAPTIVE)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(middle_F,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)
        
# img 2
        img15=Image.open("imges\q5.jpg")
        img15=img15.resize((490,640),Image.ADAPTIVE)
        self.photoimg15=ImageTk.PhotoImage(img15)
        lbl_img15=Label(middle_F,image=self.photoimg15)
        lbl_img15.place(x=490,y=0,width=500,height=340)

  
      # Seach  
        Seach_F=Frame(main_F,bd=2,bg="#fff")
        Seach_F.place(x=1020,y=10,width=500,height=40)  
        
        self.lablBill=Label(Seach_F,font=("time new roman",12,"bold"),bg="#0C134F",fg="#fff",text="Bill Number:")
        self.lablBill.grid(row=0,column=0,sticky=W,padx=1)  
        
        self.enterBill=ttk.Entry(Seach_F,  textvariable=self.search_bill,  font=("time new roman",12,"bold"),width=16)
        self.enterBill.grid(row=0,column=1,sticky=W,padx=5,pady=2)       

        self.btnBill=Button(Seach_F, command=self.find_bill , text="Search: " ,font=("time new roman",12,"bold"),bg="#0C134F",fg="#fff")
        self.btnBill.grid(row=0,column=2)



       # RightFrame Bill Area
        right_F=LabelFrame(main_F,text="Bill Area",font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        right_F.place(x=1030,y=45,width=480,height=440)
        scroll_y=Scrollbar(right_F,orient=VERTICAL)
        self.textarea=Text(right_F,yscrollcommand=scroll_y.set,bg="#fff",fg="#3E065F",font=("time new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
       # Bill Counter LabelFrame
        botton_F=LabelFrame(main_F,text="Bill Counter",font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        botton_F.place(x=0,y=485,width=1520,height=160)        
        #  SubTotal
        self.lbl_SubTotal=Label(botton_F,text="Sub Total :" ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_SubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
       
        self.enter_SubTotal=ttk.Entry(botton_F, textvariable=self.sub_total,  font=("time new roman",12,"bold"),width=16)
        self.enter_SubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)    
        #  tex  
        self.lbl_tax=Label(botton_F,text="Gov Tax :" ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
       
        self.txt_tax=ttk.Entry(botton_F, textvariable=self.tax_input, font=("time new roman",12,"bold"),width=16)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)    
        #  AmountTotal  
        self.lbl_AmountTotal=Label(botton_F,text="Total :" ,font=("time new roman",12,"bold"),bg="#fff",fg="#0C134F")
        self.lbl_AmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
       
        self.txt_AmountTotal=ttk.Entry(botton_F, textvariable=self.total,   font=("time new roman",12,"bold"),width=16)
        self.txt_AmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)    
        #  Botton Frame
        Btn_F=Frame(botton_F,bd=2,bg="#fff")
        Btn_F.place(x=320,y=0)
        
        # btn add to cart
        self.btnAddToCart=Button(Btn_F,command=self.AddItem ,height=2,text="Add To Cart: " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff")
        self.btnAddToCart.grid(row=0,column=0)
        # Gnarate Bill
        self.btnGnarateBill=Button(Btn_F, command=self.gen_bill,height=2,text="Gnarate Bill: " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff",width=15)
        self.btnGnarateBill.grid(row=0,column=1)
        #   Save
        self.btnSave=Button(Btn_F,command=self.save_bill ,height=2,text=" Save Bill: " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff",width=15)
        self.btnSave.grid(row=0,column=2)   
        # Print
        self.btnPrint=Button(Btn_F,command=self.iprint ,height=2,text="Print Bill: " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff",width=15)
        self.btnPrint.grid(row=0,column=3)   
        # Clear
        self.btnClear=Button(Btn_F,command=self.clear ,height=2,text="Clear : " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff",width=15)
        self.btnClear.grid(row=0,column=4)   
        # Exit
        self.btnExit=Button(Btn_F,command=self.root.destroy ,height=2,text="Exit : " ,font=("time new roman",12,"bold"),bg="#58287F",fg="#fff",width=15)
        self.btnExit.grid(row=0,column=5)   
        self.welcome()


        self.l=[]
        
  # ====Function Declaration=======
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":  
            messagebox.showerror("Error", "Plaease Select the Product Name")
        else:
         self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
         self.sub_total.set(str('LE.%.2f'%(sum(self.l))))
         self.tax_input.set(str('LE.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
         self.total.set(str('LE.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))








    def welcome (self):
          self.textarea.delete(1.0, END)
          self.textarea.insert(END,"\t \t \t Welcome  ") 
          self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}") 
          self.textarea.insert(END,f"\n Customer Name: { self.c_name.get()}") 
          self.textarea.insert(END,f" \n Phone Number: {self.c_phon.get()}") 
          self.textarea.insert(END,f" \n Customer Email: {self.c_email.get()}")
          self.textarea.insert(END, "\n==================================================")
          self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
          self.textarea.insert(END, "\n==================================================")
         



    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Add To Cart Product")
        else:
          text=self.textarea.get(10.0,(10.0+float(len(self.l))))
        
          self.textarea.insert(END, "\n==================================================")
          self.textarea.insert(END,f"\nSub Amount:\t\t\t{self.sub_total.get()}")
          self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}") 
          self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
          self.textarea.insert(END, "\n==================================================")



    def save_bill(self):
         op=messagebox.askyesno("Save Bill", "Do you want to save the Bill")
         if op>0:
          self.addToDatabase()
          self.bill_data=self.textarea.get(1.0, END)
          f1=open('bills/'+str(self.bill_no.get())+".txt","w")
          f1.write(self.bill_data)
          f1.close()

    def iprint(self):
          q=self.textarea.get(1.0, "end-1c")
          filename=tempfile.mktemp('.txt')
          open(filename, 'w').write(q)
          os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
           if i.split('.')[0]==self.search_bill.get():
             f1=open(f'bills/{i}','r') 
             self.textarea.delete(1.0, END)
             for d in f1:
                self.textarea.insert(END,d)
             f1.close()
             found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill is NO ")






            
    def clear(self):
          self.textarea.delete(1.0, END)
          self.c_name.set("")
          self.c_phon.set("")
          self.c_email.set("")
          x=random.randint(1000,9999)
          self.bill_no.set(str(x))
          self.search_bill.set("")
          self.product.set("")
          self.prices.set(0)
          self.qty.set(0)
          self.l=[0]
          self.total.set("")
          self.sub_total.set("")
          self.tax_input.set('')
          self.welcome()




#    functions
    def Categories(self, event=""):
        category = self.com_catgroy.get()
        match category:
          case "Monitors":
               self.com_subcatgroy.config(value=self.SubCatClothing)
               self.com_subcatgroy.current(0)
          case "Style PC":
               self.com_subcatgroy.config(value=self.SubCatLifStyle)
               self.com_subcatgroy.current(0)
          case "Mobiles":
               self.com_subcatgroy.config(value=self.SubCatMobiles)
               self.com_subcatgroy.current(0) 


     # if self.com_catgroy.get()=="Monitors":
     #    self.com_subcatgroy.config(value=self.SubCatClothing)
     #    self.com_subcatgroy.current(0)

     # if self.com_catgroy.get()=="Style PC":
     #    self.com_subcatgroy.config(value=self.SubCatLifStyle)
     #    self.com_subcatgroy.current(0)

     # if self.com_catgroy.get()=="Mobiles":
     #    self.com_subcatgroy.config(value=self.SubCatMobiles)
     #    self.com_subcatgroy.current(0)

 
      

    def ProductAdd(self, event=""):
      if self.com_subcatgroy.get()=="MSI":
        self.com_productName.config(value= self.pant)
        self.com_productName.current(0)
    # def ProductAdd(self, event=""):             
      if self.com_subcatgroy.get()=="Samsung":
        self.com_productName.config(value= self.T_shirt)
        self.com_productName.current(0)
      if self.com_subcatgroy.get()=="LG":
        self.com_productName.config(value=self.Shirt)
        self.com_productName.current(0)
      # lifestyle   
      if self.com_subcatgroy.get()=='Gaming Mouse':
        self.com_productName.config(value=self.Bath_soap)
        self.com_productName.current(0)     

      if self.com_subcatgroy.get()=='Face Creame':
        self.com_productName.config(value=self.Face_creame)
        self.com_productName.current(0)     


      if self.com_subcatgroy.get()== 'Hair Oil':
        self.com_productName.config(value=self.Hair_oil)
        self.com_productName.current(0)     
# Mobile
      if self.com_subcatgroy.get()=="Iphone":
        self.com_productName.config(value=self.Iphone)
        self.com_productName.current (0)
      if self.com_subcatgroy.get()=="Sumsung":
        self.com_productName.config(value=self.Samsung)
        self.com_productName.current (0)
      if self.com_subcatgroy.get()=="Xiome":
        self.com_productName.config(value=self.Xiome)
        self.com_productName.current (0)
      if self.com_subcatgroy.get()=="RealMe":
        self.com_productName.config(value=self.RealMe)
        self.com_productName.current (0)
      if self.com_subcatgroy.get()=="One+":
        self.com_productName.config(value=self.OnePlus)
        self.com_productName.current (0)
 
 
    def price(self,event=""):
      if self.com_productName.get()==" Optix MAG":
           self.com_price.config(value= self.price_levis)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Optix MAG342":
           self.com_price.config(value= self.price_mufti)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Optix MPG":
           self.com_price.config(value= self.price_spaykar)
           self.com_price.current (0)
           self.qty.set(1)



 

#         #    T-Shirt
      # def price(self,event=""):
      if self.com_productName.get()=='Odyssey':
           self.com_price.config(value= self.price_polo)
           self.com_price.current (0)
           self.qty.set(1)
#                 # T-Shirt
      if self.com_productName.get()=="Samsung UR":
           self.com_price.config(value=self.price_JackJones)
           self.com_price.current(0)
           self.qty.set(1)
      if self.com_productName.get() == "Samsung S":
           self.com_price.config(value=self.price_Roadster)
           self.com_price.current(0)
           self.qty.set(1)
      if self.com_productName.get()==" Odyssey G3":
           self.com_price.config(value=self.price_JackJones)
           self.com_price.current (0)
           self.qty.set(1)
# #  Shirt
      if self.com_productName.get()=="LG Ergo":
                self.com_price.config(value= self.price_Peter)
                self.com_price.current(0)
                self.qty.set(1)
      if self.com_productName.get() == "LG UltraWide":
           self.com_price.config(value=self.price_Louis)
           self.com_price.current(0)
           self.qty.set(1)
      if self.com_productName.get()=="LG UltraGear":
            self.com_price.config(value=self.price_Park)
            self.com_price.current (0)
            self.qty.set(1)
# # #   Bath Soap
      if self.com_productName.get()=="LifeBuy":
           self.com_price.config(value=self.price_life)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Lux":
           self.com_price.config(value=self.price_lux)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Santoor":
           self.com_price.config(value=self.price_santoor)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Pearl":
           self.com_price.config(value=self.price_pearl)
           self.com_price.current (0)
           self.qty.set(1)

      if self.com_productName.get()=="Fair&Lovely":
           self.com_price.config(value=self.price_fair)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Ponds":
           self.com_price.config(value=self.price_ponds)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Olay":
           self.com_price.config(value=self.price_olay)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Garnier":
           self.com_price.config(value=self.price_garnier)
           self.com_price.current (0)
           self.qty.set(1)

      if self.com_productName.get()=="Parachute":
           self.com_price.config(value=self.price_para)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Jashmin":
           self.com_price.config(value=self.price_jashmin)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Bajaj":
           self.com_price.config(value=self.price_bajaj)
           self.com_price.current (0)
           self.qty.set(1)
# Mobiles


      if self.com_productName.get()=="Iphone_X":
           self.com_price.config(value=self.price_ix)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Iphone_11":
           self.com_price.config(value=self.price_i11)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Iphone_12":
           self.com_price.config(value=self.price_i12)
           self.com_price.current (0)
           self.qty.set(1)



      if self.com_productName.get()=="Samsung M16":
           self.com_price.config(value=self.price_sm16)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Sumsung M12":
           self.com_price.config(value=self.price_sm12)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Sumsung M21":
           self.com_price.config(value=self.price_sm21)
           self.com_price.current (0)
           self.qty.set(1)


      if self.com_productName.get()=="Red11":
           self.com_price.config(value=self.price_r11)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Redme-12":
           self.com_price.config(value=self.price_r12)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="RedmePro":
           self.com_price.config(value=self.price_rpro)
           self.com_price.current (0)
           self.qty.set(1)

      if self.com_productName.get()=="Red11":
           self.com_price.config(value=self.price_r11)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="Redme-12":
           self.com_price.config(value=self.price_r12)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="RedmePro":
           self.com_price.config(value=self.price_rpro)
           self.com_price.current (0)
           self.qty.set(1)

      if self.com_productName.get()=="RealMe 12":
           self.com_price.config(value=self.price_rel12)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="RealMe 13":
           self.com_price.config(value=self.price_rel13)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="RealMe Pro":
           self.com_price.config(value=self.price_relpro)
           self.com_price.current (0)
           self.qty.set(1)

      if self.com_productName.get()=="OnePlus1":
           self.com_price.config(value=self.price_one1)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="OnePlus2":
           self.com_price.config(value=self.price_one12)
           self.com_price.current (0)
           self.qty.set(1)
      if self.com_productName.get()=="OnePlus3":
           self.com_price.config(value=self.price_one3)
           self.com_price.current (0)
           self.qty.set(1)

    def addToDatabase(self):
          try:
               con = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='123456789',
                    database='project'
               )
               c = con.cursor()
               c.execute("INSERT INTO bills VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.c_phon.get(),
                    self.c_name.get(),
                    self.c_email.get(),
                    self.categoris.get(),
                    self.sub_catogray.get(),
                    self.product.get(),
                    self.prices.get(),
                    self.qty.get(),
                    self.sub_total.get(),
                    self.tax_input.get(),
                    self.total.get(),
                    self.bill_no.get()
               ))
               con.commit()
               con.close()
               messagebox.showinfo("Success", "Data inserted successfully.")
          except Exception as e:
               messagebox.showerror("Error", f"Error inserting data: {str(e)}")
  
 
if __name__ == '__main__':
    root=Tk()
    obj=BillApp(root)
    root.mainloop()

