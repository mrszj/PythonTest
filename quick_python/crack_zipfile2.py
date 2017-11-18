import zipfile
import optparse

def extractFile(toPath, zFile, password):
    try:
        zFile.extractall(path = toPath, pwd = password)
        return password
    except Exception, e:
        return None
        
def main():
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictFile>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", type="string", help="specify dict file")
    
    (options, args) = parser.parse_args()
    
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        
    zFile = zipfile.ZipFile(zname)
    passFile = file(dname)

    for line in passFile.readlines():
        password = line.split("\n")
        guess = extractFile(".", zFile, password[0])
        
        if guess != None:
            print "Successfully, the Password is %  s " % guess
            exit(0)
        
if __name__ == '__main__':
    main()