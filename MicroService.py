import time

if __name__ == "__main__":
    while True:
        # opens the returnList file to read the author
        returnList = open("returnList.txt", "r")
        # saves the author name
        author = returnList.readline()
        returnList.close()
        time.sleep(5)
        # opens the return list to write in it
        returnList = open("returnList.txt", "w")
        # opens book file
        books = open("books.txt", "r")
        books_list = books.readlines()
        #iterates through the book list
        for i in books_list:
            if author in i:
                returnList.write(i)
        
        



