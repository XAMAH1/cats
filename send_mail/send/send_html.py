def get_code(message, code):
    html_code ='''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Информационное сообщение</title>
    <style>
    body {
        margin: 0;
        padding: 0;
        background-color: #f2f2f2;
    }
    .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .header {
        text-align: center;
        margin-bottom: 20px;
    }
    .header h1 {
        color: #00b894;
    }
    .content {
        color: #333333;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 12px;
        color: #999999;
    }
    .code {
        border: 2px solid #00b894;
        padding: 10px 10px 5px;
        border-radius: 5px;
        text-align: center;
        color: #000000; /* Черный цвет текста */
        font-weight: bold;
        margin: 20px auto; /* Выравнивание по центру */
        width: 80px;
        background-color: transparent;
        letter-spacing: 5px; /* Увеличение расстояния между цифрами */
        display: block; /* Отображение внутри квадрата */
    }
    .code-label {
        font-size: 12px;
        color: #999999;
    }
    /* Дополнительные стили для темы экологического приложения */
    body {
        background-color: #eafaf1;
        font-family: Arial, sans-serif;
    }
    .container {
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .header h1 {
        color: #00b894;
        font-size: 24px;
        margin-top: 0;
    }
    .content {
        color: #333333;
        font-size: 16px;
    }
    .footer {
        color: #999999;
        font-size: 12px;
    }
    </style>
    </head>
    <body>
    <div class="container">
    <div class="header">
    <h1>CatsShop</h1>
    </div>
    <div class="content">
    <p><span id="message">%s</span></p>
    </div>
    <div class="code">
    <p id="code">%s</p>
    <span class="code-label">код</span>
    </div>
    <div class="footer">
    <p>© 2024 CatsShop. Все права защищены.</p>
    </div>
    </div>
    </body>
    </html>
    ''' % (message, code)
    return html_code