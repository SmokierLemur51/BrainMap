"""

"""
from quart import Blueprint, render_template

public = Blueprint("public", __name__, template_folder="public_templates", url_prefix="/")


@public.route("/")
async def index():
	elements = {"title": "Joint Journal"}
	return await render_template("index.html", elements=elements)


@public.route("/creator")
async def creator():
	elements = {"title": "The Creator"}
	return await render_template("creator.html", elements=elements)


@public.route("/joint-journal")
async def journal_info():
	elements = {"title": "Joint Journal"}
	return await render_template("journal_info.html", elements=elements)


@public.route("/business")
async def business():
	return await render_template("business.html", elements=elements)