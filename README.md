# 🌐 Website Info Lookup

A simple Python command-line tool that fetches HTTP response headers for a website, resolves its domain to an IP address, and retrieves IP-based geolocation and ISP details using the [ipinfo.io](https://ipinfo.io) API.

Useful for quick **OSINT (Open-Source Intelligence)** lookups, network troubleshooting, or learning how DNS resolution and IP geolocation work under the hood.

---

## ✨ Features

- 🔗 Fetches and displays full HTTP response **headers** for any domain
- 🧭 Resolves a domain name to its **IP address** using Python's built-in `socket` module
- 📍 Retrieves **IP geolocation info** — city, region, country, coordinates, organization/ISP, postal code, and timezone
- ⚠️ Graceful error handling for invalid domains, network failures, and unexpected errors

---

## 📦 Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/) library

Install the dependency:

```bash
pip install requests
```

---

## 🚀 Usage

Clone the repository and run the script:

```bash
git clone https://github.com/maneendra2006/website-info-lookup.git
cd website-info-lookup
python app.py
```

You'll be prompted to enter a domain name:

```
Enter a domain name (e.g., google.com): facebook.com
```

### Example Output

```
Headers:

Content-Type: text/html; charset=UTF-8
Server: ECAcc (dcd/7D5A)
...

The IP address of facebook.com is: 163.70.140.35

IP: 163.70.140.35
City: Hyderabad
Region: Telangana
Country: IN
Location: 17.3840,78.4564
Organization: AS32934 Facebook, Inc.
Postal Code: 500001
Timezone: Asia/Kolkata
```

---

## 🛠️ How It Works

1. Takes a domain name as input from the user
2. Sends an HTTPS `GET` request to the domain and prints all response headers
3. Uses `socket.gethostbyname()` to resolve the domain to an IPv4 address
4. Queries `https://ipinfo.io/<ip>/json` to fetch geolocation and ISP details for that IP
5. Handles common errors:
   - `socket.gaierror` → invalid or unresolvable domain
   - `requests.exceptions.RequestException` → network-related issues
   - Generic `Exception` → catch-all for anything unexpected

---

## ⚠️ Notes & Limitations

- This script makes **unauthenticated** requests to `ipinfo.io`, which enforces rate limits for free usage (around 50,000 requests/month per IP at the time of writing). For higher limits, sign up for a free [ipinfo.io API token](https://ipinfo.io/signup) and pass it as a query parameter.
- Some websites may block requests without a `User-Agent` header — you can add one to `requests.get()` if you encounter `403` errors.
- This tool is intended for **educational and informational purposes only**. Always ensure you have permission before scanning or probing domains you don't own.

