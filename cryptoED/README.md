## 注意

1.安装

在该目录下执行`sudo python3 setup.py install --record install_log` 

​（numpy库的安装可能比较缓慢，请耐心等待）

2.使用

到任何目录下在命令行中输入`cryptoED` 

2.卸载：

到`install_log`的目录下执行，可能要以root身份运行

`cat install_log | xargs rm -rf`

`rm -rf *`

若在回收站删除不了的

到`~/.local/share/Trash`目录下，该目录就是回收站对应的目录

执行`sudo rm -rf *`

## ADFGVX密码

说明：

```
1.输入矩阵的长度为36，由26个字母和0～9组成
2.输入必须为字母
3.输入的明文或密文必须为字母或数字
```

测试：

1.加密

```
cryptoED adfgvx --en "the quick brown fox" --matrix "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8" --key "howareu"
```

2.解密    

```
cryptoED adfgvx --de "DXXFAFGFFXGGGFGXDVGDVGFAVFVAFVGG" --matrix "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8" --key "howareu" 
```

## ADFGX密码

说明：

```
1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
2.输入的明文或密文,密钥必须是字母
```

测试：

1.加密

```
cryptoED adfgx --en "the quick brown fox" --matrix "phqgmeaynofdxkrcvszwbutil" --key "howareu"
```

2.解密

```
cryptoED adfgx --de "DXADFAGXFXFFXDFXGGXDGFGAADAADXXF" --matrix "phqgmeaynofdxkrcvszwbutil" --key "howareu" 
```

## 仿射密码

说明：

```
1.m默认为26,其他情况暂时没有考虑
2.无法解密和加密的字符将原样输出
```

测试：

1.加密

```
cryptoED affine --en "the quick fox" -a 5 -b 8 
```

2.解密

```
cryptoED affine --de "zrc kewsg hat" -a 5 -b 8
```

## ascii与16,10,8,2进制之间的转换

说明：

```
1.ascii码转其他进制时,会限制输入。
2.ascii码转其他进制时是一个字符一个字符的转换
3.其他进制转ascii码时，可能出现无法识别的符号，因为输入的数字转化为ascii时，为不可打印字符 
```

测试：

1.ascii转16,10,8,2

```
cryptoED asciied --a2 "qw1测试"
```

2.16进制转ascii,10,8,2

```
cryptoED asciied --h2 "0x135f1b400"
```

3.10进制转ascii,16,8,2

```
cryptoED asciied --d2 "5200000"
```

4.8进制转ascii,16,10,2

```
cryptoED asciied --o2 "0o023654200"
```

5.2进制转ascii,16,10,8

```
cryptoED asciied --b2 "0b010011110101100010000000"
```

## 埃特巴什码

说明：

```
1.A~Z,a~z以外的字符将原样输出
```

测试：

1.加密

```
cryptoED atbash --en "the quick brown fox jumps over the lazy dog"
```

2.解密

```
cryptoED atbash --de "gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt"
```

## 自动密钥密码

说明：

```
1.输入的明文、密文及密钥必须是字母
```

测试：

1.加密

```
cryptoED autokey --en "the quick brown fox jumps over the lazy dog" --keyword "culture"
```

2.解密 

```
cryptoED autokey --de "vbpjozgdiveqvhyyaiicxcsnlfwwzvdpwvk" --keyword "culture"   
```

## 培根密码

说明：

```
1.无法加解密的将原样输出
```

测试：

1.加密

```
cryptoED baconian --en "the quick fox"
```

2.解密

```
cryptoED baconian --de "baabb aabbb aabaa  baaaa babaa abaaa aaaba ababa  aabab abbba babbb "
```

##  base64/32/16编码

说明：

```
1.进行编码和解码时，base64/32/16都会进行
2.base64编码表范围:A~Z,a~z,0~9,+,/
3.base32编码表范围:A~Z,2~7
4.base16编码表范围:0~9,A~F
```

测试：

1.编码

```
cryptoED base --en "这是一个测试"
```

```
cryptoED base --en "the quick brown fox"
```

2.解码

```
cryptoED base --de "6L+Z5piv5LiA5Liq5rWL6K+V"
```

```
cryptoED base --de "5C7ZTZUYV7SLRAHEXCVONNML5CXZK==="
```

```
cryptoED base --de "E8BF99E698AFE4B880E4B8AAE6B58BE8AF95"
```

```
cryptoED base --de "测试"   
```

 ## 博福特密码

说明：

```
1.关键字的字符必须是字母
2.无法加密或解密的将原样输出
3.加解密的过程相同
```

测试：

1.加密

```
cryptoED beaufort --en "the quick brown fox jumps over the lazy dog" --key "culture"
```

2.解密    

```
cryptoED beaufort --de "jnhdajcstufyezoxczicmozhcbkarumvrdy" --key "culture"
```

## 双密码

说明：

```
1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
2.输入的明文或密文必须是字母 
```

测试：

1.加密

```
cryptoED bifid --en "the quick brown fox" --matrix "phqgmeaylnofdxkrcvszwbuti"
```

2.解密  

```
cryptoED bifid --de "wetedtkznekyomex" --matrix "phqgmeaylnofdxkrcvszwbuti" 
```

## 凯撒密码

说明：

```
1.A~Z,a~z以外的字符将原样输出
2.有参数n时,按n的大小进行偏移
3.未指定n时,输出所有情况
4.将n指定为负数也行
```

测试：

1.加密

```
cryptoED caesar --en "the quick brown fox jumps over the lazy dog" -n 2
```

```
cryptoED caesar --en "the quick brown fox jumps over the lazy dog" -n -1
```

2.解密

```
cryptoED caesar --de "vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi" -n 2
```

```
cryptoED caesar --de "vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi"  
```

## 棋盘密码

说明：

```
1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
2.输入的明文或密文必须是字母
3.密钥必须是5个不同的字母
```

测试：

1.加密

```
cryptoED checkerboard --en "the quick brown fox" --matrix "knighpqrstoyzuamxwvblfedc" --keyl "brown" --keyu "quick"
```

2.解密  

```
cryptoED checkerboard --de "rkbkniruocbinkbqwkrioqwibunuoqwu" --matrix "knighpqrstoyzuamxwvblfedc" --keyl "brown" --keyu "quick" 
```

## escape编码

说明：

```
1.分为常用字符不编码与所有字符都编码
2.解码时，编码后的字符正常解码，未编码的常用字符直接输出
```

测试：

1.编码

```
cryptoED escape --en "asdwe@#测试"
```

```
cryptoED escape --en "asdwe@#!测试"
```

```
cryptoED escape --enall "asdwe@#测试"
```

```
cryptoED escape --en "#$*(123456789)@@"
```

```
cryptoED escape --en "#$(123456789)@@"
```

2.解码  

```
cryptoED escape --de "%u0074%u0068%u0065%u0020%u0066%u006f%u0078%u0023%u0025%u0026%u0026%u0020%u72d0%u72f8"
```

```
cryptoED escape --de "%u测试" 
```

```
cryptoED escape --de "测试%u2345"
```

```
cryptoED escape --de "%u2345测试aswes"
```

## 四方密码

说明：

```
1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
2.输入的明文或密文必须是字母
```

测试

1.加密

```
cryptoED foursquare --en "the quick brown fox" --ru "zgptfoihmuwdrcnykeqaxvsbl" --ld "mfnbdcrhsaxyogvituewlqzkp"
```

2.解密

```
cryptoED foursquare --de "eszwqafhgtdkwhrk" --ru "zgptfoihmuwdrcnykeqaxvsbl" --ld "mfnbdcrhsaxyogvituewlqzkp" 
```

## 格朗普雷密码

说明：

```
1.n的取值范围目前为6～9
2.加密结果有多种，目前只取一种，并且是随机
3.注意输入的所有单词中，26个字母必须出现一次以上
4.无法加密或解密的原样输出
```

测试：

1.加密

test.txt

```
ladybugs       
azimuths 
calfskin 
quackish 
unjovial 
evulston 
rowdyism 
sextuply
```

```
cryptoED grandpre --en "the quick fox" -n 8 --wordsfile test.txt
```

2.解密   

```
cryptoED grandpre --de "662761 4185234445 346783" -n 8 --wordsfile test.txt
```

## md5,sha家族

1.加密

```
cryptoED hashed --md5 "the quick fox"
cryptoED hashed --sha "the quick fox"   
```

2.目前只支持加密的情况



## 希尔密码

说明：

```
1.输入的明文或密文中必须全为字母
2.逆矩阵的计算有问题
```

测试：

1.加密

```
cryptoED hill --en "act" --key "gybnqkurp"
```

2.解密

```
cryptoED hill --de "poh" --key "gybnqkurp"    
```

## html实体编码

说明：

```
1.无法解码和无法编码的字符将原样输出
2.html实体参考手册 : https://www.w3school.com.cn/tags/html_ref_entities.html
3.该函数编码的范围较少,主要是",',&,<,>
4.解码主要是实体名称(&quot;&amp;),实体编号(&#34;&#38;),输出的结果为符号,解码的范围较多
```

测试：

1.编码

```
cryptoED htmled --en "<>&'" 
```

```
cryptoED htmled --en '<>&"'
```

```
cryptoED htmled --en "the <fox>"
```

```
cryptoED htmled --en "the <fox>狐狸"   
```

2.解码

```
cryptoED htmled --de "&lt;&gt;&amp;&#x27;"
```

```
cryptoED htmled --de "&lt;&gt;&amp;&quot;"
```

```
cryptoED htmled --de "the <fox>狐狸"
```

## 消息认证码

1.生成消息认证码

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "md5"
```

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha1"
```

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha224"
```

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha256"
```

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha384"
```

```
cryptoED maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha512"
```



## Morse电码

说明：

```
1.每个字符都以空格分隔
2.无法编码的将原样输出
```

测试：

1.编码

```
cryptoED morse --en "the quick brown fox"
```

```
cryptoED morse --en "the 测试"
```

```
cryptoED morse --en "the/#$%&*"
```

2.解码

```
cryptoED morse --de "- .... . --.- ..- .. -.-. -.- -... .-. --- .-- -. ..-. --- -..-"
```

```
cryptoED morse --de "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-"
```

```
cryptoED morse --de "- .... . 测试"
```

```
cryptoED morse --de "- .... . ()+￥%&*"
```

## 普莱菲尔密码

说明：

```
1.字母j当作i
2.明文的补充字母为x
3.若明文的长度为奇数，且末尾字母为x，则只能换为x
4.输入的明文或密文必须是字母
```

测试：

1.加密

```
cryptoED playfair --en "the quick brown fox jumps over the lazy dog" --key "culture"
```

```
cryptoED playfair --en "测试" --key "culture"
```

2.解密

```
cryptoED playfair --de "kundhlgtlfwueswplhsinpcgcragbuvzqavi" --key "culture"
```

```
cryptoED playfair --de "测试" --key "culture"
```

## 波利比奥斯方阵密码

说明：

```
1.解密后没保留空格
2.解密后注意i,j可相互替换
3.不可解密和不可加密的字符原样输出,解密后,除A~Z,其他都是不可解字符
```

测试：

1.编码

```
cryptoED polybiussq --en "the quick brown fox jumps over the lazy dog"
```

2.解码

```
cryptoED polybiussq --de "442315 4145241325 1242345233 213453 2445323543 34511542 442315 31115554 143422"
```

## Porta密码

说明：

```
1.密钥必须是字母
2.无法加密或解密的将原样输出
3.加密过程和解密过程相同
```

测试：

1.加密

```
cryptoED porta --en "the quick brown fox jumps over the lazy dog" --key "culture"
```

2.解密   

```
cryptoED porta --de "frwhkqryymfmfuaaolwhdalwijptzxhcngv" --key "culture" 
```

## 栅栏密码(含W型)

说明：

```
1.输入n的值有限制
2.w型的n>1
3.n为可选的，不指定n将输出所有情况
```

测试：

1.加密

```
cryptoED railfence --en "The quick brown fox jumps over the lazy dog" -n 2
```

```
cryptoED railfence --en "The quick brown fox jumps over the lazy dog" 
```

```
cryptoED railfence --enw "The quick brown fox jumps over the lazy dog" -n 2
```

```
cryptoED railfence --enw "The quick brown fox jumps over the lazy dog"
```

2.解密

```
cryptoED railfence --de "Teucbonojmsvrhlzdghqikrwfxupoeteayo" -n 2
```

```
cryptoED railfence --de "Teucbonojmsvrhlzdghqikrwfxupoeteayo"
```

```
cryptoED railfence --dew "Teucbonojmsvrhlzdghqikrwfxupoeteayo" -n 2
```

```
cryptoED railfence --dew "Teucbonojmsvrhlzdghqikrwfxupoeteayo" 
```

## ROT5/13/18/47

说明：

```
1.无法加密的将原样输出
2.加密和解密相同的字符串，结果一样
```

测试：

1.加密

```
cryptoED rot --en "the quick brown fox jumps over the lazy dog"
```

2.解密

```
cryptoED rot --de "gur dhvpx oebja sbk whzcf bire gur ynml qbt"
```

```
cryptoED rot --de "the quick brown fox jumps over the lazy dog"
```

## shellcode编码

测试：

1.编码

```
cryptoED shellcode --en "the quick brown fox jumps over the lazy dog"
```

```
cryptoED shellcode --en "这是一个测试"
```

2.解码

```
shellcode --de "\x74\x68\x65\x20\x71\x75\x69\x63\x6b\x20\x62\x72\x6f\x77\x6e\x20\x66\x6f\x78\x20\x6a\x75\x6d\x70\x73\x20\x6f\x76\x65\x72\x20\x74\x68\x65\x20\x6c\x61\x7a\x79\x20\x64\x6f\x67"
```

```
cryptoED shellcode --de "\x8fd9\x662f\x4e00\x4e2a\x6d4b\x8bd5"
```

```
cryptoED shellcode --de "测试"
```

## 敲击码编码

说明：

```
1.编码时要求输入字母，其他无法编码
2.解码时以字符中的空格作为间隔
```

测试：

1.编码

```
cryptoED tapcode --en "the quick brown fox"
```

```
cryptoED tapcode --en "the23"
```

2.解码

```
cryptoED tapcode --de ".... ..... .. ... . ..... .... .. ..... . .. .... . ... ... . . .. .... ... ... ..... ..... ... ... .... .. . ... ..... ..... .... "
```

```
cryptoED tapcode --de ".... ..... .."
```

```
cryptoED tapcode --de ".... ..... .. ...ce"    
```

## unicode与ascii/中文转换

说明：

```
1.输入的u的大小写无关
2.输入的unicode的四种方式不可混合  
```

测试：

1.unicode转ascii/中文

```
cryptoED unicode --u2az "&#x8fd9;&#x662f;&#x6d4b;&#x8bd5;"
```

```
cryptoED unicode --u2az "&#36825;&#26159;&#27979;&#35797;"
```

```
cryptoED unicode --u2az "\U8fd9\U662f\U6d4b\U8bd5"
```

```
cryptoED unicode --u2az "\U+8fd9\U+662f\U+6d4b\U+8bd5"
```

```
cryptoED unicode --u2az "&#x8fd9;&#26159;\u6d4b\U+8bd5"
```

```
cryptoED unicode --u2az "这是一个测试"
```

```
cryptoED unicode --u2az "&#测试;&#x662f;&#x4e00;&#x4e2a;&#x6d4b;&#x8bd5;"
```

```
cryptoED unicode --u2az "662f&#x4e00;&#x4e2a;&#x6d4b;&#x8bd5;"
```

2.ascii/中文转unicode

```
cryptoED unicode --az2u "the fox这是测试"
```

## URL编码

测试：

1.编码

```
cryptoED url --en "the fox&&测试"
```

2.解码

```
cryptoED url --de "the%20fox%26%26%E6%B5%8B%E8%AF%95"
```

```
cryptoED url --de "这是测试"
```

## UUencode编码

说明：

```
1.编码后会有空行
2.uu --de "/=&AE(&9O>"8FYK6+Z*^5" 有问题 可改为''
```

测试：

1.编码

```
cryptoED uu --en "the fox&&测试"
```

2.解码

```
cryptoED uu --de "2Z+^9YIBOY+B Y+BJYK6+Z*^5"
```

```
cryptoED uu --de "/=&AE(&9O>"8FYK6+Z*^5"
```

```
cryptoED uu --de '/=&AE(&9O>"8FYK6+Z*^5'
```

```
cryptoED uu --de "测试"
```

```
cryptoED uu --de "qwdqwe123"
```

```
cryptoED uu --de "@#$%^&*"
```

##  维吉尼亚密码

说明：

```
1.要求明文或密文与密钥同时输入
2.无法加密和无法解密的字符将原样输出
```

测试：

1.加密

```
cryptoED vigenere --en "the quick fox" --key "ant"
```

2.解密

```
cryptoED vigenere --de "tuxqhbcxyok" --key "ant"
```

## XXencode编码

说明：

```
1.有些和在线网站上的结果有差异
2.解码结果为中文的无法正常显示
```

测试：

1.编码

```
cryptoED xx --en "The quick brown fox jumps over the lazy dog"
```

```
cryptoED xx --en "测试"
```

```
cryptoED xx --en "#%&"
```

2.解码  

```
cryptoED xx --de "J4VZ653pOKBf647mPrRi64NjS0-eRKpkQm-jRaJm65FcNG-gMLdt64FjNk" 
```

```
cryptoED xx --de "PIi9pE"
```

```
cryptoED xx --de "6mIa"
```


