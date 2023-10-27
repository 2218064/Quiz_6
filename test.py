def validate_resident_id(resident_id):
    if len(resident_id) != 13:
        return False
    digits = [int(digit) for digit in resident_id[:-1]]
    weighted_sum = sum([digit * weight for digit, weight in zip(digits, [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5])])
    remainder = weighted_sum % 11
    diff = 11 - remainder
    if diff == int(resident_id[-1]) or (diff == 10 and int(resident_id[-1]) == 0):
        return True
    else:
        return False

resident_id = "주민등록번호 입력"
if validate_resident_id(resident_id):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
