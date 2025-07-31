import requests
import sys

def subdomain_scanner(domain, wordlist_file):
    try:
        with open(wordlist_file, 'r') as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_file}' not found.")
        return

    print(f"\n[*] Starting subdomain scan for: {domain}\n")

    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(f"[+] Found: {url} (Status: {response.status_code})")
        except requests.ConnectionError:
            pass
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {url}: {e}")

    print("\n[*] Scan complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 subdomain_scanner.py <domain> <wordlist_file>")
        print("Example: python3 subdomain_scanner.py example.com subdomains.txt")
        sys.exit(1)

    target_domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    subdomain_scanner(target_domain, wordlist_path)
