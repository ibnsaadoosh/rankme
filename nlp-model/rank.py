import textract
from os import listdir
from os.path import isfile, join
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import sys

# load the pretrained model
sbert_model = SentenceTransformer('/home/saad/Documents/work/faculty/fourth-year/graduation-project/our-work/project/second-term/rankme-server/nlp-model/paraphrase-mpnet-base-v2')


description = sys.argv[1]
resumes = sys.argv[2].split(',')

target_docs = []

def read_All_CV(filename):
    text = textract.process(filename)
    return text.decode('utf-8')

for cv in resumes:
    temp = '/home/saad/Documents/work/faculty/fourth-year/graduation-project/our-work/project/second-term/rankme-server/public/resumes/'
    text = read_All_CV(temp + cv)
    target_docs.append(text)

description_vec = sbert_model.encode(description)
results = []
for i in range(len(target_docs)):
  #Vectorize using Word2Vec
  target_vec = sbert_model.encode(target_docs[i])
  #calculating similarity using cosine similarity
  sim_score = cosine_similarity([description_vec], [target_vec])
  score = str(sim_score[0][0]);
  results.append({"score": score, "filename": resumes[i]})
  # Sort results by score in desc order
# results.sort(key=lambda k: k["percentage"], reverse=True)
print(json.dumps(results))