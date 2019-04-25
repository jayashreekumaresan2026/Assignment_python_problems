import requests as reqs
import json
from time import sleep


def print_quotes_for_30m():
    while True:
        with open("config.json") as jsonfile:
            jsoncontent = json.load(jsonfile)
            values_in_dictionary = list(jsoncontent.values())
            user_language = ["en", "ru"]
            if values_in_dictionary[0] in user_language:
                response = reqs.request(method="GET",
                                        url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                            key=values_in_dictionary[0], format=values_in_dictionary[1]))

                the_text_in_dictionary = json.loads(response.text)

                quotes_and_author = extract_the_text(the_text_in_dictionary)
                print(quotes_and_author)
                sleep(values_in_dictionary[2])

            else:
                language = "en"
                format = "json"
                response = reqs.request(method="GET",
                                        url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                            key=language, format=format))
                the_text_in_dictionary = dict(response.text)
                quotes_and_author = extract_the_text(the_text_in_dictionary)
                print(quotes_and_author)
                sleep(values_in_dictionary[2])


def extract_the_text(the_text_in_dictionary):
    author_name = the_text_in_dictionary["quoteAuthor"]
    quote_message = the_text_in_dictionary["quoteText"]
    if author_name == '':
        author_name = "UNKNOWN_AUTHOR"
        return author_name, quote_message
    else:
        return author_name, quote_message


print_quotes_for_30m()
