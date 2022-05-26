players1 = {"野球", "サッカー", "ラグビー", "ゴルフ", "水泳"}
players2 = {"サッカー", "ソフトボール", "バスケ", "バトミントン", "スノボー"}

input("心の準備ができたらEnterキーを押してください")

common = players1 & players2
total = players1 | players2

compatibility_rate = len(common) / len(total) * 100
print(f"相性度は{compatibility_rate}パーセントでした")