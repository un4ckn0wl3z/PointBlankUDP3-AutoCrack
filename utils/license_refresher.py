import subprocess

result = subprocess.Popen("date 15-10-2018", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output,error = result.communicate()

print (output)

print(" PointBlank Server UDP3 By MoMzGames ")
print("          LICENSE REFRESHER         ")
print("           by un4ckn0wl3z             ")
print("======================================")