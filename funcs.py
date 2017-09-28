

def some_test():
    """Что вернет эта функция если ее вызвать:
        1. some_test() "Good morning!"
        2. some_test("~Hello~") Ошибку, что мы передаем больше аргументов
    """
    return "Good morning!"


def have_fun():
    """Что вернет эта функция если ее вызвать:
        1. have_fun()"Good morning!"
        2. have_fun("Bye bye!!!") Ошибку, что мы передаем больше аргументов
    """
    print "Good morning!"
    return None


def bee_cool():
    """Что вернет эта функция если ее вызвать:
        1. bee_cool() "Good morning!"
    """
    print "Good morning!"


def pretty(is_pretty):
    """Что вернет эта функция если ее вызвать:
        1. pretty() Ошибка, мы передаем пустой аргумент
        2. pretty("I'm pretty!") "I'm pretty!"
        3. pretty(is_pretty=123) 123
        4. pretty(is_pretty=(2+3)) 5
        5. pretty(is_pretty="I'm pretty!") "I'm pretty!"
        6. pretty(is_pretty=None) ничего
        7. pretty(is_pretty=['Bill', 'Mike', 'Alan']) ['Bill', 'Mike', 'Alan']
    """
    return is_pretty


def what_is_u_name1(name):
    """Что вернет эта функция если ее вызвать:
        1. what_is_u_name1("Mike") "Mike"
        2. what_is_u_name1() Ошибка, мы передаем пустой аргумент
        3. what_is_u_name1("777") "777"
        4. what_is_u_name1("Agent 777") "Agent 777"
        5. what_is_u_name1(name="Viki") "Viki"
        6. what_is_u_name1(name)
        7. what_is_u_name1(name=None)
    """
    full_name = "Hi, my name is " + name
    return name


def what_is_u_name2(name):
    """Что вернет эта функция если ее вызвать:
        1. what_is_u_name2("Mike") Hi, my name is Mike
        2. what_is_u_name2() Ошибка, мы передаем пустой аргумент
        3. what_is_u_name2("777") Hi, my name is 777
        4. what_is_u_name2("Agent 777") Hi, my name is Agent 777
    """
    name = "Hi, my name is " + name
    return name


def age(age=18):
    """Что вернет эта функция если ее вызвать:
    1. age() 18
    2. age(23) 23
    3. age(0) 0
    3. age("Hello, my age is 87") "Hello, my age is 87"
    """
    return age


def new_one(*args):
    """Что вернет эта функция если ее вызвать:
        1. new_one("Hi, I'm function arguments()!") Hi, I'm function arguments()!
        2. new_one(['Bill', 'Mike', 'Alan']) ['Bill', 'Mike', 'Alan']
        3. new_one('A', 'B', 'C', 'D') ('A', 'B', 'C', 'D')
    """
    return args


def arguments(*args):
    """Что вернет эта функция если ее вызвать:
        1. arguments("Hi, I'm function arguments()!") Hi, I'm function arguments()!
        2. arguments(['Bill', 'Mike', 'Alan'])['Bill', 'Mike', 'Alan']
        3. arguments('A', 'B', 'C', 'D') 'A'
    """
    for one_arg in args:
        return one_arg
