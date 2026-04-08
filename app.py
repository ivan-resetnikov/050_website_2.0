import logging

import server

from components.article import Article



def create_app() -> None:
    # NOTE(vanya): Print debug info from the server
    logging.basicConfig()


    app = server.App()


    @app.route("/favicon.ico")
    def route_favicon() -> bytes:
        return app.load_file_bytes("./public/favicon.ico")


    @app.route("/")
    def route_index() -> bytes:
        return app.render_html_file("./pages/index.html").encode("utf-8")


    @app.route("404")
    def route_index() -> bytes:
        return app.render_html_file("./pages/404.html").encode("utf-8")


    @app.route("/article/[id]")
    def route_index(p_catchall: dict) -> bytes:
        return app.render_html_file("./pages/article.html", article=Article.from_html(f"./articles/{ p_catchall.get("id") }.html")[0].render_html()).encode("utf-8")


    app.register_components_from_dir("./components/")
    app.set_public_dir("./public/", "/public/", server.PublicAccessPolicy.SERVE_ALL)
    app.serve_until_KeyboardInterrupt("localhost", 8005)



if __name__ == "__main__":
    create_app()
