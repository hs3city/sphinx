# sphinx

_beta_

## rozwijanie

Jeśli nie masz pod ręką Badgera2040, wykomentuj wszystkie linie, które go dotyczą i traktuj jak aplikację konsolową (konieczność zmiany wczytywania przycisków na zbierania inputu od gracza). Pamiętaj, by używać tylko importów, które istnieją w [MicroPythonie](https://docs.micropython.org/en/latest/library/index.html)

Sphinx nie posiada zewn. bibliotek (poza Badger2040) i raczej nie powinien ;)

## opis

Quiz działający w konsoli i na Badger2040.

Do działania potrzebuje dwóch plików 

highscores (przykład)
```
Id: 8ce0db, Points: 0/2
Id: 905ed3, Points: 1/2
Id: cec59f, Points: 2/2
```

oraz questions.json (przykład)
```
{
  "quiz": [
    {
      "question": "What do you like to eat?",
      "answers": [
        {
          "answer": "Pasta",
          "correct": false
        },
        {
          "answer": "Pizza",
          "correct": false
        },
        {
          "answer": "Yes",
          "correct": true
        }
      ]
    },
    {
      "question": "What is your favourite color",
      "answers": [
        {
          "answer": "Green",
          "correct": true
        },
        {
          "answer": "Blue",
          "correct": false
        },
        {
          "answer": "Red",
          "correct": false
        }
      ]
    }
  ]
}

```

## flow quizu

Sphinx pobiera pytania z `questions.json` i po kolei przedstawia je uczestnikowi.

Każda prawidłowa odpowiedź zwiększa wynik gracza, który jest wyświetlany na końcu i dodawany do pliku `highscores`.

Pytań może być dowolna liczba, tak długo, są zapisane w formacie w podanym przykładzie. Quiz obecnie nie zadziała dla więcej niż 3 odpowiedzi, ale zadziała, gdy więcej niż jedna odpowiedź będzie poprawna.
