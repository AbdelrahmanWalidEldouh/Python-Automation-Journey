def myDecorator(func):
    def wrapper():
        print("Sugar Added From Decorators")

        func()

        print("#" * 20)

    return wrapper


@myDecorator
def make_tea():
    print("Tea Created")


@myDecorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
