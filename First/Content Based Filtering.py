import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer #순수하게 단어의 수를 계산
from sklearn.metrics.pairwise import cosine_similarity

from ast import literal_eval #str -> list or dict로 변경


#줄거리 기반 추천
#Tfidif vector and count vectorizer 활용
#코사인 유사도 활용


#TF_IDF

def Tf_idf(x):
    tfidf_matrix = tfidf.fit_transform(df2['x])
    tfidf_matrix.shape

#cosine -similarity

def consine1(x,y):
    cosine_sim = linear_kernel(x, y)
    test_sim_scores = sorted(test_sim_scores, key=lambda x: x[1], reverse=True) # 코사인 유사도 기준으로 내림차순 정렬


# 영화의 제목을 입력받으면 코사인 유사도를 통해서 가장 유사도가 높은 상위 10개의 영화 목록 반환
def get_recommendations(title, cosine_sim=cosine_sim):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = indices[title]
    
    # 코사인 유사도 매트릭스 (cosine_sim) 에서 idx 에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    
    # 인덱스 정보를 통해 영화 제목 추출
    return df2['title'].iloc[movie_indices]

def get_second(x):
    return x[1]

lst = ['인덱스', '유사도']

def incdices1(x):
    # 추천 영화 목록 10개의 인덱스 정보 추출
test_movie_indices = [i[0] for i in x[1:11]]


#다양한 요소 기반 추천

def features1(x):
    for feature in x:
    df2[feature] = df2[feature].apply(literal_eval)

def features2(x):
    for feature in features:
        df2[feature] = df2[feature].apply(clean_data)

# 감독 정보를 추출(감독의 이름만으로도 영화를 선택하는 경우도 있다)
def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

#줄거리 정보 전처리
def clean_data(x): #소문자로 바꾸고 띄워쓰기가 된 것은 붙이기
    if isinstance(x, list):
        return [str.lower( i.replace(' ', '')) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(' ', ''))
        else:
            return ''

def create_soup(x): #모든 컬럼을 한 줄로 표현(단어 하나하나가 의미를 가진다)
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])



