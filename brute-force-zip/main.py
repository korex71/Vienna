import zipfile
from tqdm import tqdm

file = "./secret.zip"
wordlist = "./wordlist.txt"

file = zipfile.ZipFile(file)

n_list_words = len(list(open(wordlist, "rb")))

def exec():

    n_list_words = len(list(open(wordlist, "rb")))

    print(f"\n{n_list_words} words in the wordlist\n")

    with open(wordlist, "rb") as f:
        for line in tqdm(f, total=n_list_words):
            try:
                file.extractall(pwd=line.strip())
                print("[+] Password found: {}".format(line.decode().strip()))
                exit(0)
            except:
                continue

    print(f"\n[-] Password not found in list {wordlist}.")

if(__name__ == "__main__"): exec()