def main():
    authors = {  # dictionary
        "Patricia Aakhus": "1952",
        "Edward Abbey": "1927",
        "Lynn Abbey": "1948",
        "Megan Abbott": "1971",
        "Louise Abeita": "1926"}

    for author, date in authors.items():
        if int(date) == 1971:
            print("%s was born in %d." % (author, int(date)))


main()
