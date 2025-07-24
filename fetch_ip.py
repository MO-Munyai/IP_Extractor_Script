
import pandas as pd
import re

# Load the Excel file
df = pd.read_excel('file_name.xlsx')

# Regex pattern for IPv4 addresses
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

ip_set = set()

# Search for IPs in all cells
for col in df.columns:
    for val in df[col].astype(str):
        found_ips = ip_pattern.findall(val)
        ip_set.update(found_ips)

# Save unique IPs to ip_list.txt
with open('ip_list.txt', 'a') as f:
    for ip in sorted(ip_set):
        f.write(ip + '\n')
