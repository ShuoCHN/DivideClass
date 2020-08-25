import random,time,os


peonum=80
stulist=[]
manlist=['徐鹏博','孙博','孙嘉浩','丁信宇','宋奕含','吴岩','庄宇博','曹思航','李宇博','王鑫宇','赵世博','蒋瀚霆','刘鑫','崔维彬','刘凯祺','于承恩','徐士哲','孙诗雨','徐天睿','刘祥','李玉龙','杨智明','赵子博','赵子淳','曹琪浩','于一鸣','李子学','张振豪','路桐','徐一博','李满意','许锐锋','黎沫含','王运晗','孙思琦','李飨','白忠文','白羽翔','朱子航','薛浩川','张昊然','汪鑫成','李哲','张明','王栎鑫']
girllist=['那雪冰','高宁璨','肖菲','岳洁妮','付凡雨','孟令娜','张显然','阎思彤','于文灿','于欣冉','蒋梦瑶','王俊思','韩禹凡','李宇航','马宇柏','侯佳以琳','攸晓冉','崔恩洁','潘雨萌','刘玉鑫','崔依凡','刘佳鑫','曹诗怡','张佳洋','刘林菲','刘思奇','赵珊珊','田正爱','肖雨柠','徐子帆','刘畅','王妍姝','杨雯淇','王悦琪','安春晓','赵雅涵','高吉越','梁雨欣','姚天蕊','吴一萱','董娇','赵媛媛','朱爽']

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


