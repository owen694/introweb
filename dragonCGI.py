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
                        <title> Dragon MadLib</title>
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
    col=formData.getvalue('col')
    sup = formData.getvalue('sup')
    adj0 = formData.getvalue('adj0')
    plbp = formData.getvalue('plbp')
    bp = formData.getvalue('bp')
    n0=formData.getvalue('n0')
    pla=formData.getvalue('pla')
    adj1=formData.getvalue('adj1')
    adj2=formData.getvalue('adj2')
    adj3=formData.getvalue('adj3')

    fileIn = open('dragon.txt','r')
    story = fileIn.read()
    story = story.format(Col=col,Super=sup,Adj0=adj0,Plbp=plbp,Bp=bp,N0=n0,Pla=pla, Adj1=adj1,Adj2=adj2,Adj3=adj3)
    fileIn.close()
    return story




def main():
    htmlTop()
    print ' <div id="yeet" style="height: 300px; line-height: 30px;"> <center><p> <span style="font-weight:900; font-size:30px;">Dragon</span></p>'
    print getData()
    print '</div> </div> </center>'
    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
