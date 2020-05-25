#csv 質問,解答（a-d）
import csv
import sys
import random

quest = ["a", "b", "c", "d"]
print('歴史年表ツール\n')
print('\n始めますか？\n')
oky = input("Y/n >")
if oky == "Y" or oky == "y":
    #CSVファイルの読込
    with open('C:\ws\history\history.csv',  encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print("")
            print("Q." + row[0])
            print("")
            #解答から80の差の数字を3つランダム生成
            rndm = random.sample(range(int(row[1]) - 80,int(row[1]) + 80), k=3)
            questrd = random.choice(quest)
            #a-dごとに分け処理（要改善）
            if questrd == "a":
                print("a." + row[1])
                print("b." + str(rndm[0]))
                print("c." + str(rndm[1]))
                print("d." + str(rndm[2]))
            elif questrd == "b":
                print("a." + str(rndm[0]))
                print("b." + row[1])
                print("c." + str(rndm[1]))
                print("d." + str(rndm[2]))
            elif questrd == "c":
                print("a." + str(rndm[0]))
                print("b." + str(rndm[1]))
                print("c." + row[1])
                print("d." + str(rndm[2]))
            else:
                print("a." + str(rndm[0]))
                print("b." + str(rndm[1]))
                print("c." + str(rndm[2]))
                print("d." + row[1])
            print("")
            test = input("A. >")
            
            #解答と入力を検証
            if questrd == test:
                print("正解")
            
            #途中離脱用
            elif test == "quit" or test == "exit":
                sys.exit()

            else:
                print("")
                print("不正解")
                print("A." + row[1])

else:
    sys.exit()
