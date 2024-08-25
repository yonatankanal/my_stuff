def main():
    request = input("Request: ")
    print(search(request))

def search(request):
    return f"For your answer go to \'Google.com\' and type \'{request}\' into the search bar."

if __name__ == "__main__":
    main()