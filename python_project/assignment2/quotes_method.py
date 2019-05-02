import requests as reqs
import json
from time import sleep
import xmltodict as xmltodict


# from test_case_calling_file import test_Case1

def print_quotes_in_delay(test_Case):
    while True:
        with open(test_Case) as jsonfile:
            jsoncontent = json.load(jsonfile)
            total_seconds = 0
            time_format = ['y', 'hr', 'min', 'sec']
            # specify delay time using this order year,hour, minutes,seconds without giving any space of each
            user_input = jsoncontent["delay"]
            time_list = []
            year = user_input.index("y")
            extract_the_year = user_input[:year]
            time_list.append(extract_the_year)
            hour = user_input.index("h")
            extract_the_hour = user_input[len(extract_the_year) + 1:hour]
            time_list.append(extract_the_hour)
            mini = user_input.index("m")
            extract_the_min = user_input[len(extract_the_year) + 1 + len(extract_the_hour) + 1:mini]
            time_list.append(extract_the_min)
            sec = user_input.index("s")
            extract_the_year = user_input[
                               len(extract_the_min) + 1 + len(extract_the_year) + 1 + len(extract_the_hour) + 1:sec]
            time_list.append(extract_the_year)
            for i in time_list:
                if i == "":
                    find_index = time_list.index(i)
                    time_list[find_index] = '0'
            combine_the_list = dict(zip(time_format, time_list))
            for key, value in combine_the_list.items():
                if key == 'y' and int(combine_the_list[key]) != 0:
                    total_seconds = +int(combine_the_list[key]) * 365 * 24 * 60 * 60
                elif key == 'hr' and combine_the_list[key] != 0:
                    total_seconds += int(combine_the_list[key]) * 3600
                elif key == 'min' and combine_the_list[key] != 0:
                    total_seconds += int(combine_the_list[key]) * 60
                elif key == 'sec' and combine_the_list[key] != 0:
                    total_seconds += int(combine_the_list[key])
                else:
                    total_seconds += int(combine_the_list[key])
            print(total_seconds)
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
                    sleep(total_seconds)
                else:
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
                response = reqs.request(method="GET",
                                        url="https://api.forismatic.com/api/1.0/?method=getQuote&lang={key}&format={format}".format(
                                            key=language, format=format))
                text_recieved = response.text
                quoteObj = json.loads(bytes(text_recieved, "utf-8").decode("unicode_escape"))
                author, quotes = extract_the_text(quoteObj)
                print("Author :" + author + "Says  " + quotes)
                sleep(total_seconds)


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

print_quotes_in_delay(test_Case1)
