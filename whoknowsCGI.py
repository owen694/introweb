
#!/usr/bin/python

import cgi
import itertools



def htmlTop():
    print '''Content-type:text/html\n\n
          <!DOCTYPE html>
          <html lang="en-US">
                <head>
                        <meta charset="utf-8" />
                        <title> Process Name </title>

                </head>
                <body>
                    '''

def htmlTail():
    print '''
            </body>
            </html>'''



def main():
    htmlTop()

    htmlTail()

if __name__ == "__main__":
    try:
        main()
    except:
        cgi.print_exception()
