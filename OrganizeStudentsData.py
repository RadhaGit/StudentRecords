#MAIN FUNCTION
def main():
    filein=input("enter input file: ")
    fin=open(filein,'r')
    fout1=open("barchart.dat",'w')
    fout2=open("rankings.dat",'w')
    #DICTIONARY TO STORE GRADES AS KEYS AND NAMES AS VALUES
    gradesns={}
    #DICTIONARY TO STORE GRADES AS KEYS AND COUNT OF GRADES AS VALUES
    gradessc={}
    #dICTIONARY TO STORE GRADES AS KEYS AND RANKS AS VALUES
    gradessr={}
    #DICTIONARY TO STORE 1-9 AS KEYS AND RANGE OF GRADES AS VALUES
    gradesr0={}
    #VARIABLE TO STORE NUMBER OF ENTRY LINES
    N_entries=0
    list2=[]
    #TAKING INPUT FROM FILE
    for line in fin:
        str1=line
        list1=str1.split()
        name=str(list1[0])
        score=int(list1[1])
        list2=list2+[score]
        #CHECKING WHETHER SCORE IS ALREADY EXISTED IN THE GRADES AND NAMES DICTIONARY
        if score in gradesns.keys():
            #CONCATINATING THE NAMES OF PERSONS WHO EVER GOT SAME GRADE
            gradesns[score]=gradesns[score]+' '+name
        else:
            gradesns[score]=name
        #INCREMENTING THE GRADE COUNT IF IT EXISTS OR INTIALIZING IF IT NOT EXISTED BEFORE
        if score in gradessc.keys():
            gradessc[score]=gradessc[score]+1
        else:
            gradessc[score]=1
        #INCREMENTING THE NUMBER OF STUDENT ENTRIES
        N_entries=N_entries+1
    #LIST TO STORE THE STRING OF STARS WITH A NUMBER OF GRADES APPEARED IN THAT PARTICULAR RANGE OF GRADES
    listcount=['','','','','','','','','']
    
#**********************************************************************************************************************
    # FUNCTION TO PRINT THE BARGRAPH OF RANGE OF GRADES AND CORRESPONDING COUNT NUMBER OF STARS
    def barchart():
        #CHECKING THE GRADE WITH THE GRADE RANGE
        for i in range(len(list2)):
            if list2[i]<=100 and list2[i]>=95:
                listcount[0]=listcount[0]+'*'
            elif list2[i]<=94 and list2[i]>=90:
                listcount[1]=listcount[1]+'*'
            elif list2[i]<=89 and list2[i]>=85:
                listcount[2]=listcount[2]+'*'
            elif list2[i]<=84 and list2[i]>=80:
                listcount[3]=listcount[3]+'*'
            elif list2[i]<=79 and list2[i]>=75:
                listcount[4]=listcount[4]+'*'
            elif list2[i]<=74 and list2[i]>=70:
                listcount[5]=listcount[5]+'*'
            elif list2[i]<=69 and list2[i]>=65:
                listcount[6]=listcount[6]+'*'
            elif list2[i]<=64 and list2[i]>=60:
                listcount[7]=listcount[7]+'*'
            elif list2[i]<=59 and list2[i]>=0:
                listcount[8]=listcount[8]+'*'
            else:
                print("invalid marks")
                
        # STORING THE RANGE OF GRADES AS KEYS AND STRING OF STARS AS VALUES IN DICTIONARY
        gradesrc={'100-95:':listcount[0],'94-90:':listcount[1],'89-85:':listcount[2],'84-80:':listcount[3],'79-75:':listcount[4],'74-70:':listcount[5],'69-65:':listcount[6],'64-60:':listcount[7],'59-0:':listcount[8]}
        # I MADE USE OF OTHER DICTIONARY TO GET THE RANGE OF GRADES AS PER THE ORDER AND STORED RANGE OF GRADES AS VALUES AND NUMERS FROM 1-9 AS KEYS
        gradesro={1:'100-95:',2:'94-90:',3:'89-85:',4:'84-80:',5:'79-75:',6:'74-70:',7:'69-65:',8:'64-60:',9:'59-0:'}
        for i in range(1,10,1):
            #STR1 IS STORING THE RANGE OF GRADES
            str1=str(gradesro[i])
            #STR2 IS STORING THE SRTING OF STARS CORRESPONDING RANGE OF GRADE
            str2=str(gradesrc[gradesro[i]])
            str3=str1.ljust(10)+str2.ljust(10)
            fout1.write(str3)
            fout1.write("\n")
            print(str3)
#**********************************************************************************************************************************

    # FUNCTION TO PRINT THE SORTED GRADES AND CORRESPONDING NAMES AND RANKS        
    def rankings():
        #SOTING THE GRADES AND STORING IT IN LIST3
        list3=sorted(gradessc.keys())
        rank=0
        #RANKING THE STUDENTS
        for i in range(len(list3)-1,-1,-1):
            #CHECKING WHETHER MORE THAN ONE STUDENT GOT THE SAME GRADE
            if gradessc[list3[i]]>1:
                #RANKING THE STUDENTS WHO GOT EQUAL GRADE
                rank=rank+1
                gradessr[list3[i]]=rank
                for i in range(gradessc[list3[i]]-1):
                    rank=rank+1
            #RANKING THE STUDENTS WHOSE GRADES ARE NOT EQUAL
            else:
                rank=rank+1
                gradessr[list3[i]]=rank
        gradessr[list3[i]+1]=rank
        #JUST GIVING THE TITLES OF COLUMNS 
        fout2.write("NAME".ljust(25)+"GRADE".ljust(10)+"RANKS".ljust(10))
        print("NAME".ljust(25)+"GRADE".ljust(10)+"RANKS".ljust(10))
        fout2.write("\n")
        #STORING THE NAMES IN STR1,RANKS IN STR4 FROM THEIR RESPECTIVE DICTIONARIES AS PER THE SORTED GRADE
        for i in range(len(list3)-1,-1,-1):
            str1=str(gradesns[list3[i]])
            str2=str(list3[i])
            str3=str(gradessr[list3[i]])
            #SPLITING THE NAMES OF STUDENTS WHO GOT THE SAME GRADE AND STORING THEM IN LIST4
            list4=str1.split()
            #CHECKING WHETHER MORE THAN ONE STUDENT GOT THE SAME GRADE
            if len(list4)>1:
                for i in range(len(list4)):
                    #ASSIGNING THE GRADES AND RANKS TO THE INDIVIDUAL STUDENT NAME TO WHO GOT THE SAME GRADE
                    str1=list4[i]
                    str4=str1.ljust(25)+str2.ljust(10)+str3.ljust(10)
                    print(str4)
                    fout2.write(str4)
                    fout2.write("\n")
            else:
                str4=str1.ljust(25)+str2.ljust(10)+str3.ljust(10)
                print(str4)
                fout2.write(str4)
                fout2.write("\n")

    
    #MENU          
    while(1):
        print("menu")
        print("1.barchart")
        print("2.sorted data")
        print("3.terminate")
        option=int(input("select an option :"))
        if option==1:
                barchart()
        elif option==2:
            rankings()
        elif option==3:
            #CLOSING THE FILES WHICH I OPEN
            fin.close()
            fout1.close()
            fout2.close()
            #TERMINATING STATEMENT
            break  
        else:
            print("\n please enter correct option\n")
    
main()
