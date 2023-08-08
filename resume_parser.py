# Make sure you have NLTK installed. If not, run: !pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define the required skills for the job
required_skills = "python machine learning data analysis communication"

# Sample candidate resumes
candidates = {
    "Candidate 1": "Experienced data analyst with expertise in Python and machine learning. Strong communication skills.",
    "Candidate 2": "Software engineer with a background in Java and C++. Limited experience in data analysis.",
    "Candidate 3": "Data scientist with advanced knowledge of Python, R, and statistical analysis. Good communication skills.",
}

# Preprocess required skills
required_skills = word_tokenize(required_skills.lower())
required_skills = [word for word in required_skills if word.isalpha()]

# Preprocess and tokenize candidate resumes
candidate_tokens = {}
for candidate, resume in candidates.items():
    tokens = word_tokenize(resume.lower())
    tokens = [word for word in tokens if word.isalpha()]
    candidate_tokens[candidate] = tokens

# Calculate the similarity score for each candidate
def calculate_similarity(required_skills, candidate_skills):
    overlap = set(required_skills) & set(candidate_skills)
    similarity = len(overlap) / len(required_skills)
    return similarity

# Find the best candidate based on similarity
best_candidate = None
best_similarity = 0.0

for candidate, skills in candidate_tokens.items():
    similarity = calculate_similarity(required_skills, skills)
    if similarity > best_similarity:
        best_similarity = similarity
        best_candidate = candidate

print("Best candidate:", best_candidate)
print("Similarity score:", best_similarity)
