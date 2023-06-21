# -*- coding: utf-8 -*-
import requests
import json
import os
from eth_account import Account


def check_solution(address):
    solution = 0
    while solution == 0:
        file_name = input('请输入文件名:')
        if os.path.exists(file_name):
            print('请换个名字')
        else:
            accountCount = int(input('请输入生成数量:'))
            for i in range(accountCount):
                account = Account.create()
                line = ('%s,%s' % (account.address, account.key.hex()))
                with open(file_name + "_Account.txt", 'a') as f:
                    f.write(line + '\n')
                with open(file_name + '_Only_Address.txt', 'a') as f:
                    f.write(account.address + '\n')
                with open(file_name + '_Only_Keys.txt', 'a') as f:
                    f.write(account.key.hex() + '\n')
            print('创建完成')

        solution = 1


if __name__ == '__main__':
    address = 1
    check_solution(address)
