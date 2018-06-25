from flask import Blueprint

from app.ext import cache

cache_blue=Blueprint('cache01',__name__,template_folder='templates')
'''
timeout 过期时间
key_prefix 缓存key的前缀
unless:回调函数 当返回True 缓存不起作用
'''
@cache.cached(timeout=60,key_prefix='view_%s')
@cache_blue.route('/cache/')
def test():
    print('1111')
    return '1111111'
'''
make_name 是一个函数 返回string类型
'''
@cache_blue.route('/2/<name>')
@cache.memoize(timeout=60,)
def test2(name):
    print('name')
    return '1111111'