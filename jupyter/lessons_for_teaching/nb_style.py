from IPython.core.display import HTML
css_html = open('custom.css', 'r').read()
HTML('<style>{}</style>'.format(css_html))
print("Loaded custom css")

