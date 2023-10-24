#Below is a demostration of a CSV import, column def for front API, a sub string search, a int search, using numpy and lambda to clear empty indexes and filter, and a CSV return of the results to be returned to Tableau.
#The below is preped for a MySQL token and deposit to further automate the data life cycle. Using Lambda empty values can be converted to Null deposited into SQL and filter in Tableau.

import pandas as pd
import numpy as np

#File Path for "inflation.CSV" https://www.kaggle.com/datasets/meeratif/inflation-2022
inflation_data = pd.read_csv("File_Path")

#Col dictionay
col_n = list(inflation_data.columns)

#Col dictionay
arguments = {
            'col' : {"A" : "", "B" : "", "C" : "", "D": "", "E": " "}
}

#Col dictionay
arguments['col']['A'] = col_n[0]
arguments['col']['B'] = col_n[1]
arguments['col']['C'] = col_n[2]
arguments['col']['D'] = col_n[3]


inflation_data = pd.DataFrame(inflation_data, columns=[col_n[0],col_n[1],col_n[2],col_n[3]])

#Search column for any entires that contains given string, need to add starts w/ and similar entry function tree
def str_ser(col,s_term):
    n_df = None
    df = inflation_data
    x = df.iloc[:,col].str.findall(s_term)
    x = x.apply(lambda x: np.nan if isinstance(x, list) and not x else x)
    x = x.dropna()
    x = np.array(x.index.values)
    n_df = df[df.index.isin(x)]
    user_i = input("p for print s for Save\n")
    if user_i == "p":
        print(n_df)
    elif user_i == "s":
        #Add user input for file name and path
        n_df.to_csv("Inflation_Contains_Filter.csv",index=False)
        print("File Saved\n")
    else:
        print("Invalid Command")

#Search column for interger range, need to add > and < function tree

def int_ser(col,s_term_1,s_term_2):
    n_df = None
    df = inflation_data
    x = df.iloc[:, col].between(s_term_1,s_term_2)
    x_a = x[x].index
    n_df = df.iloc[x_a]
    user_i = input("p for print s for Save\n")
    if user_i == "p":
        print(df.iloc[x_a])
    elif user_i == "s":
        #Add user input for file name and path
        n_df.to_csv("Inflation_Value_Filter.csv",index=False)
        print("File Saved\n")
    else:
        print("Invalid Command")

user_i = str()
user_i_1 = ""
user_i_2 = ""


while user_i != "q":

    if user_i == "contains":
        col = 0
        user_i_2 = input("Enter Search Term\n")
        str_ser(col,user_i_2)

    if user_i == "inflation":
        col = 1
        user_i_1 = int(input("Enter Start\n"))
        user_i_2 = int(input("Enter Stop\n"))
        int_ser(col,user_i_1,user_i_2)

    if user_i == "full report":
        heavy_table = inflation_data.to_string()
        print(heavy_table)

    user_i = input("Enter Command\n")
