#7.3 Does each user-defined function have 5 or fewer arguments
def main():
    pass

class Sun:
    # It may seem counterintuitive that single naming style
    def __init__(self, iname, irad, im):
        self.name = iname
        self.radius = irad
        self.mass = im
    def get_mass(self):
        return self.mass
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
    def six_arg_func(self, one, two, three, four, five):
        print(one, two, three, four, five, "too many args :(")
        return self.name

main()