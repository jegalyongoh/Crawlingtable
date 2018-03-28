from flask import Flask, render_template, json
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

url = "https://www.rottentomatoes.com//"    # 크롤링하고싶은 페이지 url 입력
html = urlopen(url)
source = html.read()                            # 소스를 읽는다
html.close()                                    # 모두 진행한 후 close 해준다


soup = BeautifulSoup(source, "html5lib")
table = soup.find(id="Top-Box-Office")
movies = table.find_all(class_="middle_col")
grade = table.find_all(class_="tMeterScore")


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/Crawling', methods=['POST'])               # ajax를 이용하기 위한 페이지
def Crawling():
    index = 0
    data = []
    for movie in movies :
        title = movie.get_text()                    # 제목 크롤링
        title.strip()
        link = movie.a.get('href')                      # link 크롤링
        urlCraw = 'https://www.rottentomatoes.com' + link
        gra = grade[index].get_text()                                           # 평점 크롤링
        index += 1
        push_data = [
            title, urlCraw, gra                                 #가지런히 정리
        ]
        data.append(push_data)                              # 잘 정리된 배열삽입
    return json.dumps({'data': data})                   # json파일로 이동

if __name__== "__main__":
    app.run()



