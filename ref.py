import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split


from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score 

# ### The movie review dataset
import cloudpickle as picklerick
from urllib.request import urlopen
dataset = picklerick.load(urlopen("https://drive.google.com/uc?export=download&id=1tqjekAEy_SM_sJUvjIBbajp6I-_WmHgj"))
print(dataset.keys())


print(len(dataset.target[:]))


from sklearn.model_selection import train_test_split
docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=123)
# print(size(y_train))
# print(size(y_test))
# print(docs_train[0])
# print(y_train[0])

# Task 1 
# ---
# Use TfidfVectorizer to fit_transform the training data (docs_train) and then transform the test data (docs_test)

from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
train_fit = vec.fit_transform(docs_train)
test_tran = vec.transform(docs_test)

print(train_fit.shape, test_tran.shape)

# Task 2 
# ---
# Build a SVC model to predict whether a movie review is positive or negative. Test the model accuracy on the test data. Try different values (0.01, 0.1, 1, 10) for the hyper parameter 'C' and print out the model accuracy for each of the parameter value.

from sklearn.svm import SVC
X = train_fit
y = y_train
for c in [0.01, 0.1, 1, 10, 30, 500]:
    model = SVC(kernel='linear', C=c)
    model.fit(X,y)
    y_pred = model.predict(test_tran)
    print(accuracy_score(y_test, y_pred))

# Task 3
# ---
# Naive Bayes is a prediction model based on applying Bayes’ theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable.
# 
# Build a Naive Bayes model to predict whether a movie review is positive or negative. Test the model accuracy on the test data.

from sklearn.naive_bayes import MultinomialNB as MNB

bobbyBayes = MNB().fit(X,y)
b_predict = bobbyBayes.predict(test_tran)

# for review, classification in zip(docs_test, b_predict):
#     print(f"Prediction: {dataset.target_names[classification]}Review:\n{review}\n")
print(accuracy_score(y_test, b_predict))

# Task 4
# ---
# A random forest is a ensemble (collective) model that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
# 
# Build a random forest model to predict whether a movie review is positive or negative. Test the model accuracy on the test data. Try different values (20, 100, 500) for the hyper parameter 'n_estimators', i.e., the number of decision trees in the ensemble, and print out the model accuracy for each of the parameter value.

from sklearn.ensemble import RandomForestClassifier

for num in (20, 100, 500, 1000):
    
    rfc = RandomForestClassifier(n_estimators=num)
    rfc = rfc.fit(X,y)
    rf_pred = rfc.predict(test_tran)
    print(accuracy_score(y_test, rf_pred))

# ### From the above tasks, you can observe that different models and different choice of hyper-parameter values can lead to quite different prediction performance. What is the model (and hyper-parameter) among the above that gives the best prediction? What is the worst?
# It would appear that the normal SVC using the linear kernel with any C>10 yeilds the most accurate model for the feature extraction method we used (TfidfVectorizer). Interestingly Naive Bayes got very close without the testing a tuning and was near instantaneous to compute on a dataset this small. I tried RandomForestClassifier with n_estimators=100000 and there was no change at all from 1000 trees. 
