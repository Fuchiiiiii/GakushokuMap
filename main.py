from maps.GakusyokuFuchigami import GakusyokuFuchigami # 1位の学食
from maps.KawachiGakushoku import KawachiGakushoku # 2位の学食
from maps.GakushokuHigaki import GakushokuHigaki # 3位の学食
from maps.MizunoGakusyoku import MizunoGakusyoku # 4位の学食

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakusyokuFuchigami(), 
        KawachiGakushoku(),
        GakushokuHigaki(),
        MizunoGakusyoku()
       ]


for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
