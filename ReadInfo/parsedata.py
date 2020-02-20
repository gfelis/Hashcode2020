from problem import Library, Problem


def main():

    with open('/home/nietzche/Descargas/a_example.txt', 'r') as fd:
        first_line = fd.readline().split(" ")

        n_libraries = first_line[1]
        total_time = first_line[2]

        bookScores = fd.readline().split(" ")
        index=0
        for line in fd:
            library_info = line.split(" ")
            if len(library_info) == 3:
                index = index + 1
                print("Llibreria books " + library_info[0])
                print("Sign Up days " + library_info[1])
                print("Nª llibres dia " + library_info[2])
        #libraries = []
        #libraries[index] = Library(line, library_info[1], library_info[2])
            #Problem(libraries, bookScores, total_time)


if __name__ == '__main__':
    main()
