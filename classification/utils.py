# import pickle
# import dill
# from sklearn.feature_extraction.text import TfidfVectorizer
# #from . import vectorizer_rename as vector

# def clean_url(url):
#     prefixes = ['http://www.', 'https://www.', 'www.']
#     for prefix in prefixes:
#         if url.startswith(prefix):
#             url = url.replace(prefix, '')
#             break
#     return url


# # Define the makeTokens function
# def makeTokens(f):
#     tkns_BySlash = str(f.encode('utf-8')).split('/')    # make tokens after splitting by slash
#     total_Tokens = []
#     for i in tkns_BySlash:
#         tokens = str(i).split('-')    # make tokens after splitting by dash
#         tkns_ByDot = []
#         for j in range(0, len(tokens)):
#             temp_Tokens = str(tokens[j]).split('.')    # make tokens after splitting by dot
#             tkns_ByDot = tkns_ByDot + temp_Tokens
#         total_Tokens = total_Tokens + tokens + tkns_ByDot
#     total_Tokens = list(set(total_Tokens))    # remove redundant tokens
#     if 'com' in total_Tokens:
#         total_Tokens.remove('com')    # removing .com since it occurs a lot of times and it should not be included in our features
#     return total_Tokens

# # Initialize TfidfVectorizer with custom tokenizer
# vectorizer = TfidfVectorizer(tokenizer=makeTokens)

# with open('vectorizer_dill.pkl', 'wb') as file:
#     dill.dump(vectorizer, file)


# def load_model_and_vectorizer():
#     with open('logit_model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     with open('vectorizer_dill.pkl', 'rb') as file:
#         vectorizer = dill.load(file)
#     return model, vectorizer

# def predict_url_category(url, model,vectorizer):
       
#     prediction = model.predict(vectorizer.transform(url))
#     if prediction == 'good':
#         return 'The URL is safe'
#     else:
#         return "URL APPEARS TO BE MALICIOUS"



import dill
from sklearn.feature_extraction.text import TfidfVectorizer
#from . import vectorizer_rename as vector

def clean_url(url):
    prefixes = ['http://www.', 'https://www.', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, '')
            break
    return url


# Define the makeTokens function
def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')    # make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')    # make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0, len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')    # make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))    # remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')    # removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens

# Initialize TfidfVectorizer with custom tokenizer
vectorizer = TfidfVectorizer(tokenizer=makeTokens)




def load_model_and_vectorizer():
    with open('logit_model.pkl', 'rb') as file:
        model = dill.load(file)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = dill.load(f)
    return model, vectorizer

def predict_url_category(url, model,vectorizer):
       
    prediction = model.predict(vectorizer.transform(url))
    if prediction == 'good':
        return 'The URL is safe'
    else:
        return "URL APPEARS TO BE MALICIOUS"




