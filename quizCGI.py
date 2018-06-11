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
                        <title> Hardware Quiz </title>
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



def grade(a):
    if a<6:
        return 'Uh-oh. You might consider learning more about hardware. <br /> To learn more about hardware visit: <br /> <a href="https://pclt.sites.yale.edu/introduction-pc-hardware">Introduction to PC Hardware</a>'
    elif a<9:
        return 'Not bad but there\'s room to improve. <br /> To learn more about hardware visit: <br /> <a href="https://pclt.sites.yale.edu/introduction-pc-hardware">Introduction to PC Hardware</a>'
    else:
        return 'You\'re doing great! <br /> To learn more about hardware visit: <br /> <a href="https://pclt.sites.yale.edu/introduction-pc-hardware">Introduction to PC Hardware</a>'

def main():
    formData = cgi.FieldStorage()
    q0=formData.getvalue('q0')
    q1=formData.getvalue('q1')
    q2=formData.getvalue('q2')
    q3=formData.getvalue('q3')
    q4=formData.getvalue('q4')
    q5=formData.getvalue('q5')
    q6=formData.getvalue('q6')
    q7=formData.getvalue('q7')
    q8=formData.getvalue('q8')
    q9=formData.getvalue('q9')
    ans=[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9]
    c=ans.count('correct')

    htmlTop()
    print ' <div id="yeet" style="height: 490px; line-height: 30px;"> <center><p> <span style="font-weight:900; font-size:30px;">Quiz</span></p>'
    print "Question 0:", q0, '<br />'
    print "Question 1:", q1, '<br />'
    print "Question 2:", q2, '<br />'
    print "Question 3:", q3, '<br />'
    print "Question 4:", q4, '<br />'
    print "Question 5:", q5, '<br />'
    print "Question 6:", q6, '<br />'
    print "Question 7:", q7, '<br />'
    print "Question 8:", q8, '<br />'
    print "Question 9:", q9, '<br />'
    print "Percent Correct:", c*10,'% <br/>'
    print grade(c)
    print '</div> </div> </center>'
    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
