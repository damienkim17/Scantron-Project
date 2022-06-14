## scantron project version 1.6

from statistics import mean

def intro(nameList,answerList,keyList,pointList):
    print("The list of students is:\n",nameList,"\n\nThe list of answers are:\n",answerList,"\n\nThe answer key is:\n",keyList,"\n\nAnd the questions are worth:\n",pointList) 
    return

def read_string_list_From_file(the_file):
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()  
        
    #........
    #print ("\n JUST TO TRACE, the local list of strings is:\n")
    #for element in localList:
        #print (element)  # element is a string for one student
    #........
    x = localList
    return x
    return localList


def write_result_to_file(lres,the_file): 
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return

def check_answer_all(nameList,indiv,keyList,pointList):
    studList = []
    correctList = []
    for student in nameList:
        points = 0
        studentPos = nameList.index(student)
        for num in range(len(keyList)):
            if (indiv[studentPos][num] == keyList[num]):
                points = points + float(pointList[num])
            else:
                points = points + 0
        print(student,"scored",points,"points and got",(points/25)*100,"percent.")
        studList.append(points)
    return studList

def check_answer_one(nameList,indiv,keyList,pointList):
    points = 0
    studList = []
    while True:
        arg = input("Which student would you like to check? ==>\n")
        if (arg not in nameList):
            print("This does not match with any name in the data.")
            continue
        else:
            break
    studentPos = nameList.index(arg)
    for num in range(len(keyList)):
        if (indiv[studentPos][num] == keyList[num]):
            points = points + float(pointList[num])
        else:
            points = points + 0
    print (arg,"scored",points,"points and got",(points/25)*100,"percent.")
    again = input("\nWould you like to select a different student? (yes/no) ==>\n")
    studList.append(points)
    if (again == "yes" or again == "y"):
        check_answer_one(nameList,indiv,keyList,pointList)
        points = points + float(pointList[num])
    else:
        print("\nThank you for using the service!")
    return studList

def student_data(nameList,indiv,keyList,pointList):
    ALL = {"ALL","All","ALl","AlL","aLL","alL","aLl","all",}
    SEL = {"SEL","Sel","SEl","SeL","sEL","seL","sEl","sel",}
    studList = []
    while True:
        res = str(input("\nType ALL to print the data for all students\nType SEL to print the data for selected students\n\n(ALL/SEL) ==> "))
        if res not in ALL and res not in SEL:
            print("Your input is invalid.")
            continue
        else:
            break
    if (res in ALL):
        answer_all = check_answer_all(nameList, indiv, keyList, pointList)
        res = answer_all
    elif (res in SEL):
        answer_sel = check_answer_one(nameList,indiv,keyList,pointList)
        print(answer_sel)
        res = answer_sel
    return res
    return studList
        
def main():
    ## importing the student names and their answers
    localList1 = read_string_list_From_file("IN_data_studs.txt")
          
    ## creating seperate lists for names and answers
    nameList = []
    answerList = []
    indiv = []
          
    for element in localList1:
        pos = element.find(" ")
        name = element[0:pos]
        answer = element[8:]
        nameList.append(name)
        answerList.append(answer)
    
    for element in answerList:
        indiv.append(list(element))

    ## importing the answer key and the point values for each question
    localList2 = read_string_list_From_file("IN_key+pts.txt")
          
    ## creating a list for the answer key in order (to match up with stud answers)
    keyList = []
    for number in range(21):
        keyList.append(localList2[0][number])

    ## creating a list for the point values
    pointList = localList2[1].split(" ")

    ## running the intro message
    intro(nameList,answerList,keyList,pointList)

    ## creating a list consisting of the student points
    stud_pointList = student_data(nameList,indiv,keyList,pointList)

    print("\nMaximum points scored:", max(stud_pointList))
    print("\nAverage score:", mean(stud_pointList))
    print("\nNumber of students processed:", len(stud_pointList))

main()
        
