#https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=internal-search
def electronic_shop(amount, keyboard, usb):
    array = []
    for i in range(0, len(keyboard)):
        for j in range(0, len(usb)):
            if keyboard[i] + usb[j] < amount:
                array.append(keyboard[i] + usb[j])
            else:
                 continue

    result = max(array)
    return result


amount = 1
keyboard_list = [3, 1]
usb_list = [5, 2, 8]
keyboard_list1 = [4]
usb_list1 = [5]
print(electronic_shop(amount, keyboard_list, usb_list))
print(electronic_shop(amount, keyboard_list1, usb_list1))