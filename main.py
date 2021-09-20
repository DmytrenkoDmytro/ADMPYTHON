
import subprocess

#Use DOS/Win comand (for linux the same)
<<<<<<< HEAD
def osco(c,a,p)
    subprocess.call([c,a,p])
    print("\n")


#Info about system(linux)
def osinfo()
    #command 1
    uname ="uname"
    uname_arg ="-a"
    print("Gathering system info with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])
    #command 2
    diskspace = "df"
    diskspace_arg = "-h"
    print("\n Gathering disk space info with %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])
