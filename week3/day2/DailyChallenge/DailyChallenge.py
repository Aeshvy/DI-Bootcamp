import math

# Daily Challenge Pagination:

class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = int(pageSize)
        self.totalItems = len(self.items)
        self.totalPages = math.ceil(self.totalItems / self.pageSize) 
        self.currentPage = 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        print(self.items[start:end])
    
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        
        if pageNum < 1:
            self.currentPage = 1
            print("Out of bounds! Going to first page:")
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
            print("Out of bounds! Going to the last page:")
        else:
            self.currentPage = pageNum
        return self 


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

p.firstPage()
p.getVisibleItems()

p.nextPage().nextPage()
p.getVisibleItems()

p.prevPage()
p.getVisibleItems()

p.lastPage()
p.getVisibleItems()

p.goToPage(10)
p.getVisibleItems()