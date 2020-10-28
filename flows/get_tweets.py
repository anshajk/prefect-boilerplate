from requests import Session

API = "https://api.twitter.com/2/tweets"

with Session() as s:
    site = s.get("https://anshaj.dev")
    print(site.content)