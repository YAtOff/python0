# Как да инсталираме PyGame на Windows

## Добавете Python към системния път

За да е достъпен Python през терминала (програмата "Command Prompt"), пътят до
директорията, където е инсталиран Python трябва да се добави към системния път.
Има два начина това да се направи:

 - при инсталация на Python, на първата стъпка има отметка "Add Python 3.5 to PATH" (има го само за новите версии)
 - [следвайте инструкциите] (https://www.webucator.com/blog/wp-content/uploads/2015/03/add-python-to-path.png)

## Инсталиране на пакета "wheel"

- Отворете "Command Prompt"
- изпълнете командата `pip install wheel`

## Изтеглете PyGame подходящ за вашата версия на Python и Windows

От [този сайт] (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame) изтеглете един от:

 - pygame-1.9.2a0-cp34-none-win32.whl
 - pygame-1.9.2a0-cp34-none-win_amd64.whl
 - pygame-1.9.2a0-cp35-none-win32.whl
 - pygame-1.9.2a0-cp35-none-win_amd64.whl

В "Command Prompt" навигирайте до директорията с изтегления файл.
Изпълнете команде `pip install {име на файла}`

Напр.: `pip install pygame-1.9.2a0-cp35-none-win32.whl`
