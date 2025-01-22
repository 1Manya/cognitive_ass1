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

#que3.1
sub_3_7=df.iloc[3:8]
print("\nrows from 3 to 7\n",sub_3_7)
#3.2
sub2=df.iloc[4:9,2:5]
print("\nrows from 4 to 8 and columns from 2 to 4\n",sub2)
#3.3
sub3=df.iloc[:,1:4]
print("\nrows with column index\n ' 1 to 3' ",sub3)
