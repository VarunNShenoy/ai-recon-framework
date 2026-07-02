import subprocess

def run_whatweb(live_hosts_file):
   technologies = []
   with open(live_hosts_file,"r") as file:
      for host in file:
         host = host.strip()
         if host:
             result = subprocess.run(["whatweb",host],capture_output=True,text=True)
             technology = result.stdout.strip()
             technologies.append(technology)
   return technologies
