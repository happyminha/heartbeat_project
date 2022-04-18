from flask import Blueprint, render_template, request, session, redirect, json
import models.heart as h

bp = Blueprint('heartbeat', __name__, url_prefix='/heart')
heartService = h.HeartService()


@bp.route('/')
def root():
    if 'id' in session:
        return render_template('heart/loc.html')
    else:
        return '로그인 먼저 해주세요.'


@bp.route('/getheart-list', methods=['POST'])
def getheartByLoc():
    loc = request.form['loc']
    print(loc)
    infos = heartService.getBySido(loc)
    return render_template('heart/detail.html', infos=infos)


@bp.route('/get-gps')
def get_xy():
    return render_template('heart/coordinate.html')


@bp.route('/marker')
def test_form():
    if 'id' in session:
        return render_template('heart/marker.html')
    else:
        return '로그인 먼저 해주세요.'



@bp.route('/showAllHeart', methods=['POST'])
def showAllHeart():
    hearts = heartService.getAedFullDown()
    return json.dumps(hearts)

@bp.route('/getorg')
def getByOrg_form():
    if 'id' in session:
        return render_template('heart/org.html')
    else:
        return '로그인 먼저 해주세요.'


@bp.route('/getorg', methods=['POST'])
def getByOrg():
    org = request.form['org']
    infos = heartService.getByOrg(org)
    if infos != None:
        return render_template('heart/detail.html', infos=infos)
    else:
        msg = '검색 결과가 없습니다.'
        return render_template('/error.html', msg=msg)
