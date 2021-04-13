# ElasticsearchLambda
AWS Lambda functions which serve/update Elasticsearch data

## Guide
```bash
git clone https://github.com/Fox520/ElasticsearchLambda
cd ElasticsearchLambda
python3 -m pip install pipenv
pipenv shell
pip install -r requirements.txt
```
Open `app.py` and set the variables accordingly

Create `~/.aws/credentials` and place the following
```python
[default]
aws_access_key_id = "REPLACE"
aws_secret_access_key = "REPLACE"
```

#### Deploy the API
```bash
pipenv shell
zappa init
zappa deploy dev
```

> gg to https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html for the policy
