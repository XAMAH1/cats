import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from cart.copy_cart.copy_cart import copy_user_cart
from cart.delete_cart.delete_cart import delete_cart
from cart.delete_cart.delete_cart_all import delete_cart_all
from cart.get_cart.get_cart_all import get_all_cart
from cart.post_cart.post_cart import new_cat_in_cart

cart_user = Blueprint('cart_user', __name__)


@cart_user.route("/cart", methods=["GET", "DELETE", "POST"])
@cross_origin()
def user_cart_methods():
    if request.method == "GET":
        return asyncio.run(get_all_cart())
    if request.method == "DELETE":
        return asyncio.run(delete_cart_all())
    if request.method == "POST":
        return asyncio.run(new_cat_in_cart())


@cart_user.route("/cart/<int:cart_id>", methods=["DELETE"])
@cross_origin()
def get_user_id(cart_id):
    if request.method == "DELETE":
        return asyncio.run(delete_cart(cart_id))


@cart_user.route("/cart/copy/<int:user_id>", methods=["POST"])
@cross_origin()
def copy_user_id(user_id):
    if request.method == "POST":
        return asyncio.run(copy_user_cart(user_id))
