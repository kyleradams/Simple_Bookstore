# Kyler Adams

class Book(object):
    
    
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._checkedOut = False
        self._checkedOutTo = []
        self._waitList = []
        
    def __str__(self):
        result = 'Title: ' + self._title + '\n'
        result += 'Author: ' + self._author + '\n'
        if self._checkedOut == True:
            result += 'Checked out to: ' + str(self._checkedOutTo) + '\n'
        else:
            result += 'Not checked out ' + '\n'
        result += 'Wait list: ' + '\n'
        for i in self._waitList:
            result += str(i) + '\n'
        return result
    
    def getTitle(self):
        return self._title
        
    def getAuthor(self):
        return self._author
    
    def getPatron(self):
        return str(self._checkedOutTo)
    
    def getWaitList(self):
        result = 'Wait list: \n'
        for i in self._waitList:
            result += str(i) + '\n'
        print result
        
    def borrowMe(self, patron):
        if self._checkedOut == False:
            if patron.getNumBooksOut() == patron.MAX_BOOKS_OUT:
                return 'This patron cannot borrow more books'
            else:
                self._checkedOutTo = patron
                self._checkedOut = True
                patron.inc()
        else:
            if patron not in self._waitList:
                self._waitList.append(patron)
                return 'This book is already checked out'
            else:
                return "You are already on this book's waitlist"
    
    def returnMe(self):
        if self._checkedOut == True:
            self._checkedOutTo.dec()
            self._checkedOutTo = []
            self._checkedOut = False
            if len(self._waitList) == 0:
                return 'Book returned'
            else:
                self.borrowMe(self._waitList[0])
                self._waitList.pop(0)
                return 'Book loaned to a waiting patron'

class Patron(object):
    
    MAX_BOOKS_OUT = 3
    
    def __init__(self, name):
        self._name = name
        self._numBooksOut = 0
        
    def __str__(self):
        return self._name + ', ' + str(self._numBooksOut) + ' books out'
    
    def getName(self):
        return self._name
        
    def getNumBooksOut(self):
        return self._numBooksOut
    
    def inc(self):
        self._numBooksOut += 1

    def dec(self):
        self._numBooksOut -= 1