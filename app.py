import json
import requests
from flask import Flask, request
from aws_requests_auth.aws_auth import AWSRequestsAuth

app = Flask(__name__)

# Keys are same as those used by Zappa
aws_access_key_id = ''
aws_secret_access_key = ''
es_host = ''
region = 'us-east-2'
index = 'sports'

auth = AWSRequestsAuth(aws_access_key=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key,
                       aws_host=es_host,
                       aws_region=region,
                       aws_service='es')


url = f'https://{es_host}/' + index + '/_search'


@app.route("/")
def root():
    search_term = request.args.get("q", None)
    if search_term is None:
        return {}
    # Example: fo will match Football and Formula One because of *
    query = {
        "size": 25,
        "query": {
            "wildcard": {
                "name": f"{search_term}*"
            }
        }
    }
    # Make the signed HTTP request
    r = requests.get(url, headers={"content-type": "application/json"}, auth=auth, data=json.dumps(query))

    return json.dumps(r.text)


if __name__ == "__main__":
    app.run(debug=True)
