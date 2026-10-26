# HTTP, HTTPS & status codes

## HTTP in one line
HTTP is the language browsers and servers use to talk. The browser sends a **request**, the server sends back a **response**. HTTPS is the same conversation, but encrypted.

## Request methods
| Method | Meaning | Example |
|---|---|---|
| GET | Give me something | Load a page |
| POST | Here's new data | Submit a form |
| PUT / PATCH | Update something | Edit a profile |
| DELETE | Remove something | Delete a post |

## Status codes
| Code | Meaning | Examples |
|---|---|---|
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Go somewhere else (redirect) | 301 Moved Permanently, 302 Found |
| 4xx | The client made a mistake | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | The server broke | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

**Shortcut:** 4xx = your fault, 5xx = their fault.

## HTTPS & SSL certificates
- Plain HTTP is like a postcard: anyone along the way can read it. HTTPS is a sealed envelope.
- The server shows an **SSL/TLS certificate**, an ID card proving who it is, signed by a trusted **Certificate Authority (CA)**.
- Valid certificate = padlock 🔒. Invalid = browser warning.
- **Let's Encrypt** gives out free certificates.

## What I found with curl
- `curl -I http://github.com` returned a **301** redirect, with a `location:` header pointing to `https://github.com/`. GitHub forces everyone onto HTTPS.
- `curl -I https://github.com/this-page-does-not-exist-vee` returned a **404 Not Found**.
- `curl -v https://github.com` showed the TLS handshake. GitHub's certificate was issued by:  C=GB; O=Sectigo Limited...
- `curl -I localhost` on my own Nginx returned:  200

## Troubleshooting: three kinds of "it's not working"
| What curl says | What it means | Where to look |
|---|---|---|
| Connection refused | Reached the machine, but nothing is listening on that port | Start the service (`systemctl start nginx`) |
| Timed out | Couldn't reach the machine: wrong IP, network down, or a firewall dropping traffic | Check the network, IP and firewall |
| 5xx | The server is running and answered, but something behind it broke | Check the app and read the logs |

**Key insight:** a 5xx proves the server is alive. "Refused" and "timed out" mean it never answered.

## Commands I used
- `curl -I <url>`: show only the response headers
- `curl -v <url>`: show the whole conversation, including TLS
- `sudo systemctl stop/start nginx`: break and fix my own server
