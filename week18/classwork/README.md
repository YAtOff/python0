# Notes

Напишете програма за водене на бележки.
Бележките трябва да се съхраняват във файл наречен `notes.json` в `JSON` формат.
Една бележка трябва да има такава структура:

```python
{
    "title": "some title",
    "description": "some description"
}
```

Всичките бележки да се пазят в списък.

Програмата трябва да има меню с комманди.
Ето и пример за сесия с програмата:

```
List (1)
Get (2)
Add (3)
Delete (4)
> 1

1: Note 1
2: Note 2
3: Note 3

List (1)
Get (2)
Add (3)
Delete (4)
> 3

Note number > 1

Note 1 descriptoins

List (1)
Get (2)
Add (3)
Delete (4)
> 3

Title > Note 4
Description > Note 4 description

List (1)
Get (2)
Add (3)
Delete (4)
> 1

1: Note 1
2: Note 2
3: Note 3
4: Note 4

List (1)
Get (2)
Add (3)
Delete (4)
> 4

Note number > 2

List (1)
Get (2)
Add (3)
Delete (4)
> 1

1: Note 1
2: Note 3
3: Note 4
```

Как да прочетем бележките от файл?

```python
import os.path
import json

if os.path.exists("notes.json"):
    with open("notes.json") as file:
        notes = json.load(file)
else:
    notes = []
```

Как да запишем бележките от файл?

```python
with open("notes.json", "w") as file:
    json.dump(notes, file)
```