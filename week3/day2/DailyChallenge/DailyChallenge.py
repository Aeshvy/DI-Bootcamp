import math

# Daily Challenge : Pagination

# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.

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
        
        # Ensure the page number is within the valid range
        if pageNum < 1:
            self.currentPage = 1  # Set to first page if invalid
            print("Out of bounds! Going to page 1:")
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
            print("Out of bounds! Going to the last page:")
        else:
            self.currentPage = pageNum  # Set to the valid page number
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