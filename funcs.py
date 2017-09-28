def some_test():
    """Что вернет эта функция если ее вызвать:
        1. some_test()
        2. some_test("~Hello~")
    """
    return "Good morning!"


def have_fun():
    """Что вернет эта функция если ее вызвать:
        1. have_fun()
        2. have_fun("Bye bye!!!")
    """
    print "Good morning!"
    return None


def bee_cool():
    """Что вернет эта функция если ее вызвать:
        1. bee_cool()
    """
    print "Good morning!"


def pretty(is_pretty):
    """Что вернет эта функция если ее вызвать:
        1. is_pretty()
        2. is_pretty("I'm pretty!")
        3. is_pretty(is_pretty=123)
        4. is_pretty(is_pretty=(2+3))
        5. is_pretty(is_pretty="I'm pretty!")
        6. is_pretty(is_pretty=None)
        7. is_pretty(is_pretty=['Bill', 'Mike', 'Alan'])
    """
    return is_pretty


def what_is_u_name1(name):
    """Что вернет эта функция если ее вызвать:
        1. what_is_u_name2("Mike")
        2. what_is_u_name2()
        3. what_is_u_name2("777")
        4. what_is_u_name2("Agent 777")
        5. what_is_u_name2(name="Viki")
        6. what_is_u_name2(name)
        7. what_is_u_name2(name=None)
    """
    full_name = "Hi, my name is " + name
    return name


def what_is_u_name2(name):
    """Что вернет эта функция если ее вызвать:
        1. what_is_u_name2("Mike")
        2. what_is_u_name2()
        3. what_is_u_name2("777")
        4. what_is_u_name2("Agent 777")
    """
    name = "Hi, my name is " + name
    return name


def age(age=18):
    """Что вернет эта функция если ее вызвать:
    1. age()
    2. age(23)
    3. age(0)
    3. age("Hello, my age is 87")
    """
    return age


def new_one(*args):
    """Что вернет эта функция если ее вызвать:
        1. new_one('Hi, I'm function arguments()!')
        2. new_one(['Bill', 'Mike', 'Alan'])
        3. new_one('A', 'B', 'C', 'D')
    """
    return args


def arguments(*args):
    """Что вернет эта функция если ее вызвать:
        1. arguments('Hi, I'm function arguments()!')
        2. arguments(['Bill', 'Mike', 'Alan'])
        3. arguments('A', 'B', 'C', 'D')
    """
    for one_arg in args:
        return one_arg
