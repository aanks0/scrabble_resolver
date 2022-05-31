import requests
from bs4 import BeautifulSoup


# inspired from https://blog.site2wouf.fr/2020/04/ods8-en-fichier-texte-script-python.html
# but improved
def init_scrabble_dictionary():
    base_url = "https://www.listesdemots.net/touslesmots"
    total_words = 0

    with open("my_scrabble_dic.txt", "w") as fd:
        for i in range(1, 919):
            url = f"{base_url}.htm" if i == 1 else f"{base_url}page{str(i)}.htm"
            connection_test = False
            while not connection_test:
                try:
                    req = requests.get(url, timeout=3)
                    connection_test = True
                except Exception:
                    print("Connection issue, retrying ...")
            print(req.url)
            page = req.content
            soup = BeautifulSoup(page, features="html.parser")
            span = soup.find("span", {"class": "mot"})
            words = span.string.strip()
            l_words = words.split(" ")
            for word in l_words:
                fd.write(word + "\n")
                print("|", end="")

            print()
            print(f"page {i} : OK ({len(l_words)})")
            total_words += len(l_words)
            print(f"Total words is {total_words}")


if __name__ == "__main__":
    init_scrabble_dictionary()
