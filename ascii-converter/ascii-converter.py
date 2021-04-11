import getopt, sys
import os.path
from os import path

class Converter:

    # convert from and to
    conversion = 'd2t'

    # string to convert
    string = 'd2t'

    # converted string
    cstring = ''

    # conversion map
    dat = {}

    def __init__(self, args):
        # if we have less than two args, die
        if len(args) < 2:
            self.usage(0)

        # use command line opts to set variables
        self.setOpts(args)

        # load the conversion map
        self.load()

        # convert the string
        self.convert()

    def print_cstring(self):
        print(self.cstring)

    def convert(self):

        if self.conversion.startswith('t'):
            sdat = list(self.string) 
        else:
            sdat = self.string.split(' ') 
        print(sdat)

        for c in sdat:
            self.cstring += str(self.dat[c])
            if self.conversion.startswith('t'):
                self.cstring += str(' ')
    
    def load(self):
        icol = 0
        dcol = 0
        if self.conversion == 'd2t':
            icol = 1 
        elif self.conversion == 'h2t':
            icol = 2 
        elif self.conversion == 'o2t':
            icol = 3 
        elif self.conversion == 'b2t':
            icol = 4 
        if self.conversion == 't2d':
            dcol = 1 
        elif self.conversion == 't2h':
            dcol = 2 
        elif self.conversion == 't2o':
            dcol = 3 
        elif self.conversion == 't2b':
            dcol = 4 

        f = open('ascii-conversions.dat', 'r')
        for l in f:
            l = l.rstrip('\n')
            ldat = l.split(',') 
            self.dat[ldat[icol]] = ldat[dcol]

    # get command line arguments
    def setOpts(self, args):

        flags = "hc:s:"
        longflags = ["help", "conversion", "string"]
 
        try:
            opts, args = getopt.getopt(args, flags, longflags)
        except getopt.GetoptError as err:
            self.usage(2)
 
        for o, a in opts:
            if o in ("-h", "--help"):
                self.usage(0)
                sys.exit
            elif o in ("-c", "--conversion"):
                self.conversion = a
            elif o in ("-s", "--string"):
                self.string = a

    # print usage message 
    def usage(self, ecode):
        usage = """

    usage: 
        python3 """ + __file__ + """ -h or python """ + __file__ + """ -c [conversion] -s [string to convert]
    
         -h --help:        display help info
         -c --conversion:  d2t ascii decimal to text 
                           h2t ascii hexadecimal to text 
                           b2t ascii binary to text 
                           t2d ascii texxt to decimal
                           t2h ascii texxt to hexadecimal
                           t2b ascii texxt to binary
         -s --string:      string to convert

    example decimal to text (d2t): 

        $> python3 """ + __file__ + """ -c d2t -s '89 101 115 33' 
        Yes!

    example octal to text: 

        $> python3 """ + __file__ + """ -c o2t -s '131 145 163 41' 
        Yes!

    """
        print(usage)
        sys.exit(ecode)

if __name__ == "__main__":
    try:
        c = Converter(sys.argv[1:])
        c.print_cstring()
    except KeyboardInterrupt:
        sys.exit("Exiting...");

