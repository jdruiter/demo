

def calculate_mean(nlist):
    ''' Calculates the mean of a list of numbers '''
    if not nlist:
        return None

    result = 0.0
    for n in nlist:
        result += n
    return result / len(nlist)



def print_name(prefix="", firstname="", lastname=""):
    '''Prints a name. All parameters are optional '''

    res = ""
    if prefix:
        res = "{}, ".format(prefix.strip())
    if firstname and lastname:
        res += "{} {}".format(firstname.strip(), lastname.strip())
    elif firstname:
        res += firstname.strip()
    elif lastname:
        res += lastname.strip()

    print(res)
    return res




# Tests cases:
def test_calculate_mean():
    assert calculate_mean( [1, 2, 3, 4, 5] ) == 3
    assert calculate_mean( [1.1, 2.2, 3.3, 4.4, 5.5] ) == 3.3
    assert calculate_mean([0]) == 0
    assert calculate_mean([]) == None

def test_print_name():
    assert print_name(firstname="Joris", lastname="de Ruiter", prefix="Mr") == "Mr, Joris de Ruiter"
    assert print_name(firstname="Joris", lastname="", prefix="Sir") == "Sir, Joris"
    assert print_name(firstname="Pien", lastname="Boonstra", prefix="") == "Pien Boonstra"
    assert print_name(firstname="", lastname="Boonstra", prefix="") == "Boonstra"


