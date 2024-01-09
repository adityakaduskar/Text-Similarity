from flask import Flask, request, jsonify

app = Flask(__name__)


def preprocess_text(text):
  # Convert text to lowercase to ensure case-insensitive comparison
  text = text.lower()
  # Remove non-alphanumeric characters and split the text into words
  words = [word for word in text.split() if word.isalnum()]
  return set(words)


def calculate_jaccard_similarity(text1, text2):
  # Pre-process the text
  words1 = preprocess_text(text1)
  words2 = preprocess_text(text2)

  # Calculate the intersection of the two sets
  intersection = len(words1.intersection(words2))
  union = len(words1.union(words2))

  #  Calculate the Jaccard similarity
  similarity = intersection / union if union != 0 else 0
  return similarity


@app.route('/compare', methods=['POST'])
def compare_texts():
  try:
    # Get the text inputs from the request
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']

    if not text1 or not text2:
      return jsonify({'error': 'Both text1 and text2 are required'}), 400

    #
    similarity_score = calculate_jaccard_similarity(text1, text2)

    response_data = {
        # 'text1': text1,
        # 'text2': text2,
        'similarity': similarity_score
    }

    return jsonify(response_data)

  except Exception as e:
    return jsonify({'error': f'Something went wrong: {str(e)}'}), 500


if __name__ == "__main__":
  app.run(debug=True)
