#The code below will load the movie titles and quotes from MOCK_DATA into a list of movie objects. Then it will make 2 seperate hash tables using a linked list approach to handle collisions.
#The code will also measure the number of collions, wasted spaces, and time to create each hash table. In this approach the data gets hashed by using polynomial rolling which uses ord() 
#on the char and two prime numbers 31 (larger than 26 the alphabets size) as well as 10**9+7. Using 10**9+7 as a % which will help lower collisions.
#Then the remaining number gets % by the size of the table to create its index (key). Then the code brings it to that index and adds it into that indexs list. 


import time

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
        self.table = []
        for i in range(size):
            self.table.append([])

        self.collisions = 0

        #polynomial hash stuff
        self.base = 31          #prime number larger than 26 (alphabet size)
        self.mod = 10**9 + 7    #Super big prime number


    #This is what gets the index (key) for the data. Uses polynomial rolling to hash the data. 
    def hash(self, key):
        total = 0
        for char in key:
            total = (total * self.base + ord(char)) % self.mod  #For each char h increases by 1 (starting at 0) whihc gets multiplied by 31 (a prime number larger than 26) then using ord() on the char we get an int which gets % by the large prime number to lower collision chances.
        return total % self.size        #Uses % again to reduce collisions and to make sure the index is in the table.

    def insert(self, key, movie):
        index = self.hash(key)
        linkedList = self.table[index]

        if len(linkedList) > 0:
            self.collisions = self.collisions + len(linkedList)

        linkedList.append((key, movie))

    def wastedSpace(self):
        empty = 0
        for linkedList in self.table:
            if len(linkedList) == 0:
                empty = empty + 1
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
    movies = loadMovies("MOCK_DATA.csv")

    tableSize = 10007

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