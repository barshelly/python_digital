names={"aviv":"100000","bar":"4567","natan":"990","asaf":"234"}
print(names)
summary=names["aviv"] + names["asaf"]
print("the summary is: " + str(summary))

names.update({"dudi":summary})
print (names)
print("number of entries: " + str(len(names)))
print("bar" in names)