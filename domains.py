import read
import pandas as pd

df = read.load_data()
domains = df['url'].value_counts()
domains = domains[:99:]
for domain, row in domains.items():
    print("{0}: {1}".format(domain, row))
