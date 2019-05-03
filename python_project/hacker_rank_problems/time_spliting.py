def timing_spit(user_input):
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
user_input = "2s"
timing_spit(user_input)

import requests as reqs
import json
from time import sleep

import xmltodict as xmltodict


def open_the_json_file(test_Case):
    # file=open(test_Case,"r")
    # jsoncontent = json.loads(jsoncontent)
    # file.close()
    with open(test_Case) as jsonfile:
        jsoncontent = jsonfile.read()
    print(jsonfile.closed)
    jsoncontent = json.loads(jsoncontent)
    language = jsoncontent["lang"]
    format = jsoncontent["format"]
    # timing must be in the format for year /y ,hour/h,minutes/m,seconds/s specify space timing between the timing
    user_input = jsoncontent["delay"]
    total_seconds = timing_spit(user_input)
    print_quotes_for_time(jsoncontent, total_seconds, language, format)


def print_quotes_for_time(jsoncontent, total_seconds, language, format):
    while True:
        user_language = ["en", "ru"]
        if language not in user_language:
            language = "en"
            jsoncontent['format'] = "json"
        if jsoncontent["lang"] in user_language:
            if jsoncontent["format"] == "json":
                author, quotes = common_response(language, format, total_seconds,jsoncontent)
                print("Author :" + author + " says:" + quotes)
                sleep(total_seconds)
            else:
                # response = reqs.request(method="GET",
                #                         url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                #                             key=jsoncontent["lang"], format=jsoncontent["format"]))
                # text_recieved = response.text
                text_recieved = extract_quotes_from_site(jsoncontent)
                xmltodicts = json.loads(json.dumps(xmltodict.parse(text_recieved)))
                quote_text = xmltodicts["forismatic"]['quote']
                if quote_text["quoteAuthor"] == None:
                    to_print_the_resultant_quotes(quote_text["quoteAutor"], quote_text["quoteText"], total_seconds)
                # quote_text["quoteAuthor"] = "UNKNOWN_AUTHOR"
                # print("Author: {} Says: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))
                else:
                    print("Author: {} Says: {}".format(quote_text["quoteAuthor"], quote_text["quoteText"]))
                sleep(total_seconds)


def to_print_the_resultant_quotes(author, quotes, total_seconds):
    author = "UNKNOWN_AUTHOR"
    print("Author :" + author + " says :" + quotes)
    sleep(total_seconds)


def common_response(language, format, total_seconds, jsoncontent):
    text_recieved = extract_quotes_from_site(jsoncontent)
    # response = reqs.request(method="GET",
    #                         url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
    #                             key=language, format=format))
    # text_recieved = response.text
    if language == "en":
        quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
        author, quotes = extract_the_text(quoteObj, total_seconds)
    else:
        quotes_obj = json.loads(text_recieved)
        author, quotes = extract_the_text(quotes_obj, total_seconds)
    return author, quotes


def extract_the_text(text_recieved, total_seconds):
    author_name = text_recieved["quoteAuthor"]
    quote_message = text_recieved["quoteText"]
    if author_name == '':
        to_print_the_resultant_quotes(author_name, quote_message, total_seconds)
        # author_name = "UNKNOWN_AUTHOR"
        # return author_name, quote_message
    else:
        return author_name, quote_message


def timing_spit(user_input):
    new_time_list = []
    total_seconds = 0
    append_to_the_list = user_input.split()
    for i in range(len(append_to_the_list)):
        check_the_text = append_to_the_list[i]
        extract_the_text = check_the_text[-1]
        extract_the_value = check_the_text[:-1]
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
    return total_seconds


def extract_quotes_from_site(jsoncontent):
    response = reqs.request(method="GET",
                            url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                key=jsoncontent["lang"], format=jsoncontent["format"]))
    text_recieved = response.text
    return text_recieved


test_Case1 = "test_case/config.json"
test_Case2 = "test_case/config2.json"
test_Case3 = "test_case/config3.json"
test_Case4 = "test_case/config4.json"
test_Case5 = "test_case/config5.json"
test_Case6 = "test_case/config6.json"

open_the_json_file(test_Case1)
