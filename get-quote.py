import random
def primary():
    # print("Keep it logically awesome.")

    f = open("quotes.txt", "r+")
    quotes = f.readlines()
    
    last = len(quotes) - 1
    for i in range(0, 5):
        rnd = random.randint(0, last)
        print(quotes[rnd], end = '')
    print("Add some quotes")
    while (True):
        newQuote = input()
        if(newQuote == 'X'):
            break
        f.write(newQuote)
    f.close()
if __name__== "__main__":
    primary()
