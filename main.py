# # # # # # if 1==2:
# # # # # #    print('1')
# # # # # # elif 1==3:
# # # # # #    print('2')
# # # # # # else:
# # # # # #    print('unknown')      
   
# # # # # #    switch:
# # # # # #      case1:
# # # # # #        print('1')
# # # # # #      case2:
# # # # # #        print('2')
# # # # # #      default:
# # # # # #        print('unknown')    
# # # # # num=0
# # # # # while num < 10:
# # # # #  print(num)
# # # # #  num=num+1
# # # # secretworld='python'
# # # # c=0
# # # # check = True
# # # # while check :
     
 
# # # #    userinput = print('enter your word')
# # # #    c= c + 1
# # # # if userinput==secretworld:
# # # #    print('correct') 
# # # # else:
# # # #      print('wrong')
# # # #      if c==2:
# # # #          check=False
# # # #          print('you have reached the limit')
# # # #          break
  
# # # #  counter =0
# # # #  while counter<5:
# # # #      userinput=('enter your string')
# # # #      print('-'*50)
# # # #      for i in range(0,len):
# # # #          ifuserinput[i]=='l'or  userinput[i]=='u'
# # # #             userinput=userinput.replace(userinput[i],'*')
# # # #             print(userinput[i])
# # # #             counter=counter+1
             
         
          
    

                
# # # names = ['Alice','David','Caroline']
# # # def magicTrick(names):
# # #      for i in (names):
# # #          print(i +' that was a great trick!')
# # #          print('i cant wait to see you next trick'+ i +'.\n')
# # # magicTrick(names)       
# # names = ['Alice ', 'David', 'Caroline']
# # counter = 0
# # for i in names:
# #     print(counter)
# #     if i == 'Alice':
# #        names = names[0:counter] + names[counter +1:]
# #        print(names)
# #     counter = counter +1    

# names = ['Alice','David','Caroline']
# names.append('mohammed')
# print(names)
# names.append(['Ali','Ahmed'])
# print(names)
# names.append(9)
# print(names)
# names.insert(1,'safa')
# print(names)
# list1 =[1,2,3,4,5]
# list2 =['a','b','c']
# list2.extend(list1)
# print(list2)
# sum1 =sum(list1)
# print (sum1)

list1 =[1,2,3,4,5]
minvalue = list1[0]
maxvalue =0 

for i in list1:
   if i> maxvalue:
      maxvalue =i
   if i<minvalue:
         minvalue =i
         
print ('minvalue is', minvalue)
print('maxvalue is ',maxvalue)   

print(max(list1))
print(min(list1))

print(list1.pop()) #remve the last value in the list
print(list1)
print(list1.pop(2), list1)
#print(list1.remove(1)) 
print(list1)
print(list1.reverse())
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)