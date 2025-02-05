from lib.utils import graph_query, get_error

def field_suggestions(url):
  result = False

  q = 'query { __schema { directive } }'    
  gql_response = graph_query(url, payload=q)
    
  try:
    if 'Did you mean' in get_error(gql_response):
      result = True
  except:
    pass
  
  return result
