import requests as reqs
import json
from time import sleep

import xmltodict as xmltodict


def print_quotes_for_30m():
    while True:
        with open("config.json") as jsonfile:
            jsoncontent = json.load(jsonfile)
            values_in_dictionary = list(jsoncontent.values())
            user_language = ["en", "ru"]
            if values_in_dictionary[0] in user_language:
                if values_in_dictionary[1] == "json":
                    response = reqs.request(method="GET",
                                            url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                                key=values_in_dictionary[0], format=values_in_dictionary[1]))
                    text_recieved = response.text
                    quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
                    author, quotes = extract_the_text(quoteObj)
                    print("Author :" + author + "   Says:" + quotes)
                    sleep(values_in_dictionary[2])
                else:
                    response = reqs.request(method="GET",
                                            url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                                key=values_in_dictionary[0], format=values_in_dictionary[1]))
                    text_recieved = response.text
                    xmltodicts = json.loads(json.dumps(xmltodict.parse(text_recieved)))
                    quote_text = xmltodicts["forismatic"]['quote']
                    quotes_text_in_list = list(quote_text.values())
                    if quotes_text_in_list[1] == None:
                        quotes_text_in_list[1] = "UNKNOWN_AUTHOR"
                        print("AUTHOR: {} SAYS: {}".format(quotes_text_in_list[1], quotes_text_in_list[0]))
                        sleep(values_in_dictionary[2])

                    else:
                        print("AUTHOR: {} SAYS: {}".format(quotes_text_in_list[1], quotes_text_in_list[0]))
                    sleep(values_in_dictionary[2])


            else:
                language = "en"
                format = "json"
                response = reqs.request(method="GET",
                                        url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                            key=language, format=format))
                text_recieved = response.text
                quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
                quotes, author = extract_the_text(quoteObj)
                print("Author :" + quotes + "says" + author)
                sleep(values_in_dictionary[2])


def extract_the_text(the_text_in_dictionary):
    author_name = the_text_in_dictionary["quoteAuthor"]
    quote_message = the_text_in_dictionary["quoteText"]
    print(quote_message)
    if author_name == '':
        author_name = "UNKNOWN_AUTHOR"
        return author_name, quote_message
    else:
        return author_name, quote_message


print_quotes_for_30m()
