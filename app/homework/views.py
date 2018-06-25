from flask import Blueprint, request, render_template, redirect

from app.ext import db
from app.shop.models import Shop

homework = Blueprint('homework', __name__, template_folder='templates')


@homework.route('/list/')
def list():
    # get
    page = request.values.get('page', default=1, type=int)
    #paginate = User.query.order_by(User.uid).paginate(page=page, per_page=size, error_out=False)

    size = request.values.get('size', default=10, type=int)
    paginat = db.session.query(Shop.sid, Shop.name).order_by(Shop.sid).paginate(page=page, per_page=size, error_out=False)
    shops = paginat.items
    return render_template('shops.html', shops=shops,paginate=paginat )


@homework.route('/add/', methods=['get', 'post'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.values.get('name')
        cid = request.values.get('cid', default=1, type=int)
        shop = Shop(name=name, cid=cid)
        db.session.add(shop)
        db.session.commit()
        return redirect('/work/list/')


@homework.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        sid = request.values.get('sid', type=int)
        shop = Shop.query.get(sid)
        return render_template('update.html', shop=shop)
    elif request.method == 'POST':
        sid = request.values.get('sid', type=int)
        cid = request.values.get('cid', type=int)
        name = request.values.get('name')
        Shop.query.filter(Shop.sid == sid).update({Shop.cid: cid, Shop.name: name})
        db.session.commit()
        return redirect('/work/list/')


@homework.route('/del/')
def delete():
    sid = request.values.get('sid', type=int)
    db.session.delete(Shop.query.get(sid))
    db.session.commit()
    return redirect('/work/list/')
