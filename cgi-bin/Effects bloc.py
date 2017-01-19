#!/usr/bin/env python3
print('Content-type: text/html\r\n\r')

    import cgitb
    import cgi
    import PIL	

    cgitb.enable() 

    inputs = cgi.FieldStorage() 
    resize = inputs.getvalue("effect")


    print "Content-type: text/html" 

    print "<title> MyPythonWebpage </title>"


Effects = {
	
	'Censor Box' : 
	'Pixelate' : 
	'Blur' : 
	'Crop' : 
	'White Space' : 
	'Glitch Art' : 

}