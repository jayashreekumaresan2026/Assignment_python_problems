import requests as reqs
import json
from time import sleep
import xmltodict as xmltodict


def print_quotes_in_delay():
    while True:
        with open("config.json") as jsonfile:
            jsoncontent = json.load(jsonfile)
            delay_time = int(jsoncontent["delay"])
            user_language = ["en", "ru"]
            response = reqs.request(method="GET",
                                            url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                                key=jsoncontent["lang"], format=jsoncontent["format"]))
            text_recieved = response.text
            if jsoncontent["lang"] in user_language:
                if jsoncontent["format"] == "json":
                    quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
                    author, quotes = extract_the_text(quoteObj)
                    print("Author :" + author + "   Says:" + quotes)
                    sleep(delay_time)
                else:
                    xmltodicts = json.loads(json.dumps(xmltodict.parse(text_recieved)))
                    quote_text = xmltodicts["forismatic"]['quote']
                    if quote_text["quoteAuthor"] == None:
                        quote_text["quoteAuthor"] = "UNKNOWN_AUTHOR"
                        print("AUTHOR: {} SAYS: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))


                    else:
                        print("AUTHOR: {} SAYS: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))
                    sleep(delay_time)

            else:
                language = "en"
                format = "json"
                response = reqs.request(method="GET",
                                        url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                            key=language, format=format))
                text_recieved = response.text
                quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
                author, quotes = extract_the_text(quoteObj)
                print("Author :" + author + "Says  " + quotes)
                sleep(delay_time)

def extract_the_text(the_text_in_dictionary):
    author_name = the_text_in_dictionary["quoteAuthor"]
    quote_message = the_text_in_dictionary["quoteText"]
    if author_name == '':
        author_name = "UNKNOWN_AUTHOR"
        return author_name, quote_message
    else:
        return author_name, quote_message


print_quotes_in_delay()