#!/usr/bin/env python
# -*- coding:utf-8 -*-


# The main HTML for the whole page.
PAGE_HTML = """
<p>Welcome, {name}!</p>
<p>Products:</p>
<ul>
{products}
</ul>
"""
# The HTML for each product displayed.
PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"


def make_page(username, products):
    product_html = ""
    for prodname, price in products:
        product_html += PRODUCT_HTML.format(
            prodname=prodname, price=price)
    html = PAGE_HTML.format(name=username, products=product_html)
    return html


if __name__ == '__main__':
    print make_page("pangweili", [{'book1', 100}, {'book2', 100}, {'book3', 100}, {'book4', 100} ])
