import asyncio
from flask import Blueprint, request

from cart.copy_cart.copy_cart import copy_user_cart
from cart.delete_cart.delete_cart import delete_cart
from cart.delete_cart.delete_cart_all import delete_cart_all
from cart.get_cart.get_cart_all import get_all_cart
from cart.post_cart.post_cart import new_cat_in_cart
from reuests_options.requests_options import decorator_options
from user.get_profile.get_profile import get_user_profile
from user.get_profile.get_profile_id import get_user_profile_id
from user.picture.main import user_profile_picture
from user.put_profile.put_profile import put_user_profile

cart_user = Blueprint('cart_user', __name__)


@cart_user.route("/cart", methods=["GET", "DELETE", "POST"])
def user_cart_methods():
    if request.method == "GET":
        return asyncio.run(get_all_cart())
    if request.method == "DELETE":
        return asyncio.run(delete_cart_all())
    if request.method == "POST":
        return asyncio.run(new_cat_in_cart())


@cart_user.route("/cart/<int:cart_id>", methods=["DELETE"])
def get_user_id(cart_id):
    if request.method == "DELETE":
        return asyncio.run(delete_cart(cart_id))


@cart_user.route("/cart/copy/<int:user_id>", methods=["POST"])
def copy_user_id(user_id):
    if request.method == "POST":
        return asyncio.run(copy_user_cart(user_id))
