sample_dict={"neme":"kelly","age":25,"salary":8000,"city":"New york"}
print("original dictionary:",sample_dict)
#rename
sample_dict["location"]=sample_dict.pop("city")
print("\nupdated dictionary:",sample_dict)