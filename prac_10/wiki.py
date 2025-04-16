import wikipedia

def main():
    """Get user input and display Wikipedia page details until blank input."""
    while True:
        title = input("Enter page title: ")
        if not title:
            break
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print("Page id "{}" does not match any pages. Try another id!".format(title))
    print("Thank you.")

if __name__ == "__main__":
    main()
