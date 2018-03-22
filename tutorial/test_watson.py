import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions
from pprint import pprint

creds = json.load(open('watson_creds.json'))
userdetails = creds['natural-language-understanding'][0]['credentials']
reviews = json.load(open('samplereviews.json'))

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username=userdetails['username'],
  password=userdetails['password'],
  version='2017-02-27')


def analyze(review):
  response = natural_language_understanding.analyze(
    text=review,
    features=Features(
      entities=EntitiesOptions(
        emotion=True,
        sentiment=True,
        limit=3),
      keywords=KeywordsOptions(
        emotion=True,
        sentiment=True,
        limit=3)))

  return json.dumps(response, indent=2)

analysis = []

for review in reviews:
  analysis.append(analyze(review['review']))

pprint(analysis)