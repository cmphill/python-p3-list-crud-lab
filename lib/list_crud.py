def create_an_empty_list():
    empty_list = []
    return empty_list

def create_a_list():
    i = 1
    list = []
    while i < 5:
        list.append(i)
        i += 1
    return list


def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
     l.pop()
     return l
    

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l
def retrieve_first_element_from_list(l):
    first = l[0]
    return first
def retrieve_element_from_index(l, index):
    indexed = l[index]
    return indexed

def retrieve_last_element_from_list(l):
    last = l[-1]
    return last
