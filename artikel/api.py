import requests

def get_articles():
    # Ganti URL ini dengan URL API WordPress Anda
    api_url = "https://appscenter.site/wp-json/wp/v2/posts?categories=70"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # Mengembalikan data JSON artikel
    return []

def get_article_detail(slug):
    # Ganti URL ini dengan URL API WordPress Anda
    api_url = f"https://appscenter.site/wp-json/wp/v2/posts?slug={slug}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()[0] if response.json() else None
    return None
