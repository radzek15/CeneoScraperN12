# CeneoScraperN12
## Etap 1 - Pobranie składowych pojedynczej opinii o wyranym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
* Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie
* Analiza kodu HTML pojedynczej opinii

|Składowa opinii|Celektor CSS|Nazwa zmiennej|Typ danych|
|:--------------|:-----------|:-------------|:---------|
|Opinia|`div.js_product-review`|opinion|dict|
|Identyfikator opinii|`["data-entry-id"]`|opinion_id|int|
|Autor|`span.user-post__author-name`|author|str|
|Rekomendacja|`span.user-post__author-recomendation`|recomm|bool|
|Liczba gwiazdek|`span.user-post__score-count`|stars|float|
|Treść|`div.user-post__text`|content|str|
|Lista zalet|`review-feature__col:has(> div.review-feature__title--positives) > .review-feature__item` <br> `review-feature__col:has(> div[class*="positives") > .review-feature__item` <br> `div.review-feature__title--positives ~ .review-feature__item`|pros|\[str\]|
|Lista wad|`review-feature__col:has(> div.review-feature__title--negatives) > .review-feature__item` <br> `review-feature__col:has(> div[class*="negatives") > .review-feature__item` <br> `div.review-feature__title--negatives ~ .review-feature__item`|cons|\[str\]|
|Dla ilu osób użyteczna|`span[id^="votes-yes"]` <br> `button.vote-yes > span` <br> `button.vote-yes["data-total-vote"]`|useful|int|
|Dla ilu osób nieużyteczna|`span[id^="votes-no"]` <br> `button.vote-no > span` <br> `button.vote-no["data-total-vote"]`|useless|int|
|Czy opinia potwierdzona zakupem|`div.review-pz`|purchased|bool|
|Data wystawienia opinii|`span.user-post__published > time:nth-child(1)["datetime"]`|publish_date|datetime|
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date|datetime|

* Pobranie poszczególnych składowych pojedynczej opinii do indywidualnych zmiennych
* Zdefiniowanie funkcji do pobierania elementów struktury HTML z uwzględnieniem obsługi błędów

## Etap 2 - Pobranie wszystkich opinii o produkcie
* Zdefiniowanie słownika do przechowywania składwych pojedynczej opinii
* Zdefiniowanie listy do przechowywania wszystkich opinii o produkcie
* Dodanie pętli przechodzącej po wszystkich opiniach z pojedynczej strony
* Dodanie pętli przechodzącej po wszystkich stronach z opiniami o produkcie
* Eksport opinii o produkcie do pliku .json

## Etap 3 - Refaktoryzacja kodu
* Parametryzacja kodu produktu, o którym pobierane sa opinie
* Użucie słownika składowych opinii oraz wyrażenia słownikowego (dictionary comprehension) do utworzenia słownika z składowymi pojedynczej opinii

## Etap 4 - Analiza opinii pobranych dla pojedynczego produktu
* Wyliczenie podstawowych statystyk o opiniach
* Rysowanie histogramu częstości poszczególnych ocen (gwiazdek)
* Rysowanie udziału rekomendacji w zbiorze opinii