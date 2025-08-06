import argparse
from collections import defaultdict

def load_ids(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def build_lookup(id_list):
    lookup = defaultdict(list)
    for id in id_list:
        lookup[id[-6:]].append(id)
    return lookup

def search_ids(search_ids, lookup):
    for search_id in search_ids:
        candidates = lookup.get(search_id[-6:], [])
        found = False
        for candidate in candidates:
            if candidate == search_id:
                print(f"\033[92m✅ Found: {candidate}\033[0m")
                found = True
                break
        if not found:
            print(f"\033[91m❌ Not found: {search_id}\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Order ID Search Tool")
    parser.add_argument('--file', required=True, help='Path to ID list file')
    parser.add_argument('--search', required=True, nargs='+', help='One or more IDs to search')
    args = parser.parse_args()

    id_list = load_ids(args.file)
    lookup = build_lookup(id_list)
    search_ids(args.search, lookup)

if __name__ == "__main__":
    main()
