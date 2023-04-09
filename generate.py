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
    <title>EPOCH Lab</title>
    <link rel="icon" type="image/png" href="/images/favicon.png?">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata&display=swap">
    <link rel="stylesheet" href="styles.css">
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
    articles_html = ''.join([f'<li><a href="article/{article["title"]}.html">{article["id"]}</a></li>' for article in articles])
    return template.format(articles=articles_html)

def generate_article(article):
    template = '''
<!DOCTYPE html>
<html>
<head>
    <title>EPOCH Lab | {title}</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata&display=swap">
    <style>
        body {{
            background-color: black;
            color: white;
            font-family: 'Inconsolata', sans-serif;
            padding-left: 5px;
        }}
        a {{
            color: white;
            text-decoration: none;
        }}
        img {{
            width: 930px;
        }}
    </style>
</head>
<body>
    <div>
        <p><a href="../index.html"><</a> {date}</p>
        <p>{content}</p>
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
        save_file(f'article/{article["title"]}.html', generate_article(article))

if __name__ == '__main__':
    main()