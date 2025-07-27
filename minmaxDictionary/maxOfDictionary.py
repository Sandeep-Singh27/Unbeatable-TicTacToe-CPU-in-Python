#the function should return index of the largest element in the dictionary and the largest value also

def maxOfDictionary(dictionary:dict):
    largest  = -100
    index_of_largest = int()
    for index in dictionary:
        if dictionary[index][0] > largest:
            index_of_largest = index
            largest = dictionary[index][0]
        elif dictionary[index][0]==largest:
            if dictionary[index][1] < dictionary[index_of_largest][1]:
                index_of_largest = index

    return (index_of_largest, dictionary[index_of_largest])

if __name__=="__main__":
    dictionary = {
        0 : (-10,0),
        1 : (10,2),
        2 : (0,2),
        4 : (10,0)
    }

    print(maxOfDictionary(dictionary))