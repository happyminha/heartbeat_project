from flask import Flask, render_template, request, redirect, session
from flask import Blueprint

import models.member as mem

bp = Blueprint('member', __name__, url_prefix='/member')
memService = mem.MemService()


@bp.route('/join')
def join_form():
    return render_template('member/join.html')


@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    region = request.form['region']
    tel = request.form['tel']
    m = mem.MemVo(id, pwd, name, region, tel)
    memService.addMember(m)
    return redirect('/')


@bp.route('/login')
def login_form():
    return render_template('member/login.html')


@bp.route('/login', methods=['POST'])
def login():
    msg = ''  # 로그인 상태 메시지 저장
    path = 'member/login.html'  # 처리 완료 후 이동할 페이지의 경로

    # 로그인 폼에서 입력 값 받음
    id = request.form['username']
    pwd = request.form['password']

    # 입력받은 id로 검색
    m = memService.getMember(id)
    if m == None:
        msg = '없는 아이디입니다. 회원가입을 먼저 해주세요'
    else:
        if pwd == m.pwd:
            session['id'] = id
            path = 'home.html'
            msg = '로그인 성공'
        else:
            msg = '패스워드가 일치하지 않습니다.'
    return render_template(path, msg=msg)

@bp.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id', None)
    return redirect('/')


@bp.route('/getmember')
def getMember():
    if 'id' in session:
        id = session['id']
        m = memService.getMember(id)
    else:
        return '로그인을 해주세요.'

    return render_template('member/detail.html', mem=m)


@bp.route('/edit', methods=['POST'])
def edit():
    id = request.form['id']
    pwd = request.form['pwd']
    tel = request.form['tel']
    region = request.form['region']
    m = mem.MemVo(id=id, pwd=pwd, tel=tel, region=region)
    memService.editMember(m)
    return redirect('/')

@bp.route('/del')
def delete():
    id = session['id']
    memService.delMember(id)
    session.pop('id', None)
    return redirect('/')