class Vector:
    def __inti__(self, size, values, param):
        if type(param) == list:
            self.values = param
            self.size = len(param)
        if type(param) == int:
            self.values = [float(elem) for elem in range(param)]
            self.size = len(self.values)
        elif type(param) == tuple:
            self.values = [float(elem) for elem in range(param[0], param[1])]
            self.size = len(self.values)
    def __add__(self, x):
        if type(x) == int:
            return Vector([elem + x for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Error detectd! the vector and the scalar should be in the same size")
                return 1
            return Vector([self.values[i] + x.values[i] for i in range(self.size)])

    def __radd__(self, x):
        return Vector.__add__(self, x)
    
    def __sub__(self, x):
        if type(x) == int:
            return Vector([elem - x for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Error detectd! the vector and the scalar should be in the same size")
                return 1
            return Vector([self.values[i] - x.values[i] for i in range(self.size)])
    
    def __rsub__(self, x):
        def __sub__(self, x):
        if type(x) == int:
            return Vector([x - elem for elem in self.values])
        if type(x) == Vector:
            if x.size != self.size:
                print("Error detectd! the vector and the scalar should be in the same size")
                return 1
            return Vector([x.values[i] - self.values[i] for i in range(self.size)])
    
    def __truediv__(self, x):
        if type(x) == int:
            return Vector([elem / x for elem in self.values])
        elif type(x) == Vector:
            print("Undefined")
            return 1
    def __rtruediv__(self, x):
         return print("undefined")
    def __mul__(self, x):
        if type(x) == int:
            return Vector([elem * x for elem in self.values])
        elif type(x) == Vector:
            if (x.size != self.size):
                raise EOFError
                return 1
            return sum([x.values[i] * self.values[i] for i in range(self.size)])
    def __str__(self):  
        return "elements : {}, size : {}".format(self.values, self.size)

    def __repr__(self):
        return "Vector(values={}, size={})".format(self.values, self.size)
