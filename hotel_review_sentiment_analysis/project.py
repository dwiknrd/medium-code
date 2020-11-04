import pandas as pd 
import matplotlib.pyplot as plt

# Apply first level cleaning
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score, precision_score, recall_score
###############################################################

#Load the file
train_df = pd.read_csv("train.csv")

### Checking Missing values in the Data Set and printing the Percentage for Missing Values for Each Columns ###

count = train_df.isnull().sum().sort_values(ascending=False)
percentage = ((train_df.isnull().sum()/len(train_df)*100)).sort_values(ascending=False)
missing_data = pd.concat([count, percentage], axis=1,
keys=['Count','Percentage'])

print('Count and percentage of missing values for the columns:')

missing_data

plt.figure(figsize=(12,6))
plt.title("Percentage Distributions by Review Type")
g = plt.pie(round(train_df.Is_Response.value_counts(normalize=True)*100,2),explode=(0.025,0.025), labels=round(train_df.Is_Response.value_counts(normalize=True)*100,2).index, colors=["c","m"],autopct="%1.1f%%", startangle=180)
plt.show()

#Removing columns
train_df.drop(columns = ['User_ID', 'Browser_Used', 'Device_Used'], inplace = True)

#This function converts to lower-case, removes square bracket, removes numbers and punctuation
def text_clean_1(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Apply a second round of cleaning
def text_clean_2(text):
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

def decontract_text(text):
    """
    Decontract text
    """
    # specific
    text = re.sub(r"won\'t", "will not", text)
    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"won\’t", "will not", text)
    text = re.sub(r"can\’t", "can not", text)
    text = re.sub(r"\'t've", " not have", text)
    text = re.sub(r"\'d've", " would have", text)
    text = re.sub(r"\'clock", "f the clock", text)
    text = re.sub(r"\'cause", " because", text)

    # general
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)

    text = re.sub(r"n\’t", " not", text)
    text = re.sub(r"\’re", " are", text)
    text = re.sub(r"\’s", " is", text)
    text = re.sub(r"\’d", " would", text)
    text = re.sub(r"\’ll", " will", text)
    text = re.sub(r"\’t", " not", text)
    text = re.sub(r"\’ve", " have", text)
    text = re.sub(r"\’m", " am", text)
    
    return text

train_df['cleaned_description'] = train_df['Description'].apply(lambda x: decontract_text(x))
train_df['cleaned_description'] = train_df['cleaned_description'].apply(lambda x: text_clean_1(x))
train_df['cleaned_description'] = train_df['cleaned_description'].apply(lambda x: text_clean_2(x))

from sklearn.model_selection import train_test_split

x, y = train_df['cleaned_description'], train_df['Is_Response']

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=0.1,
                                                    random_state=42)

print(f'x_train: {len(x_train)}')
print(f'x_test: {len(x_test)}')
print(f'y_train: {len(y_train)}')
print(f'y_test: {len(y_test)}')

tvec = TfidfVectorizer()
clf2 = LogisticRegression(solver = "lbfgs")

model = Pipeline([('vectorizer',tvec),('classifier',clf2)])
model.fit(iv_train, dv_train)

predictions = model.predict(iv_test)
confusion_matrix(predictions, dv_test)

y_pred = model.predict(x_test)

print(f'Accurcy: {accuracy_score(y_pred, y_test)}')
print(f'Precision: {precision_score(y_pred, y_test, average="weighted")}')
print(f'Recall: {recall_score(y_pred, y_test, average="weighted")}')

