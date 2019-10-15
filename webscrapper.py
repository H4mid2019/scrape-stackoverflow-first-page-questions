import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()


response = requests.get(
    "https://stackoverflow.com/questions?tab=Newest", headers={'User-Agent': ua.chrome})

soup = BeautifulSoup(response.text, "html.parser")


questions = soup.select(".question-summary")

quest_dict = {}
for question in questions:
    quest = question.select_one(".question-hyperlink").getText()
    vote = int(question.select_one(".vote-count-post").getText())
    quest_dict[quest] = vote

quest_dict_sorted = sorted(
    quest_dict.items(), key=lambda kv: kv[1], reverse=True)


# uncoment this lines for searching 'python' word in the first page
# target_word = 'python'
# for key, value in quest_dict_sorted:
#     if target_word in str(key):
#         print(key, "\t", value)
#     elif target_word.upper() in str(key):
#         print(key, "\t", value)
#     elif target_word.capitalize() in str(key):
#         print(key, "\t", value)


for key, value in quest_dict_sorted:
    print(key, "\t", value)
