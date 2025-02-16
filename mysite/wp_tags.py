import requests

def wordpress_tags(request):
    # URL API WordPress untuk mengambil tags
    api_url = "https://pardi.jambishow.com/wp-json/wp/v2/tags?orderby=count&order=asc&per_page=15"
    response = requests.get(api_url)
    if response.status_code == 200:
        tags = response.json()
    else:
        tags = []
    
    # Return data tags untuk digunakan di template
    return {"tags": tags}
