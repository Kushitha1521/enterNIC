count=1
while(count==1):
    nic=input("ENTER YOUR NIC:")
    len1=len(nic)
    listNic=list(nic)

    if (len1==9):
        p1=int(listNic[0])
        p2=int(listNic[1])
        p3=int(listNic[2])
        p4=int(listNic[3])
        p5=int(listNic[4])
        date=int("{0}{1}{2}".format(p3,p4,p5))
        #print(date)
        number="YOUR BIRTH YEAR :19{0}{1}".format(p1,p2)
        number1="YOUR BIRTH DATE:19{0}{1}".format(p1,p2)
        number3="19{0}{1}".format(p1,p2)
        age1=int(number3)
        
        import datetime

        x = datetime.datetime.now()
        now_year=x.year
        now_month=x.strftime("%m")
        now_date=x.strftime("%d")

        #print(now_year)
        #print(now_month)
        #print(now_date)
        
        
        if (0<=date<=366):

            if (0<date<=31):
                d="{0}.january.{1}".format(number1,date)
                c=1
            elif(31<date<=60):
                d1=date-31
                d="{0}.february.{1}".format(number1,d1)
                c=2
            elif(60<date<=91):
                d1=date-60
                d="{0}.march.{1}".format(number1,d1)
                c=3
            elif(91<date<=121):
                d1=date-91
                d="{0}.april.{1}".format(number1,d1)
                c=4
            elif(121<date<=152):
                d1=date-121
                d="{0}.may.{1}".format(number1,d1)
                c=5
            elif(152<date<=182):
                d1=date-152
                d="{0}.june.{1}".format(number1,d1)
                c=6
            elif(182<date<=213):
                d1=date-182
                d="{0}.july.{1}".format(number1,d1)
                c=7
            elif(213<date<=244):
                d1=date-213
                d="{0}.august.{1}".format(number1,d1)
                c=8
            elif(244<date<=274):
                d1=date-244
                d="{0}.september.{1}".format(number1,d1)
                c=9
            elif(274<date<=305):
                d1=date-274
                d="{0}.october.{1}".format(number1,d1)
                c=10
            elif(305<date<=335):
                d1=date-305
                d="{0}.november.{1}".format(number1,d1)
                c=11
            elif(335<date<=366):
                d1=date-335
                d="{0}.december.{1}".format(number1,d1)
                c=12

            if(int(now_month)>c):
                no_month=int(now_month)-c
                age2_y=int(now_year)-age1
                age2="{0} Years and {1} months".format(age2_y,no_month)
            else:
                no_month1=c-int(now_month)
                no_month=12-no_month1
                age2_y=(int(now_year)-age1)-1
                age2="{0} Years and {1} months".format(age2_y,no_month)
                


            
            print(number)
            print(d)
            print("AGE:",age2)
            print("GENDER : MALE")
        elif(500<=date<=866):


            if (500<date<=531):
                d="{0}.january.{1}".format(number1,date)
                c=1
            elif(531<date<=560):
                d1=date-531
                d="{0}.february.{1}".format(number1,d1)
                c=2
            elif(560<date<=591):
                d1=date-560
                d="{0}.march.{1}".format(number1,d1)
                c=3
            elif(591<date<=621):
                d1=date-591
                d="{0}.april.{1}".format(number1,d1)
                c=4
            elif(621<date<=652):
                d1=date-621
                d="{0}.may.{1}".format(number1,d1)
                c=5
            elif(652<date<=682):
                d1=date-652
                d="{0}.june.{1}".format(number1,d1)
                c=6
            elif(682<date<=713):
                d1=date-682
                d="{0}.july.{1}".format(number1,d1)
                c=7
            elif(713<date<=744):
                d1=date-713
                d="{0}.august.{1}".format(number1,d1)
                c=8
            elif(744<date<=774):
                d1=date-744
                d="{0}.september.{1}".format(number1,d1)
                c=9
            elif(774<date<=805):
                d1=date-774
                d="{0}.october.{1}".format(number1,d1)
                c=10
            elif(805<date<=835):
                d1=date-805
                d="{0}.november.{1}".format(number1,d1)
                c=11
            elif(835<date<=866):
                d1=date-835
                d="{0}.december.{1}".format(number1,d1)
                c=12

            if(int(now_month)>c):
                no_month=int(now_month)-c
                age2_y=int(now_year)-age1
                age2="{0} Years and {1} months".format(age2_y,no_month)
            else:
                no_month1=c-int(now_month)
                no_month=12-no_month1
                age2_y=(int(now_year)-age1)-1
                age2="{0} Years and {1} months".format(age2_y,no_month)
                



            
            print(number)
            print(d)
            print("AGE:",age2)
            print("GENDER : FEMALE")
        else:
            print("INVALID NIC!")

    elif (len1==12):
        n1=int(listNic[0])
        n2=int(listNic[1])
        n3=int(listNic[2])
        n4=int(listNic[3])
        n5=int(listNic[4])
        n6=int(listNic[5])
        n7=int(listNic[6])
        number="YOUR BIRTH YEAR :{0}{1}{2}{3}".format(n1,n2,n3,n4)
        number1="YOUR BIRTH DATE:{0}{1}{2}{3}".format(n1,n2,n3,n4)
        date=int("{0}{1}{2}".format(n5,n6,n7))
        #print(date)
        
        number3="{0}{1}{2}{3}".format(n1,n2,n3,n4)
        age1=int(number3)
        import datetime

        x = datetime.datetime.now()
        now_year=x.year
        now_month=x.strftime("%m")
        now_date=x.strftime("%d")

        #print(now_year)
        #print(now_month)
        #print(now_date)
        age2=int(now_year)-age1

     

        if (0<=date<=366):


            if (0<date<=31):
                d="{0}.january.{1}".format(number1,date)
                c=1
            elif(31<date<=60):
                d1=date-31
                d="{0}.february.{1}".format(number1,d1)
                c=2
            elif(60<date<=91):
                d1=date-60
                d="{0}.march.{1}".format(number1,d1)
                c=3
            elif(91<date<=121):
                d1=date-91
                d="{0}.april.{1}".format(number1,d1)
                c=4
            elif(121<date<=152):
                d1=date-121
                d="{0}.may.{1}".format(number1,d1)
                c=5
            elif(152<date<=182):
                d1=date-152
                d="{0}.june.{1}".format(number1,d1)
                c=6
            elif(182<date<=213):
                d1=date-182
                d="{0}.july.{1}".format(number1,d1)
                c=7
            elif(213<date<=244):
                d1=date-213
                d="{0}.august.{1}".format(number1,d1)
                c=8
            elif(244<date<=274):
                d1=date-244
                d="{0}.september.{1}".format(number1,d1)
                c=9
            elif(274<date<=305):
                d1=date-274
                d="{0}.october.{1}".format(number1,d1)
                c=10
            elif(305<date<=335):
                d1=date-305
                d="{0}.november.{1}".format(number1,d1)
                c=11
            elif(335<date<=366):
                d1=date-335
                d="{0}.december.{1}".format(number1,d1)
                c=12
                

            if(int(now_month)>c):
                no_month=int(now_month)-c
                age2_y=int(now_year)-age1
                age2="{0} Years and {1} months".format(age2_y,no_month)
            else:
                no_month1=c-int(now_month)
                no_month=12-no_month1
                age2_y=(int(now_year)-age1)-1
                age2="{0} Years and {1} months".format(age2_y,no_month)
                



            
            print(number)
            print(d)
            print("AGE:",age2)
            print("GENDER : MALE")
        elif(500<=date<=866):
            
            if (500<date<=531):
                d="{0}.january.{1}".format(number1,date)
                c=1
            elif(531<date<=560):
                d1=date-531
                d="{0}.february.{1}".format(number1,d1)
                c=2
            elif(560<date<=591):
                d1=date-560
                d="{0}.march.{1}".format(number1,d1)
                c=3
            elif(591<date<=621):
                d1=date-591
                d="{0}.april.{1}".format(number1,d1)
                c=4
            elif(621<date<=652):
                d1=date-621
                d="{0}.may.{1}".format(number1,d1)
                c=5
            elif(652<date<=682):
                d1=date-652
                d="{0}.june.{1}".format(number1,d1)
                c=6
            elif(682<date<=713):
                d1=date-682
                d="{0}.july.{1}".format(number1,d1)
                c=7
            elif(713<date<=744):
                d1=date-713
                d="{0}.august.{1}".format(number1,d1)
                c=8
            elif(744<date<=774):
                d1=date-744
                d="{0}.september.{1}".format(number1,d1)
                c=9
            elif(774<date<=805):
                d1=date-774
                d="{0}.october.{1}".format(number1,d1)
                c=10
            elif(805<date<=835):
                d1=date-805
                d="{0}.november.{1}".format(number1,d1)
                c=11
            elif(835<date<=866):
                d1=date-835
                d="{0}.december.{1}".format(number1,d1)
                c=12

            if(int(now_month)>c):
                no_month=int(now_month)-c
                age2_y=int(now_year)-age1
                age2="{0} Years and {1} months".format(age2_y,no_month)
            else:
                no_month1=c-int(now_month)
                no_month=12-no_month1
                age2_y=(int(now_year)-age1)-1
                age2="{0} Years and {1} months".format(age2_y,no_month)
                



                
            
            print(number)
            print(d)
            print("AGE:",age2)
            print("GENDER : FEMALE")
        else:
            print("INVALID NIC!")
        
    else:
        print("INVALID NIC! Please enter valid NIC")
    print('---------------------------------------------------')       
    check=int(input("enter one(1) check your nic | enter two(2) to Exit :"))
    
    print('---------------------------------------------------')
    count=check
print("end")
