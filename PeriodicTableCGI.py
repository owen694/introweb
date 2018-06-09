#!/usr/bin/python

import cgi
import itertools


Permutations = []
Anagrams = []
y = '''<tr>
      <th>{Name}</th>
      <th>{AtomicNumber}</th>
      <th>{Symbol}</th>
      <th>{AtomicMass}</th>
    </tr>
'''

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Periodic Table </title>
                        <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <center><a href="projects.html"><img src="projicon.png" style="margin-right:0.4%;"></a></center>

                    <ul>
                	<div class="table">

                		  <li><a href="http://lisa.stuy.edu/~ali02/projects/magic8ballCGI.py">Magic 8 Ball</a></li>
                		  <li><a href="http://lisa.stuy.edu/~ali02/projects/getWord.html">Anagrams</a></li>
                		  <li class="dropdown">
                		    <a href="javascript:void(0)" class="dropbtn">MadLibs</a>
                		    <div class="dropdown-content">
                					<a href=http://lisa.stuy.edu/~ali02/projects/getRomeo.html>Romeo and Juliet</a>
                					<a href=http://lisa.stuy.edu/~ali02/projects/getDragon.html>Dragon</a>
                					<a href=http://lisa.stuy.edu/~ali02/projects/getProverb.html>Ancient Proverb</a>
                				</div>
                		  </li>

                			<li> <a href="http://lisa.stuy.edu/~ali02/projects/quiz.html">Quiz</a>
                			</li>
                			<li> <a href="http://lisa.stuy.edu/~ali02/projects/PeriodicTableCGI.py">Data Analysis</a></li>

                	</div>
                </ul>'''

def htmlTail():
    print '''</body>
            </html>'''

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

def mean(nums):
    return sum(nums, 0.0) / len(nums)


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

def things():
    print '''<h3> General Info</h3>
            <table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th># of Metals</th>
                <th># of Gases at STP</th>
                <th># of Liquids at STP</th>
                <th># of Elements Total</th>
              </tr>
              <tr>
                <th>83</th>
                <th>11</th>
                <th>2</th>
                <th>104</th>
              </tr>
              '''
    print '</table>'

def stats():
    masses = mass()
    a = max(masses)
    b = min(masses)
    c = mean(masses)
    print '''<h3>Atomic Mass Info</h3>
            <table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th>Max Mass</th>
                <th>Min Mass</th>
                <th>Average Mass</th>
                <th>Range of Masses</th>
              </tr>
              <tr>
                <th>{maxm}</th>
                <th>{minm}</th>
                <th>{avgm}</th>
                <th>({lower},{upper})</th>
              </tr><br />
              '''.format(maxm= a, minm=b, avgm= c, lower=b, upper=a)

    print '</table><br />'

def getSortType():
    formData = cgi.FieldStorage()
    sorttype = formData.getvalue('sorttype')
    return sorttype

def selector():
    print '''<form method = "post" action = "PeriodicTableCGI.py">
                <span style="font-weight:900; ">Select Type of Data</span>:
                <select name = "sorttype">
                    <option value="0">Atomic Number (All)</option>
                    <option value="1">Alphabetic (All)</option>
                    <option value="2">Halogens (By Atomic Number)</option>
                    <option value="3">Alkali Metals (By Atomic Number)</option>
                    <option value="4">Halogens (Alphabetic)</option>
                    <option value="5">Alkali Metals (Alphabetic)</option>
                </select></br>
                <input type="submit" class="button" name="submit word" value="Submit" /><br />
                <p>    </p>
            </form>'''
    printTable()

def printTable():
    yeet = getSortType()
    if yeet == '0':
        atom()
    if yeet == '1':
        alph()
    if yeet == '2':
        printHalogens(False)
    if yeet == '3':
        printAlkali(False)
    if yeet == '4':
        printHalogens(True)
    if yeet == '5':
        printAlkali(True)
def format(a,b,c,d):
    x = []
    nam = a
    num = b
    sym = c
    masses = d
    for i in range(0,103):
         z = y.format(Name= nam[i], AtomicNumber= num[i], Symbol= sym[i], AtomicMass= masses[i])
         x.append(z)
    return x



def printHalogens(g):
    f = []
    num = numdict()
    mass = massdict()
    symbols = symdict()

    if g==True:
        halogens=sorted(['Fluorine','Chlorine','Bromine','Iodine','Astatine'])
    else:
        halogens=['Fluorine','Chlorine','Bromine','Iodine','Astatine']
    for x in halogens:
        z = y.format(Name=x, AtomicNumber= num[x], Symbol= symbols[x], AtomicMass= mass[x])
        f.append(z)
    print '''<table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th>Name</th>
                <th>Atomic Number</th>
                <th>Symbol</th>
                <th>Atomic Mass</th>
              </tr>'''
    for i in range(0,len(f)):
        print f[i]

def printAlkali(g):
    f = []
    num = numdict()
    mass = massdict()
    symbols = symdict()
    alkali=['Lithium','Sodium','Potassium','Rubidium','Cesium','Francium']
    if g:
        alkali=sorted(alkali)
    for x in alkali:
        z = y.format(Name=x, AtomicNumber= num[x], Symbol= symbols[x], AtomicMass= mass[x])
        f.append(z)
    print '''<table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th>Name</th>
                <th>Atomic Number</th>
                <th>Symbol</th>
                <th>Atomic Mass</th>
              </tr>'''
    for i in range(0,len(f)):
        print f[i]

def atom():
    x=format(names(),atomnum(),symbol(),mass())
    print '''<table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th>Name</th>
                <th>Atomic Number</th>
                <th>Symbol</th>
                <th>Atomic Mass</th>
              </tr>'''
    for i in range(0,len(x)):
        print x[i]

def alph():
    x=format(sorted(names()),sortnum(),sorted(symbol()),sortmass())
    print '''<table style="width:70%; border: 1px solid #3a807f;''">
              <tr>
                <th>Name</th>
                <th>Atomic Number</th>
                <th>Symbol</th>
                <th>Atomic Mass</th>
              </tr>'''
    for i in range(0,len(x)):
        print x[i]






def main():
    htmlTop()
    print ' <div id="yeet" style="height: 694px; line-height: 30px;"> <center><p> <span style="font-weight:900; font-size:30px;">Periodic Table of Elements</span></p>'
    print '<img src="https://upload.wikimedia.org/wikipedia/commons/6/68/Periodic_table_vectorial.png" width=60%>'
    things()
    stats()
    selector()
    print '</table>'
    print '<p> </p>'
    print '<p> </p>'
    print '<p>          </p><br/></div> </div> </center>'


    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
