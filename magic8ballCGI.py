#!/usr/bin/python

import cgi
import random



def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title>Magic 8 Ball</title>
                        <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <center><a href="http://lisa.stuy.edu/~ali02/projects/projects.html"><img src="projicon.png" style="margin-right:0.4%;"></a></center>

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

def main():
    htmlTop()
    L = ['It is certain.','It is decidedly so.','Without a doubt.',
         'Yes, definitely.','You may rely on it.','As I see it, yes.',
         'Most likely.','Outlook good.','Yes.','Signs point to yes.',
         'Reply hazy try again.','Ask again later.','Better not tell you now.',
         'Cannot predict now.','Concentrate and ask again.','Do not count on it.',
         'My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
    a = random.choice(L)
    print '''<div id="yeet" style="height: 520px;">
                <center><p> <span style="font-weight:900; font-size:30px;">Magic 8 Ball</span></p>'''
    print '<p style="width:60%;"> Per Nadine\'s request, I am putting a note here. If you hover over the ball and then click on it, it will wiggle and then give you a new message.'
    print ' <center><a href="http://lisa.stuy.edu/~ali02/projects/magic8ballCGI.py"><img class="oof" src="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png"></a><br/></center>'
    print '<center><p><h3>' + a + '</h3></p></center>'
    print '<center><a href=../index.html>Back to the Home Page</a><br></center>'
    print '<p>                         </p>'
    print '</div> </div> </center>'
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
