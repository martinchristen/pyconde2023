import os
from urllib.request import urlopen
from zipfile import ZipFile

def download(url, destfile, overwrite=False):
    print("Downloading", destfile, "from", url)

    if os.path.exists(destfile) and not overwrite:
        print("File already exists, not overwriting.")
        return
    
    response = urlopen(url) 
    info = response.info()
    cl = info["Content-Length"]
    
    if cl != None:
        filesize = int(cl)
        currentsize = 0
        
        with open(destfile, 'wb') as f:
            while True:
                chunk = response.read(16*1024)
                currentsize += len(chunk)
                
                if not chunk:
                    break
                f.write(chunk)
                percent = int(100*currentsize/filesize)
                
                bar = "*"*(percent)
                bar += "-"*((100-percent))
                print('\r{}% done \t[{}]'.format(percent, bar), end='')
        print("")
        
    else:
        print("Downloading please wait... (filesize unknown)")
        with open(destfile, 'wb') as f:
            while True:
                chunk = response.read(16*1024)
                if not chunk:
                    break
                f.write(chunk)
                

#-----------------------------------------------------------------------------------

def unzip(source, dest):
    with ZipFile(source, 'r') as zz:
        #zz.extractall(path=dest) We don't overwrite already extracted files:
        for item in zz.infolist():
                file_path = os.path.join(dest, item.filename)
                if not os.path.exists(file_path):
                    zz.extract(item, dest)
                    
                    
#-----------------------------------------------------------------------------------                