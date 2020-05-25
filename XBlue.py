"""
Copyright (c) 2020 Hugo Diaz

"""

from bs4 import BeautifulSoup
import requests
import urllib.request
from pyfiglet import Figlet
import argparse
from clint.textui import puts,colored,indent



def mainT(url):
        """
        initialisation des variables
        """
        role="null"
        data= "null"
        clas="null"
        action="null"
        i="null"
        req = ''
        tab = ["search" , "recherche" , "rech" , "results" , "resultats" , "query"]
        payload="WDLj4?bX(qDRN4aE"

        """
        request
        """
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        r = opener.open('https://www.asos.com/')
        urlT = url.split('//')
        page = r.read()
        p = page.decode("UTF-8")
        soup = BeautifulSoup(p,'html.parser')
        form = soup.find_all("form")
        t={}
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
                                        req =  'https:/' +z 
                                else:
                                        req = url +  z 
                                        
                                for b in a:
                                        #recuperer le name= du input
                                        if b.get("name"):
                                                if b.get('value'):
                                                        if b.get('value') == '':
                                                                t[b.get("name")] = payload
                                                        else :
                                                                t[b.get("name")] = b.get('value')
                                                else:
                                                        t[b.get("name")] = payload




           


        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        re = urllib.request.Request(req, headers = headers)
        resp = urllib.request.urlopen(re)
        respData = resp.read()
        a = respData.decode("UTF-8")
        sou = BeautifulSoup(a,'html.parser')
                        
        if payload in str(respData):
                print('the payload is reflected on this page ... the site is potentially XSS vulnerable')
                rep = input('Do you want to enter another url ?(y or n) ')
                if rep == "Y" or rep == "y":
                        rl = input(colored.green('Please enter an another url ?(https://www.example.com) :'))
                        mainT(rl)
                        
                        
                        
                
        else :
                print(colored.red('the payload is not reflexted on this page...Not vulnerable'))
                          
                        
                


f = Figlet(font='slant')
print(colored.blue(f.renderText('XBlue')))
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="specify the url",type=str)
args = parser.parse_args()


"""
Call function mainT
"""
mainT(args.url)



