# Entry point of your application
from src.scraper import Scraper
from src.analysis import PieBarChart
import re


def main():

    """ A request is made to the user whether he wants to scrape a website. He can
        either enter "y" for YES or "n" for NO. The user option is subject to error handling
        and he is continuously prompted until the correct option is entered
     """

    while True:
        try:
            option = input('Would you like to scrape a website (y/n) ').strip()
            if option.lower() == 'y' or option.lower() == 'n':
                break
            else:
                raise Exception('Invalid option')
        except Exception as err:
            print(str(err))
    if option.lower() == 'y':
        while True:
            try:
                web = input('Enter a website to analyze: ')
                pattern = re.compile(r'^https://www\.[a-zA-Z0-9_\-!@#$%^&*()+]+\.(org|com|net)$')
                if pattern.match(web):
                    break
                else:
                    raise Exception('Sorry, Invalid URL. start with "https://"  and end with ".com" or ".net" or ".org"')
            except Exception as err:
                print(str(err))

        my_scraper = Scraper(web)                       # An instance of Scraper class is created
        page = my_scraper.get_page()                    # The web is created and the page returned
        cleaned_up = my_scraper.clean_up(page)          # This cleans up the page
        dictionary = my_scraper.key_value(cleaned_up)   # A dictionary is created
        my_arr_keys = dictionary.keys()                 # A list of the X-axis or most common words
        my_arr_values = dictionary.values()             # A list of the Y-axis or frequency of words
        my_analyser = PieBarChart(my_arr_keys, my_arr_values)   # An instance of the PieBarChart

        top_words = my_analyser.top_word(dictionary)    # The Top 10 words is selected
        bar_chart = my_analyser.bar_chart()             # The Bar Chart is plotted
        pie_chart = my_analyser.pie_chart()             # The Pie Chart is plotted

        print('Thanks for analyzing! Come back again!')
        main()
    else:
        print('Thanks for analyzing! Come back again!')
        exit()


if __name__ == "__main__":
    main()
