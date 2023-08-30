import requests, uuid, json, os

# import azure.cognitiveservices.translator as translator

# Add your key and endpoint

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

os.environ['TRANSLATOR_TEXT_SUBSCRIPTION_KEY'] = "0615a14f92e444aab800e922b8d07ea2"
os.environ['TRANSLATOR_TEXT_ENDPOINT'] = "https://api.cognitive.microsofttranslator.com/"
os.environ['TRANSLATOR_TEXT_REGION'] = "eastus"

# TRANSLATOR_TEXT_REGION = "<eastus>"

TRANSLATOR_TEXT_SUBSCRIPTION_KEY = os.environ.get('TRANSLATOR_TEXT_SUBSCRIPTION_KEY')
TRANSLATOR_TEXT_ENDPOINT = os.environ.get('TRANSLATOR_TEXT_ENDPOINT')
TRANSLATOR_TEXT_REGION = os.environ.get('TRANSLATOR_TEXT_REGION')


if not TRANSLATOR_TEXT_SUBSCRIPTION_KEY or not TRANSLATOR_TEXT_ENDPOINT or not TRANSLATOR_TEXT_REGION:
    raise Exception('Please set/export the environment variables for subscription key, endpoint, and region.')


path = '/translate?api-version=3.0'
params = '&from=en&to=de&to=it&to=zh-Hans'
constructed_url = TRANSLATOR_TEXT_ENDPOINT + path + params

headers = {
    'Ocp-Apim-Subscription-Key': TRANSLATOR_TEXT_SUBSCRIPTION_KEY,
    'Ocp-Apim-Subscription-Region': TRANSLATOR_TEXT_REGION,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text' : 'Legal Documents Translation. Litigation. '
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))