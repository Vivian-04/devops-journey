# What happens when you type a URL into a browser

## 1. Finding the IP address (DNS)
1. The visitor types a URL, e.g. `github.com`, into the browser.
2. The computer checks its **cache** to see if it already knows the IP address.
3. If it doesn't, it asks a **DNS resolver**: either the ISP's resolver or a public one like Google's `8.8.8.8`.
4. The resolver finds the domain's **authoritative DNS server** (the official "phonebook" for that domain) and gets the IP address.
5. The resolver returns the IP address to the computer, which caches it for the record's **TTL**.

## 2. Connecting to the server
6. The computer opens a **TCP connection** to that IP on **port 443** (HTTPS), or port 80 for plain HTTP.
7. **TLS handshake:** the browser and server agree on encryption, and the server shows its **SSL certificate** to prove it's really github.com. That's the padlock.

## 3. Getting the page
8. The browser sends an **HTTP request**, e.g. `GET /`.
9. The **web server** (e.g. Nginx) sends back a **response**: a status code like `200 OK` plus the HTML.
10. The browser draws the page, then requests the extra files it needs (images, CSS, JavaScript).

## Key terms
| Term | Meaning |
|---|---|
| DNS | Turns names into IP addresses, like a phonebook |
| IP address | Finds the computer |
| Port | Finds the program on that computer (443 = HTTPS, 80 = HTTP) |
| A record | Name → IPv4 address |
| CNAME | Name → another name (an alias) |
| TTL | How long a DNS answer can be cached |

## Commands I used
- `dig github.com` shows the full DNS lookup
- `dig +short github.com` shows just the IP
- `dig @8.8.8.8 github.com` asks Google's DNS directly
