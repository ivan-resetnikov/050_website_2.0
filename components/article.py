import logging
import os
import datetime

from server import App



class ArticleError:
    SUCCESS: int = 0
    FILE_NOT_FOUND: int = 1



class Article:
    def __init__(self):
        self.html_source: str = ""
        self.creation_datetime: datetime = datetime.datetime.fromtimestamp(0)


    @classmethod
    def from_html(self, p_path: str):
        a = Article()

        if not os.path.exists(p_path):
            logging.error(f"Cannot load Article from an .html file `{p_path}` - file does not exist.")
            return (a, ArticleError.FILE_NOT_FOUND)

        with open(p_path, "r", encoding="utf-8") as f:
            raw_html_source: str = f.read()
        
        html_source: str = ""
        for line in raw_html_source.split("\n"):
            if line.startswith("@"):
                attribute_tokens: list[str] = line.split(" ")

                match attribute_tokens[0]:
                    case _:
                        pass
            else:
                html_source += line + "\n"
        
        a.html_source = html_source

        return (a, ArticleError.SUCCESS)
    

    def render_html(self) -> str:
        head: str = f"""
                <table>
                    <tr>
                        <th>
                            <img src="/public/pictures/pfp.png" class="pfp">
                        </th>
                        <td>
                            <p style="margin: 0">
                                <b>@vanya</b><br>
                                yapped on
                                <time datetime="{ self.creation_datetime.isoformat() }">{ self.format_datetime_as_human_readable(self.creation_datetime) }</time>
                            </p>
                        </td>
                    </tr>
                </table>
            """
        
        return head + self.html_source
    

    def format_datetime_as_human_readable(self, p_datetime: datetime.datetime) -> str:
        return p_datetime.strftime("%B %d, %Y at %I:%M %p")



def register_components_for_app(p_app: App) -> None:

    # @p_app.component("article")
    # def render_article() -> str:
    #     return "UNIMPLEMENTED Article component"

    pass
