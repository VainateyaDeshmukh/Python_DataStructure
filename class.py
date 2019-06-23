class FD:
    product = 'FD'

    def __init__(self):
        self.age = 0
        self.principal = 0
        self.nper = 2


class FDcmp(FD):
    def __init(self):
        super().__init__()

    def matAmt(self, age, principal):
        if (age < 60):
            irate = 8
        else:
            irate = 7

        ma = principal * (1 + irate / 100) ** self.nper
        return (ma)


class FDsmp(FD):
    def __init(self):
        super().__init__()

    def matAmt(self, age, principal):
        if (age < 60):
            irate = 8
        else:
            irate = 7

        ma = principal * (irate / 100) * self.npr + principal
        return (ma)


fd1 = FD()
fdcmp1 = FDcmp()
fdcmp1.age = 25
fdcmp1.principal = 1000
fdcmp1.matAmt(fdcmp1.age, fdcmp1.principal)

fdsmp1 = FDsmp()
fdsmp1.age = 25
fdsmp1.principal = 1000
fdsmp1.matAmt(fdsmp1.age, fdsmp1.principal)

fdcmp2 = FDcmp()
fdsmp2 = FDsmp()


def CalcMat(fdtype):
    amt = fdtype.matAmt(25, 1000)
    return amt


str = 'S'
if str == 'C':
    amt1 = CalcMat(fdcmp2)
else:
    amt1 = CalcMat(fdsmp2)

print(round(amt1))

fdcmp2 = FDcmp()
fdsmp2 = FDsmp()


def CalcMat(fdtype):
    amt = fdtype.matAmt(25, 1000)
    return amt


str = 'S'
if str == 'C':
    amt1 = CalcMat(fdcmp2)
else:
    amt1 = CalcMat(fdsmp2)

print(round(amt1))