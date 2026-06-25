import subprocess

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

#print each subdomain
for subdomain in subdomains:
    print(subdomain)

#save the results to a file

with open(f"results/{domain}.txt", "w") as file:
  for subdomain in subdomains:
    file.write(subdomain+"\n")

#print scan summary
print("\nScan Summary")
print("-"*30)
print(f"Target: {domain}")
print(f"Subdomains Found: {len(subdomains)}")
print(f"Results saved to : results/{domain}.txt")
