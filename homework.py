# dict1={"name":"Ali", "age":35, "hobby":"game"}
# dict2={"name":"Reza", "age":34, "hobby":"bazi"}
# dict3=dict()
# for i,j in dict2.items():
#     dict3[i]=j
#     for k,l in dict1.items():
#         if dict1[k]==dict2[i]:
#             pass
#         dict3[k]=l

# print(dict3)



# dict_1 = {"name":"ali","age":34,"hobby":"game"}
# dict_2 = {"name":"reza","sen":34,"sargami":"bazi"}
# def merg_dict(data_1,data_2):
#     merged_dict = {**data_1,**data_2}
#     print(merged_dict)

# merg_dict(dict_1,dict_2)






dict1={"age":35, "page":55, "number":17}


def max_value(d):
    
    return max(d, key=d.get)

print(max_value(dict1))






# my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# def count_dict(lst):
#     count = {}
#     for item in lst:
#         if item in count:
#             count[item] += 1
#         else:
#             count[item] = 1
#     return count

# print(count_dict(my_list))






# products = [
#     {"name": "computer", "category": "electronic"},
#     {"name": "tv", "category": "electronic"},
#     {"name": "book", "category": "school stuffs"},
#     {"name": "notebook", "category": "school stuffs"},
# ]


# def