from python_hosts import Hosts, HostsEntry
my_hosts = Hosts(path="C:\\Windows\\System32\\drivers\\etc\\hosts")
import subprocess
#my_hosts.remove_all_matching(address='45.76.187.53')

print(" PointBlank Server UDP3 By MoMzGames ")
print("            HOSTS PATCHER         ")
print("           by un4ckn0wl3z             ")
print("======================================")
new_entry = HostsEntry(entry_type='ipv4', address='45.76.187.53', names=['www.google.com','smtp.gmail.com'])
my_hosts.add([new_entry])

my_hosts.write()


result = subprocess.Popen("ipconfig /flushdns ", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output,error = result.communicate()

print (output)