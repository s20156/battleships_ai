from movie_recommendations import generate_recommendations
import click
import json


"""
Realizacja projektu:
* Cezary Malejka
* Mateusz Grube

Projekt ma na celu zaproponowanie użytkownikowi filmów, których nie oglądał, a które - bazując na znajomości gustu i poprzez porównanie z innymi użytkownikami - mogą najbardziej lub najmniej Mu się podobać.

Instrukcja:
Aby uruchomić projekt należy uruchomić plik main.py za pomocą interpretera pythona korzystając z opcji, które narzędzie CLI wyświetli w konsoli.
"""


@click.command()
@click.option("--recommend", "mode", flag_value="recommend", default=True)
@click.option("--dissuade", "mode", flag_value="dissuade", default=False)
@click.option("--name", prompt="Provide name of the user", help="Provide the name of the user")
def recommend(mode, name):
    data_file = "movie_ratings.json"
    with open(data_file, "r") as f:
        data = json.loads(f.read())
    try:
        recommendations = generate_recommendations(data, name)
        if mode == "recommend":
            movies = recommendations[0:5]
            print("Rekomendowane filmy:")
        elif mode == "dissuade":
            movies = recommendations[-1: -6: -1]
            print("Odradzane filmy")

        for movie in movies:
            print(movie)

    except TypeError:
        print("Error: User not in database")


if __name__ == '__main__': recommend()