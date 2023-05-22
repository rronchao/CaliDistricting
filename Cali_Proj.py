import re
import pandas as pd
import os
import geopandas
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\ronal\\Documents\\ISE 369\\Data')

df = pd.read_csv('weball22.txt', sep='|', header=None)
ca_df = df[(df[18] == 'CA')]
ca_df = ca_df.drop(3543, axis=0)  # drop duplicate name

# Get sum receipts for each district
receipts = ca_df.groupby(19, as_index=False)[5].sum()
receipts.drop(0, axis=0, inplace=True)  # Remove Senator data (District 0)
receipts = receipts.rename(columns={5: '$$'})
receipts = receipts.rename(columns={19: 'DISTRICT'})
receipts['$$'] = receipts['$$'].div(1000000)  # Set scale to millions of dollars

# Data from https://redistrictingdatahub.org/dataset/california-congressional-districts-2012-to-2021/
ca_cd = geopandas.read_file('ca_cong_2012_to_2021.zip')

# Set district number values as ints and merge
receipts['DISTRICT'] = receipts['DISTRICT'].astype(int)
ca_cd['DISTRICT'] = ca_cd['DISTRICT'].astype(int)
ca_cd = ca_cd.merge(receipts, on='DISTRICT')

# Plot total receipts from candidates from each district
ca_cd.plot(column='$$', cmap='Greens', legend=True)
plt.title('California Total Receipts Per District')
plt.legend(title="Sum Receipts In Millions")

# Data from https://en.wikipedia.org/wiki/2020_United_States_House_of_Representatives_elections_in_California
string = """District 1	154,073	43.01%	204,190	56.99%	358,263	100.0%	Republican hold
District 2	294,435	75.74%	94,320	24.26%	388,755	100.0%	Democratic hold
District 3	176,036	54.67%	145,941	45.33%	321,977	100.0%	Democratic hold
District 4	194,731	44.05%	247,291	55.95%	442,022	100.0%	Republican hold
District 5	271,233	76.09%	85,227	23.91%	356,460	100.0%	Democratic hold
District 6	229,648	73.34%	83,466	26.66%	313,114	100.0%	Democratic hold
District 7	217,416	56.62%	166,549	43.38%	383,965	100.0%	Democratic hold
District 8	124,400	43.94%	158,711	56.06%	283,111	100.0%	Republican hold
District 9	174,252	57.58%	128,358	42.42%	302,610	100.0%	Democratic hold
District 10	166,865	55.16%	135,629	44.84%	302,494	100.0%	Democratic hold
District 11	271,063	72.99%	100,293	27.01%	371,356	100.0%	Democratic hold
District 12	362,950	100.00%	0	0.00%	362,950	100.0%	Democratic hold
District 13	327,863	90.37%	34,955	9.63%	362,818	100.0%	Democratic hold
District 14	278,227	79.29%	72,684	20.71%	350,911	100.0%	Democratic hold
District 15	242,991	70.90%	99,710	29.10%	342,701	100.0%	Democratic hold
District 16	128,690	59.38%	88,039	40.62%	216,729	100.0%	Democratic hold
District 17	212,137	71.35%	85,199	28.65%	297,336	100.0%	Democratic hold
District 18	344,127	100.00%	0	0.00%	344,127	100.0%	Democratic hold
District 19	224,385	71.68%	88,642	28.32%	313,027	100.0%	Democratic hold
District 20	236,896	76.78%	71,658	23.22%	308,554	100.0%	Democratic hold
District 21	84,406	49.55%	85,928	50.45%	170,334	100.0%	Republican gain
District 22	144,251	45.77%	170,888	54.23%	315,139	100.0%	Republican hold
District 23	115,896	37.86%	190,222	62.14%	306,118	100.0%	Republican hold
District 24	212,564	58.66%	149,781	41.34%	362,345	100.0%	Democratic hold
District 25	169,305	49.95%	169,638	50.05%	338,943	100.0%	Republican hold
District 26	208,856	60.58%	135,877	39.42%	344,733	100.0%	Democratic hold
District 27	221,411	69.78%	95,907	30.22%	317,318	100.0%	Democratic hold
District 28	244,471	72.67%	91,928	27.33%	336,399	100.0%	Democratic hold
District 29	210,944	100.00%	0	0.00%	210,944	100.0%	Democratic hold
District 30	240,038	69.48%	105,426	30.52%	345,464	100.0%	Democratic hold
District 31	175,315	61.29%	110,735	38.71%	286,050	100.0%	Democratic hold
District 32	172,942	66.58%	86,818	33.42%	259,760	100.0%	Democratic hold
District 33	257,094	67.58%	123,334	32.42%	380,428	100.0%	Democratic hold
District 34	205,346	100.00%	0	0.00%	205,346	100.0%	Democratic hold
District 35	169,405	69.33%	74,941	30.67%	244,346	100.0%	Democratic hold
District 36	185,051	60.34%	121,640	39.66%	306,691	100.0%	Democratic hold
District 37	254,916	85.94%	41,705	14.06%	296,621	100.0%	Democratic hold
District 38	256,206	100.00%	0	0.00%	256,206	100.0%	Democratic hold
District 39	169,837	49.40%	173,946	50.60%	343,783	100.0%	Republican gain
District 40	135,572	72.74%	50,809	27.26%	186,381	100.0%	Democratic hold
District 41	167,938	64.04%	94,289	35.96%	262,227	100.0%	Democratic hold
District 42	157,773	42.87%	210,274	57.13%	368,047	100.0%	Republican hold
District 43	199,210	71.68%	78,688	28.32%	277,898	100.0%	Democratic hold
District 44	206,036	100.00%	0	0.00%		100.0%	Democratic hold
District 45	221,843	53.46%	193,096	46.54%	414,939	100.0%	Democratic hold
District 46	157,803	68.75%	71,716	31.25%	229,519	100.0%	Democratic hold
District 47	197,028	63.27%	114,371	36.73%	311,399	100.0%	Democratic hold
District 48	193,362	48.94%	201,738	51.06%	395,100	100.0%	Republican gain
District 49	205,349	53.13%	181,157	46.87%	386,506	100.0%	Democratic hold
District 50	166,859	46.05%	195,510	53.95%	362,369	100.0%	Republican hold
District 51	165,596	68.30%	76,841	31.70%	242,437	100.0%	Democratic hold
District 52	244,145	61.58%	152,350	38.42%	396,495	100.0%	Democratic hold
District 53	199,244	100.00%	0	0.00%	199,244	100.0%	Democratic hold"""

nums = re.findall("[\d]+.[\d][\d]%", string)  # Get Dem% and Rep%

# Remove % from string and turn to float
for i in range(len(nums)):
    nums[i] = float(nums[i][:-1])

# Take every first 2 numbers, and subtract: Dem% - Rep%
margin = []
for i in range(0, len(nums) - 1, 2):
    margin.append(round((nums[i] - nums[i + 1]), 2))

ca_cd = ca_cd.sort_values('DISTRICT', ascending=True)
ca_cd['MARGIN'] = margin

ca_cd.plot(column='MARGIN', cmap='bwr', legend=True, vmin=-50, vmax=50)
plt.title('Winning Party Margin')

plt.show()