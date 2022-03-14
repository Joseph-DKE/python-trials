import requests

fin = "n 2.1 m 2.3 o 2.4 p 2.5 q 2.6 r 2.7 s 2.8 t 2.9 u 3.0"
url = "https://betsmart.vercel.app/result?teamslist=" + fin
response = requests.post(url)
print(response.text)