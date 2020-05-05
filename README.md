# Covid Myth Busters (WhatsApp bot)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


Source of data: [WHO Myth Busters](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters)

## How does it work?

I have stored all the mythbusters listed on WHO website in (this file)[https://github.com/sukeesh/covid-fact-fake-checker/blob/master/facts.py] and later whenever there is a query, this query is matched with every factual sentence present with us and the sentence which has the maximum cosine similarity is responded.

## WhatsApp bot in action

![](WhatsApp-bot.gif)

## How to run locally?
Install requirements
```
pip3 install -r requirements.txt
```
and then run the flask server

```python
python3 main.py
```
## Contributions

There is still a lot to improve in this project and I welcome all the PRs/Feedback
