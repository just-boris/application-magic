### Дипломная работа
## Расчет эффективности стыковки волноводов с помощью интеграла перекрытия

В этом репозитории содержится текст работы и исходный код для создания иллюстраций.
Кроме того, для работы была написана вторая программа - [Py-plot](https://github.com/just-boris/Py-plot)

Текст работы написан в **_LaTeX_**, иллюстрации конвертируются из svg или строятся в **Mathplotlib**.

## Сборка проекта

### Установка зависимостей

1. Склонировать данный git-репозиторий или [скачать](https://github.com/just-boris/application-magic/archive/master.zip)
1. Установить Make если он не предустановлен в системе. Для windows предлагается [GnuMake](http://gnuwin32.sourceforge.net/packages/make.htm)
1. Установить интерпретатор Python 2.7, если его еще нет в системе
1. Установить [PIP](http://www.pip-installer.org/ru/latest/installing.html) - менеджер пакетов
1. Установить все необходимые модули `pip install -r requirements.txt`
1. Установить модули, указанные в 8 шаге установки [Py-plot](https://github.com/just-boris/Py-plot)
1. Установить [Inkscape](http://inkscape.org/download/?lang=ru) для конвертации изображений
1. Установить среду сборщик LaTeX - [Texmaker](http://www.xm1math.net/texmaker/download.html)
1. Выполнить `make`

Необходимые иллюстрации собираются в папку `img/`, собранный pdf находится в `build/`

Буду рад дополнениям и пожеланиям, которые вы можете оставить в виде issues к этому репозиторию!