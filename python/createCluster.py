import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
from df2gspread import df2gspread as d2g
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Track Covid-19").sheet1

# Extract and print all of the values
df = sheet.get_all_records()											
columns = ['Timestamp', 'Contact Number','Address','Latitude','Longitude','Date','Time','Comments','Cluster','Coordinates','Status']

sheetSet = pd.DataFrame(df, columns=columns)
sheetSet= sheetSet.head(11)
print(sheetSet)
#Remove all cells with null values
sheetSet.dropna(axis=0,how='any',subset=['Timestamp', 'Contact Number','Address','Latitude','Longitude','Date','Time','Comments','Cluster','Coordinates','Status'],inplace=True)
# Select only 2 columns from dataFrame and create a new subset DataFrame
X = sheetSet.loc[:, ['Contact Number','Latitude','Longitude','Status']] 
# sheetSet.dropna(axis=0,how='any',subset=['Latitude','Longitude'],inplace=True)
# X= sheetSet[['Contact Number','Address','latitude','longitude']]
X= X.head(11)
print(X)

K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = sheetSet[['Latitude']]
X_axis = sheetSet[['Longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
# Visualize
plt.plot(K_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

kmeans = KMeans(n_clusters = 4 , init ='k-means++')
kmeans.fit(X[X.columns[1:3]]) # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]]) # Labels of each point
X.head(11)
print(X)

X.plot.scatter(x = 'Latitude', y = 'Longitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

#X = X.groupby('cluster_label')[['cluster_label']]

#Leaving this ..just see how to serialize the object into json #
#for i in range(sheet.row_count-1):
#    sheet.update_cell(i+2, 9, X['cluster_label'][i])

cluster_Labels = X.sort_values(by ='cluster_label').cluster_label.unique().tolist()

for i in cluster_Labels: 
    {
         print(i)
         
    }


X = X[['Contact Number','Status','cluster_label']]
clustered_data = sheetSet.merge(X, left_on='Contact Number', right_on='Contact Number')
clustered_data.head(11)
print(clustered_data)

casesCluster = X.groupby('cluster_label')
print(casesCluster.groups)
print(casesCluster.size().reset_index(name='count'))
#.size().reset_index(name='count')
cluster_infected_cases = []
cluster_suspected_cases = []
for case, group in casesCluster:
  print(case)
  #print(group)
  statusCluster = group.groupby('Status')["Contact Number"].count()
  print(statusCluster)
  infected_count = statusCluster['Infected']
  cluster_infected_cases.append(infected_count)
  suspected_count = statusCluster['Suspected']
  cluster_suspected_cases.append(suspected_count)
         
print(cluster_infected_cases)
print(cluster_suspected_cases)

clusterColumns = ['cluster_label', 'cluster_center_coordinates','cluster_infected_cases','cluster_suspected_cases']

clusterSet = pd.DataFrame(list(zip(cluster_Labels, centers,cluster_infected_cases,cluster_suspected_cases)), 
               columns =clusterColumns) 
#clusterSet["cluster_label"].fillna(" ", inplace = True) 
#clusterSet["cluster_center_coordinates"].fillna(" ", inplace = True)
#lusterSet["cluster_infected_cases"].fillna(" ", inplace = True)
#clusterSet["cluster_suspected_cases"].fillna(" ", inplace = True)
print(clusterSet)

d2g.upload(clusterSet, '1jRfthUvnAiP4d9OzF6B7ZKyOLgg2cGNXygvy7dLS6Ow', wks_name='Cluster_Covid_19', credentials=creds, row_names=True)

