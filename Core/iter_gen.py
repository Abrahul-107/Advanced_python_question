'''

Iterator: Iterator in python is an object that represents stream of data which it can visit by __next__ method
Genertor: Genertor is way to create iterator for using function using yield operator

'''
def iterator_test(number):
    '''
    Conversion to iterator and visit the next items by using next methods
    '''
    it = iter(number)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    #print(next(it)) wil throw stopIteration error

number = [1,2,3,4]
iterator_test(number)



def read_large_file(file_path):
    '''
    processing big data using generator in memory 
    '''
    with open(file_path,"r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("bigdata.txt"):
    print(line)
