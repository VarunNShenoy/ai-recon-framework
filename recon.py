import os
from modules.subdomain_enum import run_subfinder
from modules.live_host_detection import run_httprobe
from modules.tech_detection import run_whatweb

os.makedirs("results/subdomains",exist_ok=True)
os.makedirs("results/live_hosts",exist_ok=True)
os.makedirs("results/technologies",exist_ok=True)

domain = input("Enter domain:")
print(f"Starting recon on {domain}")

# Run Subfinder as a function from modules

subdomains = run_subfinder(domain)


#save the results to a file

with open(f"results/subdomains/{domain}.txt", "w") as file:
  for subdomain in subdomains:
    file.write(subdomain+"\n")

print("\nChecking the live hosts")
#  Run httprobe from resuls obtained from domains.txt and use httprobe is used as function

live_hosts = run_httprobe(f"results/subdomains/{domain}.txt")

# Save live host in a file

with open(f"results/live_hosts/{domain}_live.txt","w") as file:
  for host in live_hosts:
    file.write(host + "\n")

# Run whatweb from results obtained from live_hosts.txt via function

technologies = run_whatweb(f"results/live_hosts/{domain}_live.txt")

# save the results 

with open(f"results/technologies/{domain}_tech.txt","w") as file:
  for technology in technologies:
   file.write(technology+"/n")

#print scan summary
print("\nScan Summary")
print("-"*30)
print(f"Target: {domain}")
print(f"Subdomains Found: {len(subdomains)}")
print(f"Live Hosts Found:{len(live_hosts)}")
print(f"Subdomains saved to: results/subdomains/{domain}.txt")
print(f"Live Domains saved to: results/live_hosts/{domain}_live.txt")
print(f"Technology results saved to: results/technologies/{domain}_tech.txt")
