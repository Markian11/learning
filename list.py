string = "140x40-30+715÷2"
lst = []
final_list = []
opperator_lst = []
storage = []
for j in string:
    if j != "+" and j != "-" and j != "x" and j != "÷":
        lst.append(j)
    if j == "+" or j == "-" or j == "x" or j == "÷":
       opperator_lst.append(j)
       lst.append("N") 
print(lst) 
lst.append("N")
for i in lst:
    if i != "N":
        storage.append(i)
    if i == "N":
         x="".join(storage)
         final_list.append(x)
         storage.clear()

number_list = []
for i in final_list: 
    number_list.append(int(i))

result = number_list[0]
number_list.pop(0)

for i in range(0, len(number_list)):
    if opperator_lst[i] == "+":
        result = result + number_list[i]
    if opperator_lst[i] == "-":
        result = result - number_list[i]
    if opperator_lst[i] == "x":
        result = result * number_list[i]
    if opperator_lst[i] == "÷":
        result = result / number_list[i]

print(final_list)  
print(opperator_lst)
print(number_list)
print(result)


  
 