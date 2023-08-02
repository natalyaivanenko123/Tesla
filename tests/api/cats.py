import requests

url = "https://catfact.ninja/fact"

payload = {}
headers = {
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Opera\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "XSRF-TOKEN=eyJpdiI6IklGeU00ZC9aQkNkM2FCRnprenRJdWc9PSIsInZhbHVlIjoicVdEYVpuRjhMUksyUVN4UUdjcHd3QnRUS1ExUzBZbGFuZk4wMjY3US9walJ2bXJpc0xkOU5raFY5dTRLTVcvMktWTHd1djE0bGtHNjhlSmo5WmNqZDBOc0s5Vm15OTh4UngrWlNOYnl6UGxZclhCdjgzZUxReTZyQysvVXpxZmwiLCJtYWMiOiJkNmY4MWRjODExNDRmNTg0NmQ0Y2I3MjFhYzJkNGRmOTI5N2MyYWY1OWI0ZjlkMDIzNzZmNWNiMDNmZGRhMzliIiwidGFnIjoiIn0%3D; catfacts_session=eyJpdiI6IklRdExwdVFZMzJuRXF3QWQzTDBBQUE9PSIsInZhbHVlIjoiN0JSRjdFT25EQ3ZiOUJ3OE40alZ5c3kvY21HUFJrRzByaUhQbTBucERoYndIbHVVRktsbnFVcHRNd2pvUzUxOTg4UWN1U0djV2VLZ1pjdy9TbEJNQ0hSTGJya0JtNTBUTFdhWXNONVNFUkF1YjVaZHVoakprZGxwdXBVL1hVNmoiLCJtYWMiOiI3ODRiM2ZkN2Y0MTE0Y2FhNDdmOTY5YmI0YTA3N2M0YTQyNTY1NjFjZDE4MTI3Yzc4NDgzZDk2YzNjOTg1MjEwIiwidGFnIjoiIn0%3D"
}

response = requests.request("GET", url, headers=headers, data=payload)
json = response.json()

assert(len(json["fact"]) == json["length"])
