from maps.AbstractGakushoku import AbstractGakushoku

class KawachiGakushoku(AbstractGakushoku):
    def get_menu(self):
        return "唐揚げ定食"

    def get_summary(self):
        return "ボリューム満点でコスパが良く、揚げたてで美味しい！"

    def get_author(self):
        return "川地康介"
