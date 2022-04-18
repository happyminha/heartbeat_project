# https://developers.kakao.com/docs/latest/ko/local/dev-guide#search-by-category
# 카카오 개발 가이드

# 카카오맵 api key
# bb08ed24532efc695296b299586fd991

# 자동심장 충격기 api key
# 9JVC8qrDZUUkrmVHQDWSA9wAC6EbU3AdXudhkpnIuNTUF1nHlPlYdhuU%2FhBiwkoZrLkSLWAKtYqaOc0WSC8gqw%3D%3D


from flask import Flask, render_template, request
import routes.mem_route as rm
import routes.rental_route as rr
import routes.heart_route as hr


app = Flask(__name__)

app.secret_key = 'affdasdf'

app.register_blueprint(rm.bp)
app.register_blueprint(rr.bp)
app.register_blueprint(hr.bp)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
