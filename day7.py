dict = {
    "dog":"poodle",
    "cat":"calico"
}
print(dict["dog"])
#dictionaries are ordered collections of data items that store multiple items in a single variable
#dictionary items are key value pairs that are separated by commas and within {}
""" values in dictionary can be accessed using keys, we can access values by mentioning keys either in
square brackets or by using get method"""
info={'name':'Karan','age':19,'eligible':True}
print(info['name'])
print(info.get('name'))
#the difference is that get wont throw an error for a non existent key
# print(info['name2'])->gives error
print(info.get('name2'))
#.keys will print all keys in dict
print(info.keys())
print(info.values())
print(info.items())


for key in info.keys():
    print(info[key])
