# yshalsager Personal Website

This is my website that is built using Flask and Bootstrap.

It's being used as a portfolio, a place for my various projects, and a mini-blog in Arabic and English.

The used template is [Start Bootstrap - Clean Blog](https://github.com/StartBootstrap/startbootstrap-clean-blog). This template doesn't support RTL, so I had to use [Bootstrap RTL](https://github.com/MahdiMajidzadeh/bootstrap-v4-rtl) with some custom CSS to get everything done correctly.

Since I tried to avoid unnecessary complexity I have used Python markdown library to render blog content into HTML and a dynamic flask routes register.

The multilingualism of the website is done using Flask-Babel and a simple force locale since I want the website to be available in languages I speak only. Also, not all of the content will be the same on both versions of the website.

I have used Flask-Sitemap and feedgen to generate a sitemap and RSS feeds for the website. I will think of more stuff to come later.
