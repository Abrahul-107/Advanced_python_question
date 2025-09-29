'''List comprehenstion and Dict comprehension : [expression for item in iterable if condition] '''

def list_comprehension():
    """
    List comprehension is a concise way in python for creating a list on an iterator with some conditon or expression
    """
    num_list = [1,2,3,4,5]
    squared = [ num*num for num in num_list]
    return squared

def dict_comprehension():
    """
    Dict comprehension is a concise way in python for creating a dict on anyitertor with some condition or expression and it stored in key value manner
    """
    num_list = [1,2,3,4,5]
    squred_dict = {num:num*num for num in num_list if num%2==0}
    return squred_dict

def flattening_multdimensional():
    """
    Flattening of multidimensional array using comprehension technique
    """
    multi_dim_list = [[1,2,3],[2,3,4],[3,4,5]]
    list_oned = [ nested_ele for element in multi_dim_list for nested_ele in element ]
    return list_oned


print(list_comprehension())
print(dict_comprehension())
print(flattening_multdimensional())