---

### 🧩 **rest_api_example/app.py**
```python
from flask import Flask, request, jsonify
from data_pipeline_simulation import process_data

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest_data():
    data = request.get_json()
    result = process_data(data)
    return jsonify({"status": "success", "processed_data": result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
