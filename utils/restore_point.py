from python_hosts import Hosts, HostsEntry
import subprocess
my_hosts = Hosts(path="C:\\Windows\\System32\\drivers\\etc\\hosts")



print(" PointBlank Server UDP3 By MoMzGames ")
print("           RESTORE SERVER        ")
print("           by un4ckn0wl3z             ")
print("======================================")

my_hosts.remove_all_matching(address='45.76.187.53')
my_hosts.write()
result = subprocess.Popen("w32tm /resync", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output,error = result.communicate()

print (output)

result = subprocess.Popen("ipconfig /flushdns ", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output,error = result.communicate()

print (output)