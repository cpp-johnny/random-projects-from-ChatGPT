import urllib

def download_file(url):
    urllib.request.urlretrieve(url, "file.txt")

download_file("http://example.com/file.txt")
