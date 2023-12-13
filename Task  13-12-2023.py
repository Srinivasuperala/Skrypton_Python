list1 = ["a1","b1","c1"]
list2 = ["a2","b2","c2"]
list3 = ["a3","b3","c3"]
index_list = ["a","b","c"]
final_list = [list1,list2,list3]

user_input = input("where to?")
letter_index=index_list.index(user_input[0])
number_index=int(user_input[1])-1
final_list[number_index][letter_index]="somthing"
print(f"{list1}\n{list2}\n{list3}")