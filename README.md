# Text-Similarity
An app that compares the similarity between two input texts. I have used the Jaccard similarity coefficient to implement the similarity metric.

## To run the standalone script :
```
python text_similarity.py
```
## To run the Flask app :
### 1) Install requirements.
```
pip install -r requirements.txt
```
### 2) Run the Flask app script.
```
python main.py
```
### 3) Edit the script of the request to your Flask app (request.py) with the text documents to be compared.
```Python
import requests

# Enter or edit the URL of your flask app
url = "http://127.0.0.1:5000/compare"
data = {
    "text1": "Enter the first text document here.",
    "text2": "Enter the second text document here."
}

response = requests.post(url, json=data)

print(response.json())
```
### 4) Run the script with the request to your Flask app (request.py).
```
python request.py
```
