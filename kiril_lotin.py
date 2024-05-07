
kril_harflar = "ёйцукенгшщзхъэждлорпавыфячсмитьбюўғқҳЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЎҒҚҲЁ"

lotin_harflar = "qertyuioplkjhgfdsazxvbnmQERTYUIOPLKJHGFDSAZXVBNM"

#Kril lotin lug'ati
kiril_lotin = {"й":"y", "ц":"ts", "у":"u", "к":"k", "е":"e", "н":"n", "г":"g", "ш":"sh",
              "щ":"sh", "з":"z", "х":"x", "ъ":"'", "э":"e", "ж":"j", "д":"d", "л":"l",
              "о":"o", "р":"r", "п":"p", "а":"a", "в":"v", "ы":"i", "ф":"f", "я":"ya",
              "ч":"ch", "с":"s", "м":"m", "и":"i", "т":"t", "ь":"", "б":"b", "ю":"yu",
              "ў":"o'", "ғ":"g'", "қ":"q", "ҳ":"h","ё":"yo",
               "Ў":"O'", "Қ":"Q", "Ғ":"G'", "Ҳ":"H",
              "Й":"Y", "Ц":"TS", "У":"U", "К":"K", "Е":"E", "Н":"N", "Г":"G", "Ш":"SH",
              "Щ":"SH", "З":"Z", "Х":"X", "Ъ":"'", "Э":"E", "Ж":"J", "Д":"D", "Л":"L",
              "О":"O", "Р":"R", "П":"P", "А":"A", "В":"V", "Ы":"", "Ф":"F", "Я":"YA",
              "Ч":"CH", "С":"S", "М":"M", "И":"I", "Т":"T", "Ь":"", "Б":"B", "Ю":"YU", "Ё":"Yo",
              }

#Lotin kiril harflari

lotin_kiril = { "y":"й", "u":"у", "k":"к", "n":"н", "g":"г",
               "z":"з", "x":"х", "e":"э", "j":"ж", "d":"д", "l":"л", "o":"о", "r":"р",
               "p":"п", "a":"а", "v":"в", "f":"ф", "s":"с", "m":"м",
               "i":"и", "t":"т", "b":"б", "q":"қ", "h":"ҳ", "'":"ъ",
               "Q":"Қ", "H":"Ҳ", "Y":"Й", "U":"У", "K":"К", "N":"Н",
               "G":"Г","Z":"З", "X":"Х", "E":"Э", "J":"Ж", "D":"Д", "L":"Л", "O":"О",
               "R":"Р", "P":"П", "A":"А", "V":"В", "F":"Ф", "S":"С", "M":"М",
               "I":"И", "T":"Т", "B":"Б",
            }

#Injiq harflar(ikkita belgidan iborat bo'lgan harflar: sh, ch, ...
injiq_harflar = {"yu": "ю", "o'": "ў", "g'": "ғ", "ch": "ч", "ya": "я", "sh": "ш", "yo": "ё", "ts": "ц", 
                 "O'": "Ў", "G'": "Ғ", "SH": "Ш", "Sh":"Ш", "CH": "Ч", "Ch": "Ч", "YA": "Я", "YU": "Ю", 
                 "Yo": "Ё", "Ts": "Ц", "Ya": "Я", "Yu": "Ю", "YO": "Ё", "TS": "Ц",}

def check2lotin(text):
    """Bu funksiya matnni lotinga tekshiruvchi funksiya"""
    for belgi in text:
        if belgi in kril_harflar:
            #Agar matn kiril harflaridan tashkiltopgan bo'lsa False qiymatini qaytaradi
            return False
        elif belgi in lotin_harflar:
            return True


def translate(matn:str, oraliq:int=2000, harflar=kril_harflar, lugat = kiril_lotin):
    """Bu funksiya lotin dan kirilga yoki teskarisiga o'girib beruvchi funkiya"""

    #Birinchi o'rinda matinni lotin harflariga rekshirib olamiz
    lotin = check2lotin(matn)
    if lotin == None:
        yield "Iltimos lotin yoki kiril harflari qatnashgan matn yuboring!!!"

    matn_uzunlig = len(matn)
    for i in range(1, ((matn_uzunlig // oraliq) + 2)):
        natija = ''
        matn_qismi = matn[((i - 1) * oraliq):(i * oraliq)]

        if lotin:
            harflar = lotin_harflar
            lugat = lotin_kiril
            for key in injiq_harflar:
                matn_qismi = matn_qismi.replace(key, injiq_harflar[key])

        for belgi in matn_qismi:
            if belgi in harflar:
                belgi = lugat[belgi]
            natija += belgi
        yield natija

if __name__ == '__main__':
    # text = input()
    text = """"""
    for i in translate(text):
        print(i)