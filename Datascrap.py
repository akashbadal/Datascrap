from  bs4 import BeautifulSoup
import requests
import csv
from html_table_parser.parser import HTMLTableParser
import pandas as pd



def welcome():
    print("Let's start scraping the website")



def main(a):
    a= a
    # print(a)
    b = a.iloc[0:1, 1:10]
    c = a.iloc[0:1, 10:20]
    # print(a.head(5))
    c.dropna(axis=1, inplace=True)
    c = c.rename(columns={10: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6, 17: 7, 18: 8, 19: 9})

    b = b.append(c, ignore_index=True)
    a = a.drop([0])
    a.drop([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], axis=1, inplace=True)
    a.dropna(inplace=True)
    b = b.append(a, ignore_index=True)
    b.to_excel('check2.xlsx', index=False, header=False)
    b.to_csv('check_csv.csv',index= False , header = False)
    # b.to_csv('check_csv_zip.zip',index = False, header =False,compression=compression_opts)

    #another file
def main2(a):
    a = a
    result_2 = session_requests.get(Broadband_url)
    q = HTMLTableParser()
    q.feed(result_2.text)
    a1 = pd.DataFrame(q.tables[1])

    # Editing the file
    a1.drop([0], inplace=True)  # dropping the First useless row
    # b1 = a1.iloc[0:1, 0:18]      # slicing the df from next row

    col_name = pd.DataFrame(
        {0: ['SNo'], 1: ["AREA"], 2: ["TEL_NO"], 3: ["CUST_ID"], 4: ["PLAN"], 5: ["OB_NO"], 6: ["OB_DT"],
         7: ["OB_STATUS"], 8: ["COMPL_DT"], 9: ["OB_TYPE"], 10: ["CUST_NAME"], 11: ["ADDRESS"], 12: ["CUST_MOB"],
         13: ["SE_ID"], 14: ["DISCNCT_OB"], 15: ["DISCNCT_OBDT"], 16: ["DISCNCT_OBSTAT"], 17: ["DISCNCT_COMPL_DT"]})


    c1 = a1.iloc[0:1, 18:37]
    a1.drop([1], inplace=True) # Now dropping the next 2nd row , as we have already sliced

    c1.dropna(axis=1, inplace=True) # Dropping empty spaces in intial columns
    c1 = c1.rename(
        columns={18: 0, 19: 1, 20: 2, 21: 3, 22: 4, 23: 5, 24: 6, 25: 7, 26: 8, 27: 9, 28: 10, 29: 11, 30: 12, 31: 13,
                 32: 14, 33: 15, 34: 16, 35: 17})  # Renaming the coloumns

    col_name = col_name.append(c1, ignore_index=True) # Combining the above two sliced df

    a1.drop([18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], axis=1, inplace=True)  # Now dropping the empty columns

    file_ready = col_name.append(a1, ignore_index=True) # Appended the sliced one with the remaining df
    file_ready.to_excel('Broadband2.xlsx', index=False, header=False)


if __name__ == '__main__':
    welcome()
    session_requests = requests.Session()
    login_url2 = "http://ftth.mtnldelhi.in:8080/ftthlistpnet2.jsp?STATE=ALL&subcategory1="
    login_url = "http://ftth.mtnldelhi.in:8080/login.jsp"
    Broadband_url = "http://ftth.mtnldelhi.in:8080/ftthlistpnet11.jsp?STATE=ALL&S=B%27%2C%27W"
    payload = {'uname': 'Powernet',
               'pass': '12345678'}
    s = session_requests.post(login_url, data=payload)
    result = session_requests.get(login_url2)
    p = HTMLTableParser()
    p.feed(result.text)
    a = pd.DataFrame(p.tables[1])
    main(a)
    main2(a)

    print("*******************************************************Finally ,scrapping finished--@<@$#******************************************************")

