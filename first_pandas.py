# we creating a dataframe with the help of dictionaries
# sjosh={"sid":[1,2,3,4],
#        "sname":["Naveen","Sai","Praveen","azeez"],
#        "scourse":["C","Full Stack","Python","Advance Python"],
#        "sdoj":["Nov","May","July","Sept"]
#        }
# # print(sjosh,type(sjosh))
# import pandas as pd
# df2=pd.DataFrame(sjosh)
# print(df2)

# we now create a dataframe with the help of tuples
# import pandas as pd
# empdata=[(101,"karthik",),(202,"Sneha","Vij"),(305,"priya","Himachal"),(401,"Karthik","Kurnool")]
# df3=pd.DataFrame(empdata,columns=["sid","sname","splace"])
# print(df3)
# print(type(empdata))

# import pandas as pd
# f=pd.read_csv('C:\\Users\\test\\Desktop\\sin.csv')
# print(f)

import pandas as pd
f=pd.read_csv('C:\\Users\\test\\Documents\\credits.csv')
print(f)

# import pandas as pd
# f=pd.read_excel('C:\\Users\\test\\Desktop\\pad.xlsx')
# print(f)

# from pandas import DataFrame


# vsr={"sno":[1,2,3,4],"sname":['sindhu','bindu','indu','chandu'],"smarks":[90,88,70,99],"splace":['nlg','mlg','nzb','hyt']}
# print(vsr,type(vsr))
# import pandas as pd
# df2=pd.DataFrame(vsr)
# print(df2)

# from pandas import DataFrame


# vsr=((101,"sindhu",),(102,"bindhu","nalgonda"),(103,"bindhu","devarkonda"),(104,"teju","nzb"))
# # print(vsr,type(vsr))
# df3=pd.DataFrame(vsr,columns=["sid","sname","splace"])
# print(df3)
