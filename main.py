import pdfkit
import pandas as pd

df = pd.read_csv("list.csv")
print(len(df))
f = open('Groups_Names.html', 'w')
counter = 1
try:
    print("Hellow CR welcome to our simple Group Maker App")
    inp = int(input("How Many Members Do You Wish To Have ? \n"))
    for i in range(len(df)):
        for j in range(inp):
            print(f"\n*************************  Group {counter}  ***********************************************\n")
            if len(df) < inp:
                name = df.sample()
                a = name.to_html()
                f.write(a)
                print(name)
                df = df.drop(name.index.values)
                counter += 1

            else:
                name = df.sample(inp)
                a = name.to_html()
                f.write(a)
                print(name)
                df = df.drop(name.index.values)
                counter += 1

    f.close()
    pdfkit.from_file('exp.html', 'example.pdf')
except:
    if len(df) == 0:
        print("\n\n************** Program Was Executed Successfully, CR *************\n\n")
    else:
        print("Wrong Input CR")
