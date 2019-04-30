import requests as reqs
import json
from time import sleep

import xmltodict as xmltodict


def print_quotes_for_time(test_Case):
    while True:
        with open(test_Case) as jsonfile:
            jsoncontent = json.load(jsonfile)
            #timing must be in the format for year /y ,hour/h,minutes/m,seconds/s specify space timing between the timing
            user_input= jsoncontent["delay"]
            new_time_list = []
            total_seconds = 0
            append_to_the_list = user_input.split()
            print(append_to_the_list)
            for i in range(len(append_to_the_list)):
                check_the_text = append_to_the_list[i]
                extract_the_text = check_the_text[-1]
                extract_the_value = check_the_text[:-1]
                print(extract_the_text)
                print(extract_the_value)
                if extract_the_text == 'y':
                    total_seconds = int(extract_the_value) * 365 * 24 * 60 * 60
                    new_time_list.append(total_seconds)
                elif extract_the_text == 'h':
                    total_seconds += int(extract_the_value) * 3600
                    new_time_list.append(total_seconds)
                elif extract_the_text == 'm':
                    total_seconds += int(extract_the_value) * 60
                else:
                    total_seconds += int(extract_the_value)
            print(total_seconds)
            user_language = ["en", "ru"]
            if jsoncontent["lang"] in user_language:
                if jsoncontent["format"] == "json":
                    language=jsoncontent["lang"]
                    format=jsoncontent["format"]
                    author, quotes = common_response(language, format)
                    print("Author :" + author + "says" + quotes)
                    sleep(total_seconds)
                else:
                    response = reqs.request(method="GET",
                                            url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                                key=jsoncontent["lang"], format=jsoncontent["format"]))
                    text_recieved = response.text
                    xmltodicts = json.loads(json.dumps(xmltodict.parse(text_recieved)))
                    quote_text = xmltodicts["forismatic"]['quote']
                    if quote_text["quoteAuthor"] == None:
                        quote_text["quoteAuthor"] = "UNKNOWN_AUTHOR"
                        print("AUTHOR: {} SAYS: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))
                    else:
                        print("AUTHOR: {} SAYS: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))
                    sleep(total_seconds)

            else:
                language = "en"
                format = "json"
                author,quotes=common_response(language,format)
                print("Author :" + author+ "says" + quotes)
                sleep(total_seconds)
def common_response(language,format):
        response = reqs.request(method="GET",
                                url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                    key=language, format=format))
        text_recieved = response.text
        quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
        author, quotes = extract_the_text(quoteObj)
        return author,quotes


def extract_the_text(the_text_in_dictionary):
    author_name = the_text_in_dictionary["quoteAuthor"]
    quote_message = the_text_in_dictionary["quoteText"]
    if author_name == '':
        author_name = "UNKNOWN_AUTHOR"
        return author_name, quote_message
    else:
        return author_name, quote_message

test_Case1 = "test_case/config.json"
test_Case2 = "test_case/config2.json"
test_Case3 = "test_case/config3.json"
test_Case4 = "test_case/config4.json"
test_Case5 = "test_case/config5.json"
test_Case6 = "test_case/config6.json"

print_quotes_for_time(test_Case1)
