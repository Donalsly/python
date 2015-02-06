import time
import os
f="test.txt"


# users select:
def Select():
    contact=open(f)
    contact_list=contact.readlines()
    sel=input("would you like select All?[y|n]:")
    flag=True
    if sel=="y":
        print("The all information !")
        for s in contact_list:
            s=s.rstrip('\n')
            print(s)
        else:
            flag=False
    while flag:
        user_input=input("please input what your select(quit to exit):")
        if user_input=="quit":
            break
        for line in contact_list:
            if user_input=="":
                break
            if user_input in line:
                print(line.rstrip('\n'))
                break
        else:
            print("Sorry,Selecte Faile !")
    contact.close()


# users add:
def Add():
    contact=open(f,'a+')
    c=contact.readlines()
    while True:
        user_input=input('please input what you would add(quit to exit):')
        if user_input=="quit":
            break
        if len(user_input)==0:
            continue
        else:
            contact.write("\n"+user_input)
            contact.flush()
    contact.close()
    print("After added,print all the information:")
    contact=open(f)
    contact_list=contact.readline()
    while contact_list!='':
        s=contact_list.strip('\n')
        print(s)
        contact_list=contact.readline()
    contact.close()


# users delete:
def Delete():
    contact=open(f,'r+')
    c=contact.readlines()
    while True:
        user_input=input('please input what you would delete(quit to exit):')
        if user_input=="":
            continue
        if user_input=="quit":
            break
        for i in c:
            if user_input in i:
                print(i.rstrip('\n'))
                u_input=input("would you like delete this[y\\n]:")
                if u_input =="n":
                    break
                if u_input =="y":
                    #print c.index(i)
                    del c[c.index(i)]
    contact.close()
    contact=open(f,'w')
    for i in c:
        contact.write(i)
        contact.flush()
    contact.close()
    print("After deleted,print all the information:")
    contact=open(f)
    contact_list=contact.readline()
    while contact_list!='':
        s=contact_list.rstrip('\n')
        print(s)
        contact_list=contact.readline()
    contact.close()
    

# users modfile:
def Modf():
    f="test1.txt"
    contact=open(f,'r+')
    c=contact.readlines()
    while True:
        user_input=input('please input modfile(quit to exit):')
        if user_input=="":
            continue
        if user_input=="quit":
            break
        for i in c:
            if user_input in i:
                print(i.rstrip('\n'))
                m=i.split(' ')
                print(m)
                while True:
                    m_input=input("input modif [num/name/department/tel]:")
                    if m_input == "num":
                        new_name=input("please input you new number:")
                        m[0]=new_name
                        k=m[0]+' '+m[1]+' '+m[2]+' '+m[3]
                        print(k.rstrip('\n'))
                        c[c.index(i)]=k
                        break
                    elif m_input == "name":
                        new_name=input("please input you new name:")
                        m[1]=new_name
                        k=m[0]+' '+m[1]+' '+m[2]+' '+m[3]
                        print(k.rstrip('\n'))
                        c[c.index(i)]=k
                        break
                    elif m_input == "department":
                        new_name=input("please input you new department:")
                        m[2]=new_name
                        k=m[0]+' '+m[1]+' '+m[2]+' '+m[3]
                        print(k.rstrip('\n'))
                        c[c.index(i)]=k
                        break
                    elif m_input == "tel":
                        new_name=input("please input you new tel:")
                        m[3]=new_name
                        k=m[0]+' '+m[1]+' '+m[2]+' '+m[3]+'\n'
                        print(k.rstrip('\n'))
                        c[c.index(i)]=k
                        break
                    else:
                        print("Input error,please input again!")
                break
        else:
            print("No match!please input again!") 
    contact.close()
    contact=open(f,'w')
    for i in c:
        contact.write(i)
        contact.flush()
    contact.close()
    print("After modifile,print all the information:")
    contact=open(f)
    contact_list=contact.readline()
    while contact_list!='':
        s=contact_list.rstrip('\n')
        print(s)
        contact_list=contact.readline()
    contact.close()


# users show:
def Show():
    os.system("cls")
    print("\n**********************")
    print("Beijing Time")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("**********************")
    print(" 1.selcete\n 2.Add\n 3.modfile\n 4.delete\n 5.init\n 6.print\n 7.remove the file\n 8.quit")
    print("______________________\n")

# uesers initiat:
def init():
    if os.path.isfile("test.txt") == True:
        print("test.txt file exists!")
    else:
        print("Need to create a file [test.txt]")
        in_input=input("would you like to create the file?[y/n]:")
        if in_input == "y":
            f=open("test.txt",'w')
            f.write("1"+' '+"JK409"+' '+'IT'+' '+'99999999'+'\n')
            f.close()
            print("File has been created successfully !")
            time.sleep(2)


# print all information:
def print_all_info():
    print("The all information !")
    contact=open(f)
    contact_list=contact.readline()
    while contact_list!='':
        s=contact_list.rstrip('\n')
        print(s)
        contact_list=contact.readline()
    contact.close()

 
# function main:
def Main():
    while True:
        Show()
        user_input=input("plesse input you chioce[1/2/3/4/5/6/7/8]:")
        if user_input =="":
            continue
        if user_input =="1" or user_input =="selecte":
            Select()
        if user_input =="2" or user_input =="add":
            Add()
        if user_input =="3" or user_input =="modfile":
            Modf()
        if user_input =="4" or user_input =="delete":
            Delete()
        if user_input =="5" or user_input =="init":
            init()
        if user_input =="6" or user_input =="print":
            print_all_info()
        if user_input =="7" or user_input =="remove_the_file":
            os.remove(f,dir_fd=None)
            print("successed remove the %s"%f)
            time.sleep(2)
        if user_input =="8" or user_input =="quit":
            break


if __name__=="__main__":
    while True:
        user_name=input("Please input your user name:" ).strip()
        if len(user_name)==0:
            continue
        if user_name=="Lody":
            while True:
                passwords=input("Please input your passwords:").strip()
                if len(passwords)==0:
                    continue
                if passwords=="123":
                    Main()
                    break
                else:
                     print("Input wrong passwords!Please input again!")
            print("Welcome use the system!")
            break
        else:
            print("Input wrong user name!Please input again!")
    

