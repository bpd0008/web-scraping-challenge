from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars = {}
    
    #1
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find('div', class_='content_title')
    news_title = soup.find('a').text
    print(news_title)

    news_p = soup.find('div', class_='article_teaser_body').text
    print(news_p)
    
    #2
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find('article', class_='carousel_item')

    footer = articles.find('footer')
    link = footer.find('a')
    featured_image_url = link['data-fancybox-href']

    print('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' + href)

    #3
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    table = pd.read_html(url)
    #table
    df = table[0]
    #df
    html_t = df.to_html()
    html_t
    
    #4
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    
    cer = soup.find('div', class_='downloads')
    link = cer.find('a')
    cerberus_href = link['href']

    print(cerberus_href)
    
    
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    
    schia = soup.find('div', class_='downloads')
    link = schia.find('a')
    schia_href = link['href']

    print(schia_href)
    
    
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    
    syrtis = soup.find('div', class_='downloads')
    link = syrtis.find('a')
    syrtis_href = link['href']

    print(syrtis_href)
    
    
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    
    valles = soup.find('div', class_='downloads')
    link = valles.find('a')
    valles_href = link['href']

    print(valles_href)
    
    
    hemisphere_image_urls = [
    {'title': 'Valles Marineris Hemisphere', 'img_url': valles_href},
    {'title': 'Syrtis Major Hemisphere', 'img_url': syrtis_href},
    {'title': 'Schiaparelli Hemisphere', 'img_url': schia_href},
    {'title': 'Cerberus Hemisphere', 'img_url': cerberus_href}
    ]
    
    browser.quit()
    return hemisphere_image_urls.py