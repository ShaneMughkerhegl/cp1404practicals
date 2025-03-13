"""
Wimbledon Champions Data Processor
Estimate: 30 minutes
Actual:   35 minutes
"""

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        return [line.strip().split(',') for line in file.readlines()[1:]]

def process_data(data):
    champions = {}
    countries = set()
    for year, country, champion in data:
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, sorted(countries)

def main():
    data = read_file("wimbledon.csv")
    champions, countries = process_data(data)
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items(), key=lambda x: x[1], reverse=True):
        print(f"{champion} {wins}")
    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()