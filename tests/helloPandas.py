import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

a = [1,2,7]

myvar = pd.DataFrame(mydataset)
myvar2 = pd.Series(a, index=['Quan', 'Lan', 'Anh'])
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar3 = pd.Series(calories)
myvar.loc[0,'cars'] = 'Mec'

print(myvar)
print(myvar.duplicated())
print(myvar2)
print(myvar3)
print(pd.__version__)
