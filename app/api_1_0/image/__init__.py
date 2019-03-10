# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 17:53
@Author  : Young
@QQ      : 403353323 
@File    : __init__.py
@Software: PyCharm
"""
from flask import Blueprint
from flask_restful import Api
from app.api_1_0.image.add_image import AddPicture
from app.api_1_0.image.get_image import GetAllImage, GetOneImage
from app.api_1_0.image.delete_image import DeleteImage

image = Blueprint('image', __name__)
source = Api(image)

source.add_resource(AddPicture, '/addImage', endpoint='add_picture')
source.add_resource(GetAllImage, '/getAllImage', endpoint='get_all_image')
source.add_resource(GetOneImage, '/getOneImage/<string:image_uuid>', endpoint='get_one_image')
source.add_resource(DeleteImage, '/deleteImage/<string:image_uuid>', endpoint='delete_image')
