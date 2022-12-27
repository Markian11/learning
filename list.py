string = '23x40-30'
lst = []
final_list = []
for i in string:
    if i != "+" and i != "-" and i != "x" and i != "÷":
        lst.append(i)
        x="".join(lst)
        final_list.append(x)
    # if i == "+" or i == "-" or i == "x" or i == "÷":
    #  x = string.split(i)

# for i in l:
#     if i == "+" or i == "-" or i == "x" or i == "÷":
#         if i == "+":
#            result = int([i-1])+int([i+1])

# print(result)

# for i in l:
#     if i == "+" or i == "-" or i == "x" or i == "÷":
#         if i == "+":
#             print(l.index[i])



print(final_list)
  
 