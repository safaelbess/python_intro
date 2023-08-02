# # # # # # # # if 1==2:
# # # # # # # #    print('1')
# # # # # # # # elif 1==3:
# # # # # # # #    print('2')
# # # # # # # # else:
# # # # # # # #    print('unknown')      
   
# # # # # # # #    switch:
# # # # # # # #      case1:
# # # # # # # #        print('1')
# # # # # # # #      case2:
# # # # # # # #        print('2')
# # # # # # # #      default:
# # # # # # # #        print('unknown')    
# # # # # # # num=0
# # # # # # # while num < 10:
# # # # # # #  print(num)
# # # # # # #  num=num+1
# # # # # # secretworld='python'
# # # # # # c=0
# # # # # # check = True
# # # # # # while check :
     
 
# # # # # #    userinput = print('enter your word')
# # # # # #    c= c + 1
# # # # # # if userinput==secretworld:
# # # # # #    print('correct') 
# # # # # # else:
# # # # # #      print('wrong')
# # # # # #      if c==2:
# # # # # #          check=False
# # # # # #          print('you have reached the limit')
# # # # # #          break
  
# # # # # #  counter =0
# # # # # #  while counter<5:
# # # # # #      userinput=('enter your string')
# # # # # #      print('-'*50)
# # # # # #      for i in range(0,len):
# # # # # #          ifuserinput[i]=='l'or  userinput[i]=='u'
# # # # # #             userinput=userinput.replace(userinput[i],'*')
# # # # # #             print(userinput[i])
# # # # # #             counter=counter+1
             
         
          
    

                
# # # # # names = ['Alice','David','Caroline']
# # # # # def magicTrick(names):
# # # # #      for i in (names):
# # # # #          print(i +' that was a great trick!')
# # # # #          print(i+' cant wait to see you next trick'+ i +'.\n')
# # # # # magicTrick(names)       
# # # # names = ['Alice ', 'David', 'Caroline']
# # # # counter = 0
# # # # for i in names:
# # # #     print(counter)
# # # #     if i == 'Alice':
# # # #        names = names[0:counter] + names[counter +1:]
# # # #        print(names)
# # # #     counter = counter +1    

# # # names = ['Alice','David','Caroline']
# # # names.append('mohammed')
# # # print(names)
# # # names.append(['Ali','Ahmed'])
# # # print(names)
# # # names.append(9)
# # # print(names)
# # # names.insert(1,'safa')
# # # print(names)
# # # list1 =[1,2,3,4,5]
# # # list2 =['a','b','c']
# # # list2.extend(list1)
# # # print(list2)
# # # sum1 =sum(list1)
# # # print (sum1)

# # list1 =[1,2,3,4,5]
# # minvalue = list1[0]
# # maxvalue =0 

# # for i in list1:
# #    if i> maxvalue:
# #       maxvalue =i
# #    if i<minvalue:
# #          minvalue =i
         
# # print ('minvalue is', minvalue)
# # print('maxvalue is ',maxvalue)   

# # print(max(list1))
# # print(min(list1))

# # print(list1.pop()) #remove the last value in the list
# # print(list1)
# # print(list1.pop(2), list1)
# # #print(list1.remove(1)) 
# # print(list1)
# # print(list1.reverse())
# # print(list1)
# # list1.sort()
# # print(list1)
# # list1.sort(reverse=True)
# # print(list1)

# # list2=[1,2,3,'5','6',9,'f']



# # sum1=0.00



# # list1=[1,2,3,'9','8',3.7,4.5,'r',8,9]
# # for i in list1:
# #   try:
# #    sum1 = sum1 + float(i)
       
# #    list1[list1.index(i)]=float(i)
# #   except ValueError:
# #    print('not a number')
# #    list1.remove(i)
    
# # print (sum1)
# #print sum1    
# #print (list1.avg())
# # print(list1.sum())
# # print(list1.max())
# # print(list1.min())

# student={'name':'','age':'','job':'','country':'','parent':{'father':'','mother':'',},'skills':[]}
# # for i in student:
# #   student[i]= input('enter the '+ i +'i')
# #   print(student)

# for i in student:
#   if type(student[i])==int:
  
#         student[i] = int(input('enter the ' + i +':'))
  
  
  
    
#   elif type(student[i])==list:
#     times= int(input('how many skills do you want'))
#     for j in range (times): 
#      student[i].append(input('enter the  '+ i +':'))  
    
#   elif type(student[i])==dict:
#     student[i]['father']=input('enter the father name:')
#     student[i]['mother']=input('enter the mother name;') 
    
#   else:
#     student[i]=input('enter the' + i +':')
# print (student)      
  


student={}
students=[]

entervalue=True
while entervalue:
  inserttimes = int(input ('how many elements do you want to have?'))
  deckey= input ('enter the key of the student')
  valueType =int(input ('enter the type of the value 1 for str 2 for int 3 for list 4 for dict'))
  if valueType ==1:
    student[deckey]=input ('enter the value')
   
  elif valueType==2:
  
    student[deckey]= int(input('enter the value'))  
    
  elif valueType==3:
    times = int (input('how many skills do you want to add'))
    for j in range(times):
      decValue=[]
      listValue =input('enter the value ')
      decValue.append(listValue)
      
  elif valueType==4:
    stdictionary={}
    times= int(input('how many dictionary keys do you want to add?'))
    for i in (times):
      deckey=input('enter the dictinary key :')   
      decValue =input ("enter the dictionary value") 
      stdictionary[deckey]=decValue
    
  
  addother=input('do you want to add an other student?')     
  if addother=='no':
    entervalue=False
   
  students.append(student)     
  print(students) 
 