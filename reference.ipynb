{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "-0L9szp3VfNZ"
   },
   "source": [
    "Homework 2\n",
    "---\n",
    "**Due Nov. 26 (Tue) by end of the day.**\n",
    "\n",
    "Do all your work on this notebook. Submit your homework by uploading the notebook file to moodle. Your submission notebook should contain:\n",
    "\n",
    "- Code\n",
    "- Output from running your code (printouts)\n",
    "- Answer to any questions or any comments (type in a markdown cell)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "Populating the interactive namespace from numpy and matplotlib\n"
    }
   ],
   "source": [
    "%pylab inline\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "from sklearn.datasets import load_files\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.metrics import accuracy_score, f1_score "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "-d0fGTrQVfNp"
   },
   "source": [
    "### The movie review dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "dict_keys(['data', 'filenames', 'target_names', 'target', 'DESCR'])\n"
    }
   ],
   "source": [
    "import cloudpickle as picklerick\n",
    "from urllib.request import urlopen\n",
    "dataset = picklerick.load(urlopen(\"https://drive.google.com/uc?export=download&id=1tqjekAEy_SM_sJUvjIBbajp6I-_WmHgj\"))\n",
    "print(dataset.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "2000\n"
    }
   ],
   "source": [
    "print(len(dataset.target[:]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "docs_train, docs_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.25, random_state=123)\n",
    "# print(size(y_train))\n",
    "# print(size(y_test))\n",
    "# print(docs_train[0])\n",
    "# print(y_train[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "4lmI2mFaVfNu"
   },
   "source": [
    "Task 1 \n",
    "---\n",
    "Use TfidfVectorizer to fit_transform the training data (docs_train) and then transform the test data (docs_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "(1500, 35329) (500, 35329)\n"
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "vec = TfidfVectorizer()\n",
    "train_fit = vec.fit_transform(docs_train)\n",
    "test_tran = vec.transform(docs_test)\n",
    "\n",
    "print(train_fit.shape, test_tran.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "-vdPNYZWVfNz"
   },
   "source": [
    "Task 2 \n",
    "---\n",
    "Build a SVC model to predict whether a movie review is positive or negative. Test the model accuracy on the test data. Try different values (0.01, 0.1, 1, 10) for the hyper parameter 'C' and print out the model accuracy for each of the parameter value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "0.492\n0.524\n0.838\n0.846\n0.846\n0.846\n"
    }
   ],
   "source": [
    "from sklearn.svm import SVC\n",
    "X = train_fit\n",
    "y = y_train\n",
    "for c in [0.01, 0.1, 1, 10, 30, 500]:\n",
    "    model = SVC(kernel='linear', C=c)\n",
    "    model.fit(X,y)\n",
    "    y_pred = model.predict(test_tran)\n",
    "    print(accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "WHc9S4QTVfN2"
   },
   "source": [
    "Task 3\n",
    "---\n",
    "Naive Bayes is a prediction model based on applying Bayes’ theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable.\n",
    "\n",
    "Build a Naive Bayes model to predict whether a movie review is positive or negative. Test the model accuracy on the test data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "0.8\n"
    }
   ],
   "source": [
    "from sklearn.naive_bayes import MultinomialNB as MNB\n",
    "\n",
    "bobbyBayes = MNB().fit(X,y)\n",
    "b_predict = bobbyBayes.predict(test_tran)\n",
    "\n",
    "# for review, classification in zip(docs_test, b_predict):\n",
    "#     print(f\"Prediction: {dataset.target_names[classification]}Review:\\n{review}\\n\")\n",
    "print(accuracy_score(y_test, b_predict))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "0OC9jLH7VfN4"
   },
   "source": [
    "Task 4\n",
    "---\n",
    "A random forest is a ensemble (collective) model that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.\n",
    "\n",
    "Build a random forest model to predict whether a movie review is positive or negative. Test the model accuracy on the test data. Try different values (20, 100, 500) for the hyper parameter 'n_estimators', i.e., the number of decision trees in the ensemble, and print out the model accuracy for each of the parameter value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "0.696\n0.76\n0.796\n0.782\n"
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "for num in (20, 100, 500, 1000):\n",
    "    \n",
    "    rfc = RandomForestClassifier(n_estimators=num)\n",
    "    rfc = rfc.fit(X,y)\n",
    "    rf_pred = rfc.predict(test_tran)\n",
    "    print(accuracy_score(y_test, rf_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "huHnUxFZVfN7"
   },
   "source": [
    "### From the above tasks, you can observe that different models and different choice of hyper-parameter values can lead to quite different prediction performance. What is the model (and hyper-parameter) among the above that gives the best prediction? What is the worst?"
   ]
  },
  {
   "cell_type": "markdown",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-10-c11fcff059b0>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-c11fcff059b0>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    It would appear that the normal SVC using the linear kernel with any C>10 yeilds the most accurate model for the feature extraction method we used (TfidfVectorizer). Interestingly Naive Bayes got very close without the testing a tuning and was near instantaneous to compute on a dataset this small. I tried RandomForestClassifier with n_estimators=100000 and there was no change at all from 1000 trees.\u001b[0m\n\u001b[0m           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "It would appear that the normal SVC using the linear kernel with any C>10 yeilds the most accurate model for the feature extraction method we used (TfidfVectorizer). Interestingly Naive Bayes got very close without the testing a tuning and was near instantaneous to compute on a dataset this small. I tried RandomForestClassifier with n_estimators=100000 and there was no change at all from 1000 trees. "
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "colab": {
   "collapsed_sections": [],
   "name": "Homework2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}