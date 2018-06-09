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
                        <title> Process Name </title>
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

def getData():
    formData = cgi.FieldStorage()
    pln0=formData.getvalue('pln0')
    place = formData.getvalue('place')
    n0 = formData.getvalue('n0')
    pln1 = formData.getvalue('pln1').title()
    n1 = formData.getvalue('n1')
    adj0=formData.getvalue('adj0')
    v0=formData.getvalue('v0')
    num=formData.getvalue('num')
    adj1=formData.getvalue('adj1')
    bp=formData.getvalue('bp')
    v1=formData.getvalue('v1')

    fileIn = open('romeo.txt','r')
    story = fileIn.read()
    story = story.format(Pln0=pln0, Place=place, N0=n0, Pln1=pln1, N1=n1, Adj0=adj0, V0=v0, Num=num, Adj1=adj1, Bp=bp, V1= v1)
    fileIn.close()
    return story




def main():
    htmlTop()
    print ' <div id="yeet" style="height: 530px; line-height: 30px;"> <center><p> <span style="font-weight:900; font-size:30px;">Romeo and Juliet</span></p>'
    print getData()
    print '</div> </div> </center>'
    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
