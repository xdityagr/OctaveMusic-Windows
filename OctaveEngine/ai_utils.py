import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from concurrent.futures import ThreadPoolExecutor

class StringProcessor:

    # Efficient preprocessing function using regex and lowercasing in one step
    def _preprocess_text(self, text):
        return re.sub(r'[^a-z0-9\s]', '', text.lower())  # Combine to a single line

    # Preprocess multiple texts in parallel
    def _preprocess_texts(self, texts):
        with ThreadPoolExecutor() as executor:
            return list(executor.map(self._preprocess_text, texts))  # Use parallel processing

    
    def compute_similarity(self, pattern, candidates, threshold=0.75):

        """Computes similarity between pattern & candidates using TF-IDF algorithm.

        Returns:
            (index of candidate, similarity_score, surpasses_threshold)
            similarity_score: Ranges from 0 to 1, where closer to 1, means highly similar string.
            suprasses_threshold : True/False depending on if the score surpasses the given threshold.
        """
        # Preprocess pattern and candidates list in parallel
        candidates = self._preprocess_texts(candidates)
        pattern = self._preprocess_text(pattern)
        
        if not candidates or not pattern:
            print('HEREEEEEEEEEEEEEEEEEEEEEEEEEEE')
            return [(i, 0.0, False) for i in range(len(candidates))]
    
        # Create a combined list for TF-IDF vectorization
        documents = [pattern] + candidates
        
        try: 

            # Efficiently initialize and fit the TF-IDF vectorizer
            vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
            tfidf_matrix = vectorizer.fit_transform(documents)  
            
            # Compute cosine similarities between the patern and all candidate documents
            cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
            
            # Return similarity scores along with corresponding indices
        

            return [(i, cosine_similarities[0][i], cosine_similarities[0][i] > threshold) for i in range(len(candidates))]
        
        except Exception as e:
            print(f"Error in TF-IDF computation: {e}")
            return [(i, 0.0, False) for i in range(len(candidates))]

def objectify(object, iterable):
    return [object(item) for item in iterable]



# print(sorted(thumbnails))
# Example usage:
# string_processor = StringProcessor()
# search_query = " blinding lights "
# found_queries = [
#     "blinding lights by the weeknd", "the hills by the weeknd", "miss you by the weeknd", "starboy, the weeknd"
# ]

# similarity_scores = string_processor.compute_similarity(search_query, found_queries)
# print(similarity_scores)
# for index, score, surpasses_threshold in similarity_scores:
#     print(f"Found index {index} with similarity score: {score:.4f} -> Surpasses threshold : {surpasses_threshold}")

# """
# Found index 0 with similarity score: 0.7129
# Found index 1 with similarity score: 0.0000
# Found index 2 with similarity score: 0.0000
# Found index 3 with similarity score: 0.0000
# Found index 4 with similarity score: 0.0000
# Found index 5 with similarity score: 0.0000

# """