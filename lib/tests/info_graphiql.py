from urllib.parse import urlparse
from lib.utils import request_get

def detect_graphiql(url):
  result = False

  heuristics = ('graphiql.min.css', 'GraphQL Playground', 'GraphiQL', 'graphql-playground')
  endpoints = ['/graphiql', '/playground', '/console', '/graphql']
  
  parsed = urlparse(url)
  url = '{}://{}'.format(parsed.scheme, parsed.netloc)
  
  for endpoint in endpoints:
    response = request_get(url + endpoint)
    try:
      if response and any(word in response.text for word in heuristics):
        result = True
        break
    except:
      pass
  
  return result
