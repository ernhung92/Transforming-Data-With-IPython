import read
import pandas
import dateutil
import datetime

df = read.load_data()

def extract_hour(x):
    time_stamp = dateutil.parser.parse(x)
    return time_stamp.hour

df["hour"] = df["submission_time"].apply(extract_hour)
print(df["hour"].value_counts())
