import os
import csv

def save_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def generate_homepage(articles):
    template = '''
<!DOCTYPE html>
<html>
<head>
    <title>epochlab</title>
    <link rel="icon" type="image/png" href="/images/favicon.png?">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata&display=swap">
    <style>
        .image-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }}
        .image-container img {{
            max-width: 100%;
            max-height: 100%;
        }}
        ul {{
            display: flex;
            flex-wrap: nowrap;
            margin: 5;
            padding: 0;
            list-style-type: none;
            gap: 1rem;
        }}
        a {{
            color: black;
            text-decoration: none;
        }}
        body {{
            font-family: 'Inconsolata', sans-serif;
        }}
    </style>
</head>
<body>
    <div class="image-container">
        <img src="https://github.com/epochlab/archive/blob/main/sample.png?raw=true">
        <ul>{articles}
        </ul>
    </div>
</body>
</html>
'''
    articles_html = ''.join([f'<li><a href="article/{article["id"]}.html">{article["id"]}</a></li>' for article in articles])
    return template.format(articles=articles_html)

def generate_article(article):
    template = '''
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata&display=swap">
    <style>
        body {{
            background-color: black;
            color: white;
            font-family: 'Inconsolata', sans-serif;
        }}
        a {{
            color: white;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div>
    <p><a href="../index.html"><</a> {date}</p>
    </div>
</body>
</html>
'''
    return template.format(**article)

def main():
    with open('articles.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        articles = list(reader)

    os.makedirs('article', exist_ok=True)
    save_file('index.html', generate_homepage(articles))

    for article in articles:
        save_file(f'article/{article["id"]}.html', generate_article(article))

if __name__ == '__main__':
    main()