## i春秋

### Rotated!

```
题目内容：
They went and ROTated the flag by 5 and then ROTated it by 8! The scoundrels! Anyway once they were done this was all that was left VprPGS{jnvg_bar_cyhf_1_vf_3?} 
tips：flag格式是IceCTF
```

```
使用ROT13解密
IceCTF{wait_one_plus_1_is_3?}
```

### Substituted

```
Lw!
Gyzvecy ke WvyVKT!
W'zz by reso dsbdkwksky tzjq teo kly ujr. Teo keujr, gy joy dksurwmq bjdwv vorakeqojalr jmu wkd jaazwvjkwemd. Vorakeqojalr ljd j zemq lwdkeor, jzklesql gwkl kly juxymk et vecaskyod wk ljd qekkym oyjzzr vecazwvjkyu. Decy dwcazy ezu vwalyod joy kly Vjydjo vwalyo, kly Xwqymyoy vwalyo, kly dsbdkwkskwem vwalyo, glwvl wd klwd emy, jmu de em. Jzcedk jzz et klydy vwalyod joy yjdwzr boeiym keujr gwkl kly lyza et vecaskyod. Decy myg ymvorakwem cykleud joy JYD, kly vsooymk dkjmujou teo ymvorakwem, jzemq gwkl ODJ. Vorakeqojalr wd j xjdk twyzu jmu wd xyor wmkyoydkwmq klesql. De iwvi bjvi, oyju sa em decy veez vwalyod jmu ljxy tsm!
El jmu teo reso oyveoud cr mjcy wd WvyVKT{jzgjrd_zwdkym_ke_reso_dsbdkwksky_tzjqd}.
```

```
使用https://quipqiup.com/频率分析
IceCTF{always_listen_to_your_substitute_flags}
```

### Alien Message

```
题目内容：

We found this suspicous image suspicous image online and it looked like it had been planted there by an alien life form. Can you see if you can figure out what they're trying to tell us? 
```

![cry-alien_message](E:\备份\笔记\图片\cry-alien_message.png)

```
一一对应
```

![96dda144ad345982790b73e30cf431adcbef843a](E:\备份\笔记\图片\96dda144ad345982790b73e30cf431adcbef843a.jpg)

```
IceCTF{gOOd_n3wZ_3vERyoN3_1_L1k3_fU7ur4Ma_4nd_tH3iR_4maZ1nG_3As7eR_39G5}
```



### RSA?

```
题目内容：
John was messing with RSA again... he encrypted our flag! I have a strong feeling he had no idea what he was doing however, can you get the flag for us?

N=0x180be86dc898a3c3a710e52b31de460f8f350610bf63e6b2203c08fddad44601d96eb454a34dab7684589bc32b19eb27cffff8c07179e349ddb62898ae896f8c681796052ae1598bd41f35491175c9b60ae2260d0d4ebac05b4b6f2677a7609c2fe6194fe7b63841cec632e3a2f55d0cb09df08eacea34394ad473577dea5131552b0b30efac31c59087bfe603d2b13bed7d14967bfd489157aa01b14b4e1bd08d9b92ec0c319aeb8fedd535c56770aac95247d116d59cae2f99c3b51f43093fd39c10f93830c1ece75ee37e5fcdc5b174052eccadcadeda2f1b3a4a87184041d5c1a6a0b2eeaa3c3a1227bc27e130e67ac397b375ffe7c873e9b1c649812edcd

e=0x1

c=0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d
```

```
求明文m
m=c+n*k
k=0,1,2,3....
将十六进制的m转ASCII码字符
注意e=1,可暴力求解
代码：
import binascii
N="0x180be86dc898a3c3a710e52b31de460f8f350610bf63e6b2203c08fddad44601d96eb454a34dab7684589bc32b19eb27cffff8c07179e349ddb62898ae896f8c681796052ae1598bd41f35491175c9b60ae2260d0d4ebac05b4b6f2677a7609c2fe6194fe7b63841cec632e3a2f55d0cb09df08eacea34394ad473577dea5131552b0b30efac31c59087bfe603d2b13bed7d14967bfd489157aa01b14b4e1bd08d9b92ec0c319aeb8fedd535c56770aac95247d116d59cae2f99c3b51f43093fd39c10f93830c1ece75ee37e5fcdc5b174052eccadcadeda2f1b3a4a87184041d5c1a6a0b2eeaa3c3a1227bc27e130e67ac397b375ffe7c873e9b1c649812edcd"
e=0x1
c="0x4963654354467b66616c6c735f61706172745f736f5f656173696c795f616e645f7265617373656d626c65645f736f5f63727564656c797d"
n1 = int(N,16)
c1 = int(c,16)
for k in range(1000):
    m = c1 + k * n1
    print(binascii.unhexlify(hex(m)[2:]).decode())
输出：
IceCTF{falls_apart_so_easily_and_reassembled_so_crudely}
```

### 回旋13踢

```
题目内容：
看我回旋13踢
synt{5pq1004q-86n5-46q8-o720-oro5on0417r1}
```

```
凯撒密码
ROT13
flag{5cd1004d-86a5-46d8-b720-beb5ba0417e1}
```

### RSA

```
题目内容：
This time John managed to use RSA " correctly "&ellipsis; I think he still made some mistakes though

N=0x1564aade6f1b9f169dcc94c9787411984cd3878bcd6236c5ce00b4aad6ca7cb0ca8a0334d9fe0726f8b057c4412cfbff75967a91a370a1c1bd185212d46b581676cf750c05bbd349d3586e78b33477a9254f6155576573911d2356931b98fe4fec387da3e9680053e95a4709934289dc0bc5cdc2aa97ce62a6ca6ba25fca6ae38c0b9b55c16be0982b596ef929b7c71da3783c1f20557e4803de7d2a91b5a6e85df64249f48b4cf32aec01c12d3e88e014579982ecd046042af370045f09678c9029f8fc38ebaea564c29115e19c7030f245ebb2130cbf9dc1c340e2cf17a625376ca52ad8163cfb2e33b6ecaf55353bc1ff19f8f4dc7551dc5ba36235af9758b

e=0x10001

phi=0x1564aade6f1b9f169dcc94c9787411984cd3878bcd6236c5ce00b4aad6ca7cb0ca8a0334d9fe0726f8b057c4412cfbff75967a91a370a1c1bd185212d46b581676cf750c05bbd349d3586e78b33477a9254f6155576573911d2356931b98fe4fec387da3e9680053e95a4709934289dc0bc5cdc2aa97ce62a6ca6ba25fca6ae366e86eed95d330ffad22705d24e20f9806ce501dda9768d860c8da465370fc70757227e729b9171b9402ead8275bf55d42000d51e16133fec3ba7393b1ced5024ab3e86b79b95ad061828861ebb71d35309559a179c6be8697f8a4f314c9e94c37cbbb46cef5879131958333897532fea4c4ecd24234d4260f54c4e37cb2db1a0

d=0x12314d6d6327261ee18a7c6ce8562c304c05069bc8c8e0b34e0023a3b48cf5849278d3493aa86004b02fa6336b098a3330180b9b9655cdf927896b22402a18fae186828efac14368e0a5af2c4d992cb956d52e7c9899d9b16a0a07318aa28c8202ebf74c50ccf49a6733327dde111393611f915f1e1b82933a2ba164aff93ef4ab2ab64aacc2b0447d437032858f089bcc0ddeebc45c45f8dc357209a423cd49055752bfae278c93134777d6e181be22d4619ef226abb6bfcc4adec696cac131f5bd10c574fa3f543dd7f78aee1d0665992f28cdbcf55a48b32beb7a1c0fa8a9fc38f0c5c271e21b83031653d96d25348f8237b28642ceb69f0b0374413308481

c=0x126c24e146ae36d203bef21fcd88fdeefff50375434f64052c5473ed2d5d2e7ac376707d76601840c6aa9af27df6845733b9e53982a8f8119c455c9c3d5df1488721194a8392b8a97ce6e783e4ca3b715918041465bb2132a1d22f5ae29dd2526093aa505fcb689d8df5780fa1748ea4d632caed82ca923758eb60c3947d2261c17f3a19d276c2054b6bf87dcd0c46acf79bff2947e1294a6131a7d8c786bed4a1c0b92a4dd457e54df577fb625ee394ea92b992a2c22e3603bf4568b53cceb451e5daca52c4e7bea7f20dd9075ccfd0af97f931c0703ba8d1a7e00bb010437bb4397ae802750875ae19297a7d8e1a0a367a2d6d9dd03a47d404b36d7defe8469
```

```
（1）则已知n,p,q,e,d,c,phi,求m  条件过多
（2）伪代码
m=pow(c,d,N)
（3）将m转成ASCII码字符 binascii.unhexlify(hex(m)[2:]).decode()
解密代码：
import binascii
N='0x1564aade6f1b9f169dcc94c9787411984cd3878bcd6236c5ce00b4aad6ca7cb0ca8a0334d9fe0726f8b057c4412cfbff75967a91a370a1c1bd185212d46b581676cf750c05bbd349d3586e78b33477a9254f6155576573911d2356931b98fe4fec387da3e9680053e95a4709934289dc0bc5cdc2aa97ce62a6ca6ba25fca6ae38c0b9b55c16be0982b596ef929b7c71da3783c1f20557e4803de7d2a91b5a6e85df64249f48b4cf32aec01c12d3e88e014579982ecd046042af370045f09678c9029f8fc38ebaea564c29115e19c7030f245ebb2130cbf9dc1c340e2cf17a625376ca52ad8163cfb2e33b6ecaf55353bc1ff19f8f4dc7551dc5ba36235af9758b'
d='0x12314d6d6327261ee18a7c6ce8562c304c05069bc8c8e0b34e0023a3b48cf5849278d3493aa86004b02fa6336b098a3330180b9b9655cdf927896b22402a18fae186828efac14368e0a5af2c4d992cb956d52e7c9899d9b16a0a07318aa28c8202ebf74c50ccf49a6733327dde111393611f915f1e1b82933a2ba164aff93ef4ab2ab64aacc2b0447d437032858f089bcc0ddeebc45c45f8dc357209a423cd49055752bfae278c93134777d6e181be22d4619ef226abb6bfcc4adec696cac131f5bd10c574fa3f543dd7f78aee1d0665992f28cdbcf55a48b32beb7a1c0fa8a9fc38f0c5c271e21b83031653d96d25348f8237b28642ceb69f0b0374413308481'
c='0x126c24e146ae36d203bef21fcd88fdeefff50375434f64052c5473ed2d5d2e7ac376707d76601840c6aa9af27df6845733b9e53982a8f8119c455c9c3d5df1488721194a8392b8a97ce6e783e4ca3b715918041465bb2132a1d22f5ae29dd2526093aa505fcb689d8df5780fa1748ea4d632caed82ca923758eb60c3947d2261c17f3a19d276c2054b6bf87dcd0c46acf79bff2947e1294a6131a7d8c786bed4a1c0b92a4dd457e54df577fb625ee394ea92b992a2c22e3603bf4568b53cceb451e5daca52c4e7bea7f20dd9075ccfd0af97f931c0703ba8d1a7e00bb010437bb4397ae802750875ae19297a7d8e1a0a367a2d6d9dd03a47d404b36d7defe8469'
n1 = int(N,16)
d1 = int(d,16)
c1 = int(c,16)
m = pow(c1,d1,n1)
print(binascii.unhexlify(hex(m)[2:]).decode())
```

### classical

```
题目
Ld hcrakewcfaxr, f hofjjlhfo hlaxuc lj f krau ev hlaxuc kxfk zfj tjui xljkeclhfoor gtk dez xfj vfooud, vec kxu pejk afck, ldke iljtju. 
Ld hedkcfjk ke peiucd hcrakewcfaxlh foweclkxpj, pejk hofjjlhfo hlaxucj hfd gu acfhklhfoor hepatkui fdi jeoyui gr xfdi. Xezuyuc, 
OrmkO3vydJCoe2qyNLmcN2qlpJXnM3SxM2Xke3q9 kxur fcu foje tjtfoor yucr jlpaou ke gcufn zlkx peiucd kuhxdeoewr. 
Kxu kucp ldhotiuj kxu jlpaou jrjkupj tjui jldhu Wcuun fdi Cepfd klpuj, kxu uofgecfku Cudfljjfdhu hlaxucj, Zecoi Zfc LL hcrakewcfaxr jthx fj kxu Udlwpf pfhxldu fdi guredi. 
F btlhn gcezd veq mtpa eyuc kxu ofsr iew.
```

```
1.使用https://quipqiup.com/频率分析
2.凯撒轮转
3.base64

频率分析后：
In cryptography, a classical cipher is a type of cipher that was used historically but now has fallen, for the most part, into disuse. In contrast to modern cryptographic algorithms, most classical ciphers can be practically computed and solved by hand. However, LyjtL3fvnSRlo2xvKIjrK2ximSHkJ3ZhJ2Hto3x9 they are also usually very simple to break with modern technology. The term includes the simple systems used since Greek and Roman times, the elaborate Renaissance ciphers, World War II cryptography such as the Enigma machine and beyond. A quick brown fox jump over the lazy dog.

```



### RSA

```
题目内容
n is 966808932627497190635859236054960349099463975227350564265384373280336699853387254070662881265937565163000758606154308757944030571837175048514574473061401566330836334647176655282619268592560172726526643074499534129878217409046045533656897050117438496357231575999185527675071002803951800635220029015932007465117818739948903750200830856115668691007706836952244842719419452946259275251773298338162389930518838272704908887016474007051397194588396039111216708866214614779627566959335170676055025850932631053641576566165694121420546081043285806783239296799795655191121966377590175780618944910532816988143056757054052679968538901460893571204904394975714081055455240523895653305315517745729334114549756695334171142876080477105070409544777981602152762154610738540163796164295222810243309051503090866674634440359226192530724635477051576515179864461174911975667162597286769079380660782647952944808596310476973939156187472076952935728249061137481887589103973591082872988641958270285169650803792395556363304056290077801453980822097583574309682935697260204862756923865556397686696854239564541407185709940107806536773160263764483443859425726953142964148216209968437587044617613518058779287167853349364533716458676066734216877566181514607693882375533

e is 65537

c is 168502910088858295634315070244377409556567637139736308082186369003227771936407321783557795624279162162305200436446903976385948677897665466290852769877562167487142385308027341639816401055081820497002018908896202860342391029082581621987305533097386652183849657065952062433988387640990383623264405525144003500286531262674315900537001845043225363148359766771033899680111076181672797077410584747509581932045540801777738548872747597899965366950827505529432483779821158152928899947837196391555666165486441878183288008753561108995715961920472927844877569855940505148843530998878113722830427807926679324241141182238903567682042410145345551889442158895157875798990903715105782682083886461661307063583447696168828687126956147955886493383805513557604179029050981678755054945607866353195793654108403939242723861651919152369923904002966873994811826391080318146260416978499377182540684409790357257490816203138499369634490897553227763563553981246891677613446390134477832143175248992161641698011195968792105201847976082322786623390242470226740685822218140263182024226228692159380557661591633072091945077334191987860262448385123599459647228562137369178069072804498049463136233856337817385977990145571042231795332995523988174895432819872832170029690848

```

```
（1）将n进行分解得p,q
（2）求phi_n=(p-1)*(q-1)
（3）由phi_n,e求d
（4）由c,d,n求m
（5）伪代码：
import gmpy2
phi_n=(p-1)*(q-1)
d=gmpy2.invert(e,phi_n)
m=pow(c,d,n)
（6）将m转换成ASCII码字符
代码：
import gmpy2
import binascii
n = 966808932627497190635859236054960349099463975227350564265384373280336699853387254070662881265937565163000758606154308757944030571837175048514574473061401566330836334647176655282619268592560172726526643074499534129878217409046045533656897050117438496357231575999185527675071002803951800635220029015932007465117818739948903750200830856115668691007706836952244842719419452946259275251773298338162389930518838272704908887016474007051397194588396039111216708866214614779627566959335170676055025850932631053641576566165694121420546081043285806783239296799795655191121966377590175780618944910532816988143056757054052679968538901460893571204904394975714081055455240523895653305315517745729334114549756695334171142876080477105070409544777981602152762154610738540163796164295222810243309051503090866674634440359226192530724635477051576515179864461174911975667162597286769079380660782647952944808596310476973939156187472076952935728249061137481887589103973591082872988641958270285169650803792395556363304056290077801453980822097583574309682935697260204862756923865556397686696854239564541407185709940107806536773160263764483443859425726953142964148216209968437587044617613518058779287167853349364533716458676066734216877566181514607693882375533
p = 31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928797450473
q = 31093551302922880999883020803665536616272147022877428745314830867519351013248914244880101094365815998050115415308439610066700139164376274980650005150267949853671653233491784289493988946869396093730966325659249796545878080119206283512342980854475734097108975670778836003822789405498941374798016753689377992355122774401780930185598458240894362246194248623911382284169677595864501475308194644140602272961699230282993020507668939980205079239221924230430230318076991507619960330144745307022538024878444458717587446601559546292026245318907293584609320115374632235270795633933755350928537598242214216674496409625928997877221
e = 65537
phi = (p-1)*(q-1)
d =  gmpy2.invert(e,phi)
c = 168502910088858295634315070244377409556567637139736308082186369003227771936407321783557795624279162162305200436446903976385948677897665466290852769877562167487142385308027341639816401055081820497002018908896202860342391029082581621987305533097386652183849657065952062433988387640990383623264405525144003500286531262674315900537001845043225363148359766771033899680111076181672797077410584747509581932045540801777738548872747597899965366950827505529432483779821158152928899947837196391555666165486441878183288008753561108995715961920472927844877569855940505148843530998878113722830427807926679324241141182238903567682042410145345551889442158895157875798990903715105782682083886461661307063583447696168828687126956147955886493383805513557604179029050981678755054945607866353195793654108403939242723861651919152369923904002966873994811826391080318146260416978499377182540684409790357257490816203138499369634490897553227763563553981246891677613446390134477832143175248992161641698011195968792105201847976082322786623390242470226740685822218140263182024226228692159380557661591633072091945077334191987860262448385123599459647228562137369178069072804498049463136233856337817385977990145571042231795332995523988174895432819872832170029690848
m =  pow(c,d,n)
print(binascii.unhexlify(hex(m)[2:]).decode())
flag{d1fference_between_p_And_q_1s_t00_5mall}
```

### Over the Hill

```
题目内容：
Over the hills and far away... many times I've gazed, many times been bitten. Many dreams come true and some have silver linings, I live for my dream of a decrypted flag

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"

matrix = [[54, 53, 28, 20, 54, 15, 12, 7],
          [32, 14, 24, 5, 63, 12, 50, 52],
          [63, 59, 40, 18, 55, 33, 17, 3],
          [63, 34, 5, 4, 56, 10, 53, 16],
          [35, 43, 45, 53, 12, 42, 35, 37],
          [20, 59, 42, 10, 46, 56, 12, 61],
          [26, 39, 27, 59, 44, 54, 23, 56],
          [32, 31, 56, 47, 31, 2, 29, 41]]

ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"
```

```
https://blog.csdn.net/hanjinrui15/article/details/102254551
在https://sagecell.sagemath.org/中输入代码，点击运行(语言选择python,sage都可)
??使用python编译无法运行？
或者直接在sage中运行 
from sage.all import *
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"
n = len(alphabet)
Zn = IntegerModRing(n) #对n取余
secret  = [[54, 53, 28, 20, 54, 15, 12, 7],

          [32, 14, 24, 5, 63, 12, 50, 52],

          [63, 59, 40, 18, 55, 33, 17, 3],

          [63, 34, 5, 4, 56, 10, 53, 16],

          [35, 43, 45, 53, 12, 42, 35, 37],

          [20, 59, 42, 10, 46, 56, 12, 61],

          [26, 39, 27, 59, 44, 54, 23, 56],

          [32, 31, 56, 47, 31, 2, 29, 41]]

secret = matrix(Zn, secret).inverse() #求逆矩阵
ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"
blocks = [ciphertext[i: i + secret.ncols()] for i in range(0, len(ciphertext), secret.ncols())] #分割密文
plaintext = ''
for block in blocks:
    decrypted_block = secret * matrix(Zn, [alphabet.find(c) for c in block]).transpose() #逆矩阵与密文(一行)的转置矩阵的乘积 
    plaintext += ''.join(alphabet[int(i[0])] for i in decrypted_block)
print(plaintext) #之前 的乘积的到一个矩阵,列表中的每个元素也是列表，所以取i[0]

```



### RSA2

```
题目内容:
I guess the 3rd time is the charm? Or not..

N=0xee290c7a603fc23300eb3f0e5868d056b7deb1af33b5112a6da1edc9612c5eeb4ab07d838a3b4397d8e6b6844065d98543a977ed40ccd8f57ac5bc2daee2dec301aac508f9befc27fae4a2665e82f13b1ddd17d3a0c85740bed8d53eeda665a5fc1bed35fbbcedd4279d04aa747ac1f996f724b14f0228366aeae34305152e1f430221f9594497686c9f49021d833144962c2a53dbb47bdbfd19785ad8da6e7b59be24d34ed201384d3b0f34267df4ba8b53f0f4481f9bd2e26c4a3e95cd1a47f806a1f16b86a9fc5e8a0756898f63f5c9144f51b401ba0dd5ad58fb0e97ebac9a41dc3fb4a378707f7210e64c131bca19bd54e39bbfa0d7a0e7c89d955b1c9f

e=0x10001

c=0x3dbf00a02f924a70f44bdd69e73c46241e9f036bfa49a0c92659d8eb0fe47e42068eaf156a9b3ee81651bc0576a91ffed48610c158dc8d2fb1719c7242704f0d965f8798304925a322c121904b91e5fc5eb3dc960b03eb8635be53b995217d4c317126e0ec6e9a9acfd5d915265634a22a612de962cfaa2e0443b78bdf841ff901423ef765e3d98b38bcce114fede1f13e223b9bd8155e913c8670d8b85b1f3bcb99353053cdb4aef1bf16fa74fd81e42325209c0953a694636c0ce0a19949f343dc229b2b7d80c3c43ebe80e89cbe3a3f7c867fd7cee06943886b0718a4a3584c9d9f9a66c9de29fda7cfee30ad3db061981855555eeac01940b1924eb4c301
```

```
（1）分解n得p，q
（2）计算phi_n=(p-1)*(q-1)
（3）计算d
（4）计算m=pow(c,d,n)
（5）代码
import gmpy2
phi_n=(p-1)*(q-1)
d=gmpy2.invert(e,phi_n)
m=pow(c,d,n)
（6）将m转换为对应的ASCII码

```

### Round Rabins!

```
John gave up on RSA and moved to Rabin. ...he still did it wrong though flag.txt  What a box! 

N=0x6b612825bd7972986b4c0ccb8ccb2fbcd25fffbadd57350d713f73b1e51ba9fc4a6ae862475efa3c9fe7dfb4c89b4f92e925ce8e8eb8af1c40c15d2d99ca61fcb018ad92656a738c8ecf95413aa63d1262325ae70530b964437a9f9b03efd90fb1effc5bfd60153abc5c5852f437d748d91935d20626e18cbffa24459d786601

c=0xd9d6345f4f961790abb7830d367bede431f91112d11aabe1ed311c7710f43b9b0d5331f71a1fccbfca71f739ee5be42c16c6b4de2a9cbee1d827878083acc04247c6e678d075520ec727ef047ed55457ba794cf1d650cbed5b12508a65d36e6bf729b2b13feb5ce3409d6116a97abcd3c44f136a5befcb434e934da16808b0b
```

```
# 有问题
https://blog.csdn.net/jcbx_/article/details/101066670
import gmpy2
import binascii
N='0x6b612825bd7972986b4c0ccb8ccb2fbcd25fffbadd57350d713f73b1e51ba9fc4a6ae862475efa3c9fe7dfb4c89b4f92e925ce8e8eb8af1c40c15d2d99ca61fcb018ad92656a738c8ecf95413aa63d1262325ae70530b964437a9f9b03efd90fb1effc5bfd60153abc5c5852f437d748d91935d20626e18cbffa24459d786601'
n = int(N,16)
c='0xd9d6345f4f961790abb7830d367bede431f91112d11aabe1ed311c7710f43b9b0d5331f71a1fccbfca71f739ee5be42c16c6b4de2a9cbee1d827878083acc04247c6e678d075520ec727ef047ed55457ba794cf1d650cbed5b12508a65d36e6bf729b2b13feb5ce3409d6116a97abcd3c44f136a5befcb434e934da16808b0b'
c = int(c,16)
print(n)
p = 8683574289808398551680690596312519188712344019929990563696863014403818356652403139359303583094623893591695801854572600022831462919735839793929311522108161
q = p
mp = pow(c, int((p+1)/4), p)
mq = pow(c, int((q+1)/4), q)
# p的模q逆元
yp = gmpy2.invert(p, q)
# q的模p逆元
yq = gmpy2.invert(q, p)
#
m1 = (yq*p*mq+yq*q*mp) % n
m2 = n - m1
m3 = (yp*p*mq-yq*q*mp) % n
m4 = n - m3

flag1 = binascii.unhexlify(m1[2:]).decode()
print(flag1)
```

### Sand Castles on the Beach

```
We found this very mysterious image, it doesn't look complete and there seems to be something hidden on it... does this mean anything to you? beach.jpg This flag is not in the standard flag format. The flag contains digits and no special characters, convert the message to lowercase and then add IceCTF{message} to it. 10331c4d 
```

```
https://blog.51cto.com/tdcqvip/1941818
```

### 致敬经典

```
lrua{1uy3yj9l-yw9u-48j2-uuj8-36h03706y7u7}
```

```
https://blog.csdn.net/vanarrow/article/details/107781616
代码 ：
immport string
c = "lrua{1uy3yj9l-yw9u-48j2-uuj8-36h03706y7u7}"
flag = ""
for ch in  c:
    if ch in string.ascii_lowercase:
        pos = string.ascii_lowercase.index(ch)
        if pos % 2 != 0:
            flag += string.ascii_lowercase[pos - 6]
        else:
            flag += string.ascii_lowercase[(pos + 6)%26]
    else:
        flag += ch
print(flag)
```

### 传感器1

```
已知ID为0x8893CA58的温度传感器的未解码报文为：3EAAAAA56A69AA55A95995A569AA95565556

此时有另一个相同型号的传感器，其未解码报文为：3EAAAAA56A69AA556A965A5999596AA95656

请解出其ID，提交flag{hex（不含0x）}。
```

```
有问题
https://blog.csdn.net/hhhparty/article/details/51873342
c = '3EAAAAA56A69AA55A95995A569AA95565556'
data1 = {'5':'00','9':'10','6':'01','A':'11'}
data2 = {'5':'11','9':'01','6':'10','A':'00'}
ans1 = ""
ans2 = ""
flag = ""
for ch in c:
    if ch in data1.keys():
        ans1 += data1[ch]
for ch in c:
    if ch in data2.keys():
        ans2 += data2[ch]
ans1 = int(ans1,2)
ans1 =  hex(ans1).upper()
print(ans1)
ans2 = int(ans2,2)
ans2 =  hex(ans2).upper()
print(ans2)

```

### SimpleMath





### rsa256

```
题目内容
四份文件：
（1）encrypted.message1
（2）encrypted.message2
（3）encrypted.message3
（4）public.key
```

```
（1）.key文件
使用openssl
openssl rsa -pubin -text -modulus  -in public.key
获得公钥对：e,n
(2)分解n得p,q
(3)计算phi_n=(p-1)*(q-1)
(4)计算d
(5)使用d解密message文件
(6)代码
import gmpy2
import rsa
d=int(gmpy2.invert(e,(p-1)*(q-1)))
primarykey=rsa.PrivateKey(n,e,d,p,q)
with open('encrypted.message1','rb')as f:
    print(rsa.decrypt(f.read(),primarykey).decode(),end='')
with open('encrypted.message2','rb')as f:
    print(rsa.decrypt(f.read(),primarykey).decode(),end='')
with open('encrypted.message3','rb')as f:
    print(rsa.decrypt(f.read(),primarykey).decode(),end='')
```

### Attack of the Hellman!

```
We managed to intercept a flag transmission but it was encrypted :(. Wegot the Diffie-Hellman public key exchange parameters and some scripts
they used for the transmission along with the enscrypto.flag Can you get it for us? 
```



### medium RSA

```
题目内容
两个文件：
（1）flag.enc
（2）pubkey.pem
```

```
（1）使用openssl
openssl rsa -pubin -text -modulus  -in public.pem
获得公钥对：e,n
(2)分解n得p,q
(3)计算phi_n=(p-1)*(q-1)
(4)计算d
(5)使用d对flag.enc进行解密
(6)代码
import gmpy2
import rsa
d=int(gmpy2.invert(e,(p-1)*(q-1)))
primarykey=rsa.PrivateKey(n,e,d,p,q)
with open("flag.enc","rb")as f:
    print(rsa.decrypt(f.read(),primarykey).decode())
```

## BUUCTF

### 变异凯撒

```
题目：变异凯撒
加密密文：afZ_r9VYfScOeO_UL^RWUc
格式：flag{ }
```

```
1.进行凯撒轮转后，没有符合的
2.格式为：flag{}，对比ascii码
3.python脚本
str1 = 'afZ_r9VYfScOeO_UL^RWUc'
i = 5
s = ''
for ch in str1:
    s += chr(ord(ch)+i)
    i=i+1
print(s) 
```

```
题目：传统知识+古典密码
小明某一天收到一封密信，信中写了几个不同的年份 辛卯，癸巳，丙戌，辛未，庚辰，癸酉，己卯，癸巳。
信的背面还写有“+甲子”，请解出这段密文。key值：CTF{XXX}
```

```
1.年份顺序加60
2.栅栏+凯撒
```

```
题目：try them all
You have found a passwd file containing salted passwords. An unprotected configuration file has revealed a salt of 5948. The hashed password for the 'admin' user appears to be 81bdf501ef206ae7d3b92070196f7e98, try to brute force this password.
```

```
1.md5解密
2.去掉5948
```

```
题目：robomunication（有问题）
We recorded the following file between two robots. Find out what evil things they are plotting, and recover their secret key!
题目链接： http://ctf5.shiyanbar.com/crypto/robomunication/robo.rar 
```

```
1.摩斯电码
```

```
题目：奇怪的短信
收到一条奇怪的短信:
          335321414374744361715332
          你能帮我解出隐藏的内容嘛？！
格式：CTF{xxx}
```

```
1.手机键盘（九键）
2.33：第三个键的第三个字母
```

```
题目：围在栅栏中的爱
最近一直在好奇一个问题，QWE到底等不等于ABC？
-.- .. --.- .-.. .-- - ..-. -.-. --.- --. -. ... --- --- 
flag格式：CTF{xxx}
```

```
1.摩斯电码
2.手机键盘（26键）
3.栅栏密码
```

```
题目：疑惑的汉字
现有一段经过加密的密文，内容如下：王夫 井工 夫口 由中人 井中 夫夫 由中大。请找出这段密文隐藏的消息明文。
格式：CTF{ }
```

```
1.笔画出头数转化为数字
2.ASCII码
```

```
题目：古典密码
密文内容如下{79 67 85 123 67 70 84 69 76 88 79 85 89 68 69 67 84 78 71 65 72 79 72 82 78 70 73 69 78 77 125 73 79 84 65}
请对其进行解密
提示：1.加解密方法就在谜面中
     2.利用key值的固定结构
格式：CTF{ }
```

```
1.ASCII码
2.列置换
```

```
题目：困在栅栏里的凯撒
小白发现了一段很6的字符：NlEyQd{seft}
```

```
1.栅栏加密
2.凯撒轮转
```

```
题目：Decode
flag格式:ctf{}
题目链接： http://ctf5.shiyanbar.com/crypto/Readme.txt 
0x253464253534253435253335253433253661253435253737253464253531253666253738253464253434253637253462253466253534253662253462253464253534253435253738253433253661253435253737253466253531253666253738253464253434253435253462253464253534253435253332253433253661253435253738253464253531253666253738253464253534253535253462253464253534253431253330253433253661253435253737253465253531253666253738253464253661253435253462253466253534253633253462253464253534253435253737253433253661253662253334253433253661253662253333253433253661253435253738253465253431253364253364
```

```
1.ASCII码
2.url解码
3.base64解码
4.ASCII码
```

```
题目：enc
Fady不是很理解加密与编码的区别 所以他使用编码而不是加密，给他的朋友传了一些秘密的消息。
enc文件
```

```
1.打开文件发现为01，认为是摩斯电码，但不是
2.以8位为一字节转为字符串
crypto = 'ZERO ONE ...'
ls = []
str0 = ''
str1 = ''
ls = crypto.split(" ")
#print(ls)
for ch in ls:
    if ch == 'ZERO':
        str0 += '0'
    elif ch == 'ONE':
        str0 += '1'
for i in range(0,len(str0),8):
    str1 += chr(int(str0[i:i+8],2)) 
print(str1)
3.base64解码
4.摩斯电码
5.插入特殊字符（有问题）
```

```
题目：告诉你个秘密
636A56355279427363446C4A49454A7154534230526D6843
56445A31614342354E326C4B4946467A5769426961453067
```

```
1.ASCII码（16进制）
2.base46解码
3.键盘密码
4.见https://www.cnblogs.com/levelstrcpy/p/9939720.html
```

## 攻防世界

### 幂数加密

```
题目：
你和小鱼终于走到了最后的一个谜题所在的地方，上面写着一段话“亲爱的朋友， 很开心你对网络安全有这么大的兴趣，希望你一直坚持下去，不要放弃 ，学到一些知识， 走进广阔的安全大世界”，你和小鱼接过谜题，开始了耐心细致的解答。flag为cyberpeace{你解答出的八位大写字母}
8842101220480224404014224202480122
```

```
1.应为云影加密或01248密码
2.见http://www.tuili.com/blog/u/503/archives/2009/1200.html
```

```
23.题目：你猜猜（攻防世界）
我们刚刚拦截了，敌军的文件传输获取一份机密文件，请君速速破解。
你猜猜.txt
```

```
1.打开文件后发现为16进制
2.使用010editor打开，发现PK,flag.txt
3.进行压缩，再打开压缩包需要密码
4.使用ZipPasswordTool得到密码
```

```
24.题目：Easy-one（有问题->问题已解决，见后，运算符的优先级->减号的优先级高于异或运算的优先级）（攻防世界）
破解密文，解密msg002.enc文件
encryptor.c
msg001
msg001.enc
msg002.enc
```

```
1.已知加密算法，一部分明文，一部分密文，算出密钥，求解另一份密文
2.部分代码：
c = open('msg001.enc','rb').read().strip()
m = open('msg001','rb').read().strip()
t = 0
key = ''
for i in range(len(m)):
    ch = ((c[i]-i*i-m[i])^t)&0xff
    t=m[i]
    key += chr(ch)
print(key)
#此部分有问题！！！！
c = open('msg002.enc','rb').read().strip()
key = 'VeryLongKeyYouWillNeverGuess'
pub = ''
t = 0
for i in range(len(c)):
    p = (c[i] - ord((key[i%len(key)]))^t -i*i)&0xff
    t = p
    pub += chr(p)
print(pub)
```

```
25.题目：说我作弊需要证据(有问题)(攻防世界)
X老师怀疑一些调皮的学生在一次自动化计算机测试中作弊，他使用抓包工具捕获到了Alice和Bob的通信流量。狡猾的Alice和Bob同学好像使用某些加密方式隐藏通信内容，使得X老师无法破解它，也许你有办法帮助X老师。X老师知道Alice的RSA密钥为(n, e) = (0x53a121a11e36d7a84dde3f5d73cf, 0x10001) (192.168.0.13)?,Bob的RSA密钥为(n, e) =(0x99122e61dc7bede74711185598c7, 0x10001) (192.168.0.37)
文件：Basic-06.pcapng
```

```
1..pcapng文件使用wireshark打开
2.分析发现192.168.0.13向192.168.0.37发包
3.追踪TCP流
4.base64解码
SEQ = 13; DATA = 0x3b04b26a0adada2f67326bb0c5d6L; 
SIG = 0x2e5ab24f9dc21df406a87de0b3b4L;
5.密文为DATA使用Bob的密钥进行解密
```

```
26.题目：easychallenge（攻防世界）
你们走到了一个冷冷清清的谜题前面，小鱼看着题目给的信息束手无策，丈二和尚摸不着头脑 ，你嘿嘿一笑，拿出来了你随身带着的笔记本电脑，噼里啪啦的敲起来了键盘，清晰的函数逻辑和流程出现在 了电脑屏幕上，你敲敲键盘，更改了几处地方，运行以后答案变出现在了电脑屏幕上。
easychallenge.pyc
```

```
1.将.pyc文件反编译
2.对反编译后的文件中的加密算法进行解密
import base64
import chardet
def decode1(ans):
    s = ''
    for i in ans:
        x = (ord(i) - 25) ^ 36
        s += chr(x)
    return s
def decode2(ans):
    s = ''
    for i in str(ans):
        x = (ord(i)^36) - 36#注意优先级
        if x in range(0x110000):
            s += chr(x)
    return s
def decode3(ans):#注意编码格式
    return base64.b32decode(ans)
flag = ' '
final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='
print(chardet.detect(decode3(final)))#查看编码格式
flag = decode1(decode2(decode3(final).decode('ISO-8859-1')))
print(flag)
    3.写好加密算法后，发现报错，编码问题
```

```
27.题目：轮转机加密（攻防世界）
你俩继续往前走，来到了前面的下一个关卡，这个铺面墙上写了好多奇奇怪怪的 英文字母，排列的的整整齐齐，店面前面还有一个大大的类似于土耳其旋转烤肉的架子，上面一圈圈的 也刻着很多英文字母，你是一个小历史迷，对于二战时候的历史刚好特别熟悉，一拍大腿：“嗨呀！我知道 是什么东西了！”。提示：托马斯·杰斐逊
1:  < ZWAXJGDLUBVIQHKYPNTCRMOSFE <
2:  < KPBELNACZDTRXMJQOYHGVSFUWI <
3:  < BDMAIZVRNSJUWFHTEQGYXPLOCK <
4:  < RPLNDVHGFCUKTEBSXQYIZMJWAO <
5:  < IHFRLABEUOTSGJVDKCPMNZQWXY <
6:  < AMKGHIWPNYCJBFZDRUSLOQXVET <
7:  < GWTHSPYBXIZULVKMRAFDCEONJQ <
8:  < NOZUTWDCVRJLXKISEFAPMYGHBQ <
9:  < XPLTDSRFHENYVUBMCQWAOIKZGJ <
10: < UDNAJFBOWTGVRSCZQKELMXYIHP <
11： < MNBVCXZQWERTPOIUYALSKDJFHG <
12： < LVNCMXZPQOWEIURYTASBKJDFHG <
13： < JZQAWSXCDERFVBGTYHNUMKILOP <

密钥为：2,3,7,5,13,12,9,1,8,10,4,11,6
密文为：NFQKSEVOQOFNP
```

```
str1 = '1:  < ZWAXJGDLUBVIQHKYPNTCRMOSFE <2:  < KPBELNACZDTRXMJQOYHGVSFUWI <3:  < BDMAIZVRNSJUWFHTEQGYXPLOCK <4:  < RPLNDVHGFCUKTEBSXQYIZMJWAO <5:  < IHFRLABEUOTSGJVDKCPMNZQWXY <6:  < AMKGHIWPNYCJBFZDRUSLOQXVET <7:  < GWTHSPYBXIZULVKMRAFDCEONJQ <8:  < NOZUTWDCVRJLXKISEFAPMYGHBQ <9:  < XPLTDSRFHENYVUBMCQWAOIKZGJ <10: < UDNAJFBOWTGVRSCZQKELMXYIHP <11： < MNBVCXZQWERTPOIUYALSKDJFHG <12： < LVNCMXZPQOWEIURYTASBKJDFHG <13： < JZQAWSXCDERFVBGTYHNUMKILOP <'
s = str1.split('<')
i = 0
str2 = []
for ch in s:
    if i == 1:
        str2.append(ch.strip())
        i = 0
    else:
        i = 1
#print(str2)
key = [2,3,7,5,13,12,9,1,8,10,4,11,6]
tr = 'NFQKSEVOQOFNP'
j = 0
ans = []
for i in key:
    str3 = str2[i-1]
    t = str3.find(tr[j])
    forward = str3[0:t]
    back = str3[t:]
    str4 = back + forward
    ans.append(str4)
    j = j+1
str5 = ''
#矩阵
flag = []
for i in range(len(ans[0])):
    for j in range (len(ans)):
        str5 += ans[j][i]
    flag.append(str5.lower())
    str5 = ''
    
print(flag)
```

```
28.题目：easy_ECC(有问题)（攻防世界）
已知椭圆曲线加密Ep(a,b)参数为
p = 15424654874903
a = 16546484
b = 4548674875
G(6478678675,5636379357093)
私钥为
k = 546768
求公钥K(x,y)
```

```
'''
easy_ECC答案
a = 0xcb19fe553fa
b = 0x50545408eb4

print(a+b)
'''
import collections
#import random

EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')

curve = EllipticCurve(
   'secp256k1',
   # Field characteristic.
   p=int(input('p=')),
   # Curve coefficients.
   a=int(input('a=')),
   b=int(input('b=')),
   # Base point.
   g=(int(input('Gx=')),
      int(input('Gy='))),
   # Subgroup order.
   n=int(input('k=')),
   # Subgroup cofactor.
   h=1,
)


# Modular arithmetic ##########################################################

def inverse_mod(k, p):
   """Returns the inverse of k modulo p.

  This function returns the only integer x such that (x * k) % p == 1.

  k must be non-zero and p must be a prime.
  """
   if k == 0:
       raise ZeroDivisionError('division by zero')

   if k < 0:
       # k ** -1 = p - (-k) ** -1 (mod p)
       return p - inverse_mod(-k, p)

   # Extended Euclidean algorithm.
   s, old_s = 0, 1
   t, old_t = 1, 0
   r, old_r = p, k

   while r != 0:
       quotient = old_r // r
       old_r, r = r, old_r - quotient * r
       old_s, s = s, old_s - quotient * s
       old_t, t = t, old_t - quotient * t

   gcd, x, y = old_r, old_s, old_t

   assert gcd == 1
   assert (k * x) % p == 1

   return x % p


# Functions that work on curve points #########################################

def is_on_curve(point):
   """Returns True if the given point lies on the elliptic curve."""
   if point is None:
       # None represents the point at infinity.
       return True

   x, y = point

   return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0


def point_neg(point):
   """Returns -point."""
   assert is_on_curve(point)

   if point is None:
       # -0 = 0
       return None

   x, y = point
   result = (x, -y % curve.p)

   assert is_on_curve(result)

   return result


def point_add(point1, point2):
   """Returns the result of point1 + point2 according to the group law."""
   assert is_on_curve(point1)
   assert is_on_curve(point2)

   if point1 is None:
       # 0 + point2 = point2
       return point2
   if point2 is None:
       # point1 + 0 = point1
       return point1

   x1, y1 = point1
   x2, y2 = point2

   if x1 == x2 and y1 != y2:
       # point1 + (-point1) = 0
       return None

   if x1 == x2:
       # This is the case point1 == point2.
       m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
   else:
       # This is the case point1 != point2.
       m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

   x3 = m * m - x1 - x2
   y3 = y1 + m * (x3 - x1)
   result = (x3 % curve.p,
             -y3 % curve.p)

   assert is_on_curve(result)

   return result


def scalar_mult(k, point):
   """Returns k * point computed using the double and point_add algorithm."""
   assert is_on_curve(point)



   if k < 0:
       # k * point = -k * (-point)
       return scalar_mult(-k, point_neg(point))

   result = None
   addend = point

   while k:
       if k & 1:
           # Add.
           result = point_add(result, addend)

       # Double.
       addend = point_add(addend, addend)

       k >>= 1

   assert is_on_curve(result)

   return result


# Keypair generation and ECDHE ################################################

def make_keypair():
   """Generates a random private-public key pair."""
   private_key = curve.n
   public_key = scalar_mult(private_key, curve.g)

   return private_key, public_key



private_key, public_key = make_keypair()
print("private key:", hex(private_key))
print("public key: (0x{:x}, 0x{:x})".format(*public_key))
```

```
29.题目：Easy-one(攻防世界)
破解密文，解密msg002.enc文件
```

```
1.利用msg001和msg001.enc求出密钥
with open('msg001','rb') as f1:
    p = f1.read().strip()

#print(p)
with open('msg001.enc','rb') as f2:
    c = f2.read().strip()

#print(c)
t = 0
key = ''
for i in range(len(p)):
    k = ((c[i] - p[i] - i*i)^t) & 0xff
    t = p[i]
    key += chr(k)
2.使用密钥和加密算法求明文
key = 'VeryLongKeyYouWillNeverGuess'
with open('msg002.enc','rb') as f1:
    c = f1.read().strip()
t = 0
flag = ''
for i in range(len(c)):
    p = (c[i] - (ord(key[i%len(key)]) ^ t) - i*i) & 0xff
    t = p
    flag += chr(p)
    
print(flag)
```

```
30.题目：Easy_Crypto（攻防世界）
小明在密码学课上新学了一种加密算法，你能帮他看看么
```

```
1.将加密算法用python实现
2.将最后一步改为解密算法（注意i,j的初始化）
s = []
t = []
key = 'hello world'
for i in range(256):
    s.append(i)
    t.append(key[i % len(key)])

j = 0     
for i in range(256):
    j = (j + s[i] + ord(t[i]))%256
    s[i],s[j] = s[j],s[i]
    
flag = ''
p = 0
with open('enc.txt','rb') as f:
    flagx = f.read().strip()
i = 0 
j = 0 
for m in range(37):
    i = (i+1)%256
    j = (j+s[i])%256
    s[i],s[j] = s[j],s[i]
    x = (s[i] + (s[j]%256))%256
    
    flag += chr(flagx[m] ^ s[x])
    
print(flag)

```

```
31.题目：rsa（2019上海）
chall.py
output
```

```
1.打开.py文件,为rsa加密算法，求解明文，再求解flag.
2.再求明文前，求解e,d,p,q
3.由于e<1000,可由暴力求解
4.(p-1)*(q-1) = pq - (p+q)+1
5.计算d,计算明文
6.计算flag
代码：
#求e e = 251
import libnum
import gmpy2
import math
n = 9538795663851271297602738029671089878718012242935213096566250130325046936720540247534143498025477544161347330379679111765871420732255741210434736423951962189227302658997497664520929375215715960063615792480965807127438948044298348300153102760490410578638259665656608784635088735809470916136628779400145983632930861883762707606629208260803446083579674497451514650309351925430391515629898218875049677870989016071086844819626778388370764400242376469343158294638240660190754978627356076115228410162956087266527271225439142347304100660800517276772407728290414074912243665126741030948775883739544952378188264714716087909797
y = 368284101618076523549199130884422355928051525996327977632544904437878504262870825378516827225793010165434494157238379685995430409966951122729243411694569562164062815098110639750101378457641471316188502263725098231679401928494160942213175404259256770984218593245458108598930926260386443799301699336309331946341173652201791293571029025818674575198311845811957606474490230382511996537893448524426809391980637983473305318819523408854264623254226127223862150173575206444726570183096891630129244778802793476295746913846105454198627
e = 0
while True:
     if pow(123,e,n) == y:
         print(e)

     e = e+1
     if e > 1000:
        break
        
import gmpy2
import binascii
from fractions import Fraction
from os import urandom
import libnum
n = 9538795663851271297602738029671089878718012242935213096566250130325046936720540247534143498025477544161347330379679111765871420732255741210434736423951962189227302658997497664520929375215715960063615792480965807127438948044298348300153102760490410578638259665656608784635088735809470916136628779400145983632930861883762707606629208260803446083579674497451514650309351925430391515629898218875049677870989016071086844819626778388370764400242376469343158294638240660190754978627356076115228410162956087266527271225439142347304100660800517276772407728290414074912243665126741030948775883739544952378188264714716087909797
#fenzi = 19077591327702542595205476059342179757436024485870426193132500260650093873441080495068286996050955088322694660759358223531742841464511482420869472847903924378454605317994995329041858750431431920127231584961931614254877896088596696600306205520980821157276519331313217569270177471618941832273257558800291967266057799408185825199394392306374394195697993019961311696247374832761757990150416392201444079060627610573918631913438062954960835929982836033906925917632413007648356037059843552967726871763559759125837289869091638924336309932526582201350695938677991368335828814565265478203873169858685929462350511138398905572292
#he = fenzi - 2*n
he = 196075640660409986135975784767502028538644025058282395628670981900974958890619954451344723318649578431744942274184506178219307129498083095220609328355931687266846079805131400737270051437647584592782747418213354229728108610925547647805880482097163218511341484311783416306321402379596024705973981708966729752698

#phi = n - he +1

phi = 9538795663851271297602738029671089878718012242935213096566250130325046936720540247534143498025477544161347330379679111765871420732255741210434736423951962189227302658997497664520929375215715960063615792480965807127438948044298348300153102760490410578638259665656608784635088735809470916136628779400145983632734786243102297620493232476035944055041030472393232254680680943529416556739278264423704954552339437639341902545442272210151457270744293374122548966282308972923908898822224675377958358725308502673744523807225788117575992049874969628966527246193250856400902180814957614642454481359948927672214283005749358157100

e = 251
d = int(gmpy2.invert(e,phi))
c = 7303495910407762399046490836902121070389476875516762048462433039234972742941586801378979220008051262826174054961747648114128456872349675769941760630519744351742977740846748646739901172672743584989842268056810152117350241337045055812845489372389014195433916347255846499434232234822333192328886207187844781726928951986353054876826105507064928478812402103648940709131760865763234071703554208057808885564381400571862422316195578258814602362582573148358552148686182480215663291366798585241933446701357953551496955627421526567152576426417189707335038601040167826900549139608192971559659991213411381604721734898065256138516
msg = pow(c,d,n)
print('0x%x'%msg)


import gmpy2
from fractions import Fraction
from secret import flag,e
import libnum
from os import urandom
k = 1024
p = gmpy2.next_prime(int(urandom(k / 8).encode('hex'),16))
q = gmpy2.next_prime(int(urandom(k / 8).encode('hex'),16))
n = p*q
assert(e<1000)
print (n)
#n = 9538795663851271297602738029671089878718012242935213096566250130325046936720540247534143498025477544161347330379679111765871420732255741210434736423951962189227302658997497664520929375215715960063615792480965807127438948044298348300153102760490410578638259665656608784635088735809470916136628779400145983632930861883762707606629208260803446083579674497451514650309351925430391515629898218875049677870989016071086844819626778388370764400242376469343158294638240660190754978627356076115228410162956087266527271225439142347304100660800517276772407728290414074912243665126741030948775883739544952378188264714716087909797
print(Fraction(int(p+1),int(p)) +Fraction(int(q+1),int(q)))
#x = 19077591327702542595205476059342179757436024485870426193132500260650093873441080495068286996050955088322694660759358223531742841464511482420869472847903924378454605317994995329041858750431431920127231584961931614254877896088596696600306205520980821157276519331313217569270177471618941832273257558800291967266057799408185825199394392306374394195697993019961311696247374832761757990150416392201444079060627610573918631913438062954960835929982836033906925917632413007648356037059843552967726871763559759125837289869091638924336309932526582201350695938677991368335828814565265478203873169858685929462350511138398905572292
#/9538795663851271297602738029671089878718012242935213096566250130325046936720540247534143498025477544161347330379679111765871420732255741210434736423951962189227302658997497664520929375215715960063615792480965807127438948044298348300153102760490410578638259665656608784635088735809470916136628779400145983632930861883762707606629208260803446083579674497451514650309351925430391515629898218875049677870989016071086844819626778388370764400242376469343158294638240660190754978627356076115228410162956087266527271225439142347304100660800517276772407728290414074912243665126741030948775883739544952378188264714716087909797
#求p,q
print(pow(123,e,n))
#求e e = 251
#368284101618076523549199130884422355928051525996327977632544904437878504262870825378516827225793010165434494157238379685995430409966951122729243411694569562164062815098110639750101378457641471316188502263725098231679401928494160942213175404259256770984218593245458108598930926260386443799301699336309331946341173652201791293571029025818674575198311845811957606474490230382511996537893448524426809391980637983473305318819523408854264623254226127223862150173575206444726570183096891630129244778802793476295746913846105454198627
#求d
#d = gmpy2.invert(e,(p-1)*(q-1))
msg = libnum.s2n(flag)
assert(msg<n)
print(pow(msg,e,n))
#c = 7303495910407762399046490836902121070389476875516762048462433039234972742941586801378979220008051262826174054961747648114128456872349675769941760630519744351742977740846748646739901172672743584989842268056810152117350241337045055812845489372389014195433916347255846499434232234822333192328886207187844781726928951986353054876826105507064928478812402103648940709131760865763234071703554208057808885564381400571862422316195578258814602362582573148358552148686182480215663291366798585241933446701357953551496955627421526567152576426417189707335038601040167826900549139608192971559659991213411381604721734898065256138516
#msg = pow(c,d,n)
```

```
题目：说我作弊需要证据（攻防世界）
X老师怀疑一些调皮的学生在一次自动化计算机测试中作弊，他使用抓包工具捕获到了Alice和Bob的通信流量。狡猾的Alice和Bob同学好像使用某些加密方式隐藏通信内容，使得X老师无法破解它，也许你有办法帮助X老师。X老师知道Alice的RSA密钥为(n, e) = (0x53a121a11e36d7a84dde3f5d73cf, 0x10001) (192.168.0.13)?,Bob的RSA密钥为(n, e) =(0x99122e61dc7bede74711185598c7, 0x10001) (192.168.0.37)
文件：Basic-06.pcapng
```

```
1..pcapng文件使用wireshark打开，发现是Alice向Bob发送信息,追踪TCP流
2.发现为Base64加密，解密后的SEQ = 13; DATA = 0x3b04b26a0adada2f67326bb0c5d6L; SIG = 0x2e5ab24f9dc21df406a87de0b3b4L;
....
3.将SEQ，DATA，SIG部分取出
4.使用Bob的私钥对DATA解密，使用Alice的公钥对SIG进行验证，并将密文的序号记录下来。
代码：
#base64解码
import base64
output = open('out.txt','a+')
f = open('1.txt','r') 
for f1 in f.readlines():
    f1 = base64.b64decode(f1).decode()
    output.write(f1+'\n')
f.close()
output.close()
#DATA解密，SIG验证
import gmpy2
#nA = 0x53a121a11e36d7a84dde3f5d73cf
#print(nA,16)
e = 65537
nA = 1696206139052948924304948333474767
pA = 38456719616722997
qA = 44106885765559411
dA = int(gmpy2.invert(e,(pA-1)*(qA-1)))
nB = 3104649130901425335933838103517383
pB = 49662237675630289
qB = 62515288803124247
dB = int(gmpy2.invert(e,(pB-1)*(qB-1)))
#nB = 0x99122e61dc7bede74711185598c7
#print(nB,16)
data = []
sig = []
dict1 = {}
f2 = open('out.txt','r')#注意要以读文件的方式打开
for ch in f2.readlines():
    b_d = ch.find('DATA = ')
    e_d = ch.find('L;')
    c = int(ch[b_d+7:e_d],16)
    data = pow(c,dB,nB)
    b_s = ch.find('SIG = ')
    m = int(ch[b_s+6:-3],16)
    sig = pow(m,e,nA)#有换行符  
    b_n = ch.find('SEQ = ')
    e_n = ch.find(';')
    num = int(ch[b_n+6:e_n])
    if data == sig:
        dict1[num] = data
flag = ''
for i in range(len(dict1)):
    flag += chr(dict1[i])
print(flag)
f2.close()
```

```
题目：x_xor_md5（攻防世界）
key 不存在
```

```
1.使用010editor打开文件后，发现为乱码，但有重复的值，01780c4c109e3237120cfbbacb8f6a53
2.题目为key不存在，则整个题目应该为求解key,标题为xor，则求xor_key
3.假设xor_key为01780c4c109e3237120cfbbacb8f6a53，取其二进制，与整个文件进行异或，注意，取二进制时，会去掉前面的0,因此在参与运算时，要将'0'加上。
4.在以xor_key=01780c4c109e3237120cfbbacb8f6a53，进行异或后，发现rctf后为[,实际应该为{,因此对xor_key进行调整，对xor_key异或0x20,此时的xor_key=21582c6c30be1217322cdb9aebaf4a73
5.发现最后一行的文字无法显示，出现了*key.和.ut,猜测第一个.为*,第二个为b,但RCTF{}中的许多字母都用形近的数字表示，因此猜测*key.为*key*,源文件的*key.处的最后一列为73,最后变为2A,则xor_key=21582c6c30be1217322cdb9aebaf4a59
6.又因为文中提示'the flag is not',同时题目中说明key不存在，题目提到md5,则将xor_key进行md5解密，为that.
代码：
#直接更改异或key，不用反复对文件进行操作
h1 = 0x01780c4c109e3237120cfbbacb8f6a53
b2 = bin(h1)[2: ]
b2 = '0000000'+b2#转出来的二进制去掉了开头的0000 000
b3 = '00100000'#与0x20异或
b0 = ''
for i in range(len(b2)):
    ch = int(b2[i]) ^ int(b3[i%(len(b3))])
    b0 += str(ch)
#b0 = 0x21582c6c30be1217322cdb9aebaf4a73
    '''
#调整后
b0 = 0x21582c6c30be1217322cdb9aebaf4a59
b0 = '00'+bin(b0)[2: ]
with open('as','rb') as f:
    b1 = bin(int(f.read().hex(),16))[2: ] 
b1 = '0'+ b1#转出来的二进制去掉了开头的0,且返回的b1为字符串，不需要加str()
f1 = open('out1.txt','w')
str2 = ''
for i in range(len(b1)):
    ch = int(b1[i]) ^ int(b0[i%(len(b0))])
    str2 += str(ch)
str2 = '0b'+str2
str2 = hex(int(str2,2))[2:]
'''    
#与0x20异或
h1 = '00100000'
str2 = ''
for i in range(len(str1)):
    ch = int(str1[i]) ^ int(h1[i%(len(h1))])
    str2 += str(ch)
str2 = '0b'+str2
str2 = hex(int(str2,2))[2:]
'''
f1.write(str2)  

#print(f1.read())#未保存，为空文件
f1.close()

f.close()

```

## 2019湖湘杯复赛 

### easyRSA

```
题目：（2019湖湘杯复赛）
from Crypto.Util.number import *
import libnum
import gmpy2

flag = open("flag.txt","rb").read()
m=libnum.s2n(flag)
p=getPrime(1024)
q=getPrime(1024)
n=p*q
e=65537
c=pow(m,e,n)
phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)
dp=d%(p-1)
print dp,n,e,c

#84373069210173690047629226878686144017052129353931011112880892379361035492516066159394115482289291025932915787077633999791002846189004408043685986856359812230222233165493645074459765748901898518115384084258143483508823079115319711227124403284267559950883054402576935436305927705016459382628196407373896831725 22000596569856085362623019573995240143720890380678581299411213688857584612953014122879995808816872221032805734151343458921719334360194024890377075521680399678533655114261000716106870610083356478621445541840124447459943322577740268407217950081217130055057926816065068275999620502766866379465521042298370686053823448099778572878765782711260673185703889168702746195779250373642505375725925213796848495518878490786035363094086520257020021547827073768598600151928787434153003675096254792245014217044607440890694190989162318846104385311646123343795149489946251221774030484424581846841141819601874562109228016707364220840611 
65537 14874271064669918581178066047207495551570421575260298116038863877424499500626920855863261194264169850678206604144314318171829367575688726593323863145664241189167820996601561389159819873734368810449011761054668595565217970516125181240869998009561140277444653698278073509852288720276008438965069627886972839146199102497874818473454932012374251932864118784065064885987416408142362577322906063320726241313252172382519793691513360909796645028353257317044086708114163313328952830378067342164675055195428728335222242094290731292113709866489975077052604333805889421889967835433026770417624703011718120347415460385182429795735

```

```
公式推导：
由题目可知：
dp ≡ d mod(p-1)  (1)
dp*e ≡ d*e mod(p-1)  (2)
由(2)可得
d*e = k1*(p-1) + dp*e ≡ 1 mod(phi)(3)
由(3)可得
k1*(p-1) + dp*e = k2*phi + 1
得
(p-1)*[k1-k2(q-1)] = 1 - dp*e
整理后：
dp*e = (p-1)*[k2*(q-1) - k1] + 1
由于 dp = d mod(p-1)
则dp < (p-1)
即 e > [k2*(q-1) - k1]
令x = [k2*(q-1) - k1],x∈(0,e)
经过遍历即可将p求出。
同时
q = n//p;
phi = (p-1)*(q-1);
d = gmpy2.invert(e,phi);
m = gmpy2.powmod(c,d,n);
在将m转化为对应的字符即可
代码如下：
from Crypto.Util.number import *
import libnum
import gmpy2
import binascii
dp = 84373069210173690047629226878686144017052129353931011112880892379361035492516066159394115482289291025932915787077633999791002846189004408043685986856359812230222233165493645074459765748901898518115384084258143483508823079115319711227124403284267559950883054402576935436305927705016459382628196407373896831725
n = 22000596569856085362623019573995240143720890380678581299411213688857584612953014122879995808816872221032805734151343458921719334360194024890377075521680399678533655114261000716106870610083356478621445541840124447459943322577740268407217950081217130055057926816065068275999620502766866379465521042298370686053823448099778572878765782711260673185703889168702746195779250373642505375725925213796848495518878490786035363094086520257020021547827073768598600151928787434153003675096254792245014217044607440890694190989162318846104385311646123343795149489946251221774030484424581846841141819601874562109228016707364220840611
e = 65537 
c = 14874271064669918581178066047207495551570421575260298116038863877424499500626920855863261194264169850678206604144314318171829367575688726593323863145664241189167820996601561389159819873734368810449011761054668595565217970516125181240869998009561140277444653698278073509852288720276008438965069627886972839146199102497874818473454932012374251932864118784065064885987416408142362577322906063320726241313252172382519793691513360909796645028353257317044086708114163313328952830378067342164675055195428728335222242094290731292113709866489975077052604333805889421889967835433026770417624703011718120347415460385182429795735

for x in range(1, e):
    if e*dp%x == 1:
        p=(e*dp-1)//x+1
        if n%p == 0:
            q=n//p
            phi=(p-1)*(q-1)
            d=gmpy2.invert(e, phi)
            m=gmpy2.powmod(c, d, n)
            n = binascii.unhexlify(format(m,'x')).decode('utf-8')
            print(n)

```

```
RSAROLL：
RSA roll！roll！roll！
flag格式：flag{xxx}
{920139713,19}
 
704796792
752211152
274704164
18414022
368270835
483295235
263072905
459788476
483295235
459788476
663551792
475206804
459788476
428313374
475206804
459788476
425392137
704796792
458265677
341524652
483295235
534149509
425392137
428313374
425392137
341524652
458265677
263072905
483295235
828509797
341524652
425392137
475206804
428313374
483295235
475206804
459788476
306220148
```

```
import gmpy2
n = 920139713
p = 18443
q = 49891
e = 19
d = int(gmpy2.invert(e,(p-1)*(q-1)))
crypto = [704796792,752211152,274704164,18414022,368270835,483295235,263072905,459788476,483295235,459788476,
          663551792,475206804,459788476,428313374,475206804,459788476,425392137,704796792,458265677,341524652,
          483295235,534149509,425392137,428313374,425392137,341524652,458265677,263072905,483295235,828509797,
          341524652,425392137,475206804,428313374,483295235,475206804,459788476,306220148]
flag1 = []
for c in crypto:
    flag1.append(pow(c,d,n))
print(flag1)
flag = []
for f in flag1:
    flag.append(chr(f))
print("".join(flag))
```

