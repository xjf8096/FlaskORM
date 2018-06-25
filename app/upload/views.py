from flask import Blueprint, request, render_template

from app.ext import images

upload_blue=Blueprint('upload',__name__)
'''
必须是post请求 
form-data
'''
@upload_blue.route('/img/',method=['GET','POST'])
def upload_img():
    if request.method=='POST':
    #文件上传对象
        images.save(request.files['img'])
        return ''
    elif request.method=='GET':
        return render_template('upload.html')


