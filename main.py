import random,time,os


peonum=80
stulist=[]
manlist=['海川','爱予','鹏博','博','嘉浩','信宇','奕含','岩','宇博','思航','宇博','鑫宇','世博','瀚霆','鑫','维彬','凯祺','承恩','士哲','诗雨','天睿','祥','玉龙','智明','子博','子淳','琪浩','一鸣','子学','振豪','桐','一博','满意','锐锋','沫含','运晗','思琦','飨','忠文','羽翔','子航','浩川','昊然','鑫成','哲','明','栎鑫']
girllist=['雪冰','宁璨','菲','洁妮','凡雨','令娜','显然','思彤','文灿','欣冉','梦瑶','俊思','禹凡','宇航','宇柏','佳以琳','晓冉','恩洁','雨萌','玉鑫','依凡','佳鑫','诗怡','佳洋','林菲','思奇','珊珊','正爱','雨柠','子帆','畅','妍姝','雯淇','悦琪','春晓','雅涵','吉越','雨欣','天蕊','一萱','娇','媛媛','爽']

print("""
--------------------------------------------------------------------
|            智能分班系统©（齐市一中初中部限定版） ALPHA1.0    
|                     Author：ShuoCHN                    
|             本程序仅供齐齐哈尔市第一中学初中部使用            
|         如需定制其它程序请联络zhaoshuo100@foxmail.com      
|                                                       
|                        使用说明：
|       本程序通过基于Python的随机数生成函数进行阳光分班操作
|               可保证分班结果无任何人工因素介入
|      源代码查询：https://github.com/ShuoCHN/DivideClass
|--------------------------------------------------------------------

""")



while True:
    userchoice = int(input("欢迎使用，请按照提示输入相应数字：\n格式化系统请输入0,对男生分班输入1，对女生分班输入2，保存并退出请输入3:"))
    stulist = []
    if userchoice==1:
        peonum=len(manlist)
        for i in range(0,peonum):
            stulist.append(manlist[i])
    elif userchoice==2 :
        peonum=len(girllist)
        for i in range(0,peonum):
            stulist.append(girllist[i])
    elif userchoice==0:
        if os.path.exists("男生分班信息.txt"):os.remove("男生分班信息.txt")
        if os.path.exists("女生分班信息.txt"): os.remove("女生分班信息.txt")
        print("清理完成，可以开始正式使用↓↓↓")
        continue
    elif userchoice==3:
        print("感谢使用，软件版权©ShuoCHN")
        time.sleep(3)
        break

    quwei = 0
    while True:
        quwei=0
        quwei_choice = input("缓出模式请输入S，性能模式请输入E (均为大写)：")
        if quwei_choice== 'S':
            quwei=1
            break
        elif quwei_choice == 'E':
            quwei=0
            break
        else:
            print("您的输入有误，请重新输入.")

    if userchoice==1:manfile = open("男生分班信息.txt", 'w+')
    else:girlfile = open("女生分班信息.txt", 'w+')


    cnt1=0
    print("\n\n分组A人员名单:")
    if userchoice == 1: manfile.write("分组A人员名单:\n")
    else:girlfile.write("分组A人员名单:\n")
    xunum=peonum/2
    if userchoice==2: xunum+=1
    while( len(stulist)>xunum):
        choice_stu=random.randint(0, len(stulist)-1)
        cnt1+=1
        if quwei == 1:time.sleep(0.5)
        pstr=str(cnt1)+": "+stulist[choice_stu]
        print(pstr)
        pstr+='\n'
        if userchoice==1: manfile.write(pstr)
        else:girlfile.write(pstr)

        del stulist[choice_stu]


    cnt2=0
    print("\n\n分组B人员名单:")
    if userchoice == 1: manfile.write("\n\n分组B人员名单:\n")
    else:girlfile.write("\n\n分组B人员名单:\n")
    while( len( stulist ) ):
        choice_stu=random.randint(0, len(stulist)-1)
        cnt2+=1
        if quwei == 1 :time.sleep(0.3)
        pstr=str(cnt2)+": "+stulist[choice_stu]
        print(pstr)
        pstr += '\n'
        if userchoice == 1:manfile.write(pstr)
        else:girlfile.write(pstr)
        del stulist[choice_stu]

    if userchoice==1:manfile.close()
    else:girlfile.close()
    print("分班信息已存储至与此exe同一目录下\n\n")


