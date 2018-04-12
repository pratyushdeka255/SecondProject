from urllib.request import urlopen
"""
Looking for bad words ina text file. read the contents and send them to a web service for finding the bad words

"""

def read_file():
    contents = open(r"C:\Users\HP\Desktop\CurseWords\movie_quotes1.txt")
    quotes = contents.read()
    #print(quotes)
    check_badwords(quotes)

def check_badwords(word_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q=shit")
    output = connection.read()
    print(output)

read_file()