# s = input('enter a number: ')
# try:
#     n = int(s)
# except ValueError:
#     print('無法轉成整數')
# except NameError:
#     print('NameError')


# try:
#     with open('test.txt', 'r') as f:
#         for line in f:
#             x = int(line.strip())
# except FileNotFoundError:
#     print("找不到檔案")
# except ValueError as ex:
#     print("把捕捉到的錯誤直接印出來" , ex)
# else:
#     print('如果沒有錯誤就會走進else')
# finally:
#     print('不管如何都會走到這裡')

error_enter = 0
i = 0
while True:
    try:
        s = int(input('請輸入一個數字： '))
        print(f'good, you enter a number:',s)
    except ValueError:
        error_enter += 1
        if error_enter >= 3:
            print('超過次數，請稍後再試')
            break
        print('請輸入數字')
    except KeyboardInterrupt:
            print('遊戲結束')
            break
    finally:
        i += 1
        print(f'這是第{i}次玩')

    