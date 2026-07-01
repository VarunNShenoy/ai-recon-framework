import subprocess

def run_httprobe(subdomain_file):

   with open (subdomain_file,"r") as infile:
      http_probe_result = subprocess.run(["/root/go/bin/httprobe"],stdin=infile,capture_output=True,text=True)
   live_hosts = http_probe_result.stdout.splitlines()
   return live_hosts
