import logging

import server


# NOTE(vanya): Print debug info from the server
logging.basicConfig()


app = server.App()


@app.route("/")
def route_index() -> bytes:
    return app.render_html_file("./pages/index.html").encode("utf-8")


@app.route("/favicon.ico")
def route_favicon() -> bytes:
    return app.load_file_bytes("./public/favicon.ico")


@app.route("/sex")
def route_favicon() -> bytes:
    return app.load_file_bytes("sex.mp4")


app.register_components_from_dir("./components/")
app.set_public_dir("./public/", server.PublicAccessPolicy.SERVE_ALL)
app.serve_until_KeyboardInterrupt("localhost", 8005)
