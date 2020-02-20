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
        first_line = fd.readline().split(" ")

        #n_libraries = first_line[1]
        total_time = first_line[2]

        bookScores = fd.readline().split(" ")
        index = 0
        for line in fd:
            library_info = line.split(" ")
            if len(library_info) == 3:
                index = index + 1
                print("Llibreria books " + library_info[0])
                print("Sign Up days " + library_info[1])
                print("Nª llibres dia " + library_info[2])
        libraries = []
        libraries[index] = problem.Library(line, library_info[1], library_info[2])
        problem.Problem(libraries, bookScores, total_time)

if __name__ == '__main__':
    problem = None
    if len(sys.argv) > 2:
        print("Usage: ./problem inputfile.txt")
    if len(sys.argv) == 2:
        problem = parsedata(sys.argv[1])






