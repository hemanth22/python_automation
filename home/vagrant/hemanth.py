list1 = [
    {"corp": "eBay",     "name": "Matt",    "status": "Part Time"},
    {"corp": "Adobe",    "name": "Rajeev",  "status": "Part Time"},
    {"corp": "Adobe",    "name": "Olaf",    "status": "Full Time"},
    {"corp": "Facebook", "name": "Manny",   "status": "Full Time"},
    {"corp": "Magento",  "name": "Norton",  "status": "Part Time"},
]

a = list1[0]
b = { k:v for k,v in a.items() }
print(str(b).keys(name))

"""
class Employee: ...


report = Employee.report()
print(report)

"""

"""
Manny   | Facebook | Full Time 
Rajeev  | Adobe    | Part Time   

# sort criteria is that Full Time Employees should be printed first then Part Time based on the company name and then the user name
"""
