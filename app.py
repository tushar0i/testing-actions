from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'message': "Hello from CI/CD 1st",
        'status': 'success'
    }
    return jsonify(data)    

if __name__ == '__main__':
    print("server is runnig on port 8900")
    app.run(host="0.0.0.0", port=8900) 
