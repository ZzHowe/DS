import math
import matplotlib.pyplot as plt

def Dempster(mtA1,mtA2,mtB1,mtB2,mtC1,mtC2,mtAB1,mtAB2,mtAC1,mtAC2,mtBC1,mtBC2,mtABC1,mtABC2):
    k = 0
    k1 = mtA1 * mtB2
    k2 = mtA1 * mtC2
    k3 = mtA1 * mtBC2
    k4 = mtB1 * mtA2
    k5 = mtB1 * mtC2
    k6 = mtB1 * mtAC2
    k7 = mtC1 * mtA2
    k8 = mtC1 * mtB2
    k9 = mtC1 * mtAB2
    k10 = mtAB1 * mtC2
    k11 = mtAC1 * mtB2
    k12 = mtBC1 * mtA2

    k = k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9 + k10 + k11 + k12
    print("k的值为{}".format(k))
    k = 1 - k
    k = 1 / k
    mA = k * (mtA1 * (mtA2 + mtAC2 + mtAB2 + mtABC2) + \
              mtAC1 * (mtA2 + mtAB2) + mtAB1 * (mtA2 + mtAC2) + mtABC1 * mtA2)
    mB = k * (mtB1 * (mtB2 + mtBC2 + mtAB2 + mtABC2) + \
              mtBC1 * (mtB2 + mtAB2) + mtAB1 * (mtB2 + mtBC2) + mtABC1 * mtB2)
    mC = k * (mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2) + \
              mtAC1 * (mtC2 + mtBC2) + mtBC1 * (mtC2 + mtAC2) + mtABC1 * mtC2)
    # print("mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)的值为{}".format(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)))
    # print("mtAC1 * (mtC2 + mtBC2)的值为{}".format(mtAC1 * (mtC2 + mtBC2)))

    mAB = k * (mtAB1 * (mtAB2 + mtABC2) + mtABC1 * mtAB2)
    mBC = k * (mtBC1 * (mtBC2 + mtABC2) + mtABC1 * mtBC2)
    mAC = k * (mtAC1 * (mtAC2 + mtABC2) + mtABC1 * mtAC2)
    mABC = k * (mtABC1 * mtABC2)

    # print("mA的值为{}".format(mA))
    # print("mB的值为{}".format(mB))
    # print("mC的值为{}".format(mC))
    # print("mAB的值为{}".format(mAB))
    # print("mAC的值为{}".format(mAC))
    # print("mBC的值为{}".format(mBC))
    # print("mABC的值为{}".format(mABC))

    return mA,mB,mC,mAB,mBC,mAC,mABC
numbers = []
valuesA = []
valuesB = []
valuesC = []
valuesAB = []
valuesAC = []
valuesBC = []
valuesABC = []

mtA1 = 0
mtA2 = 0
mtB1 = 0
mtB2 = 0
mtC1 = 0
mtC2 = 0
mtAC1 = 0
mtAC2 = 0
mtBC1 = 0
mtBC2 = 0
mtAB1 = 0
mtAB2 = 0
mtABC1 = 0
mtABC2 = 0

N = int(input('请输入迭代次数N'))
n = int(input("请输入辩框数n"))

basetA = -math.log(4/19,10)
basetB = -math.log(4/19,10)
basetC = -math.log(4/19,10)
basetAB = -math.log(5/9,10)
basetAC = 0
basetBC = 0
basetABC = -math.log(6/9,10)

entirety = basetA + basetB + basetC + basetAB + basetAC + basetBC + basetABC

baseA = basetA / entirety
baseB = basetB / entirety
baseC = basetC / entirety
baseAB = basetAB / entirety
baseAC = basetAC / entirety
baseBC = basetBC / entirety
baseABC = basetABC / entirety

ma1 = float(input("请输入ma1"))
ma2 = float(input("请输入ma2"))
mb1 = float(input("请输入mb1"))
mb2 = float(input("请输入mb2"))
mab1 = float(input("请输入mab1"))
mab2 = float(input("请输入mab2"))

if n > 2:
    mc1 = float(input("请输入mc1"))
    mc2 = float(input("请输入mc2"))
    mbc1 = float(input("请输入mbc1"))
    mbc2 = float(input("请输入mbc2"))
    mac1 = float(input("请输入mac1"))
    mac2 = float(input("请输入mac2"))
    mabc1 = float(input("请输入mabc1"))
    mabc2 = float(input("请输入mabc2"))


mtA1 = (baseA + ma1) / 2
mtA2 = (baseA + ma2) / 2

mtB1 = (baseB + mb1) / 2
mtB2 = (baseB + mb2) / 2

print("没有进行迭代的mtA1的值为{}".format(mtA1))

if mab1 > 0 or mab2 > 0:
    mtAB1 = (baseAB + mab1) / 2
    mtAB2 = (baseAB + mab2) / 2

if n > 2:
    mtC1 = (baseC + mc1) / 2
    mtC2 = (baseC + mc2) / 2

    if mabc1 > 0 or mabc2 > 0:
        mtABC1 = (baseABC + mabc1) / 2
        mtABC2 = (baseABC + mabc2) / 2
    if mac1 > 0 or mac2 > 0:
        mtAC1 = (baseAC + mac1) / 2
        mtAC2 = (baseAC + mac2) / 2
    if mbc1 > 0 or mbc2 > 0:
        mtBC1 = (baseBC + mbc1) / 2
        mtBC2 = (baseBC + mbc2) / 2



i = 1

for i in range(1,N+1,1):
    mtA1 = (mtA1 + ma1) / 2
    mtA2 = (mtA2 + ma2) / 2
    mtB1 = (mtB1 + mb1) / 2
    mtB2 = (mtB2 + mb2) / 2
    mtAB1 = (mtAB1 + mab1) / 2
    mtAB2 = (mtAB2 + mab2) / 2
    numbers.append(i)

    if n > 2 :
        mtC1 = (mtC1 + mc1) / 2
        mtC2 = (mtC2 + mc2) / 2
        mtAC1 = (mtAC1 + mac1) / 2
        mtAC2 = (mtAC2 + mac2) / 2
        mtBC1 = (mtBC1 + mbc1) / 2
        mtBC2 = (mtBC2 + mbc2) / 2

        mtABC1 = (mtABC1 + mabc1) / 2
        mtABC2 = (mtABC2 + mabc2) / 2

    #print(basetA)
    #print(baseA)
    print('这是第{}次迭代'.format(i))
    print("mtA1的值为{}".format(mtA1))
    print("mtB1的值为{}".format(mtB1))
    print("mtA2的值为{}".format(mtA2))
    print("mtB2的值为{}".format(mtB2))
    print("mtC1的值为{}".format(mtC1))
    print("mtC2的值为{}".format(mtC2))
    print("mtAB1的值为{}".format(mtAB1))
    print("mtAB2的值为{}".format(mtAB2))
    print("mtAC1的值为{}".format(mtAC1))
    print("mtAC2的值为{}".format(mtAC2))
    print("mtBC1的值为{}".format(mtBC1))
    print("mtBC2的值为{}".format(mtBC2))
    print("mtABC1的值为{}".format(mtABC1))
    print("mtABC2的值为{}".format(mtABC2))

    mA,mB,mC,mAB,mBC,mAC,mABC=Dempster(mtA1,mtA2,mtB1,mtB2,mtC1,mtC2,mtAB1,mtAB2,mtAC1,mtAC2,mtBC1,mtBC2,mtABC1,mtABC2)
    # print(numbers)
    # print("mA的值为{}".format(mA))
    # print("mB的值为{}".format(mB))
    # print("mC的值为{}".format(mC))
    # print("mAB的值为{}".format(mAB))
    # print("mAC的值为{}".format(mAC))
    # print("mBC的值为{}".format(mBC))
    # print("mABC的值为{}".format(mABC))

    # k1 = mtA1 * mtB2
    # k2 = mtA1 * mtC2
    # k3 = mtA1 * mtBC2
    # k4 = mtB1 * mtA2
    # k5 = mtB1 * mtC2
    # k6 = mtB1 * mtAC2
    # k7 = mtC1 * mtA2
    # k8 = mtC1 * mtB2
    # k9 = mtC1 * mtAB2
    # k10 = mtAB1 * mtC2
    # k11 = mtAC1 * mtB2
    # k12 = mtBC1 * mtA2
    #
    # k = k1 + k2 + k3 + k4 + k5 + k6 + k7 + k8 + k9 + k10 + k11 + k12
    #
    # print('这是第{}次迭代'.format(i))
    # print("mtA1的值为{}".format(mtA1))
    # print("mtB1的值为{}".format(mtB1))
    # print("mtA2的值为{}".format(mtA2))
    # print("mtB2的值为{}".format(mtB2))
    # print("mtC1的值为{}".format(mtC1))
    # print("mtC2的值为{}".format(mtC2))
    # print("mtAB1的值为{}".format(mtAB1))
    # print("mtAB2的值为{}".format(mtAB2))
    # print("mtAC1的值为{}".format(mtAC1))
    # print("mtAC2的值为{}".format(mtAC2))
    # print("mtABC1的值为{}".format(mtABC1))
    # print("mtABC2的值为{}".format(mtABC2))
    # print("k的值为{}".format(k))
    # k = 1 - k
    # k = 1 / k
    #
    # mA = k*(mtA1 * (mtA2 + mtAC2 + mtAB2 + mtABC2) +\
    #           mtAC1 * (mtA2 + mtAB2) + mtAB1 * (mtA2 + mtAC2) + mtABC1 * mtA2)
    # mB = k*(mtB1 * (mtB2 + mtBC2 + mtAB2 + mtABC2) +\
    #           mtBC1 * (mtB2 + mtAB2) + mtAB1 * (mtB2 + mtBC2) + mtABC1 * mtB2)
    # mC = k*(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2) +\
    #           mtAC1 * (mtC2 + mtBC2) + mtBC1 * (mtC2 + mtAC2) + mtABC1 * mtC2)
    # #print("mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)的值为{}".format(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)))
    # #print("mtAC1 * (mtC2 + mtBC2)的值为{}".format(mtAC1 * (mtC2 + mtBC2)))
    #
    # mAB = k*(mtAB1 * (mtAB2 + mtABC2) + mtABC1 * mtAB2)
    # mBC = k*(mtBC1 * (mtBC2 + mtABC2) + mtABC1 * mtBC2)
    # mAC = k*(mtAC1 * (mtAC2 + mtABC2) + mtABC1 * mtAC2)
    # mABC = k*(mtABC1 * mtABC2)
    # print("mABC的值为{}".format(mABC))
    valuesA.append(mA)
    valuesB.append(mB)
    valuesC.append(mC)
    valuesABC.append(mABC)
    #
    print("mA的值为{}".format(mA))
    print("mB的值为{}".format(mB))
    print("mC的值为{}".format(mC))
    print("mAB的值为{}".format(mAB))
    print("mAC的值为{}".format(mAC))
    print("mBC的值为{}".format(mBC))
    print("mABC的值为{}".format(mABC))

    print(mA + mB + mC + mAB + mAC + mBC + mABC)
    #print("mA的一部分值为{}".format(mtA1 * (mtA2 + mtAC2 + mtAB2 + mtABC2)))
    #print("mA的另一部分值为{}".format(mtAC1 * (mtA2 + mtAB2) + mtAB1 * (mtA2 + mtAC2) + mtABC1 * mtA2))
    #print("mC的一部分值为{}".format(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)))
    #print("mC的另一部分值为{}".format(mtAC1 * (mtC2 + mtBC2) + mtBC1 * (mtC2 + mtAC2) + mtABC1 * mtC2))





def draw_number(numbers,valuesA,valuesB,valuesC,valuesABC):
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    #    plt.bar(step,cost, color="red")
    #    plt.plot(step,cost)
    plt.plot(numbers, valuesA, color="red", label="m(a)")
    plt.plot(numbers, valuesB, color="blue", label="m(b)")
    plt.plot(numbers, valuesC, color="green", label="m(c)")
    plt.plot(numbers, valuesABC, color="black", label="m(abc)")

    plt.legend()  # 显示图例
    plt.xlabel("N")
    plt.ylabel("m(X)")
    #plt.title("m_final(A)与N大小的变化规律图")
    plt.show()  # 画图
