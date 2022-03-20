print("|    Welcome To BiletSis v1.0 Bus Ticket System  |   ")


busserv =[]
ticketserv =[]
ticketlist=[]
timelist=[]
fmlist=[]
pricelist=[]
while True:
   if(busserv):
      print("\n---------  BUS SERVICES STATUS ---------")
      num = len(busserv)
      for x in range(0,num):
         print(x ,"-",busserv[x])

   menu1 = int(input("\n---------  MENU   ---------\n1 - Add New Bus Service \n2 - Add Ticket \n3 - Show Tickets \n0 - Exit\nPlease, Choose one  :"))
   if(menu1 == 1):
      menu2 = str(input("Enter the bus service name : "))
      busserv.append(menu2)
      print("\nService added succesfully  !\n")
      menu3 = str(input("Add one more service ? yes(Y)/no(N) : "))
      while(menu3 =="Y"):
         menu2 = str(input("\nEnter the bus service name : "))
         busserv.append(menu2)

         menu3 = str(input("\nAdd one more service ? yes(Y)/no(N) : "))
         continue

   elif(menu1 ==2 ):
      if (busserv):
         print("\n---------  BUS SERVICES LIST  ---------")
         num = len(busserv)
         for x in range(0, num):
            print(x, "-", busserv[x])
            ticketserv.append(x)
         menu4 = int(input("\nPlease select any Service : "))
         if(menu4 > -1):

            print("\nYour choice",busserv[ticketserv[menu4]])

            menu5 = str(input("\nPlease enter the bus seat : "))
            ticketlist.append(menu5)
            menu6 = str(input("\nPlease enter the bus time : "))
            timelist.append(menu6)
            menu7 = str(input("\nPlease enter the Male (M) /Female (F) : "))
            fmlist.append(menu7)
            menu8 = str(input("\nPlease enter the Price($) : "))
            pricelist.append(menu8)
         else:
            print("Error , wrong number ....\n")
      else:
         print("Bus service list is empty...\n")
         continue
   elif(menu1 == 3):
      num1 = len(fmlist)
      if(num1>=0):
         print("---------  TICKET LIST    ---------\n","Total Ticket :",num1,)
         for y in range(0,num1):
            print("\n",ticketserv[y]," - ",busserv[y],"-  Bus Seat : ",ticketlist[y], " - Bus Time :  ",timelist[y],"   -  Female/Male : ",fmlist[y],"   -  Price : ",pricelist[y])
            menu3 = str(input("\nGo Homepage ? Press Enter ... "))

      else:
         continue
   elif(menu1 == 0 ):
      quit()