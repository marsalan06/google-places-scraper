from google_places_scraper import GooglePlacesScraper

scraper = GooglePlacesScraper(api_key="Your-API-Key-Here")
scraper.run(
    user_location_input="Disco Bakery Karachi Pakistan",
    radius=1000,
    export_format="csv",     # or json / yaml
    type_="school",
    max_results=13
)
