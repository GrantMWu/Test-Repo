import requests

def lookup(param):
    try:
        api_key = '2b15dcdccd77a2803a30cea7e78b42a1'
        api_id = '27e4f5c3'
        response = requests.get(f"https://api.edamam.com/api/recipes/v2?type=public&q=%22{param}%22&app_id={api_id}&app_key={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        result = response.json()
        return result  # , next, count
    except (KeyError, TypeError, ValueError):
        return None

print(lookup('chicken'))
