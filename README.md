# Text-Similarity
An app that compares the similarity between two input texts.

## To run the standalone script
```
python text_similarity.py
```
## To run the Flask app
### Install requirements
```
pip install -r requirements.txt
```
### Run the Flask app script
```
python main.py
```
### Edit the script of the request with the text documents to be compared
```python
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
### Run the script with the request to your Flask app
```
python request.py
```
