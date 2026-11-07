#To start the code runs through the MOCK_DATA file and gets the total number of rows (the table size). Then the code will load the movie titles and quotes from MOCK_DATA into a list of movie objects. 
#Then it will make 2 seperate hash tables using a linear probing approach to handle collisions.
#The code will measure the number of collions, wasted spaces, and time to create each hash table. In this approach the data gets hashed by using ord() and adding up the total for each letter (poor hash funstion). 
#Then the total gets % by the size of the table to create its index (key). Then the code brings it to that index and adds it into that indexs unless it's already filled. 
#In which case it will run down the list till there is an open spot for the data.


import time

#Runs through the data to get the table size.
def totalRows(MOCK_DATA):
    with open(MOCK_DATA, "r", encoding="utf-8") as f:
        return sum(1 for line in f)

class Movie:
    def __init__(self, title, genre, data, director, revenue, rating, duration, company, quote):
        self.title = title
        self.genre = genre
        self.data = data
        self.director = director
        self.revenue = revenue
        self.rating = rating
        self.duration = duration
        self.company = company
        self.quote = quote


class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

        self.collisions = 0

    #This is what gets the index (key) for the data. Adding up every ord() then % by the size of the table. Simple but can produce clustering.
    def hashFunction(self, key):
        total = 0
        for char in key:
            total = total + ord(char)

        return total % self.size        #Uses % to make sure the index is in the table.

    def insert(self, key, movie):
        index = self.hashFunction(key)
        start = index

            #Linear probing
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = movie
                return

            self.collisions +=1
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = movie
            

    def wastedSpace(self):
        empty=0
        for spaces in self.keys:
            if spaces is None:
                empty +=1
        return empty

    def printStats(self, name):
        print()
        print(name)
        print("Wasted space:", self.wastedSpace(), "wasted spaces")
        print("Collisions:", self.collisions)


def loadMovies(MOCK_DATA):
    movies = []
    file = open(MOCK_DATA, "r", encoding="utf-8")

    for line in file:
        line = line.strip()
        if line == "":
            continue


        parts = line.split(",")

        if len(parts) >= 9:
                    title, genre, data, director, revenue, rating, duration, company, quote = parts [:9]
                    movies.append(Movie(title, genre, data, director, revenue, rating, duration, company, quote))

    file.close()
    return movies


def main():
    tableSize = totalRows("MOCK_DATA.csv")

    movies = loadMovies("MOCK_DATA.csv")

    startTime = time.time()

    titleTable = HashTable(tableSize)
    for movie in movies:
        titleTable.insert(movie.title, movie)

    titleTime = time.time() - startTime

    startTime = time.time()

    quoteTable = HashTable(tableSize)
    for movie in movies:
        quoteTable.insert(movie.quote, movie)

    quoteTime = time.time() - startTime

    titleTable.printStats("Title Hash Table")
    print("Time taken:", titleTime,"seconds")

    quoteTable.printStats("Quote Hash Table")
    print("Time taken:", quoteTime,"seconds")


main()