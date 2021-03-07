import pickle
from time import sleep
from selenium import webdriver

artwork_links = []


def collect_art_id(artists_id):
    for n in range(0, len(artists_id)):
        artist_page = f'https://www.pixiv.net/users/{artists_id[n]}/illustrations'
        driver_location = '/usr/bin/chromedriver'
        binary_location = '/usr/local/bin/chromium'
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location
        browser = webdriver.Chrome(
            executable_path=driver_location, chrome_options=options)

        browser.get(artist_page)
        sleep(3)

        COUNTER = 1
        next_page = browser.find_elements_by_class_name('_2m8qrc7')
        while COUNTER < len(next_page)-1:
            print('Current page', COUNTER)
            # Collect all artworks_frames
            artworks = browser.find_elements_by_class_name("iasfms-0")
            # Collect artwork link
            for artwork in artworks:
                artwork_link = artwork.find_element_by_css_selector(
                    'div.iasfms-0 > a.iasfms-4').get_attribute('href')
                print(artwork_link)
                artwork_links.append(artwork_link)
            sleep(4)
            if COUNTER == len(next_page)-2:
                print(COUNTER)
                print(len(next_page)-2)
            else:
                next_page[-1].click()
            sleep(5)
            COUNTER += 1
            print(COUNTER)
        print(len(artwork_links))

        with open('artwork_links.pkl', "wb") as f:
            pickle.dump(artwork_links, f)

        browser.quit()


if __name__ == '__main__':
    artists_id = ['30959821', '2188232']  # pixiv user id
    collect_art_id(artists_id)
