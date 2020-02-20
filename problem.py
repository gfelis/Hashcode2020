import sys

class Library():
    def __init__(self, books, singuptime, scanrate):
        self.books = books # (list)
        self.signUpTime = singuptime # int
        self.scanrate = scanrate # int
        self.signedUpDate = 0

class Problem():
    def __init__(self, libraries, bookScores, time):
        self.libraries = libraries # libraries
        self.bookScores = bookScores # (list) constant, score for book in position
        self.time = time # (int)
        self.scannedBooks = set()
        self.signedUpLibraries = []
        self.scores = [0] * len(self.libraries)  # score for each library
        self.date = 0# (int)

    def computeTotalScores(self):
        for i, library in enumerate(self.libraries):
            self.scores[i] = self.libraryScore(library)

    def libraryScore(self, library):
        totalBookScores = 0
        for elem in library.books:
            totalBookScores += self.bookScores[elem]

        score = totalBookScores ###TO DO
        return score

    def liveOneDay(self):
        self.date += 1

    def signUpLibrary(self, library):
        if library.signUpTime < (self.time - self.date):
            library.signedUpDate = self.date + library.signUpTime
        for i in range(len(self.libraries)):
            if self.libraries[i] == library:
                self.signedUpLibraries.append(i)
                self.libraries[i] = None


    def chooseHighestLibrary(self):
        highestLibrary = self.libraries[0]
        for i, score in enumerate(self.scores):
            if score > self.scores[i]:
                highestLibrary = self.libraries[i]
        return highestLibrary

    def scanBooks(self, library):
        for book in library.books:
            self.scannedBooks.add(book)


    def solve(self):
        while(self.date < self.time):
            self.computeTotalScores()
            libraryToSignUp = self.chooseHighestLibrary()
            self.signUpLibrary(libraryToSignUp)
            self.liveOneDay()
            self.scanBooks(libraryToSignUp)

        self.write()

    def write(self):
        print(len(self.libraries))
        print(self.libraries(self.signedUpLibraries[0]) + " " + self.libraries(self.signedUpLibraries[0]))



def parsedata(inputfile):

    with open(inputfile, 'r') as fd:
        first_line = next(fd).split('\n')[0].split(' ')
        total_time = int(first_line[2])
        bookScores = []
        line2 = next(fd).split('\n')[0].split(' ')
        for i in range(len(line2)):
            bookScores.append(int(line2[i]))
        libraries = []
        singUpTime = 0
        scanrate = 0
        for line in fd:
            library_info = line.split('\n')[0].split(' ')
            books = []
            if len(library_info) == 3:
                singUpTime = int(library_info[1])
                scanrate = int(library_info[2])
            if len(library_info) > 3:
                for j in range(len(library_info)):
                    books.append(int(library_info[j]))
                libraries.append(Library(books, singUpTime, scanrate))
                
        return Problem(libraries, bookScores, total_time)


if __name__ == '__main__':
    problem = None
    if len(sys.argv) > 2:
        print("Usage: ./problem inputfile.txt")
    if len(sys.argv) == 2:
        problem = parsedata(sys.argv[1])
        problem.solve()






