import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choices(characters, k=6))  # Generate a random 6-character string
        self.url_mapping[short_url] = original_url
        return short_url

    def redirect(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

if __name__ == "__main__":
    url_shortener = URLShortener()

    long_url = "https://www.nasa.gov/mission_pages/station/main/index.html?"
    "fbclid=IwAR1x_XcTZu9g6pRtZqCgqOqysYBsK5djbsivAObgNlxjsGnwS57JFpP7ZL8#signs_of_life"
    
    short_url = url_shortener.shorten_url(long_url)
    print("Short URL:", short_url)
    print("Original URL:", url_shortener.redirect(short_url))


