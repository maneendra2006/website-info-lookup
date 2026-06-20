import requests
import socket
import json

# Get domain from user
host = input("Enter a domain name (e.g., google.com): ").strip()

try:
    # Get website headers
    req = requests.get("https://" + host, timeout=10)

    print("\nHeaders:\n")
    for key, value in req.headers.items():
        print(f"{key}: {value}")

    # Resolve hostname to IP
    ip_address = socket.gethostbyname(host)
    print(f"\nThe IP address of {host} is: {ip_address}\n")

    # Get IP information
    req_two = requests.get(f"https://ipinfo.io/{ip_address}/json", timeout=10)
    resp_ = req_two.json()

    print("IP:", resp_.get("ip", "N/A"))
    print("City:", resp_.get("city", "N/A"))
    print("Region:", resp_.get("region", "N/A"))
    print("Country:", resp_.get("country", "N/A"))
    print("Location:", resp_.get("loc", "N/A"))
    print("Organization:", resp_.get("org", "N/A"))
    print("Postal Code:", resp_.get("postal", "N/A"))
    print("Timezone:", resp_.get("timezone", "N/A"))

except socket.gaierror:
    print("Error: Could not resolve the domain name.")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")