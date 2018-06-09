

def main():
    print pstdev(mass())

def alph():
    x = []
    nam = sorted(names())
    num = sortnum()
    sym = sorted(symbol())
    masses = sortmass()
    for i in range(0,103):
        z = y.format(Name= nam[i], AtomicNumber= num[i], Symbol= sym[i], AtomicMass= masses[i])
        x.append(z)
    return x


def sortnum():
    nam = sorted(names())
    dictn = numdict()
    nums = []
    for i in range(103):
        nums.append(dictn[nam[i]])
    return nums


def sortmass():
    nam = sorted(names())
    dictn = massdict()
    masses = []
    for i in range(103):
        masses.append(dictn[nam[i]])
    return masses
        
    
def symdict():
    a = dict()
    nam=names()
    symbols=symbol()
    for i in range(0,103):
        a[nam[i]]=symbols[i]
    return a
def massdict():
    a = dict()
    nam=names()
    masses=mass()
    for i in range(0,103):
        a[nam[i]]=masses[i]
    return a

def numdict():
    a = dict()
    nam=names()
    nums=atomnum()
    for i in range(0,103):
        a[nam[i]]=nums[i]
    return a


y = '''<tr>
      <th>{Name}</th>
      <th>{AtomicNumber}</th>
      <th>{Symbol}</th>
      <th>{AtomicMass}</th>
    </tr>
'''
def mean(nums):
    return sum(nums, 0.0) / len(nums)

def format():
    x = []
    nam = names()
    num = atomnum()
    sym = symbol()
    masses = mass()
    for i in range(0,5):
         z = y.format(Name= nam[i], AtomicNumber= num[i], Symbol= sym[i], AtomicMass= masses[i])
         x.append(z)
    return x

def names():
    names=[]
    fileIn = open('elements.csv','r')
    data = fileIn.readlines()
    for line in data:
        a=line.split(',')
        names.append(a[0])
    names.pop(0)
    fileIn.close()
    return names

def atomnum():
    num=[]
    fileIn = open('elements.csv','r')
    data = fileIn.readlines()
    for line in data:
        a=line.split(',')
        num.append(a[1])
    num.pop(0)
    fileIn.close()
    return num

def symbol():
    sym=[]
    fileIn = open('elements.csv','r')
    data = fileIn.readlines()
    for line in data:
        a=line.split(',')
        sym.append(a[2])
    sym.pop(0)
    fileIn.close()
    return sym
    
def mass():
    mass=[]
    fileIn = open('elements.csv','r')
    data = fileIn.readlines()
    for line in data:
        a=line.split(',')
        mass.append(a[3])
    mass.pop(0)
    for i in range(0,len(mass)):
        mass[i]=float(mass[i])
    fileIn.close()
    return mass

main()
