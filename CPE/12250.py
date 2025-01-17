def main():
    from sys import stdin
    e = stdin.readline
    words = {
        "HELLO" : "ENGLISH",
        "HOLA" : "SPANISH",
        "HALLO" : "GERMAN",
        "BONJOUR" : "FRENCH",
        "CIAO" : "ITALIAN",
        "ZDRAVSTVUJTE" : "RUSSIAN"
    }
    count = 0
    while True:
        n = e().strip()
        if n == "#": break
        count += 1
        print(f"Case {count}: {words.get(n, 'UNKNOWN')}")
main()