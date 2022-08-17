import os

ip = int(input("How many times do you want to commit? \n"))

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')	

print("Commited " + str(ip) + " times")
os.system('git push')