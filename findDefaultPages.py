import urllib.request
import urllib.parse
from socket import timeout
import getopt, sys
import os.path
from os import path

words = {
    b'Apache2 server after installation on Debian systems' : 'Default Webpage Found' + "\t" + 'Apache2 on Debian/Ubuntu',
    b'Apache2 server after installation on Ubuntu systems' : 'Default Webpage Found' + "\t" + 'Apache2 on Debian/Ubuntu',
    b'Apache 2 Test Page' : 'Default Webpage Found' + "\t" + 'Apache 2 running',
    b'Welcome to nginx' : 'Default Webpage Found' + "\t" + 'Nginx Unknown Version',
    b'Apache Server Status' : 'Default Webpage Found' + "\t" + 'Apache Unknown Version',
    b'Welcome to the Advanced Extranet Server, ADVX!' : 'Default Webpage Found'  + "\t" + 'ADVX ',
    b'Fedora Core Test Page' : 'Default Webpage Found' + "\t" + 'Outdated Apache 2.0 on Fedora',
    b'Apache HTTP Server on Fedora Core'  : 'Default Webpage Found' + "\t" + 'Outdated Apache 2.0 on Fedora',
    b'xampp/index'  : 'Default Webpage Found' + "\t" + 'Xampp',
    b'Apache/2.0.* (Linux/SuSE)' : 'Default Webpage Found' + "\t" + 'Outdated Apache2.0 on Linux SuSE' ,
    b'Test Page for Apache' : 'Default Webpage Found  ' + "\t" + 'Outdated Apache Unknown Version',
    b'404 Object Not Found' :  'Default Webpage Found  ' + "\t" + 'Outdated IIS5.0',
    b'Microsoft-IIS/5.0 server at'  : 'Default Webpage Found  ' + "\t" + 'Outdated IIS5.0' ,
    b'index.of'  : 'Default Webpage Found  ' + "\t" + 'IIS Unknow Version',
    b'alt="IIS7"'  : 'Default Webpage Found  ' + "\t" + 'IIS7',
    b'Welcome.png'  : 'Default Webpage Found  ' + "\t" + 'IIS Unknown Version',
    b'The initial installation of Debian/GNU Apache' : 'Default Webpage Found  ' + "\t" + 'Apache Unknown Version'
}

def setOpts():

    global ifile
    ifile = False
    flags = "hf:"
    longflags = ["help", "file"]

    try:
        opts, args = getopt.getopt(sys.argv[1:], flags, longflags)
    except getopt.GetoptError as err:
        print()
        print(str(err))
        usage(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage(0)
            sys.exit
        elif o in ("-f", "--file"):
            ifile = a
            # if file provided is not an actual file
            if not path.isfile(ifile):
                assert False, "ERROR: invalid file provided to -f or --file argument; for usage info python findDefaultPages.py -h"
        else:
            assert False, "ERROR: unhandled option; for usage info python findDefaultPages.py -h"

    if not ifile:
        assert False, "ERROR: no file provided via -f or --file argument; for usage info python findDefaultPages.py -h"


def usage(ecode):
    print()
    print('usage: python findDefaultPages.py -h or python findDefaultPages.py -f [file]')
    print('     -h --help:     display help info')
    print('     -f --file:     path to file containing urls or ip addresses to query for default webserver pages')
    print()
    sys.exit(ecode)

def search():
    global words
    protocols = ['http','https'] 
    url = '' 

    f = open(ifile, "r")
    for l in f:
        l = l.rstrip('\n')
        for p in protocols:
            # build url with protocol and port
            url = p + '://' + str(l)
             
            # make sure connection works
            try: 
                headers = {"User-Agent": "Mozilla/5.0 (windows NT 6.1; Win64; x63)"}
                req = urllib.request.Request(url=url,headers=headers)
                resp = urllib.request.urlopen(req, timeout=3)
            except timeout:
                print('Timeout error against url: ' + str(url))
                continue
            except Exception as e:
                print(str(url) + "\t" + str(e))
                continue

            # check contents for particular content
            # use > -1 to check for content to exist
            # use == -1 t check for content not existing
            contents = resp.read()
            for w in words:
                if contents.find(w)>-1:
                    print(url + "\t" + words[w])

def main():
    setOpts()
    search()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Exiting...");
