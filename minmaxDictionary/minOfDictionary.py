#the function should return index of the smallest element in the dictionary and the smallest value also

def minOfDictionary(dictionary:dict):
    smallest  = +100
    index_of_smallest = int()
    for index in dictionary:
        if dictionary[index][0] < smallest:
            index_of_smallest = index
            smallest = dictionary[index][0]
        elif dictionary[index][0]==smallest:
            if dictionary[index][1] < dictionary[index_of_smallest][1]:
                index_of_smallest = index
    

    return (index_of_smallest, dictionary[index_of_smallest])

if __name__=="__main__":
    dictionary = {
        0 : (-10,0),
        1 : (10,2),
        2 : (0,2),
        4 : (10,0)
    }

    print(minOfDictionary(dictionary))