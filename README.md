# Spotify Visualization App

#### By: <a href="https://github.com/Tatraa">Kacper Tatrocki</a>, <a href="https://github.com/marcins21">Marcin Sitko</a>, <a href="https://github.com/mvtzmv">Maria Żuchwoska</a>, <a href="https://github.com/IngaKiepas">Inga Kiepas</a> 



# Dokumentacja 
| Plik                                                         | 
|--------------------------------------------------------------|
| [main_page.py](#mainpagepy)                                  |   
| [charts.py](#chartspy)                                       |   
| [spotifySt.py](#spotifystpy)                                 |   
| [pages/similar_songs.py](#pagessimilarsongspy)               |   
| [pages/artist_album_of_the_year](#pagesartistalbumoftheyear) |  
|                                                              |  
|                                                              |   


# main_page.py

### Importowane biblioteki:
    streamlit - służy do tworzenia interfejsu użytkownika.
    plotly_express - używany do tworzenia wykresów interaktywnych.
    search_track i search_artist z modułu spotifySy  - funkcje związane z wyszukiwaniem utworów i artystów w serwisie Spotify.
    charts - moduł zawierający funkcje do tworzenia wykresów plik [charts.py](#chartspy) .

**_NOTE:_** st.set_page_config(layout='wide') - ustawia szeroki układ strony.

### Funkcje 
    load_data(path: str)`-> pd.DataFrame - funkcja, która wczytuje dane z pliku CSV o podanej ścieżce i zwraca ramkę danych (DataFrame) za pomocą biblioteki pandas.
    Jeśli plik nie istnieje, wyświetla komunikat o błędzie.

    home_page(data) - funkcja reprezentująca stronę główną. Tworzy różne wykresy i interaktywne elementy na stronie, takie jak przyciski rozwijane, zakładki, kontener do odtwarzania muzyki itp.
# charts.py
**_NOTE:_** Moduł służący do implementacji wykresów 

# spotifySt.py

### Funkcje 
    search_track(query) - funkcja przyjmuje jako argument zapytanie (query) i zwraca adres URL do fragmentu utworu z Spotify. Wykorzystuje metodę `sp.search` z biblioteki spotipy do wyszukania utworu na podstawie zapytania.
    search_artist(query, use_custom_width=None) - funkcja przyjmuje jako argument zapytanie (query) i opcjonalnie szerokość (use_custom_width). Wykorzystuje metodę sp.search z biblioteki spotipy do wyszukania artysty na podstawie zapytania. Wyświetla zdjęcie artysty, jeśli istnieje, używając biblioteki streamlit.
    search_albums(query, use_custom_width=None) - Funkcja wszukuje albumy oraz wykorzystuje te same kwestie co `search_artist(query, use_custom_width=None)
# pages/similar_songs.py

### Klasa Song:

    Metoda __init__ - konstruktor klasy Song, inicjalizuje obiekt Song z podanymi atrybutami: name, dnce, nrgy, bpm, top_genre i artist.

### Klasa MusicRecommendationSystem:

    Metoda __init__ - konstruktor klasy MusicRecommendationSystem, inicjalizuje obiekt MusicRecommendationSystem z podanym atrybutem sensitivity.
    Metoda add_song - dodaje utwór do systemu rekomendacji.
    Metoda find_similar_songs - znajduje podobne utwory na podstawie wybranego utworu. Opcjonalnie, gdy get_selected_song jest ustawione na True, zwraca wybrany przez użytkownika utwór.
    Metoda calculate_similarity - oblicza podobieństwo między dwoma utworami na podstawie ich cech.
    Metoda get_similarity - zwraca wartość miary podobieństwa między utworami.

### Funkcja load_data:

    Dekorator @st.cache_data - dekorator funkcji, który cache'uje wynik funkcji na podstawie podanego argumentu path.
    Funkcja load_data - wczytuje dane z pliku CSV na podstawie ścieżki path i zwraca ramkę danych.

### Funkcja runner:

    Wczytuje dane z pliku CSV za pomocą funkcji load_data.
    Tworzy obiekt  "Music Recommendation System".
    Zarządza wrażliwością (sensitivity) systemu rekomendacji przy użyciu suwaka.
    Inicjalizuje obiekt MusicRecommendationSystem i dodaje do niego utwory na podstawie wczytanych danych.
    Tworzy kontener na odtwarzacz Spotify.
    Pozwala użytkownikowi wybrać utwór z listy dostępnych utworów.
    Wyświetla informacje o wybranym utworze, w tym zdjęcie artysty i odtwarzacz Spotify.
    Znajduje podobne utwory na podstawie wybranego utworu i wyświetla je wraz z informacjami i odtwarzaczem Spotify.

# pages/artist_album_of_the_year
test

