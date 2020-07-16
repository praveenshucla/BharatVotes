from tkinter import *
import pickle
import os
import login
import time
from tkinter import StringVar
from tkinter import scrolledtext
from tkinter import messagebox

add_dict = []
retrieve = []
retrieveback = []
count = -1
showallindex = 0
tcount = 0
delete_count = 0
delete_index_list = []
a =[]  # global variable for tranfering content from binary to text file

root = Tk()
mystring1 = StringVar(root)
mystring2 = StringVar(root)
mystring3 = StringVar(root)
mystring4 = StringVar(root)
mystring5 = StringVar(root)
mystring6 = StringVar(root)
mystring7 = StringVar(root)
mystring8 = StringVar(root)
mystring9 = StringVar(root)
searchstring = StringVar(root)
deletestring = StringVar(root)

#####################################      Main window          #################################################

localtime=time.asctime(time.localtime(time.time()))

def mainwindow(root):

    Frame(root, width=3000, height=1000, bg='white').place(x=0, y=0)
    frame = Frame(root, width=3000, height=200, bg="#333399").place(x=0, y=0)
    lbl = Label(root, text="fairVote", bg="#333399", fg="white", font=("Times New Roman", 45)).place(x=675, y=1)
    lblinfo = Label(root, text=localtime, bg="#333399", fg="white", font=("Times New Roman", 20)).place(x=640,y=60)
    btn = Button(root, text="Database", bg="white", fg="black", font=("Times New Roman", 20),command=lambda: vote(root)).place(x=300, y=100)
    Button(root, text="Elections", bg="white", fg="black", font=("Times New Roman", 20),command=lambda: devote(root)).place(x=421, y=100)
    Button(root, text="Resources", bg="white", fg="black", font=("Times New Roman", 20),command=lambda: eevote(root)).place(x=545, y=100)
    Button(root, text="Blog", bg="white", fg="black", font=("Times New Roman", 20),command=lambda: fevote(root)).place(x=678, y=100)
    Button(root, text="Get Involved", bg="white", fg="black", font=("Times New Roman", 20),command=lambda: gevote(root)).place(x=752, y=100)
    Button(root, text="Suggestions", bg="white", fg="black", font=("Times New Roman", 20), command=lambda: feedback(root)).place(x=914, y=100)
    Button(root, text="About Us", bg="white", fg="black", font=("Times New Roman", 20), command=lambda: hevote(root)).place(x=1064, y=100)
    Button(root, text="Exit", bg="white", fg="black", font=("Times New Roman", 20), command=lambda: quit(root)).place(x=1191, y=100)

    pfile = open("vote.bin", "rb")

    temp = []  # for getting count of records in binary file

    global count , delete_index_list

    delete_index_list.clear()

    while 1:  # this helps in counting how many recotrds are present currently in file

        try:
 
            temp = pickle.load(pfile)


        except(EOFError) :
                  break



    pfile.close()

    with open("deletedentries","rb") as dfile :

        while 1:  # this helps in counting how many records are present currently in file

            try:
                delete_index_list = pickle.load(dfile)

            except(EOFError):  # in case the file  reaches its end

                break
            except:  # in case the file  initially , has no content
                break

    

    count = len(temp) -1
    print("length in file rn : ",len(temp))
    print("count in file rn : ", count )


def devote(root):
    xframe = Frame(root, width=1200, height=600, bg="#b366ff").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    lb2 = Label(root, text="Elections In India ", bg="#b366ff", fg="black", font=("Times New Roman", 30)).place(x=300, y=250)
    lb3 = Label(root, text="Elections in India are the largest democratic electoral exercise in the world. Results of these elections are followed closely \nas they have a direct bearing on the lives of the country's over 1.3 billion population.The government of India is based on \nFederalism. There are 3 levels where elected officials can be appointed: Gender, federal and local levels. Election Commission of \nIndia is the apex body which oversees all the matters related to elections.", bg="#b366ff", fg="black", font=("Times New Roman", 15)).place(x=300, y=350)
    lb4 = Label(root, text="The Parliament of India has 2 houses: Lok Sabha and Rajya Sabha. The members of Lok Sabha elect the Prime Minister of the country. \nIt is also known as lower house. And comprises a total of 552 members. From Genders, 530 members are selected, while 20 \nmembers in the Lok Sabha represent the union territories. Two of the members are chosen from the Anglo Indian community by the \nPresident. The members of the Lok Sabha are elected every 5 years.", bg="#b366ff", fg="black", font=("Times New Roman", 15)).place(x=300, y=450)
    lb5 = Label(root, text="While Lok Sabha is called the lower house, the upper house of Parliament is called Rajya Sabha. It consists of 250 members which \nare elected from Genders' legislative assemblies and the Electoral College of Union Territories. The tenure for the Rajya \nSabha is 6 years and comprises 238 members. After two years, one-third of the members retire. Twelve members from different fields, \nlike scientists, artists, sports personality, journalists, businessmen, jurists and more, are also nominated.", bg="#b366ff", fg="black", font=("Times New Roman", 15)).place(x=300, y=550)

def eevote(root):
    xframe = Frame(root, width=1200, height=600, bg="#ffa64d").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    lb2 = Label(root, text="Requirements for registering to vote ", bg="#ffa64d", fg="black", font=("Times New Roman", 25)).place(x=300, y=250)
    lb3 = Label(root, text="You can enroll as a Voter if you: ", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=300)
    lb4 = Label(root, text="->are an Indian citizen ", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=325)
    lb5 = Label(root, text="->have attained the age of 18 years on the qualifying date", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=350)
    lb6 = Label(root, text="->are ordinarily resident of the part/polling area of the constituency where you want to be enrolled. ", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=375)
    lb7 = Label(root, text="->are not disqualified to be enrolled as an elector ", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=400)
    lb8 = Label(root, text="How To Register Offline ", bg="#ffa64d", fg="black", font=("Times New Roman", 25)).place(x=300, y=450)
    lb9 = Label(root, text="You can also enroll offline. Fill Form 6 in two copies . Form 6 is also available free of cost in offices of Electoral Registration \nOfficers / Assistant Electoral Registration Officers and Booth Level Officers. Call 1950 for any help.", bg="#ffa64d", fg="black", font=("Times New Roman", 15)).place(x=300, y=500)

def fevote(root):
    xframe = Frame(root, width=1200, height=600, bg="#ff6666").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    lb2 = Label(root, text="2019 Indian general election", bg="#ff6666", fg="black", font=("Times New Roman", 30)).place(x=300, y=250)
    lb3 = Label(root, text="The 2019 Indian general election was held in seven phases from 11 April to 19 May 2019 to constitute the 17th Lok Sabha. \nThe counting of votes will be conducted on 23 May, and on the same day the results will be declared. About 900 million Indian \ncitizens were eligible to vote in one of the seven phases depending on the region. The 2019 elections attracted a turnout of over 67% \n– the highest ever in the history of Indian general elections, as well the highest recorded participation in Indian elections by women. \nAccording to most exit polls released on May 19 2019, Genders The Washington Post, the BJP-led alliance and incumbent prime \nminister Narendra Modi appeared poised to win reelection; however exit polls in India have an inconsistent record.", bg="#ff6666", fg="black", font=("Times New Roman", 15)).place(x=300, y=350)
    lb4 = Label(root, text="The election schedule was announced on 10 March 2019, and with it the Model Code of Conduct came into force.The final \nturnout for the 2019 Lok Sabha Elections stood at 67.11%, the highest ever turnout recorded in any of the Lok Sabha elections till \ndate. The percentage is 1.16 percentage higher than the 2014 elections whose turnout stood at 65.95%.", bg="#ff6666", fg="black", font=("Times New Roman", 15)).place(x=300, y=500)

def gevote(root):
    xframe = Frame(root, width=1200, height=600, bg="#2eb8b8").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    lb2 = Label(root, text="Election Day Officials are recruited to assist voters, provide operational support, and ensure the integrity of the \nvoting process. Volunteers gain first-hand knowledge and experience in the electoral process while receiving a stipend. \nWork hours vary by position.The volunteer coordinator works closely with the Field Director to identify, recruit and manage \nvolunteers to help with various campaign activities. They help coordinate the work the volunteers, utilize their skills and \ntalents well and provide motivation.", bg="#2eb8b8", fg="black", font=("Times New Roman", 15)).place(x=300, y=250)
    lb3 = Label(root, text="Nonprofit organizations may volunteer as Election Day Officials as a fundraiser, and donate their stipend to their \norganization. Interested organizations will need to provide a tax clearance certificate, memorandum of agreement, and \na list of volunteers. No political action committees or groups organized for political purposes may participate.", bg="#2eb8b8", fg="black", font=("Times New Roman", 15)).place(x=300, y=375)

def hevote(root):
    xframe = Frame(root, width=1200, height=600, bg="#cc6699").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    lb2 = Label(root, text="Made by :-", bg="#cc6699", fg="black", font=("Times New Roman", 25)).place(x=300, y=250)
    lb3 = Label(root, text="Praveen Kumar Shukla \nUSN- 1VI16IS081 \nEmail- praveenkrshukla7@gmail.com \nMob- 9731903981", bg="#cc6699", fg="black", font=("Times New Roman", 20)).place(x=300, y=350)
    lb4 = Label(root, text="Sohail S \nUSN- 1VI16IS111 \nEmail- shaik32146@gmail.com \nMob- 9482191134", bg="#cc6699", fg="black", font=("Times New Roman", 20)).place(x=800, y=350)


# end of mainwindow method



##########################    WHENEVER USER HITS THE DB BUTTON  CONTROL REACHES HERE         #########################

def vote(root):
    frame = Frame(root, width=1200, height=600, bg="#2eb8b8").place(x=200, y=175) # MINI WINDOW OF SMARTvoteS RECORD
    p1 = Button(frame, text=" REGISTER ", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16), command=lambda: add(root)).place(x=200, y=300)
    p2 = Button(root, text="  REMOVE  ", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16),command=lambda: delete(root)).place(x=200, y=350)
    p3 = Button(frame, text="  UPDATE  ", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16), command=lambda: update(root)).place(x=200, y=400)
    p4 = Button(frame, text="   SEARCH   ", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16),command=lambda: search(root)).place(x=200, y=450)
    p5 = Button(frame, text="CLEAR LIST", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16), command=lambda: delete_all(root)).place(x=200, y=550)
    p6 = Button(frame, text=" VIEW LIST ", bg="#b3b3b3", fg="#0000b3", font=("Times New Roman", 16),command=lambda: showall(root)).place(x=200, y=600)




############################        THIS FUNCTION DISPLAYS A SPECIFIC  RECORD     ############################

def display(root , showallindex , temp_list) :     # CALLED IN VARIOUS OTHER FUNCTIONS

    name = temp_list[showallindex][0]

    age = temp_list[showallindex][1]

    gender = temp_list[showallindex][2]

    category = temp_list[showallindex][3]

    phone = temp_list[showallindex][4]

    email = temp_list[showallindex][5]

    area = temp_list[showallindex][6]

    district = temp_list[showallindex][7]

    pin = temp_list[showallindex][8]

    vote(root)

    Label(root, text=" VOTER ID NUMBER %s " % (showallindex + 1), font="ariel 20 bold ", bg="#2eb8b8", fg="black",
          bd=7, width=30).place(x=550, y=190)

    Label(root, text=" Name ", font="ariel 14 bold ").place(x=550, y=250)

    Label(root, text=" %s " % name, bd=7, width=40).place(x=800, y=250)

    Label(root, text=" Age ", font="ariel 14 bold ").place(x=550, y=300)

    Label(root, text=" %s " % age, bd=7, width=40).place(x=800, y=300)

    Label(root, text=" Gender ", font="ariel 14 bold ").place(x=550, y=350)

    Label(root, text=" %s " % gender, bd=7, width=40).place(x=800, y=350)

    Label(root, text=" Category ", font="ariel 14 bold ").place(x=550, y=400)

    Label(root, text=" %s " % category, bd=7, width=40).place(x=800, y=400)

    Label(root, text=" Phone no ", font="ariel 14 bold ").place(x=550, y=450)

    Label(root, text=" %s " % phone, bd=7, width=40).place(x=800, y=450)

    Label(root, text=" Email ", font="ariel 14 bold ").place(x=550, y=500)

    Label(root, text=" %s " % email, bd=7, width=40).place(x=800, y=500)

    Label(root, text=" Area ", font="ariel 14 bold ").place(x=550, y=550)

    Label(root, text=" %s " % area, bd=7, width=40).place(x=800, y=550)

    Label(root, text=" District ", font="ariel 14 bold ").place(x=550, y=600)

    Label(root, text=" %s " % district, bd=7, width=40).place(x=800, y=600)

    Label(root, text=" Pin code ", font="ariel 14 bold ").place(x=550, y=650)

    Label(root, text=" %s " % pin, bd=7, width=40).place(x=800, y=650)



#################                 WHEN USER HITS TH PREV BUTTON                #################################


def navigateprev(root, showallindex , temp_list):

    try:

        breakcount = 1
        if showallindex > 0 :  # if index is present in the file !!

            showallindex -= 1       # decrementing the index by 1

            if (showallindex) in delete_index_list:  # if the record was deleted by the user

                navigateprev(root, showallindex, temp_list)
                breakcount = 0

            if showallindex < 0 :     # even the very first record has been shown
                i - s

            if breakcount :

                display(root ,showallindex ,temp_list)
                Button(root, text=" NEXT ", font=" ariel 14 bold ",
                       command = lambda: navigatenext(root, showallindex, temp_list)).place( x=950, y=700)

                Button(root, text=" PREV ", font=" ariel 14 bold ",
                       command = lambda: navigateprev(root, showallindex, temp_list)).place( x=850,  y=700)

                Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: vote(root)).place(x=1200, y=700)


        else :    # if user is on first record and tries to see the previous record

                    messagebox.showinfo(" important message ! " , " No Previous records  !!")
                    vote(root)

    except:

        messagebox.showinfo(" important message ! ", " Error in displaying the previous record !!")



######################      *       #################################     *     ######################

def navigatenext(root , showallindex ,temp_list):    # when user hits the  NEXT  button

        try :

            if  showallindex < len(temp_list) :         # if index is present in the file !!

                showallindex += 1
                global delete_index_list
                breakcount = 1
                print(" delete index list :",delete_index_list)
                print("showallindex :", showallindex)


                if showallindex >= len(temp_list):   # chcking if it crosses the last element index
                    print(" yes ...)")
                    i - s             # control will go to the except block


                if (showallindex) in delete_index_list :  # if the record was deleted by the user

                    navigatenext(root,showallindex , temp_list)
                    breakcount = 0


                print("showallindex new : ", showallindex)


                print(temp_list)

                if breakcount :   # this checks if index has not been deleted earlier

                    display(root, showallindex, temp_list)

                    Button(root, text=" NEXT ", font=" ariel 14 bold ",
                           command=lambda: navigatenext(root, showallindex, temp_list)).place(x=950, y=700)

                    Button(root, text=" PREV ", font=" ariel 14 bold ",
                           command=lambda: navigateprev(root, showallindex, temp_list)).place(x=850, y=700)

                    Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: vote(root)).place(x=1200, y=700)


        except Exception as e:

            messagebox.showinfo(" important message ! ", " all records shown !!")
            print(str(e))


##########################         WHWNEVER USER HITS THE SHOW ALL BUTTON ,CONTROL REACHES HERE !           ###########################


def showall(root):

            try :

                vote(root)
                temp_list = []
                global showallindex
                showallindex = 0

                with open("vote.bin", "rb") as myFile:

                    while 1:

                        try:
                            temp_list = pickle.load(myFile)
                            print(temp_list)

                        except(EOFError):

                            print("entered in eof error block")
                            break

                        except:  # in case file initially, has no content

                            temp_list = []
                            messagebox.showinfo("  ********* IMPPORTANT MESSAGE ******** ", " NO RECORD TO SHOW !")
                            vote(root)
                            break  # coming out of the loop

                if len(delete_index_list) == len(temp_list):  # if all the records have been deleted by the user
                    error

                if (showallindex) in delete_index_list:  # if the first record was deleted by the user

                    navigatenext(root, showallindex, temp_list)

                display(root, showallindex, temp_list)  # calling the display function to display the records


                Button(root, text=" NEXT ", font=" ariel 14 bold ",
                       command=lambda: navigatenext(root, showallindex, temp_list)).place(x=950, y=700)


                Button(root, text=" PREV ", font=" ariel 14 bold ",
                       command=lambda: navigateprev(root, showallindex, temp_list)).place(x=850, y=700)


                Button(root, text=" CLOSE ", font=" ariel 14 bold", command=lambda: vote(root)).place(x=1200, y=700)

            except :

                 messagebox.showinfo( "  *******  IMPORTANT MESSAGE  ****** " , " NO RECORD TO SHOW !! ")

##########################         WHWNEVER USER HITS THE DELETE ALL BUTTON ,CONTROL REACHES HERE !           ###########################


def delete_all(root):

    vote(root)

    Label(root, text=" ARE YOU SURE ? ", font="ariel 14 bold", bg='#2eb8b8', fg='black').place(x=750, y=350)


    Button(root, text="  Yes  ", font="ariel 14 bold", bg='white', fg='black', command=lambda: truncfile(root)).place(x=750, y=400)

    Button(root, text="  No  ", font="ariel 14 bold", bg='white', fg='black', command=lambda: vote(root)).place(x=750,y=450)


    def truncfile(root):

        with open("vote.bin", "wb") as pfile:

            pfile.truncate()

        with open("deletedentries", "wb") as pfile:  # also we will have to truncate this file

            pfile.truncate()


        with open("finalvote.txt", "w+") as pfile:

            pfile.truncate()

        global delete_index_list , count

        delete_index_list.clear()
        count = -1
        vote(root)

        messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORDS HAVE BEEN DELETED ! ')
        vote(root)



##########################         WHWNEVER USER HITS THE ADD RECORD BUTTON ,CONTROL REACHES HERE !           ###########################


def add(root):

    vote(root)
    mystring1.set("")        # SETTING VALUES TO NOTHING SO THAT ENTRY BOXES BECOME EMPTY WHENEVER THE BUTTON IS CLICKED AGAIN
    mystring2.set("")
    mystring3.set("")
    mystring4.set("")
    mystring5.set("")
    mystring6.set("")
    mystring7.set("")
    mystring8.set("")
    mystring9.set("")

    add1 = Label(root, text="  Name ", font="ariel 14 bold ").place(x=550, y=200)

    entry1 = Entry(root, textvariable=mystring1, bd=7, width=40).place(x=800, y=200)

    add2 = Label(root, text=" Age  ", font="ariel 14 bold ").place(x=550, y=250)

    entry2 = Entry(root, textvariable=mystring2, bd=7, width=40).place(x=800, y=250)

    add3 = Label(root, text=" Gender ", font="ariel 14 bold ").place(x=550, y=300)

    entry3 = Entry(root, textvariable=mystring3, bd=7, width=40).place(x=800, y=300)

    add1 = Label(root, text=" Category  ", font="ariel 14 bold ").place(x=550, y=350)

    entry4 = Entry(root, textvariable=mystring4, bd=7, width=40).place(x=800, y=350)

    add1 = Label(root, text=" Phone no ", font="ariel 14 bold ").place(x=550, y=400)

    entry5 = Entry(root, textvariable=mystring5, bd=7, width=40).place(x=800, y=400)

    add1 = Label(root, text=" Email ", font="ariel 14 bold ").place(x=550, y=450)

    entry6 = Entry(root, textvariable=mystring6, bd=7, width=40).place(x=800, y=450)

    add1 = Label(root, text=" Area ", font="ariel 14 bold ").place(x=550, y=500)

    entry7 = Entry(root, textvariable=mystring7, bd=7, width=40).place(x=800, y=500)

    add1 = Label(root, text=" District ", font="ariel 14 bold ").place(x=550, y=550)

    entry8 = Entry(root, textvariable=mystring8, bd=7, width=40).place(x=800, y=550)

    add1 = Label(root, text=" Pin code ", font="ariel 14 bold ").place(x=550, y=600)

    entry9 = Entry(root, textvariable=mystring9, bd=7, width=40).place(x=800, y=600)



    def e5():  # this function is called when add information button is clicked by the user

        add_list = []
        temp_list = []
        add1_list = []

        if  mystring1.get()!="" and mystring2.get()!="" and mystring3.get()!="" and mystring4.get()!="" and mystring5.get()!="" and mystring6.get()!="" and mystring7.get()!="" and mystring8.get()!="" and mystring9.get()!="" :  # to make sure no entry box is left empty

            add_list.append(mystring1.get())
            add_list.append(mystring2.get())
            add_list.append(mystring3.get())
            add_list.append(mystring4.get())
            add_list.append(mystring5.get())
            add_list.append(mystring6.get())
            add_list.append(mystring7.get())
            add_list.append(mystring8.get())
            add_list.append(mystring9.get())
            global add_dict, count

            if count > -1:           # IF RECORDS ARE PRESENT IN THE FILE INITIALLY

                print("initial count in add  :", count)

                with open("vote.bin", "rb") as myFile:


                    while 1:

                        try:

                            temp_list = pickle.load(myFile)

                        except(EOFError):

                            break

                        except:  # in case file initially, has no content

                            temp_list = []
                            break  # coming out of the loop

                count = len(temp_list)-1
                add_dict.clear()  # clearing the list so that new data can be stored
                add_dict = temp_list[:]  # cloning the list
                add_dict.append(add_list)  # adding the add list to the add dict list

                count += 1
                r = str(count + 1)  # for serial number

                with open("vote.bin", "ab") as myFile:

                    pickle.dump(add_dict, myFile)  # this statement dumps the data of the list add_list into the file phone.txt


                transfer()      # content gets transferred to text file


            else:     # if there is no record in the file !

                count = 0
                r = str(count + 1)  # for serial number

                with open("vote.bin", "ab") as myFile:

                    add1_list.append(add_list)
                    pickle.dump(add1_list, myFile)  # this statement dumps the data of the list add_list into the file phone.txt


                transfer()  # content gets transferred to text file

            print("add dict which is being written in file : ", add1_list)  # checking purpose

            pfile = open("vote.bin", "r")  # opens the file in read mode

            messagebox.showinfo('        ******** NOTIFICATION ********'," Your Information has been added and your \n VOTER ID NUMBER IS : %s  ! DO KEEP IT SAFE!!" % r)

            addbutton = Button(root, text=" ADD MORE ", font=" ariel 16 bold", width=22,command=lambda: add(root)).place(x=900, y=700)


        else :     # case where user leaves an entry box empty

            messagebox.showinfo(" ******Important Message ******* " , " ENTER THE DETAILS PROPERLY !! ")
            add(root)

    Button(root, text=" ADD THE INFORMATION ", font=" ariel 16 bold", command=e5).place(x=900,y=700)



##########################         WHWNEVER USER HITS THE DELETE RECORD BUTTON ,CONTROL REACHES HERE !           ###########################

def delete(root):  # delete function which deletes the record when delte button is clicked by the user

    vote(root)
    pfile = open("vote.bin", 'rb')  # opening file in read binary mode

    global retrieve, retrieveback
    retrieve.clear()  # erasing initial stored data so that new data from the list which got edited at some point can be stored


    while 1:

        try:  # till the end of file is reached

            retrieveback = pickle.load(pfile)

        except (EOFError):  # when file reaches its end

            break  # go out of while loop

        except:

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  RECORD CANNOT BE DELETED .FILE IS EMPTY !!")
            vote(root)
            break


    deletestring.set("")

    retrieve = retrieveback[:]

    pfile.close()

    vote(root)

    Label(root, text=" ENTER THE VOTER ID NUMBER  ", font=" ariel 17 bold ").place(x=650, y=300)

    Entry(root, textvariable=deletestring, bd=13).place(x=700, y=400)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempdel(root)).place(x=900, y=400)  # if okay button is clicked then temp del function is called


    def tempdel(root):

        vote(root)

        Label(root, text=" ARE YOU SURE THAT YOU WANT TO DELETE ? ", font="ariel 14 bold", bg='#2eb8b8"', fg='white').place(x=700, y=200)

        Button(root, text="  Yes  ", font="ariel 14 bold", bg='white', fg='black',command=lambda: confirm_delete(root)).place(x=750, y=250)

        Button(root, text="  No  ", font="ariel 14 bold", bg='white', fg='black', command=lambda: vote(root)).place(x=850, y=250)

        def confirm_delete(root):  # if the user hits the yes button

            global delete_index_list

            try:

                index = int(deletestring.get()) - 1  # Index = (index entered by the user -1)


                if index in delete_index_list:  # in case record was already been deleted

                    vote(root)
                    messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD HAS ALREADY BEEN DELETED ! ')
                    vote(root)


                else:

                    if count < 0:  # case when file is empty and user tries to search for record

                        messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                        vote(root)


                    else:  # if user tries to delete some records  in a non-empty file !

                        if index in range(0, len(retrieve)):  # if user enters the index present in file !

                            global delete_count
                            delete_index_list.clear()


                            with open("deletedentries", "rb") as dfile:

                                while 1:

                                    try:
                                        delete_index_list = pickle.load(dfile)

                                    except:  # In case when initially file is  empty
                                        break

                            delete_count = len(delete_index_list)
                            delete_index_list.insert(delete_count, index)


                            with open("deletedentries", "wb") as dfile:
                                pickle.dump(delete_index_list, dfile)

                            retrieve.pop(index)  # deleting desired index record
                            retrieve.insert(index, [0])


                            with open("vote.bin", "wb+") as pfile:  # here we are deleting the old content of file and adding the new updated content

                                pfile.truncate()
                                pickle.dump(retrieve, pfile)


                            transfer()   # content will be transfered to text file

                            vote(root)

                            messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD HAS BEEN DELETED ! ')

                            vote(root)


                        else:  # if user tries to delete a record which is not present in the file

                            messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD NOT FOUND ! ')
                            vote(root)

            except:  # control will come in this block if user enters a string in the serial number entry box

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', " PLEASE ENTER A VALID SERIAL NUMBER  !")
                vote(root)



##########################         WHWNEVER USER HITS THE SEARCH RECORD BUTTON ,CONTROL REACHES HERE !           ###########################

def search(root):

    vote(root)

    searchstring.set("")

    print("search string is : ", searchstring.get())

    Label(root, text=" ENTER THE VOTER ID NUMBER  ", font=" ariel 17 bold ").place(x=650, y=300)

    Entry(root, textvariable=searchstring, bd=13).place(x=700, y=400)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempsearch()).place(x=900, y=400)


    def tempsearch():

        global delete_index_list , count
        search_retrieve = []
        searchretrieve_back = []

        try:

            index = int(searchstring.get()) - 1


            if count < 0:  # case when file is empty and user tries to search for record

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                vote(root)


            else:  # in case when file has content i.e. , the file is not empty

                with open("deletedentries", "rb") as dfile:

                    while 1:

                        try:

                            delete_index_list = pickle.load(dfile)


                        except:  # In case when initially file is  empty

                            break


                if index in delete_index_list:  # if user deleted a record and is searching for the same

                    vote(root)
                    messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD WAS DELETED  SO YOU CAN\'T SEARCH FOR IT!! ')
                    vote(root)

                else:  # otherwise the normal searching process

                    pfile = open("vote.bin", 'rb')
                    searchretrieve_back.clear()  # to delete the previous content so that new can be loaded

                    while 1:

                        try:  # till the end of file is reached

                            searchretrieve_back = pickle.load( pfile)  # loading the data from the file to the list named search_retrieve

                        except (EOFError):  # when file reaches its end

                            break  # go out of while loop

                    search_retrieve = searchretrieve_back[:]
                    pfile.close()


                    if index in range(0, len(search_retrieve)):        # if record is present in file

                        display(root , index , search_retrieve)         # calling the display function to display the record

                    else:         # if record is not in the file

                        messagebox.showinfo(' IMPORTANT MESSAGE !! ', " SEARCHED RECORD IS NOT IN THE FILE !")
                        vote(root)

        except:  # control will come in this block if user enters a string in the serial number entry box

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', " PLEASE ENTER A VALID SERIAL NUMBER  !")
            vote(root)



##########################         WHWNEVER USER HITS THE UPDATE BUTTON ,CONTROL REACHES HERE !           ###########################

def update(root):

    vote(root)

    updatestring = StringVar(root)
    upstring1 = StringVar(root)
    upstring2 = StringVar(root)
    upstring3 = StringVar(root)
    upstring4 = StringVar(root)
    upstring5 = StringVar(root)
    upstring6 = StringVar(root)
    upstring7 = StringVar(root)
    upstring8 = StringVar(root)
    upstring9 = StringVar(root)


    upstring1.set("")  # so that user comes to that particular window , the entry boxes are empty
    upstring2.set("")
    upstring3.set("")
    upstring4.set("")
    upstring5.set("")
    upstring6.set("")
    upstring7.set("")
    upstring8.set("")
    upstring9.set("")

    vote(root)

    Label(root, text=" ENTER THE VOTER ID NUMBER  ", font=" ariel 17 bold ").place(x=650, y=300)

    Entry(root, textvariable=updatestring, bd=13).place(x=700, y=400)

    Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: tempupdate(root)).place(x=900, y=400)


    def tempupdate(root):

        temp_list = []

        try:

            index = int(updatestring.get()) - 1

            with open("vote.bin", "rb") as pfile:

                while 1:  # this block is used to load all the content of main file (phone.bin) in the temp list

                    try:

                        temp_list = pickle.load( pfile)  # this list is used in this method to count the no of records in file

                    except:  # In case when either the file is empty  initially or it reaches END OF FILE
                        break


            if index in range(0, len(temp_list)):  # if the index entered by the user is  present in the file

                if count < 0:  # case when file is empty and user tries to update a record

                    messagebox.showinfo(' IMPORTANT MESSAGE !! ', " NO RECORD IS PRESENT IN THE FILE !")
                    vote(root)


                else:  # when file has some content to be updated

                    global delete_index_list

                    with open("deletedentries", "rb") as dfile:

                        while 1:  # this block is used to load the content of 'delete file' in delete index list

                            try:

                                delete_index_list = pickle.load(dfile)

                            except:  # In case when initially file is  empty OR when it reaches the end of file

                                break


                    if index in delete_index_list:  # if user deleted a record and wants to update the same

                        vote(root)
                        messagebox.showinfo("  IMPORTANT MESSAGE ", ' RECORD WAS DELETED  SO YOU CAN\'T UPDATE IT!! ')
                        vote(root)


                    else:

                        vote(root)

                        Label(root, text="New  Name ", font="ariel 14 bold ").place(x=550, y=200)

                        Entry(root, textvariable=upstring1, bd=7, width=40).place(x=800, y=200)

                        Label(root, text="New Age  ", font="ariel 14 bold ").place(x=550, y=250)

                        Entry(root, textvariable=upstring2, bd=7, width=40).place(x=800, y=250)

                        Label(root, text="New Gender ", font="ariel 14 bold ").place(x=550, y=300)

                        Entry(root, textvariable=upstring3, bd=7, width=40).place(x=800, y=300)

                        Label(root, text="New Category  ", font="ariel 14 bold ").place(x=550, y=350)

                        Entry(root, textvariable=upstring4, bd=7, width=40).place(x=800, y=350)

                        Label(root, text="New Phone no ", font="ariel 14 bold ").place(x=550, y=400)

                        Entry(root, textvariable=upstring5, bd=7, width=40).place(x=800, y=400)

                        Label(root, text="New Email ", font="ariel 14 bold ").place(x=550, y=450)

                        Entry(root, textvariable=upstring6, bd=7, width=40).place(x=800, y=450)

                        Label(root, text="New Area ", font="ariel 14 bold ").place(x=550, y=500)

                        Entry(root, textvariable=upstring7, bd=7, width=40).place(x=800, y=500)

                        Label(root, text="New District ", font="ariel 14 bold ").place(x=550, y=550)

                        Entry(root, textvariable=upstring8, bd=7, width=40).place(x=800, y=550)

                        Label(root, text="New Pin code ", font="ariel 14 bold ").place(x=550, y=600)

                        Entry(root, textvariable=upstring9, bd=7, width=40).place(x=800, y=600)

                        Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: doneupdate(root)).place(x=900, y=650)


                        def doneupdate(root):

                            update_retrieve = []

                            with open("vote.bin", "rb") as pfile:

                                while 1:

                                    try:

                                        update_retrieve = pickle.load(pfile)

                                    except (EOFError):

                                        break


                            print("update after reading from file :", update_retrieve)

                            update_retrieve[index][0] = upstring1.get()

                            update_retrieve[index][1] = upstring2.get()

                            update_retrieve[index][2] = upstring3.get()

                            update_retrieve[index][3] = upstring4.get()

                            update_retrieve[index][4] = upstring5.get()

                            update_retrieve[index][5] = upstring6.get()

                            update_retrieve[index][6] = upstring7.get()

                            update_retrieve[index][7] = upstring8.get()

                            update_retrieve[index][8] = upstring9.get()



                            with open("vote.bin", "wb") as pfile:

                                pfile.truncate()
                                pickle.dump(update_retrieve, pfile)


                            transfer()    # content will be tranfered to text file

                            display(root , index , update_retrieve)            # calling the display function to display the record

                            Button(root, text=" OKAY ", font=" ariel 18 bold", command=lambda: vote(root)).place(x=900, y=700)


            else:  # if the index entered by the user is not present in the file

                messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  RECORD IS NOT IN THE FILE !")
                vote(root)

        except:

            messagebox.showinfo(' IMPORTANT MESSAGE !! ', "  PLEASE ENTER A VALID SERIAL NUMBER !! ")
            vote(root)



##########################         WHWNEVER USER HITS THE FEEDBACK BUTTON ,CONTROL REACHES HERE !           ###########################

def feedback(root):    
     # DEFINITION OF THE METHOD BEGINS
    feed_list = []

    mainwindow(root)
    Label(root, text=" FEEDBACK ", font=("arial", 15)).place(x=500, y=230)

    txt = scrolledtext.ScrolledText(root, width=80, height=20)
    txt.place(x=450, y=300, )

    Button(root, text=" DONE ", command=lambda: clearfeed(root)).place(x=1000, y=580)

    def clearfeed(root):

        txt.insert(END, " \n\n\n Thank You !! \n Your Feedback holds importance for us !\n\n")
        Button(root, text=" OKAY ", command=lambda: mainwindow(root)).place(x=500, y=680)
        '''txt.get(1.0 ,feed_list)
        print(feed_list)'''



##########################         THIS FUNCTION TRANSFERS ALL THE CONTET FROM TH BINARY FILE TO THE TEXT FILE           ###########################

def transfer():       # this method transfers content of binary file to text file

    global a
    filecount = 0


    with open("vote.bin", "rb") as pfile:

        while 1:

            try:

               a = pickle.load(pfile)

            except (EOFError) :

              break

    with open("finalvote.txt", "w") as textfile:

            textfile.truncate()


    while filecount<len(a):

        try:

            with open("finalvote.txt", "a") as textfile:

                str1 = a[filecount][0]
                str2 = a[filecount][1]
                str3 = a[filecount][2]
                str4 = a[filecount][3]
                str5 = a[filecount][4]
                str6 = a[filecount][5]
                str7 = a[filecount][6]
                str8 = a[filecount][7]
                str9 = a[filecount][8]
                totalspace =20
                print("1 : %d\n " % filecount, str1, str2, str3, str4, str5)
                ind = str(filecount+1)
                textfile.write(" RECORD NO. ")
                textfile.write(ind)
                textfile.write(" :  ")
                textfile.write(str1)
                textfile.write(" "*(totalspace-len(str1)) )
                textfile.write(str2)
                textfile.write(" "*(totalspace-len(str2)) )
                textfile.write(str3)
                textfile.write(" "*(totalspace-len(str3)) )
                textfile.write(str4)
                textfile.write(" "*(totalspace-len(str4)) )
                textfile.write(str5)
                textfile.write(" "*(totalspace-len(str5)) )
                textfile.write(str6)
                textfile.write(" "*(totalspace-len(str6)) )
                textfile.write(str7)
                textfile.write(" "*(totalspace-len(str7)) )
                textfile.write(str8)
                textfile.write(" "*(totalspace-len(str8)) )
                textfile.write(str9)
                textfile.write("\n \n")
                filecount += 1

        except :  # when deleted record is referred

                 filecount += 1
                 continue


###########################         WHWNEVER USER HITS THE QUIT BUTTON ,CONTROL REACHES HERE !           ###########################

def quit(root) :  # WHEN USER HITS QUIT BUTTON

    root.destroy()  # root get destroys and tkinter window shuts down


##########################      THIS BLOCK IS RESPONSIBLE FOR CALLING THE MAIN WINDOW FRAME OF TKINTER           ###########################

mainwindow(root)

root.title("fairVote project")  # renames the title of the tkinter window

root.geometry('300x300')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

root.geometry("%dx%d+0+0" % (w, h))  # this statement opens the tkinter window in maximized form

mainloop()