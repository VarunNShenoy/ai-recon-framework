import subprocess
import os

os.makedirs("results/subdomains",exist_ok=True)
os.makedirs("results/live_hosts",exist_ok=True)

domain = input("Enter domain:")
print(f"Starting recon on {domain}")

# Run Subfinder
result = subprocess.run(["subfinder","-d", domain],
capture_output=True,
text=True
)

#Convert Output into a list
subdomains = result.stdout.splitlines()
print("\nSubdomains Found:\n")


#save the results to a file

with open(f"results/subdomains/{domain}.txt", "w") as file:
  for subdomain in subdomains:
    file.write(subdomain+"\n")

#Run httpx on discovered subdomains

print("\nChecking the live hosts")

with open(f"results/subdomains/{domain}.txt","r") as infile:
   httprobe_result = subprocess.run(["/root/go/bin/httprobe"],stdin=infile,capture_output=True,text=True)

#Convert the results into text

live_hosts = httprobe_result.stdout.splitlines()

# Save live host in a file

with open(f"results/live_hosts/{domain}_live.txt","w") as file:
  for host in live_hosts:
    file.write(host + "\n")

#print scan summary
print("\nScan Summary")
print("-"*30)
print(f"Target: {domain}")
print(f"Subdomains Found: {len(subdomains)}")
print(f"Live Hosts Found:{len(live_hosts)}")
print(f"Subdomains saved to: results/subdomains/{domain}.txt")
print(f"Live Domains saved to: results/live_hosts/{domain}_live.txt")

