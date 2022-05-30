from bs4 import BeautifulSoup

dummy = "<html><form _glpi_csrf_token=\"{token}\"></form></html>"

def process(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    metas = soup.find_all("meta")
    for meta in metas:
        if (meta.get("property")):
            token = meta.get("content")
            return dummy.format(token=token)
    print(html)
    raise Exception("token not found")

# Just for testing
if __name__ == '__main__':
    import sys
    file = sys.argv[1]
    with open(file, 'r') as f:
        data = f.read()
        print(process(data))
