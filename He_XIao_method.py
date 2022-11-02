import math
import matplotlib.pyplot as plt

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

if n == 2:
    baseA = 1/3
    baseB =1/3
    baseC =0
    baseAB = 1/3
    baseAC = 0
    baseBC = 0
    baseABC = 0
if n == 3:
    baseA = 1 / 7
    baseB = 1 / 7
    baseC = 1 / 7
    baseAB = 1 / 7
    baseAC = 1 / 7
    baseBC = 1 / 7
    baseABC = 1 / 7


ma1 = float(input("请输入ma1"))
ma2 = float(input("请输入ma2"))
mb1 = float(input("请输入mb1"))
mb2 = float(input("请输入mb2"))
mab1 = float(input("请输入mab1"))
mab2 = float(input("请输入mab2"))

if n > 2:
    mc1 = float(input("请输入mc1"))
    mc2 = float(input("请输入mc2"))
    mac1 = float(input("请输入mac1"))
    mac2 = float(input("请输入mac2"))
    mbc1 = float(input("请输入mbc1"))
    mbc2 = float(input("请输入mbc2"))
    mabc1 = float(input("请输入mabc1"))
    mabc2 = float(input("请输入mabc2"))


mtA1 = (baseA + ma1) / 2
mtA2 = (baseA + ma2) / 2

mtB1 = (baseB + mb1) / 2
mtB2 = (baseB + mb2) / 2

mtAB1 = (baseAB + mab1) / 2
mtAB2 = (baseAB + mab2) / 2

if n > 2:
    mtC1 = (baseC + mc1) / 2
    mtC2 = (baseC + mc2) / 2


    mtABC1 = (baseABC + mabc1) / 2
    mtABC2 = (baseABC + mabc2) / 2

    mtAC1 = (baseAC + mac1) / 2
    mtAC2 = (baseAC + mac2) / 2

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

    k1 = mtA1 * mtB2
    k2=mtA1 * mtC2
    k3=mtA1 * mtBC2
    k4=mtB1 * mtA2
    k5=mtB1 * mtC2
    k6=mtB1 * mtAC2
    k7=mtC1 * mtA2
    k8=mtC1 * mtB2
    k9=mtC1 * mtAB2
    k10=mtAB1 * mtC2
    k11=mtAC1 * mtB2
    k12=mtBC1 * mtA2

    k = k1 +k2+k3+k4+k5+k6+k7+k8+k9+k10+k11+k12

    print('这是第{}次迭代'.format(i))
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

    mta = (mtA1 * (mtA2 + mtAC2 + mtAB2 + mtABC2) +\
              mtAC1 * (mtA2 + mtAB2) + mtAB1 * (mtA2 + mtAC2) + mtABC1 * mtA2)
    mtb = (mtB1 * (mtB2 + mtBC2 + mtAB2 + mtABC2) +\
              mtBC1 * (mtB2 + mtAB2) + mtAB1 * (mtB2 + mtBC2) + mtABC1 * mtB2)
    mtc = (mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2) +\
              mtAC1 * (mtC2 + mtBC2) + mtBC1 * (mtC2 + mtAC2) + mtABC1 * mtC2)
    #print("mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)的值为{}".format(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)))
    #print("mtAC1 * (mtC2 + mtBC2)的值为{}".format(mtAC1 * (mtC2 + mtBC2)))

    mtab = (mtAB1 * (mtAB2 + mtABC2) + mtABC1 * mtAB2)
    mtbc = (mtBC1 * (mtBC2 + mtABC2) + mtABC1 * mtBC2)
    mtac = (mtAC1 * (mtAC2 + mtABC2) + mtABC1 * mtAC2)
    mtabc = (mtABC1 * mtABC2)
    # print("mABC的值为{}".format(mABC))
    entirety = 1 - k
    pa = mta / entirety
    pb = mtb / entirety
    pab = mtab / entirety

    pc = mtc / entirety
    pac = mtac / entirety
    pbc = mtbc / entirety
    pabc = mtabc / entirety

    print('K的值为{}'.format(k))
    mA = mta + k * pa
    mB = mtb + k * pb
    mC = mtc + k * pc
    mAB = mtab + k * pab
    mAC = mtac + k * pac
    mBC = mtbc + k * pbc
    mABC = mtabc + k * pabc
    # entirety = 1 - k
    # pa = mA / entirety
    # pb = mB / entirety
    # pab = mAB / entirety
    #
    # pc = mC / entirety
    # pac = mAC / entirety
    # pbc = mBC / entirety
    # pabc = mABC / entirety

    #print('K的值为{}'.format(k))
    # mA = mA + k * pa
    # mB = mB + k * pb
    # mC = mC + k * pc
    # mAB = mAB + k * pab
    # mAC = mAC + k * pac
    # mBC = mBC + k * pbc
    # mABC = mABC + k * pabc

    print("mA的值为{}".format(mA))
    print("mB的值为{}".format(mB))
    print("mC的值为{}".format(mC))
    print("mAB的值为{}".format(mAB))
    print("mAC的值为{}".format(mAC))
    print("mBC的值为{}".format(mBC))
    print("mABC的值为{}".format(mABC))
    #print("mA的一部分值为{}".format(mtA1 * (mtA2 + mtAC2 + mtAB2 + mtABC2)))
    #print("mA的另一部分值为{}".format(mtAC1 * (mtA2 + mtAB2) + mtAB1 * (mtA2 + mtAC2) + mtABC1 * mtA2))
    #print("mC的一部分值为{}".format(mtC1 * (mtC2 + mtBC2 + mtAC2 + mtABC2)))
    #print("mC的另一部分值为{}".format(mtAC1 * (mtC2 + mtBC2) + mtBC1 * (mtC2 + mtAC2) + mtABC1 * mtC2))
    print(numbers)

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

#m12
#mA的值为0.35941324436776584
#mB的值为0.31102797884586053
#mC的值为0.2966023167550824
#mAB的值为0.010669490009962201
#mAC的值为0.007901812963650187
#mBC的值为0.012623171138634957
#mABC的值为0.002137509350273106

#m123
#mA的值为0.6276016338332095
#mB的值为0.30702761648601934
#mC的值为0.055455356100426234
#mAB的值为0.0031608550181540488
#mAC的值为0.0029542877277498126
#mBC的值为0.003743663583174031
#mABC的值为0.0008413551192229959

#m1234



#m12
#mA的值为0.3468054928157841
#mB的值为0.30507648304010127
#mC的值为0.2930973127969122
#mAB的值为0.017012772246680217
#mAC的值为0.014624751459275977
#mBC的值为0.01934716566702608
#mABC的值为0.004209147114321014

#m123
#mA的值为0.574383988321353
#mB的值为0.30847339200504964
#mC的值为0.09605392900611645
#mAB的值为0.006535043559805155
#mAC的值为0.006221230000369564
#mBC的值为0.007250331737727019
#mABC的值为0.0016174996957121974

#m1234
#mA的值为0.7204684158485022
#mB的值为0.22900133837482511
#mC的值为0.0365156581904494
#mAB的值为0.00413706844903928
#mAC的值为0.0041028639262919876
#mBC的值为0.0056074663739460445
#mABC的值为0.0012003580902133944