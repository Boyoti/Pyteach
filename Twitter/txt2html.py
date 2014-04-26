# A simple program to convert a text file to a html document
# 


htmlpre="<html><head></head><body>"
htmlpost="</body></html>"

def makehtml(line):
	print "<a href='%s'>%s</a>" % (line,line)
import sys # get the file name as command line argument
file = open(sys.argv[1])
print htmlpre
for line in file.readlines():
#	makehtml(line)
	try:
		splitline = line.split('http:')
	
		print "<p>%s %s,</p>" % (splitline[0], makehtml('http:'+splitline[1]))
	except:
		print "<p>%s</p>" % line
print htmlpost

