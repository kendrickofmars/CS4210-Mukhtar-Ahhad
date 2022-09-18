#-------------------------------------------------------------------------
# AUTHOR: Ahhad
# FILENAME: CS4210_Assignment1_Mukhtar_Ahhad
# SPECIFICATION: combing through contact_lens.csv and converting labels to numerical values
# FOR: CS 4210- Assignment #1
# TIME SPENT: 6
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH 
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
from sklearn.preprocessing import LabelEncoder #transform labels into data values
import matplotlib.pyplot as plt
import csv
db = [] # will store values of csvfile in row format, skipping the label row
X = [] #converts training features such as age, spectacle prescription, astigmatism, & tear production into 4d array values
Y = [] #vector, aka single-dimensional array
#reading the data in a csv file
with open(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\contact_lens.csv", 'r') as csvfile:
    #when reading in a file, either escape the backslashes or use forward slashes,
    # or convert to raw string by putting 'r' in front of absolute/relative path
    #using with encapsulates prep and cleanup of normal file operations like opening, reading, closing,printing etc
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features to numbers and add to the 4D 
#array X. for instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

transformation_dict = {'Young':1 , 'Prepresbyopic':2, 'Presbyopic': 3, 'Myope': 4, 'Hypermetrope':5,
                       'No':6, 'Yes': 7, 'Reduced':8, 'Normal':9 }
for i,key in enumerate(db): #looping through the array of categorical features and classes
    if key in db == 'Young': #if the value in the rows matches they keys in transformation_dict
        X[0].append(transformation_dict.values(key))#append the value to the 4D array X
    if key in db == 'Prepresbyopic':
        X[0].append(transformation_dict.values(key))
    if key in db == 'Presbyopic':
        X[0].append(transformation_dict.values(key))
    if key in db == 'Myope':
        X[1].append(transformation_dict.values(key))
    if key in db == 'Hypermetrope':
        X[1].append(transformation_dict.values(key))
    if key in db == 'No':
        X[1].append(transformation_dict.values(key)) 
    if key in db == 'Yes':
        X[2].append(transformation_dict.values(key))
    if key in db == 'Reduced':
        X[2].append(transformation_dict.values(key))
    if key in db == 'Normal':
        X[2].append(transformation_dict.values(key)) 
# we input values 0-3 for each subarray, so we can append different values depending on the key
#X = [[1,1,1,1,2,2,2,3,3,3],[4,4,4,4,4,4,4,4,5,5],[6,6,6,6,7,7,7,7,7,7],[8,8,8,8,8,8,9,9,9,9]]    



    
#transform the original categorical training classes to numbers and add to the 
#vector Y. for instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
Y = [] 
transformation_dict_2 = {"Yes":1, "No":2}
for j, key in enumerate(db):
    if key == 'Yes':
        Y.append(transformation_dict_2.values(key))
    if key == 'No':
        Y.append(transformation_dict_2.values(key))

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)
#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], 
class_names=['Yes','No'], filled=True, rounded=True)
plt.show()




#labelEncoder = LabelEncoder() # an instance of labelencoder 
#csvfile["Age_2"] = labelEncoder.fit_transform(csvfile["Age"]) #assignment of numerical values &
#storing it in another column called "Column"
#csvfile  #display the dataframe
#feature categories are Age, Spectacle Prescription, Astigmatism(binary), Tear Production
#csvfile["Age"] = csvfile["Age"].astype('category')
#csvfile.dtypes
#csvfile["Age"] = csvfile["Age"].cat.codes
#csvfile