from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/lottery')
def lottery():
    # 生成六個隨機數字
    numbers = random.sample(range(1, 50), 6)  # 隨機選擇範圍從 1 到 49 的六個數字
    numbers.sort()  # 可選：對數字進行排序（可選）
    
    # HTML 模板
    html_template = '''
    <html>
        <head>
            <title>Lottery Numbers</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                .container {
                    text-align: center;
                    margin-top: 50px;
                }
                .number {
                    display: inline-block;
                    width: 40px;
                    height: 40px;
                    line-height: 40px;
                    margin: 5px;
                    text-align: center;
                    border: 2px solid black;
                    background-color: yellow;
                    font-size: 18px;
                    font-weight: bold;
                }
                .numbers {
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>樂透號碼</h1>
                <div class="numbers">
                    {% for number in numbers %}
                        <div class="number">{{ number }}</div>
                    {% endfor %}
                </div>
            </div>
        </body>
    </html>
    '''
    
    # 使用模板引擎渲染 HTML
    return render_template_string(html_template, numbers=numbers)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9527)
