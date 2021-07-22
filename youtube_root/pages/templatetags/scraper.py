from django import template

register = template.Library()
import requests
from bs4 import BeautifulSoup

@register.simple_tag
def get_subscribers(url):
  html = requests.get(url).content
  soup = BeautifulSoup(html,"html.parser")
  result = soup.find_all('div', class_="columns left p-top-small p-bottom-small info b-bottom")
  start = str(result).find("Video Views:")
  start += 21
  string = str(result)[start:]
  i = 0
  while string[i].isdigit() or string[i] == ",":
    i+=1
  end = i + start

  total_views = "Total Views: " + (str(result)[start:end])

  begin = str(result).find("Sub Count:")
  begin += 19
  string = str(result)[begin:]
  i = 0
  while string[i].isdigit() or string[i] == ",":
    i+=1
  finish = i + begin
  total_subs = "Total Subscribers: " + (str(result)[begin:finish])
  return total_subs + " " + total_views