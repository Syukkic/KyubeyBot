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
        browser.quit()

        with open('artwork_links.pkl', "wb") as f:
            pickle.dump(artwork_links, f)


if __name__ == '__main__':
    artists_id = ['30959821', '2188232', '10453155', '32008', '8517776', '71312', 
                  '6269645', '1056186', '13695413', '2254287', '12064216', 
                  '2131660', '4935', '11211325', '490219', '12411452', '158395',
                  '187034', '3673728', '17089321', '59205', '366788', '7457683', 
                  '163536', '1565632', '126905', '27517', '20223617', '1710950', 
                  '20223617', '1710950', '810305', '47488', '143452', '935581']  # pixiv user id
    collect_art_id(artists_id)
