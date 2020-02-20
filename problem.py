import sys

class Library():
    def __init__(self, books, singuptime, scanrate):
        self.books = books # (list)
        self.singUpTime = singuptime # int
        self.scanrate = scanrate # int
        self.signedUpDate = None

class Problem():
    def __init__(self, libraries, bookScores, time):
        self.libraries = libraries # libraries
        self.bookScores = bookScores # (list) constant, score for book in position
        self.time = time # (int)
        self.scores = None  # score for each library
        self.date = 0# (int)

    def computeTotalScores(self):
        for i, library in enumerate(self.libraries):
            self.scores[i] = self.libraryScore(library)

    def libraryScore(self, library):
        totalBookScores = 0
        for i, elem in enumerate(library.books):
            totalBookScores += self.bookScores[i]

        score = totalBookScores ###TO DO
        return score

    def liveOneDay(self):
        self.date += 1

    def signUpLibrary(self, library):
        if library.signUpTime < (self.time - self.date):
            library.signedUpDate = self.date + library.signUpTime

    def chooseHighestLibrary(self):
        highestLibrary = self.libraries[0]
        for i, score in enumerate(self.scores):
            if score > highestLibrary.score:
                highestLibrary = self.libraries[i]
        return highestLibrary


def parsedata(inputfile):

    with open(inputfile, 'r') as fd:
        first_line = next(fd).split('\n')[0].split(' ')
        #n_libraries = first_line[1]
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

        int = 0






