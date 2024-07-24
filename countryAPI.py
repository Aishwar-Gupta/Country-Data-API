# pip3 install fastapi
# pip3 install uvicorn

from fastapi import FastAPI
import scrapper

app = FastAPI()


@app.get("/")
def home():
    dictionary = {"/all-countries": "List of all the countries in the world.",
                  "/{Alphabet}": "List of all countries that start with that {Alphabet}.",
                  "/population/{country}": "Returns the Population of the {country}.",
                  "/country-population/{count}": "Return {count} number of country's population in alphabetical order."}
    return dictionary


@app.get("/all-countries")
def all_countries():
    return scrapper.all_countries()


@app.get("/{letter}")
def country_by_letter(letter):
    return scrapper.country_by_letter(letter.upper())


@app.get("/population/{country}")
def country_population(country):
    return scrapper.country_population(country)


@app.get("/country-population/{count}")
def populations(count):
    return scrapper.population(count)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
