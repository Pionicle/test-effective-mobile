# **Playwright + Pytest + Allure: Тестирование сайта effective-mobile.ru**

- ![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
- ![Playwright](https://img.shields.io/badge/Playwright-1.49-darkgreen.svg)
- ![Allure](https://img.shields.io/badge/Allure-2.13-yellow.svg)

## **Описание**

Этот проект предназначен для автоматизированного тестирования главной страницы [effective-mobile.ru](https://effective-mobile.ru) с использованием **Playwright**, **Pytest** и **Allure**.

## **Функциональность**

- Тестирование, проверяющие переход по всем блокам по клику (О нас, Контакты и пр.)

---

## Установка Pytest

```sh
pip install -U pytest
```

---

## Установка Playwright Pytest

```sh
pip install pytest-playwright
playwright install
```

---

## Установка Allure

```sh
pip install allure-pytest
```

---

## **Запуск тестов**

### **1. Обычный запуск**

```sh
pytest -v -s
```

### **2. Запуск тестов с отчетом `Allure`**

```sh
pytest --alluredir=results
allure generate results
allure open allure-report
```

---

## **Структура проекта**

```
test-effective-mobile/
│── tests/
│   ├── test_home_page.py   # Тесты главной страницы
│
│── pages/
│   ├── home_page.py       # Главная страница
│
│── conftest.py            # Фикстуры pytest
│── requirements.txt       # Зависимости проекта
│── README.md              # Описание проекта
```

---
