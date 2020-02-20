import parsedata.py
import sys

class Library():
    def __init__(self, books, singuptime, scanrate):
        self.books = books # (list)
        self.singuptime = singuptime # int
        self.scanrate = scanrate # int

class Problem():
    def __init__(self):
        self.libraries # libraries
        self.scores # score for each library
        self.bookScores # (list) constant, score for book in position
        self.time # (int)
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

    def singUpLibrary(self, index):




if __name__ == '__main__':
    problem = None
    if len(sys.argv) > 2:
        print("Usage: ./problem inputfile.txt")
    if len(sys.argv) == 2:
        problem = parsedata(sys.argv[1])








