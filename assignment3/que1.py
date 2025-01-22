import pandas as pd
mydataset={
    'Tid':[1,2,3,4,5,6,7,8,9,10],
    'refund':["yes","No","No","Yes","No","No","Yes","No","No","No"],
    'Maritalstatus':["single","Married","single","Married","Divorced","Married","Divorced","single","Married","single"],
    'TaxableIncome':["125k","100k","70k","120k","95k","60k","220k","85k","75k","90k"],
    'cheat':["No","No","No","No","Yes","No","No","Yes","No","Yes",]
}
df=pd.DataFrame(mydataset)
print(df)

