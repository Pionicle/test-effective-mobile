FROM python:3.10.16-slim-bookworm


# Необходимые инструменты для установки Allure
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Установка JDK 17
RUN apt-get update && \
    apt install -y openjdk-17-jre-headless


# Установка Allure
RUN curl -L -o allure-2.32.0.zip https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.zip && \
    unzip allure-2.32.0.zip &&  \
    mv allure-2.32.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/local/bin/allure && \
    rm allure-2.32.0.zip


# Установка зависимостей 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Установка chromium для Playwright
RUN playwright install --with-deps chromium


# Копирование файлов проекта
WORKDIR /app
COPY . .


# Запускаем тесты и генерируем отчет Allure
CMD ["sh", "-c", "pytest --alluredir=results && allure generate results --clean -o allure-report && allure open allure-report -p 5952"]