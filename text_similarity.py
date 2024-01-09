def preprocess_text(text):
    # Convert text to lowercase to ensure case-insensitive comparison
    text = text.lower().replace("'","")

    # Remove non-alphanumeric characters and split the text into words
    words = [word for word in text.split() if word.isalnum()]
    return set(words)

def calculate_jaccard_similarity(text1, text2):
    # Tokenize the input texts into words
    words1 = preprocess_text(text1)
    #print(words1)
    words2 = preprocess_text(text2)
    #print(words2)

    # Calculate the intersection and union of the sets
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))

    # Calculate the Jaccard similarity coefficient
    similarity = intersection / union if union != 0 else 0

    return similarity

def main():
    # Get input texts from the user
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    # Calculate and print the Jaccard similarity
    similarity_score = calculate_jaccard_similarity(text1, text2)
    print(f"Jaccard Similarity: {similarity_score}")

if __name__ == "__main__":
    main()