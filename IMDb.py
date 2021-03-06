import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


imdb_df  = pd.read_csv('C:\\Users\\benfi\\Documents\\Pycharm\\imdb_top_1000.csv')
imdb_df.head()
imdb_df.tail()
imdb_df.shape
imdb_df.info()

imdb_df = imdb_df.rename(columns={"Series_Title": "Movies_Title"})

imdb_df.columns
imdb_df.dtypes



#3 numeric values when there should be 5 (Gross and RunTime as strings need to be converted to floats)

imdb_df['Gross'] = imdb_df['Gross'].str.replace(',', '').astype('float')
imdb_df['Runtime'] = imdb_df['Runtime'].apply(lambda text: text.split()[0]).astype('int')

imdb_df.info()


#Count Missing Values in Each Column
imdb_df.isnull().sum()


#Replace Missing Values

imdb_df['Certificate'] = imdb_df['Certificate'].replace(np.nan, 'Unknown')
imdb_df['Meta_score'] = imdb_df['Meta_score'].replace(np.nan, np.mean(imdb_df['Meta_score']))
imdb_df['Gross'] = imdb_df['Gross'].replace(np.nan, np.mean(imdb_df['Gross']))

imdb_df.isnull().sum()
#Check if any 0 value in any columns
imdb_df['Poster_Link'].isnull().sum()


#Drop Irrelevent Columns (Poster Link, Overview)

imdb_df.columns

imdb_df2=imdb_df.drop(['Poster_Link', 'Overview'], axis = 1)

imdb_df2.describe()

imdb_df2.columns
imdb_df2.shape

#Sample Shawshank
imdb_df2.iloc[0]


#Sort by gross

gross_df = imdb_df2.sort_values(["Gross"], ascending=False)
gross_df.head()

#Top 5 Grossing
top_gross = imdb_df2.sort_values(['Gross'], ascending = False)

fig,ax=plt.subplots(figsize=(15,5))
ax.set(facecolor = 'Black')
sns.barplot(x=top_gross['Movies_Title'][:5], y=top_gross['Gross'][:5], palette = 'hls')
plt.title('5 Highest Grossing Movies', fontweight = 'bold', fontsize = 15)
plt.xlabel('Movies', fontsize = 10, fontweight = 'bold')
plt.ylabel('Gross', fontsize = 10, fontweight = 'bold')


#Subsetting IMDB 9 or Greater

rating9_df=imdb_df2[imdb_df2["IMDB_Rating"]>8.99]
rating9_df[["Movies_Title", "IMDB_Rating"]]

#Check Correlation between Gross Revenue and IMDb Rating
imdb_df2.corr()

## Top 5 voted movies

top_voted = imdb_df2.sort_values(['No_of_Votes'], ascending = False)

fig,ax=plt.subplots(figsize=(15,5))
ax.set(facecolor = 'Black')
sns.barplot(x=top_voted['Movies_Title'][:5], y=top_voted['No_of_Votes'][:5], palette = 'hls')
plt.title('5 Top Voted Movies', fontweight = 'bold', fontsize = 15)
plt.xlabel('Movies', fontsize = 10, fontweight = 'bold')
plt.ylabel('Votes', fontsize = 10, fontweight = 'bold')




###Certificate

imdb_df2.Certificate.value_counts()

#Drop Unknown, and anything with less than 4

Certificate_names= ['U', 'A', 'UA', 'R', 'PG-13',
     'PG', 'Passed']
Certificate_Size=[234,197,175,146,43,37,34]



fig1, ax1 = plt.subplots()
ax1.pie(Certificate_Size,  labels=Certificate_names, autopct='%1.1f%%',
      shadow=True, startangle=90)
ax1.axis('equal')



#Movies Released By Year

imdb_df2.Released_Year.value_counts().head()

fig,ax = plt.subplots(figsize=(30,7))
ax.set(facecolor = 'black')
sns.countplot(x=imdb_df2['Released_Year'], order = imdb_df2['Released_Year'].value_counts().index,palette='hls' )
plt.xticks(rotation = 90)
plt.xlabel('Movies', fontsize= 10, fontweight = 'bold')
plt.ylabel('Years', fontsize= 10, fontweight = 'bold')
plt.title('Movies by Year', fontsize = 15, fontweight = 'bold')




#Movies Runtime

print(imdb_df2['Runtime'].mean())

fig,axs=plt.subplots(figsize=(20,5))
g=sns.kdeplot(imdb_df2['Runtime'])
g.set_title("Time Duration of movies", weight = "bold")

plt.show()
