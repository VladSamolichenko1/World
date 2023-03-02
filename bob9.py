#import urllib.request
# import requests
# import bs4
# opener = urllib.request.build_opener()
# responce = opener.open("https://httpbin.org/get")
# print(responce.read())

# responce = requests.get("https://httpbin.org/get")
# # print(responce.content)
# print(responce.text)

#response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
#print(response.text)

# response = requests.get("https://coinmarketcap.com/")
#
# response_text = response.text
#
# response_parse = response_text.split("<span")
# for elem in response_parse:
#     if elem.startswith("$"):
#         for elem_2 in elem.split("</span"):
#             if elem_2.startswith("$") and elem_2[1].isdigit():
#                 print(elem_2)

# response = requests.get("https://coinmarketcap.com/")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, feaatures="html.parser")
#     soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
#     res = soup_list[0].find("span")
#     print(res.text)

















import sqlite3

connection = sqlite3.connect("databaza_DB.sl3", 5)

cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Anna'); ")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kate'); ")
# cur.execute("INSERT INTO first_table (name) VALUES ('Roma'); ")
# connection.commit()
# cur.execute("UPDATE first_table SET name='Kate' rowid=2")
# cur.execute("DELETE FROM first_table WHERE rowid=3;")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# connection.commit()
# res = cur.fetchall()
# print(res)

cur.execute("DROP TABLE first_table")
connection.commit()
connection.close()