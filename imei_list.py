import re
imeis_string = '464564646465464, 454546465464646,  454646564646454'


def imei_extractor(v):
    if bool(re.match(r'\d{15}([,\s]\s*\d{15})*$', v)):
        return re.split(r'\W+', v)
    else:
        raise ValueError

#regex = /^\d{15}([,\s]\s*\d{15})*$/gm

print(imei_extractor(imeis_string))