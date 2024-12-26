from collections import Counter
from typing import List, Tuple
import re

def find_top_k_frequent_words(text: str, k: int) -> List[Tuple[str, int]]:
    """
    Find the k most frequent words in a text string.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Using regex to split into words
    words = [word for word in re.split(r'\W+', text) if word]
    print(f"words : {words}")
    
    # Count word frequencies using Counter
    word_counts = Counter(words)
    
    # Get the k most common words
    top_k = word_counts.most_common(k)
    
    return top_k


if __name__ == "__main__":

    text = "Hello world! Hello everyone. This is a simple test. Test, test, hello."
    k = 2
    
    result = find_top_k_frequent_words(text, k)
    print(result)
