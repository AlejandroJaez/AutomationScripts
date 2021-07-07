
imei1 = 355316082611279
imei2 = 490154203237518
imei3 = 490154203237517


def valid_imei(x): return True if sum(sum(int(i) for i in str(int(x)*2)) if idx %2 == 1 else int(x) for idx, x in enumerate(str(x))) % 10 == 0 else False


def valid_lenght(value: str):
    return True if len(str(value)) == 15 else False


print(imei1, valid_imei(imei1))
print(imei1, valid_lenght(imei1))