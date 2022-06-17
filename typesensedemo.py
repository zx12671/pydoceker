import typesense

client = typesense.Client({
    'nodes': [{
      'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
      'port': '8108',      # For Typesense Cloud use 443
      'protocol': 'http'   # For Typesense Cloud use https
    }],
    'api_key': 'Hu52dwsas2AdxdE',
    'connection_timeout_seconds': 2
  })
def build():
  books_schema = {
    'name': 'books',
    'fields': [
      {'name': 'title', 'type': 'string' },
      {'name': 'authors', 'type': 'string[]', 'facet': True },

      {'name': 'publication_year', 'type': 'int32', 'facet': True },
      {'name': 'ratings_count', 'type': 'int32' },
      {'name': 'average_rating', 'type': 'float' }
    ],
    'default_sorting_field': 'ratings_count'
  }

  # client.collections.create(books_schema)

  # create_response = client.collections.create({
  #   "name": "companies",
  #   "fields": [
  #     {"name": "company_name", "type": "string" },
  #     {"name": "num_employees", "type": "int32" },
  #     {"name": "country", "type": "string", "facet": True }
  #   ],
  #   "default_sorting_field": "num_employees"
  # })




# document = {
#  "id": "127",
#  "company_name": "李响公司",
#  "num_employees": 5217,
#  "country": "CHINA"
# }

# client.collections['companies'].documents.create(document)

search_parameters = {
  'q'         : 'harry potter',
  'query_by'  : 'title',
  'sort_by'   : 'publication_year:desc'
}

# build()
res = client.collections['books'].documents.search(search_parameters)
hit = res["hits"]
print(hit)
# client.collections['companies'].documents.search(search_parameters)