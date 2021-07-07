import re
imeis_string = '355316082611279, 351756051523999,  490154203237519'

def valid_imei(x): return True if sum(sum(int(i) for i in str(int(x)*2)) if idx %2 == 1 else int(x) for idx, x in enumerate(str(x))) % 10 == 0 else False

def imei_extractor(v):
    if bool(re.match(r'\d{15}([,\s]\s*\d{15})*$', v)):
        imeis = re.split(r'\W+', v)
        for imei in imeis:
            if not valid_imei(int(imei.strip())):
                raise ValueError(imei,"no es un imei valido")
            else:
                return imeis
    else:
        raise ValueError

#regex = /^\d{15}([,\s]\s*\d{15})*$/gm

print(imei_extractor(imeis_string))