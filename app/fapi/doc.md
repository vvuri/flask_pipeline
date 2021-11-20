## FastAPI
FastAPI построен на базе Starlette и Pydantic.
- **Starlette** — ASGI микро-фреймворк для написания веб-приложений.
- **Pydantic** — библиотека для парсинга и валидации данных основанная на Python type-hints.
- **Uvicorn** — это ASGI-совместимый веб-сервер, который мы будем использовать для запуска нашего приложения.

Run server: 
- так прав не хватает ```$ uvicorn main:app --reload```
- через ```uvicorn.run(app, host='0.0.0.0', port=8000)``` работает

Swagger: ```http://127.0.0.1:8000/docs```

