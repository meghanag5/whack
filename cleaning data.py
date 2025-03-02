import pandas as pd
data = [['APPLING', 0, 5, 2, 15], ['ATKINSON', 0, 2, 0, 7], ['BACON', 0, 2, 2, 8], 
    ['BAKER', 0, 0, 0, 0], ['BANKS', 0, 5, 1, 10], ['BERRIEN', 0, 5, 4, 48], 
    ['BLECKLEY', 0, 3, 1, 24], ['BRYAN', 0, 5, 4, 35], ['BURKE', 0, 3, 2, 55],
    ['CALHOUN', 0, 0, 0, 10], ['CANDLER', 0, 5, 5, 13], ['CHARLTON', 0, 0, 0, 3],
    ['CHATTAHOOCHEE', 0, 0, 0, 0], ['CHATTOOGA', 0, 5, 3, 17], ['CLAY', 0, 0, 0, 16],
    ['CLINCH', 0, 1, 1, 9], ['COFFEE', 0, 14, 2, 59], ['COOK', 0, 2, 1, 10],
    ['DADE', 0, 0, 0, 0], ['DAWSON', 0, 12, 0, 23], ['DOOLY', 0, 0, 0, 0],
    ['ECHOLS', 0, 1, 0, 1], ['ELBERT', 0, 3, 0, 30], ['EVANS', 0, 1, 2, 25],
    ['FRANKLIN', 0, 7, 1, 24], ['GILMER', 0, 17, 2, 63], ['GLASCOCK', 0, 0, 1, 1],
    ['GORDON', 0, 12, 2, 69], ['GREENE', 0, 1, 2, 13], ['HABERSHAM', 0, 17, 1, 26],
['HARALSON', 0, 10, 2, 44], ['HART', 0, 11, 5, 73], ['JEFF DAVIS', 0, 3, 3, 28],
    ['JENKINS', 0, 4, 1, 35], ['JOHNSON', 0, 0, 0, 0], ['LAMAR', 0, 2, 0, 7],
    ['LANIER', 0, 1, 0, 22], ['LEE', 0, 9, 5, 55], ['LIBERTY', 0, 18, 27, 173],
    ['LINCOLN', 0, 1, 1, 21], ['LONG', 0, 3, 1, 16], ['LUMPKIN', 0, 4, 0, 31],
    ['MACON', 0, 0, 2, 9], ['MARION', 0, 0, 2, 2], ['MCDUFFIE', 0, 4, 3, 37],
    ['MCINTOSH', 0, 0, 5, 25], ['MILLER', 0, 0, 0, 0], ['MONROE', 0, 1, 1, 8],
    ['MONTGOMERY', 0, 0, 1, 10], ['MORGAN', 0, 0, 0, 3], ['MURRAY', 0, 2, 0, 31],
['OGLETHORPE', 0, 0, 0, 0], ['PICKENS', 0, 1, 1, 10], ['PIERCE', 0, 8, 1, 26],
    ['PIKE', 0, 5, 1, 16], ['POLK', 0, 17, 12, 72], ['PULASKI', 0, 0, 4, 35],
    ['QUITMAN', 0, 0, 0, 0], ['RABUN', 0, 3, 0, 14], ['SCHLEY', 0, 3, 0, 3],
    ['SCREVEN', 0, 0, 1, 4], ['SEMINOLE', 0, 2, 1, 25], ['STEPHENS', 0, 9, 3, 28],
    ['STEWART', 0, 0, 0, 0], ['TALBOT', 0, 2, 1, 15], ['TALIAFERRO', 0, 0, 0, 0],
    ['TAYLOR', 0, 1, 0, 11], ['TELFAIR', 0, 0, 0, 16], ['TOWNS', 0, 4, 0, 14],
    ['TREUTLEN', 0, 1, 0, 6], ['TURNER', 0, 4, 0, 6], ['TWIGGS', 0, 1, 0, 6],
['UNION', '0', '2', '0', '13'],
['WARREN', '0', '0', '0', '0'],
['WASHINGTON', '0', '0', '1', '8'],
['WEBSTER', '0', '0', '0', '0'],
['WHEELER', '0', '1', '0', '6'],

['WHITE', '0', '3', '0', '5'],
['WILCOX', '0', '2', '1', '9'],
['BARROW', '1', '20', '12', '119'],
['BROOKS', '1', '5', '4', '18'],
['BUTTS', '1', '3', '1', '18'],

['CARROLL', '1', '29', '15', '177'],
['CATOOSA', '1', '19', '6', '65'],
['COLUMBIA', '1', '20', '4', '121'],
['CRAWFORD', '1', '6', '1', '16'],
['EARLY', '1', '1', '1', '81'],

['EFFINGHAM', '1', '14', '2', '36'],
['FANNIN', '1', '9', '0', '32'],
['GRADY', '1', '3', '5', '10'],
['HANCOCK', '1', '2', '1', '6'],
['HARRIS', '1', '3', '0', '8'],

['HEARD', '1', '2', '0', '6'],
['JACKSON', '1', '6', '5', '66'],
['JASPER', '1', '3', '0', '34'],
['JONES', '1', '7', '5', '38'],
['LAURENS', '1', '10', '4', '76'],

['MADISON', '1', '7', '1', '49'],
['OCONEE', '1', '4', '3', '17'],
['PUTNAM', '1', '9', '2', '36'],
['RANDOLPH', '1', '0', '0', '13'],
['TERRELL', '1', '1', '3', '9'],

['THOMAS', '1', '27', '24', '135'],
['WALKER', '1', '18', '3', '122'],
['WHITFIELD', '1', '56', '15', '325'],
['WILKES', '1', '2', '1', '51'],
['WILKINSON', '1', '0', '0', '15'],

['WORTH', '1', '6', '4', '42'],
['CHEROKEE', '2', '60', '14', '213'],
['DODGE', '2', '4', '5', '43'],
['IRWIN', '2', '5', '1', '16'],
['JEFFERSON', '2', '3', '2', '60'],

['MERIWETHER', '2', '7', '1', '51'],
['MITCHELL', '2', '7', '2', '47'],
['PEACH', '2', '7', '7', '78'],
['TATTNALL', '2', '9', '2', '14'],
['TOOMBS', '2', '4', '11', '83'],

['UPSON', '2', '8', '4', '24'],
['WARE', '2', '17', '11', '91'],
['WAYNE', '2', '15', '0', '37'],
['BARTOW', '3', '43', '24', '200'],
['BRANTLEY', '3', '7', '0', '33'],

['CAMDEN', '3', '25', '8', '95'],
['DECATUR', '3', '10', '10', '116'],
['EMANUEL', '3', '1', '5', '22'],
['FAYETTE', '3', '7', '9', '60'],
['FORSYTH', '3', '28', '9', '120'],

['GLYNN', '3', '30', '28', '179'],
['TIFT', '3', '15', '7', '143'],
['BALDWIN', '4', '25', '20', '160'],
['BEN HILL', '4', '13', '4', '135'],
['BULLOCH', '4', '20', '30', '108'],

['CHATHAM', '4', '18', '24', '119'],
['COLQUITT', '4', '14', '14', '107'],
['CRISP', '4', '8', '8', '183'],
['PAULDING', '4', '95', '13', '498'],
['ROCKDALE', '4', '27', '17', '150'],

['CLARKE', '5', '93', '81', '408'],
['COWETA', '6', '89', '25', '855'],
['SUMTER', '6', '10', '15', '187'],
['WALTON', '6', '16', '17', '108'],
['DOUGLAS', '7', '34', '48', '322'],

['FLOYD', '8', '48', '38', '428'],
['HOUSTON', '8', '25', '70', '518'],
['SPALDING', '9', '26', '39', '288'],
['CLAYTON', '10', '14', '49', '170'],
['LOWNDES', '10', '67', '59', '249'],

['HALL', '11', '70', '49', '388'],
['HENRY', '12', '204', '81', '450'],
['NEWTON', '16', '48', '32', '285'],
['DOUGHERTY', '17', '39', '53', '628'],
['COBB', '28', '213', '217', '1198'],

['TROUP', '31', '28', '176', '241'],
['GWINNETT', '35', '430', '437', '1985'],
['MUSCOGEE', '36', '74', '168', '1200'],
['BIBB', '37', '110', '241', '1712'],
['RICHMOND', '44', '108', '159', '878'],

['DEKALB', '117', '294', '1018', '4149'],
['FULTON', '177', '224', '818', '3954'],
]
columns = ['CountyName', 'MurderCount', 'RapeCount', 'RobberyCount', 'AssaultCount']
df = pd.DataFrame(data, columns=columns)
columns = ['County', 'MurderCount', 'RapeCount', 'RobberyCount', 'AssaultCount']
df = pd.DataFrame(data, columns=columns)

# Convert columns to integers for calculations
df[['MurderCount', 'RapeCount', 'RobberyCount', 'AssaultCount']] = df[['MurderCount', 'RapeCount', 'RobberyCount', 'AssaultCount']].astype(int)

# Assign weights: Murder = 4, Rape = 3, Assault = 2, Robbery = 1
weights = {'MurderCount': 4, 'RapeCount': 3, 'RobberyCount': 1, 'AssaultCount': 2}

# Calculate danger score for each county
df['DangerScore'] = (
    df['MurderCount'] * weights['MurderCount'] +
    df['RapeCount'] * weights['RapeCount'] +
    df['RobberyCount'] * weights['RobberyCount'] +
    df['AssaultCount'] * weights['AssaultCount']
)

# Sort by DangerScore in descending order
df = df.sort_values(by='DangerScore', ascending=False)

# Display the top 10 most dangerous counties
print("Top 10 Most Dangerous Counties:")
print(df.head(10))
# path = 'crime_24.csv'
# crime_data = pd.read_csv(path)
# # crime_data.info()
# # crime_data.head()

# crime_data = crime_data.replace('-', pd.NA)

# # Define columns to convert to numeric (skip the first column which is 'County')
# numeric_columns = crime_data.columns[1:]

# # Remove commas and percentage signs, then convert to numeric
# crime_data[numeric_columns] = crime_data[numeric_columns].replace({',': '', '%': ''}, regex=True)
# crime_data[numeric_columns] = crime_data[numeric_columns].apply(pd.to_numeric, errors='coerce')
# #displays counties
# unique_counties = crime_data['County'].unique()

# print(unique_counties[:]) 

# crime_data.info()
# crime_data.head()





