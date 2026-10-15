from maps.AbstractGakushoku import AbstractGakushoku

class GakushokuSample(AbstractGakushoku):

    def get_menu(self):
        return "すき家のネギトロ丼です"

    def get_summary(self):
        return "正直そこまで美味しそうに見えない見た目なのにしっかり美味しいところ"

    def get_author(self):
        return "水野　結音"