import requests

def get_projects():
    # Ganti URL ini dengan URL API WordPress Anda
    api_url = "https://appscenter.site/wp-json/wp/v2/posts?categories=69"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # Mengembalikan data JSON artikel
    return []



def get_project_detail(slug):
    # Ganti URL ini dengan URL API WordPress Anda
    api_url = f"https://appscenter.site/wp-json/wp/v2/posts?slug={slug}"
    response = requests.get(api_url)
    if response.status_code == 200:
        article = response.json()[0] if response.json() else None
        if article:
            # Ambil daftar ID tag dari artikel
            tag_ids = article.get('tags', [])
            tags = []

            # Ambil detail tag berdasarkan ID tag
            for tag_id in tag_ids:
                tag_response = requests.get(f"https://appscenter.site/wp-json/wp/v2/tags/{tag_id}")
                if tag_response.status_code == 200:
                    tags.append(tag_response.json())

            # Tambahkan informasi tag ke artikel
            article['tags_details'] = tags
            return article
    return None