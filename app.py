import dash
from dash import Dash, html
import logger
import flask
import os

logger

app = Dash(__name__, use_pages=True, external_stylesheets=['https://use.fontawesome.com/releases/v5.7.2/css/all.css'], meta_tags=[{'name':'viewport','content':"width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no, maximum-scale=1"},{'name':"apple-mobile-web-app-capable",'content':'yes'},{'name':"apple-mobile-web-app-status-bar-style",'content':"black-translucent"}])

server = app.server
app.scripts.config.serve_locally = False
app.scripts.append_script({
    'external_url': "https://www.googletagmanager.com/gtag/js?id=G-7KZYT80WN5"}
)
app.scripts.append_script({
    'external_url': "https://cdn.jsdelivr.net/gh/RobinGuerard21/AlpineFanApp/main/gtag.js"}
)

app.layout = html.Div(className="window", children=[
    html.Link(rel="manifest", href="/assets/site.webmanifest"),
    # Beginning of the sidebar
    html.Div(className="side-bar", children=[
        # Top part of the sidebar
        html.Div(className="vert-nav", children=[
            html.A(children=html.Img(className="logo", src=app.get_asset_url('images/logo.png')), href='/'),
            html.A(href='/grand-prix', children=html.Div(className="link",
                                                         children=[html.I(className="fas fa-flag-checkered"),
                                                                   html.Label(className="desktop",
                                                                              children='Grand Prix')])),
            html.A(href='/seasons', children=html.Div(className="link",
                                                      children=[html.I(className="fas fa-trophy"),
                                                                html.Label(className="desktop", children='Seasons')])),
            html.A(href='/statistics', children=html.Div(className="link",
                                                         children=[html.I(className="fas fa-chart-line"),
                                                                   html.Label(className="desktop",
                                                                              children='Statistics')]))
        ]),
        # Bottom part of the sidebar
        html.Div(className="vert-nav", children=[
            html.A(href='/documentation', children=html.Div(className="link",
                                                            children=[html.I(className="fas fa-book"),
                                                                      html.Label(className="desktop",
                                                                                 children='Documentation')])),
            html.A(href='/notebooks', children=html.Div(className="link",
                                                        children=[html.I(className="fas fa-file"),
                                                                  html.Label(className="desktop",
                                                                             children='Notebooks')])),
            html.A(href='/contact', children=html.Div(className="link",
                                                      children=[html.I(className="fas fa-address-card"),
                                                                html.Label(className="desktop", children='Contact')]))
        ]),
    ]),
    # End of the sidebar
    # Pages part
    dash.page_container

]
                      )


@server.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(server.root_path, 'assets'),
                                     'favicon.ico')


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
