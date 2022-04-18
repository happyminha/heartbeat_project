from flask import Flask, render_template, request, redirect, session
from flask import Blueprint

import models.rental as rent
import models.heart as heart

bp = Blueprint('rental', __name__, url_prefix='/rental')
rentService = rent.RentService()
heartService = heart.HeartService()


@bp.route('/')
def home():
    render_template('home.html')

@bp.route('/add')
def add_form():
    rnum = request.args.get('rnum', 0, int)
    i = rentService.getHeartByRnum(rnum)
    if len(i) == 0:
        heartData = heartService.getAedFullDown()
        data = heartData['item'][rnum - 1]
        return render_template('rental/form.html', data=data)
    else:
        msg = '이미 대여가 완료된 모델입니다. 다른 모델을 선택해 주세요.'
        return render_template('/error.html', msg=msg)


@bp.route('/setRental')
def setRental():
    rnum = request.args.get('rnum', 0, int)
    heartData = heartService.getAedFullDown()
    data = heartData['item'][rnum - 1]
    return render_template('rental/form.html', data=data)


@bp.route('/add', methods=['POST'])
def add():
    aed_name = request.form['aed_name']
    rental_id = request.form['rental_id']
    location = request.form['location']
    r_start_date = request.form['r_start_date']
    r_end_date = request.form['r_end_date']
    r_num = request.form['r_num']
    r = rent.RentVo(aed_name=aed_name, rental_id=rental_id, location=location, r_start_date=r_start_date,
                    r_end_date=r_end_date, r_num=r_num)
    rentService.addHeart(r)
    return redirect('/')


@bp.route('/mylist')
def mylist():
    id = session['id']
    data = rentService.getHeartById(id)
    return render_template('rental/mylist.html', data=data)


@bp.route('/del')
def delete():
    aed_name = request.args.get('aed_name')
    rentService.delHeart(aed_name)
    return redirect('/')


@bp.route('/list')
def list():
    rentals = rentService.getAll()  # 전체출력
    return render_template('rental/list.html', rentals=rentals)