# Importing socket library
import socket
url=["www.uetpeshawar.edu.pk","www.nccs.pk","wwwnavttc.gov.pk","www.au.edu.pk","www.uop.edu.pk","www.kpfsa.gov.pk","wwwkpcerc.com","www.kth.gov.pk","www.fi.gov.pk","www.peshawarhighcourt.gov.pk"]
for i in url:
    try:
        host_name = i
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
            print("Unable to get Hostname and IP")
#get_Host_name_ip(wwwuetpeshawar.edu.pk)
