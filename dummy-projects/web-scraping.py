import profile
from urllib import response
import requests
from bs4 import BeautifulSoup as bs
user_name = "Emmanuel-Odero"#input('Entre the username ')
user_acc_url = "https://github.com/"+user_name
results = requests.get(user_acc_url)
soup = bs(results.content, "html.parser")
profile_image = soup.find('img',{'alt':'Avatar'})['src']
print(profile_image)