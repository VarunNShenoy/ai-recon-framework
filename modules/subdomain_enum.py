import subprocess

def run_subfinder(domain):
   result = subprocess.run(["subfinder","-d",domain],
   capture_output=True,
   text=True
)

   subdomains= result.stdout.splitlines()

   return subdomains
