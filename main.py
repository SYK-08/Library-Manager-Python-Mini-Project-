import datetime

def gettime():
    return datetime.datetime.now()

class Library:

    def __init__(self, lib_name, list_of_books, username):
        self.list_of_books = list_of_books
        self.lib_name = lib_name
        self.username = username


    def displayBooks(self):
        choice = input("Choose a category from below(1,2,3):\n1.Novels\n2.Personal Growth\n3.Biographies\nType here:")

        if choice == "1":
            with open("PYTHON/Projects/Novels.txt") as a:
                print(a.read())

        elif choice == "2":
            with open("PYTHON/Projects/Personal-dev.txt") as b:
                print(b.read())

        elif choice == "3":
            with open("PYTHON/Projects/biographies.txt") as c:
                print(c.read())

#Need to work on this method.
    def lendBook(self):
        choice2 = input("Choose a category(1,2,3): \n1.Novels\n2.Personal Growth\n3.Biographies.\nType here:")
        
        if choice2 == "1":
            with open("PYTHON/Projects/Novels.txt") as d:
                data = d.read()
                print(data)
            a_book = input("Choose one book from above(type the EXACT name):")
            with open("PYTHON/Projects/Novels.txt", "w") as e:
                for line in data:
                    if line.strip("\n") != a_book:
                        e.write(line)
                    else:
                        print("Book not available:(")
                print(f"You took {a_book} from {self.lib_name}")
                with open("PYTHON/Projects/lendedBooks.txt", "a") as f:
                    f.seek(0,2)
                    f.write("\n")
                    f.write(a_book + " was lended at " + str([str(gettime())]) + " by " + self.username)

                       
        elif choice2 == "2":
            with open("PYTHON/Projects/Personal-dev.txt") as g:
                data2 = g.read()
                print(data2)
            b_book = input("Choose one book from above(type the EXACT name):")
            with open("PYTHON/Projects/Personal-dev.txt", "w") as h:
                for line in data2:
                    if line.strip("\n") != b_book:
                        h.write(line)
                    else:
                        print("Book not  available:(")

                print(f"You took {b_book} from {self.lib_name}")
                with open("PYTHON/Projects/lendedBooks.txt", "a") as i:
                    i.seek(0,2)
                    i.write("\n")
                    i.write(b_book + " was lended at " + str([str(gettime())]) + " by " + self.username)


        elif choice2 == "3":
            with open("PYTHON/Projects/biographies.txt") as j:
                data3 = j.read()
                print(data3)
            c_book = input("Choose one book from above(type the EXACT name):")
            with open("PYTHON/Projects/biographies.txt", "w") as k:
                for line in data3:
                    if line.strip("\n") != c_book:
                        k.write(line)
                    else:
                        print("Book not available:(")

                print(f"You took {c_book} from {self.lib_name}")
                with open("PYTHON/Projects/lendedBooks.txt", "a") as l:
                    l.seek(0,2)
                    l.write("\n")
                    l.write(c_book + " was lended at " + str([str(gettime())]) + " by " + self.username)

            
    def addBook(self):
        add = input("Which type of book you want to contribute?(1,2,3):\n1.Novels\n2.Personal Growth\n3.Biographies\nType here:")

        if add == "1":
            a_book = input("Enter the name of the Book here:")
            with open("PYTHON/Projects/Novels.txt", "a") as a:
                a.seek(0,2)
                a.write("\n")
                a.write(a_book)
                with open("PYTHON/Projects/contributions.txt", "a") as d:
                    d.seek(0,2)
                    d.write("\n")
                    d.write(a_book + " was contributed by " + self.username + " at " + str([str(gettime())]))

        elif add == "2":
            b_book = input("Enter the name of the Book here:")
            with open("PYTHON/Projects/Personal-dev.txt", "a") as b:
                b.seek(0,2)
                b.write("\n")
                b.write(b_book)
                with open("PYTHON/Projects/contributions.txt", "a") as e:
                    e.seek(0,2)
                    e.write("\n")
                    e.write(b_book + " was contributed by " + self.username + " at " + str([str(gettime())]))

        elif add == "3": 
            c_book = input("Enter the name of the Book here:")
            with open("PYTHON/Projects/biographies.txt", "a") as c:
                c.seek(0,2)
                c.write("\n")
                c.write(c_book)
                with open("PYTHON/Projects/contributions.txt", "a") as f:
                    f.seek(0,2)
                    f.write("\n")
                    f.write(c_book + " was contributed by " + self.username + " at " + str([str(gettime())]))
        

    def returnBook(self):
        book = open("PYTHON/Projects/returnedBooks.txt", "r+")
        book2 = open("PYTHON/Projects/lendedBooks.txt", "r+")

        with open("PYTHON/Projects/lendedBooks.txt") as l:
            print(l.read())
        
        question = input("Which book do you want to return?:")
        string = book2.read()
        string_  = book.read()

        if question in string:
            book.seek(0,2)
            book.write("\n")
            book.write(self.username + " returned the book " + question + " at " + str([str(gettime())]))

            for line in string:
                if question in string_:
                    if string_.strip("\n") ==  question:
                        book2.write(line)

        else:
            question2 = input("You haven't lended that book.\nWould you like to donate it?(y/n):")

            if question2 == "n":
                print("Okay:)")
            
            elif question2 == "y":
                Library.addBook(syk)

        book.close()
        book2.close()


syk = Library("Pathsala r Library", Library.displayBooks, "Shreyash Kashyap" )

def main():
    print("Welcome to the Library Manager program:)")
    choose = input("What do you want to do?\n1.See all the books available.\n2.Lend a book.\n3.Contribute books.\n4.Return lended book.\nType here:")

    if choose == "1":
        Library.displayBooks(syk)
    
    elif choose == "2":
        Library.lendBook(syk)
    
    elif choose == "3":
        Library.addBook(syk)
    
    elif choose == "4":
        Library.returnBook(syk)

main()
