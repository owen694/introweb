#!/usr/bin/python

import cgi
import itertools

Permutations = []
Anagrams = []

def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Anagrams and Permutations </title>
                        <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <center><a href="projects.html"><img src="projicon.png" style="margin-right:0.4%;"></a></center>

                    <ul>
                	<div class="table">
                          <li><a href="http://lisa.stuy.edu/~ali02">Home Page</a></li>
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


def getData():
    formData = cgi.FieldStorage()

    word=formData.getvalue('word')
    word = word.lower()
    return word


def makePermutations():
    word = getData()
    for w in itertools.permutations(word):
        Permutations.append(''.join(w))
    return Permutations

def findAnagrams():
    FileIn = open('/etc/dictionaries-common/words', 'r')
    DictionDirty = FileIn.readlines()
    Dictionary = []
    for i in DictionDirty:
        Dictionary.append(i.strip(' \n'))
    for i in Permutations:
        if i in Dictionary:
            Anagrams.append(i)
    FileIn.close()
    return Anagrams




def main():
    htmlTop()
    print ' <div id="yeet" style="line-height: 30px;"> <center>'
    boop = ', '.join(makePermutations())
    Anagrams=list(set(findAnagrams()))
    print '<center> <h3> Permutations: </h3> </center>'
    print "<p style='width:70%;'>{}</p>".format(boop)
    print '<center> <h3> Anagrams: </h3> </center>'
    for x in Anagrams:
        print '<center>', x, '</center>'
    print '</div> </div> </center>'
    
    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
