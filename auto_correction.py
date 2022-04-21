from serpapi import GoogleSearch
import os

params = {
  "api_key": "5ead802eb4382388831a3c1daac78d3cf9b8e16312638ddd1dd64723a6c1247d",
  "engine": "google",
  "q": "штрудиль",
  "gl": "ru",
  "hl": "ru"
}

search = GoogleSearch(params)
results = search.get_dict()

print(results['search_information']['spelling_fix'])