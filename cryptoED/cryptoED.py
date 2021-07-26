#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author : garlic
# @Time   : 2020/2/1 上午10:57
import click
import binascii
import base64
import quopri
import urllib.parse
import chardet
import math
import string
import html
import numpy
import hashlib
import hmac
import gmpy2


@click.group()
def crypto():
    pass


def get_key(dict, value):  # 在字典中，由value获得key
    for k, v in dict.items():
        if v == value:
            return k


@click.command()
@click.option('--a2', help='ascii转16,10,8,2')
@click.option('--h2', help='16进制转ascii,10,8,2')
@click.option('--d2', help='10进制转ascii,16,8,2')
@click.option('--o2', help='8进制转ascii,16,10,2')
@click.option('--b2', help='2进制转ascii,16,10,8')
def asciiED(a2, h2, d2, o2, b2):
    """
    ascii与16,10,8,2进制之间的转换
    """
    # =============================================================================
    # 1.ascii码转其他进制时,会限制输入。
    # 2.ascii码转其他进制时是一个字符一个字符的转换
    # 3.其他进制转ascii码时，可能出现无法识别的符号，因为输入的数字转化为ascii时，为不可打印字符
    # =============================================================================
    # =============================================================================
    # 测试：
    # 1.ascii转16,10,8,2
    # (1)asciied --a2 "12"
    # （2）asciied --a2 "qw"
    # （3）asciied --a2 "qw1234"
    # （4）asciied --a2 "qw1#$%"
    # （5）asciied --a2 "qw1测试"
    # （6）asciied --a2 "   "
    # 2.16进制转ascii,10,8,2
    # （1）asciied --h2 "0x135f1b400"
    # 3.10进制转ascii,16,8,2
    # （1）asciied --d2 "5200000"
    # 4.8进制转ascii,16,10,2
    # （1）asciied --o2 "0o023654200"
    # 5.2进制转ascii,16,10,8
    # （1）asciied --b2 "0b010011110101100010000000"
    # =============================================================================
    if a2:  # ascii转16,10,8,2
        s16 = ''  # 转16
        s16_1 = ''
        s10 = ''  # 转10
        s8 = ''  # 转8
        s2 = ''  # 转2
        for ch in a2:
            if ord(ch) < 32 or ord(ch) > 126:
                click.echo("请输入ASCII可打印字符")
                return
            # 转16
            s = hex(ord(ch))[2:]
            s16 += s + " "
            s16_1 += s
            # 转10
            s10 += str(ord(ch)) + " "
            # 转8
            s = str(oct(ord(ch)))[2:]
            if len(s) % 3:
                s = '0' * (3 - len(s) % 3) + s
            s8 += s + " "
            # 转2
            s = str(bin(ord(ch))[2:])
            if len(s) % 8:
                s = '0' * (8 - len(s) % 8) + s
            # 转换成二进制后不会自动补0
            s2 += s + " "

        click.echo("ascii转16进制(1):" + s16)
        click.echo("ascii转16进制(2):" + '0x' + s16_1)
        click.echo("ascii转10进制:" + s10)
        click.echo("ascii转 8进制:" + s8)
        click.echo("ascii转 2进制:" + s2)

    elif h2:  # 16进制转ascii,10,8,2
        try:
            s10 = int(h2, 16)
            s2 = str(bin(s10))[2:]
            if len(s2) % 8:
                s2 = '0' * (8 - len(s2) % 8) + s2
            s2 = '0b' + s2
            s8 = str(oct(s10))[2:]
            if len(s8) % 3:
                s8 = '0' * (3 - len(s8) % 3) + s8
            s8 = '0o' + s8
            click.echo("16进制转2进制:" + s2)
            click.echo("16进制转8进制:" + s8)
            click.echo("16进制转10进制:" + str(s10))

        except Exception as e:
            click.echo("16进制转2,8,10错误:" + str(e.args))
        try:
            h2 = h2.replace("0x", "")
            sa = bytes.decode(binascii.unhexlify(h2))
            click.echo("16进制转ascii码:" + sa)
        except Exception as e:
            click.echo("16进制转ascii码错误:" + str(e.args))
    elif d2:  # 10进制转ascii,16,8,2
        s2 = ""
        s8 = ""
        s16 = ""
        sa = ""
        if " " in d2:
            d = d2.split(" ")
            for ch in d:
                s2 += str(bin(int(ch)))[2:] + " "
                s8 += str(oct(int(ch)))[2:] + " "
                s16 += hex(int(ch))[2:] + " "
                sa += chr(int(ch))
            click.echo("10进制转2进制:" + s2)
            click.echo("10进制转8进制:" + s8)
            click.echo("10进制转16进制:" + s16)
            click.echo("10进制转ascii码:" + sa)
        else:
            try:
                s2 = str(bin(int(d2)))[2:]
                if len(s2) % 8:
                    s2 = '0' * (8 - len(s2) % 8) + s2
                s2 = '0b' + s2
                click.echo("10进制转2进制:" + s2)
                s8 = str(oct(int(d2)))[2:]
                if len(s8) % 3:
                    s8 = '0' * (3 - len(s8) % 3) + s8
                s8 = '0o' + s8
                click.echo("10进制转8进制:" + s8)
                s16 = hex(int(d2))
                click.echo("10进制转16进制:" + s16)
            except Exception as e:
                click.echo("10进制转2,8,16进制错误:" + str(e.args))
            try:
                s = hex(int(d2))
                sa = bytes.decode(binascii.unhexlify(str(s)[2:]))
                click.echo("10进制转ascii码:" + sa)
            except Exception as e:
                click.echo("10进制转ascii码错误:" + str(e.args))

    elif o2:  # 8进制转ascii,16,10,2
        try:
            s2 = str(bin(int(o2, 8)))[2:]
            if len(s2) % 8:
                s2 = '0' * (8 - len(s2) % 8) + s2
            s2 = '0b' + s2
            click.echo("8进制转2进制:" + s2)
            s10 = int(o2, 8)
            click.echo("8进制转10进制:" + str(s10))
            s16 = hex(s10)
            click.echo("8进制转16进制:" + s16)
        except Exception as e:
            click.echo("8进制转2,10,16进制错误:" + str(e.args))
        try:
            s = hex(int(o2, 8))
            sa = bytes.decode(binascii.unhexlify(str(s)[2:]))
            click.echo("8进制转ascii码:" + sa)
        except Exception as e:
            click.echo("8进制转ascii码错误:" + str(e.args))
    elif b2:  # 2进制转ascii,16,10,8
        try:
            s8 = str(oct(int(b2, 2)))[2:]
            if len(s8) % 3:
                s8 = '0' * (3 - len(s8) % 3) + s8
            s8 = '0o' + s8
            click.echo("2进制转8进制:" + s8)
            s10 = int(b2, 2)
            click.echo("2进制转10进制:" + str(s10))
            s16 = hex(s10)
            click.echo("2进制转16进制:" + s16)
        except Exception as e:
            click.echo("2进制转8,10,16进制错误:" + str(e.args))
        try:
            s = hex(int(b2, 2))
            sa = bytes.decode(binascii.unhexlify(str(s)[2:]))
            click.echo("2进制转ascii码:" + sa)
        except Exception as e:
            click.echo("2进制转ascii码错误:" + str(e.args))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='base64/32/16编码')
@click.option('--de', help='base64/32/16解码')
def base(en, de):
    """
    base64/32/16编码
    """
    # =============================================================================
    # 1.进行编码和解码时，base64/32/16都会进行
    # 2.base64编码表范围:A~Z,a~z,0~9,+,/
    # 3.base32编码表范围:A~Z,2~7
    # 4.base16编码表范围:0~9,A~F
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.编码
    # （1）base --en "这是一个测试"
    # （2）base --en "the quick brown fox"
    # 2.解码
    # （1）base --de "6L+Z5piv5LiA5Liq5rWL6K+V"
    # （2）base --de "5C7ZTZUYV7SLRAHEXCVONNML5CXZK==="
    # （3）base --de "E8BF99E698AFE4B880E4B8AAE6B58BE8AF95"
    # （4）base --de "测试"
    # =============================================================================
    if en:
        click.echo("base64编码:" + bytes.decode(base64.b64encode(str.encode(en))))
        click.echo("base32编码:" + bytes.decode(base64.b32encode(str.encode(en))))
        click.echo("base16编码:" + bytes.decode(base64.b16encode(str.encode(en))))

    elif de:
        try:
            encoding64 = chardet.detect(base64.b64decode(de))['encoding']
            click.echo("base64解码:" + base64.b64decode(de).decode(encoding64))
        except Exception as e:
            click.echo("base64解码错误:" + str(e.args))
        try:
            encoding32 = chardet.detect(base64.b32decode(de))['encoding']
            click.echo("base32解码:" + base64.b32decode(de).decode(encoding32))
        except Exception as e:
            click.echo("base32解码错误:" + str(e.args))
        try:
            encoding16 = chardet.detect(base64.b16decode(de))['encoding']
            click.echo("base16解码:" + base64.b16decode(de).decode(encoding16))
        except Exception as e:
            click.echo("base16解码错误:" + str(e.args))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='shellcode编码')
@click.option('--de', help='shellcode解码')
def shellcode(en, de):
    """shellcode编码 """
    # =============================================================================
    # 测试
    # 1.编码
    # （1）shellcode --en "the quick brown fox jumps over the lazy dog"
    # （2）shellcode --en "这是一个测试"
    #
    # 2.解码
    # （1）shellcode --de "\x74\x68\x65\x20\x71\x75\x69\x63\x6b\x20\x62\x72\x6f\x77\x6e\x20\x66\x6f\x78\x20\x6a\x75\x6d\x70\x73\x20\x6f\x76\x65\x72\x20\x74\x68\x65\x20\x6c\x61\x7a\x79\x20\x64\x6f\x67"
    # （2）shellcode --de "\x8fd9\x662f\x4e00\x4e2a\x6d4b\x8bd5"
    # （3）shellcode --de "测试"
    # =============================================================================
    if en:
        ans = ""
        # en = "".join(en.split(" "))
        for ch in en:
            s = "\\x" + str(hex(ord(ch)))[2:]
            ans += s
        click.echo("shellcode编码:" + ans)
    elif de:
        ans = ""
        ls = de.split("\\x")
        try:
            for ch in ls:
                if ch:  # 分割时第一个为空
                    s = chr(int(ch, 16))
                    ans += s
            click.echo("shellcode解码:" + ans)
        except Exception as e:
            click.echo("shellcode解码错误:" + str(e.args))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='quoted-printable编码')
@click.option('--de', help='quoted-printable解码')
def qp(en, de):
    """quoted-printable编码 """
    # =============================================================================
    # 测试
    # 1.编码
    # （1）qp --en "这是一个测试"
    # （2）qp --en "the fox&&   测试"
    # 2.解码
    # （1）qp --de "=E8=BF=99=E6=98=AF=E4=B8=80=E4=B8=AA=E6=B5=8B=E8=AF=95"
    # （2）qp --de "the fox&&   测试"
    # =============================================================================
    if en:
        click.echo("quoted-printable编码:" + bytes.decode(quopri.encodestring(str.encode(en))))
        # encode,decode是对文件加解密,encodestring,decodestring是对字符串加解密
    elif de:
        click.echo("quoted-printable解码:" + bytes.decode(quopri.decodestring(str.encode(de))))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='XXencode编码')
@click.option('--de', help='XXencode解码')
def xx(en, de):
    """XXencode编码"""
    # =============================================================================
    # 1.有些和在线网站上的结果有差异
    # 2.解码结果为中文的无法正常显示
    # =============================================================================

    # =============================================================================
    # 测试
    # 1.编码
    # （1）xx --en "The quick brown fox jumps over the lazy dog"
    # （2）xx --en "测试"
    # （3）xx --en "#%&"
    # 2.解码
    # （1）xx --de "J4VZ653pOKBf647mPrRi64NjS0-eRKpkQm-jRaJm65FcNG-gMLdt64FjNk"
    # （2）xx --de "PIi9pE"
    # （3）xx --de "6mIa"
    # =============================================================================
    alldata = "+-" + string.digits + string.ascii_uppercase + string.ascii_lowercase
    if en:
        tmp = ''
        for ch in en:
            ch = str(bin(ord(ch))[2:])
            if len(ch) % 8 != 0:
                ch = '0' * (8 - len(ch) % 8) + ch
            tmp += ch
        # tmp += tmp + '0'*(24 - len(tmp)%24)
        # print(tmp)
        if len(tmp) % 6 != 0:
            tmp = tmp + '0' * (6 - len(tmp) % 6)
        tmp1 = []
        for i in range(0, len(tmp), 6):
            tmp1.append(tmp[i:i + 6])
        ans = ''
        for ch in tmp1:
            i = int(ch, 2)
            ans += alldata[i]
        click.echo("XXencode编码:" + ans)
    elif de:
        ans = ''
        tmp = ''
        for ch in de:
            if ch not in alldata:
                click.echo("错误：无法解码")
                return
            i = alldata.index(ch)
            sh = bin(i)[2:]
            if len(sh) % 6 != 0:
                sh = '0' * (6 - len(sh) % 6) + sh
            tmp += sh
        for i in range(0, len(tmp), 8):
            ch = chr(int(tmp[i:i + 8], 2))
            ans += ch
        click.echo("XXencode解码:" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='UUencode编码')
@click.option('--de', help='UUencode解码')
def uu(en, de):
    """UUencode编码 """

    # =============================================================================
    # 1.编码后会有空行
    # 2.uu --de "/=&AE(&9O>"8FYK6+Z*^5" 有问题 可改为''
    # =============================================================================

    # =============================================================================
    # 测试
    # 1.编码
    # （1）uu --en "the fox&&测试"
    #
    # 2.解码
    # （1）uu --de "2Z+^9YIBOY+B Y+BJYK6+Z*^5"
    # （2）uu --de "/=&AE(&9O>"8FYK6+Z*^5"
    # （3）uu --de '/=&AE(&9O>"8FYK6+Z*^5'
    # （4）uu --de "测试"
    # （5）uu --de "qwdqwe123"
    # （6）uu --de "@#$%^&*"
    # =============================================================================
    if en:
        click.echo("UUencode编码:" + bytes.decode(binascii.b2a_uu(str.encode(en))))
    elif de:
        try:
            click.echo("UUencode解码:" + bytes.decode(binascii.a2b_uu(str.encode(de))))
        except Exception as e:
            click.echo("UUencode解码错误:" + str(e.args))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='URL编码')
@click.option('--de', help='URL解码')
def url(en, de):
    """URL编码 """
    # =============================================================================
    # 测试
    # 1.编码
    # （1）url --en "the fox&&测试"
    #
    # 2.解码
    # （1）url --de "the%20fox%26%26%E6%B5%8B%E8%AF%95"
    # （2）url --de "这是测试"
    # =============================================================================
    if en:
        click.echo("URL编码:" + urllib.parse.quote(en))
    elif de:
        click.echo("URL解码:" + urllib.parse.unquote(de))
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--u2az', help='unicode转ascii/中文')
@click.option('--az2u', help='ascii/中文转unicode')
def unicode(u2az, az2u):
    """  unicode与ascii/中文转换 """
    # =============================================================================
    # 1.输入的u的大小写无关
    # 2.输入的unicode的四种方式不可混合
    # =============================================================================

    # =============================================================================
    # 测试
    # 1.unicode转ascii/中文
    # （1）unicode --u2az "&#x8fd9;&#x662f;&#x6d4b;&#x8bd5;"
    # （2）unicode --u2az "&#36825;&#26159;&#27979;&#35797;"
    # （3）unicode --u2az "\U8fd9\U662f\U6d4b\U8bd5"
    # （4）unicode --u2az "\U+8fd9\U+662f\U+6d4b\U+8bd5"
    # （5）unicode --u2az "&#x8fd9;&#26159;\u6d4b\U+8bd5"
    # （6）unicode --u2az "这是一个测试"
    # （7）unicode --u2az "&#测试;&#x662f;&#x4e00;&#x4e2a;&#x6d4b;&#x8bd5;"
    # （8）unicode --u2az "662f&#x4e00;&#x4e2a;&#x6d4b;&#x8bd5;"
    # 2.ascii/中文转unicode
    # （1）unicode --az2u "the fox这是测试"
    #
    # =============================================================================

    if u2az:
        try:
            if "&#x" in u2az:
                ls = u2az.split("&#x")
                ls1 = []
                for ch in ls:
                    if ch:
                        ls1.append(ch[:-1])
                ans = ""
                for ch in ls1:
                    if ch:
                        s = chr(int(ch, 16))
                        ans += s
                click.echo("unicode转ascii/中文:" + ans)
            elif "&#" in u2az:
                ls = u2az.split("&#")
                ls1 = []
                for ch in ls:
                    if ch:
                        ls1.append(ch[:-1])
                ans = ""
                for ch in ls1:
                    if ch:
                        s = chr(int(ch))
                        ans += s
                click.echo("unicode转ascii/中文:" + ans)
            elif "\\U+" in u2az.upper():
                ls = (u2az.upper()).split("\\U+")
                ans = ""
                for ch in ls:
                    if ch:
                        s = chr(int(ch, 16))
                        ans += s
                click.echo("unicode转ascii/中文:" + ans)
            elif "\\U" in u2az.upper():
                ls = (u2az.upper()).split("\\U")
                ans = ""
                for ch in ls:
                    if ch:
                        s = chr(int(ch, 16))
                        ans += s
                click.echo("unicode转ascii/中文:" + ans)
            else:
                click.echo("unicode转ascii/中文错误:" + "应为&#x[Hex];,&#[Decimal];,\\U[Hex],\\U+[Hex]之一")
        except Exception as e:
            click.echo("unicode转ascii/中文错误:" + str(e.args))



    elif az2u:
        ans1 = ""
        ans2 = ""
        ans3 = ""
        ans4 = ""
        for ch in az2u:
            s1 = str(hex(ord(ch)))[2:]
            s2 = str(ord(ch))
            s3 = str(hex(ord(ch)))[2:]
            s4 = str(hex(ord(ch)))[2:]
            if len(s1) % 4:  # 编码范围??
                s1 = "0" * (4 - len(s1) % 4) + s1
            if len(s2) % 5:
                s2 = "0" * (5 - len(s2) % 5) + s2
            if len(s3) % 4:
                s3 = "0" * (4 - len(s3) % 4) + s3
            if len(s4) % 4:
                s4 = "0" * (4 - len(s4) % 4) + s4
            ans1 += "&#x" + s1 + ";"
            ans2 += "&#" + s2 + ";"
            ans3 += "\\U" + s3
            ans4 += "\\U+" + s4
        click.echo("ascii/中文转unicode(1):" + ans1)
        click.echo("ascii/中文转unicode(2):" + ans2)
        click.echo("ascii/中文转unicode(3):" + ans3)
        click.echo("ascii/中文转unicode(4):" + ans4)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='escape编码(常用不编码)')
@click.option('--enall', help='escape编码(所有都编码)')
@click.option('--de', help='escape解码')
def escape(en, enall, de):
    """escape编码 """
    # =============================================================================
    # 1.分为常用字符不编码与所有字符都编码
    # 2.解码时，编码后的字符正常解码，未编码的常用字符直接输出
    # =============================================================================

    # =============================================================================
    # 测试：
    # 1.编码
    # （1）escape --en "asdwe@#测试"
    # （2）escape --en "asdwe@#!测试"
    # （3）escape --enall "asdwe@#测试"
    # （4）escape --en "#$*(123456789)@@"
    # （5）escape --en "#$(123456789)@@"
    # 2.解码
    # （1）escape --de "%u0074%u0068%u0065%u0020%u0066%u006f%u0078%u0023%u0025%u0026%u0026%u0020%u72d0%u72f8"
    # （2）escape --de "%u测试"
    # （3）escape --de "测试%u2345"
    # （4）escape --de "%u2345测试aswes"
    # =============================================================================

    if en:
        ans = ""
        for ch in en:
            if ord(ch) >= 21 and ord(ch) <= 126:
                s = ch
            else:
                s = str(hex(ord(ch)))[2:]
                if len(s) % 4:  # 不足4位补0,一般情况???utf-16编码范围??
                    s = "0" * (4 - len(s) % 4) + s
                s = "%u" + s
            ans += s
        click.echo("escape编码(常用不编码):" + ans)
    elif enall:
        ans = ""
        for ch in enall:
            s = str(hex(ord(ch)))[2:]
            if len(s) % 4:
                s = "0" * (4 - len(s) % 4) + s
            ans += "%u" + s
        click.echo("escape编码(所有都编码):" + ans)

    elif de:
        ans = ""
        tmp = de.split("%u")  # 一般情况，第一个为空
        if tmp[0]:
            # python cryptoED.py escapeed --de "wq12@#%u8fd9"
            ans += tmp[0]
        if len(tmp) >= 2:  # python cryptoED.py escapeed --de "这是一个测试%u8fd9"
            tmp1 = []
            for i in range(1, len(tmp)):
                tmp1.append(tmp[i])
            try:
                for ch in tmp1:
                    if len(ch) > 4:  # 存在常用字符
                        s1 = ch[0:4]
                        s2 = ch[4:]
                        s = chr(int(s1, 16)) + s2
                        ans += s
                    else:
                        s = chr(int(ch, 16))
                        ans += s
            except Exception as e:
                click.echo("escape解码错误:" + str(e.args))
                return
        click.echo("escape解码:" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='html实体编码')
@click.option('--de', help='html实体解码')
def htmlED(en, de):
    """html实体编码"""
    # =============================================================================
    # 1.无法解码和无法编码的字符将原样输出
    # 2.html实体参考手册 : https://www.w3school.com.cn/tags/html_ref_entities.html
    # 3.该函数编码的范围较少,主要是",',&,<,>
    # 4.解码主要是实体名称(&quot;&amp;),实体编号(&#34;&#38;),输出的结果为符号,解码的范围较多
    #
    # =============================================================================

    # =============================================================================
    # 测试：
    # 1.编码
    # （1）htmled --en "<>&'"
    # （2）htmled --en '<>&"'
    # （3）htmled --en "the <fox>"
    # （4）htmled --en "the <fox>狐狸"
    # 2.解码
    # （1）htmled --de "&lt;&gt;&amp;&#x27;"
    # （2）htmled --de "&lt;&gt;&amp;&quot;"
    # （3）htmled --de "the <fox>狐狸"
    # =============================================================================

    if en:
        ans = ''
        for ch in en:
            if ch in ['<', '>', '"', "'", '&']:
                ans += html.escape(ch)
            else:
                i = ord(ch)
                ans += '&#' + str(i) + ';'
        # click.echo("html实体编码:" + "正在努力中,谢谢支持!!!")
        # ans = html.escape(ans)
        click.echo("html实体编码:" + ans)
    elif de:
        ans = html.unescape(de)
        click.echo("html实体解码:" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='敲击码编码')
@click.option('--de', help='敲击码解码')
# @click.option('--show',help='查看明文密文对应关系')
def tapcode(en, de):
    """敲击码编码"""
    '''
      1 2  3  4 5
    1 A B C/K D E 
    2 F G  H  I J
    3 L  M  N O P
    4 Q  R  S T U
    5 V  W  X Y Z
    
    F  => 2,1 => .. .
    O  => 3,4 => ... ....
    X  => 5,3 => ..... ... 
    '''
    # =============================================================================
    # 1.编码时要求输入字母，其他无法编码
    # 2.解码时以字符中的空格作为间隔
    # =============================================================================

    # =============================================================================
    # 测试：
    # 1.编码
    # （1）tapcode --en "the quick brown fox"
    # （2）tapcode --en "the23"
    #
    # 2.解码
    # （1）tapcode --de ".... ..... .. ... . ..... .... .. ..... . .. .... . ... ... . . .. .... ... ... ..... ..... ... ... .... .. . ... ..... ..... .... "
    # （2）tapcode --de ".... ..... .."
    # （3）tapcode --de ".... ..... .. ...ce"
    # =============================================================================

    #    data = {'A': '. .', 'B': '. ..', 'C': '. ...',
    #               'D': '. ....', 'E': '. .....', 'F': '.. .',
    #               'G': '.. ..', 'H': '.. ...', 'I': '.. ....',
    #               'J': '.. .....', 'K': '. ...', 'L': '... .',
    #               'M': '... ..', 'N': '... ...', 'O': '... ....',
    #               'P': '... .....', 'Q': '.... .', 'R': '.... ..',
    #               'S': '.... ...', 'T': '.... ....', 'U': '.... .....',
    #               'V': '..... .', 'W': '..... ..', 'X': '..... ...',
    #               'Y': '..... ....', 'Z': '..... .....'}
    alldata = string.ascii_lowercase
    data = {}
    for i in range(5):
        for j in range(5):  # 生成字母与 . 对应的字典
            data[alldata[5 * i + j]] = (i + 1) * '.' + ' ' + (j + 1) * '.'
    print("明密文对应关系：")
    print(data)
    if en:
        ans = ""
        en = "".join((en.lower()).split(" "))
        for ch in en:
            if ch not in alldata:  # 输入的字符不是字母
                click.echo("错误：明文为字母")
                return
            if ch in data.keys():
                ans += data[ch] + ' '
        click.echo("敲击码编码:" + ans)
    elif de:
        tmp = (de.strip()).split(" ")  # 去掉两边可能的空格
        if len(tmp) % 2 != 0:
            click.echo("错误：以空格相隔的密文数应为偶数位")
            return
        tmp1 = []
        for i in range(0, len(tmp), 2):
            tmp1.append(tmp[i] + " " + tmp[i + 1])
        ans = ''
        for ch in tmp1:
            if ch in data.values():
                ans += get_key(data, ch)
            else:
                click.echo("错误：无法解码")
                return
        click.echo("敲击码解码:" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option('--en', help='Morse编码')
@click.option('--de', help='Morse解码')
def morse(en, de):
    """Morse电码 """
    # =============================================================================
    # 1.每个字符都以空格分隔
    # 2.无法编码的将原样输出
    # =============================================================================

    # =============================================================================
    # 测试：
    # 在线：http://www.zhongguosou.com/zonghe/moErSiCodeConverter.aspx
    # 1.编码：
    # （1）morse --en "the quick brown fox"
    # （2）morse --en "the 测试"
    # （3）morse --en "the/#$%&*"
    #
    # 2.解码
    # （1）morse --de "- .... . --.- ..- .. -.-. -.- -... .-. --- .-- -. ..-. --- -..-"
    # （2）morse --de "- .... ./--.- ..- .. -.-. -.-/-... .-. --- .-- -./..-. --- -..-"
    # （3）morse --de "- .... . 测试"
    # （4）morse --de "- .... . ()+￥%&*"
    #
    # =============================================================================
    alldata = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        '.': '.-.-.-', ':': '---...', ',': '--..--',
        ';': '-.-.-.', '?': '..--..', '=': '-...-',
        "'": '.----.', '/': '-..-.', '!': '-.-.--',
        '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '(': '-.--.', ')': '-.--.-', '$': '...-..-',
        '&': '.-...', '@': '.--.-.', '+': '.-.-.'
    }

    if en:
        ans = ""
        for ch in en.upper():
            if ch in alldata.keys():
                ans += alldata[ch] + " "
            else:
                ans += ch
        click.echo("Morse编码:" + ans)
    elif de:
        ans = ""
        de = de.replace('/', ' ')
        ls = (de.strip()).split(" ")
        for ch in ls:
            if ch in alldata.values():
                ans += get_key(alldata, ch)
            else:
                ans += ch
        click.echo("Morse解码:" + ans.lower())
    else:
        click.echo("请查看帮助信息：--help")

    ########################################################################################################################


@click.command()
@click.option('--en', help='栅栏密码加密')
@click.option('--de', help='栅栏密码解密')
@click.option('--enw', help='W型栅栏密码加密')
@click.option('--dew', help='W型栅栏密码解密')
@click.option('-n', type=int, help='栏数（可选）')
# 全部输出的情况,n的限制
def railfence(en, de, enw, dew, n):
    """栅栏密码(含W型)"""
    # =============================================================================
    # 1.输入n的值有限制
    # 2.w型的n>1
    # 3.n为可选的，不指定n将输出所有情况
    # =============================================================================

    # =============================================================================
    # 测试
    # 1.加密
    # （1）railfence --en "The quick brown fox jumps over the lazy dog" -n 2
    # （2）railfence --en "The quick brown fox jumps over the lazy dog"
    # （3）railfence --enw "The quick brown fox jumps over the lazy dog" -n 2
    # （4）railfence --enw "The quick brown fox jumps over the lazy dog"
    # 2.解密
    # （1）railfence --de "Teucbonojmsvrhlzdghqikrwfxupoeteayo" -n 2
    # （2）railfence --de "Teucbonojmsvrhlzdghqikrwfxupoeteayo"
    # （3）railfence --dew "Teucbonojmsvrhlzdghqikrwfxupoeteayo" -n 2
    # （4）railfence --dew "Teucbonojmsvrhlzdghqikrwfxupoeteayo"
    # =============================================================================
    if en and n:  # n为0或者为空时不会执行
        if n < 0:  # 有参数n并且n<=0的情况
            click.echo("错误:" + "n>0")
            return
        en = en.replace(" ", "")  # 去掉空格
        ls = []
        for i in range(0, len(en), n):
            if len(en) > n + i:  # 等号问题
                ls.append(en[i:i + n])
            else:
                ls.append(en[i:])
        ls1 = []
        for i in range(len(ls[0])):
            for j in range(len(ls)):
                if len(ls[j]) > i:
                    ls1.append(ls[j][i])
        ans = "".join(ls1)
        click.echo("栅栏密码加密:" + ans)

    elif en and n == None:  # 不指定n，则输出所有情况
        en = en.replace(" ", "")  # 去掉空格
        m = len(en) + 1
        for k in range(1, m):
            ls = []
            for i in range(0, len(en), k):
                if len(en) > k + i:  # 等号问题
                    ls.append(en[i:i + k])
                else:
                    ls.append(en[i:])
            ls1 = []
            for i in range(len(ls[0])):
                for j in range(len(ls)):
                    if len(ls[j]) > i:
                        ls1.append(ls[j][i])
            ans = "".join(ls1)
            click.echo("栅栏密码加密" + "(" + str(k) + "):" + ans)

    elif de and n:
        if n < 0:
            click.echo("栅栏密码解密错误:" + "n>0")
            return
        m = math.ceil(len(de) / n)
        ls = []
        for i in range(0, len(de), m):
            if len(de) > m + i:  # 等号问题
                ls.append(de[i:i + m])
            else:
                ls.append(de[i:])
        # print(ls)
        ls1 = []
        for i in range(len(ls[0])):
            for j in range(len(ls)):
                if len(ls[j]) > i:
                    ls1.append(ls[j][i])
        ans = "".join(ls1)
        click.echo("栅栏密码解密:" + ans)

    elif de and n == None:
        l = len(de) + 1
        for k in range(1, l):
            m = math.ceil(len(de) / k)
            ls = []
            for i in range(0, len(de), m):
                if len(de) > m + i:  # 等号问题
                    ls.append(de[i:i + m])
                else:
                    ls.append(de[i:])
            # print(ls)
            ls1 = []
            for i in range(len(ls[0])):
                for j in range(len(ls)):
                    if len(ls[j]) > i:
                        ls1.append(ls[j][i])
            ans = "".join(ls1)
            click.echo("栅栏密码解密:" + "(" + str(k) + "):" + ans)

    elif enw and n:
        if n < 1 or n > len(enw):
            click.echo("错误:" + "n>1 并且 n < len（enw）")
            return
        enw = enw.replace(" ", "")  # 去掉空格
        tmp = []
        for i in range(n):
            tmp.append(enw[i])

        flag = 0
        pos = n - 1
        for i in range(n, len(enw)):
            if flag == 0:
                pos = pos - 1
                tmp[pos] += enw[i]
                if pos == 0:
                    flag = 1

            elif flag == 1:
                pos = pos + 1
                tmp[pos] += enw[i]
                if pos == n - 1:
                    flag = 0
        ans = "".join(tmp)
        click.echo("栅栏密码加密（w型）:" + ans)

    elif enw and n == None:
        enw = enw.replace(" ", "")  # 去掉空格
        l = len(enw)
        for k in range(2, l):  # 注意w型要求栏数大于1
            tmp = []
            for i in range(k):
                tmp.append(enw[i])
            flag = 0
            pos = k - 1
            for i in range(k, l):
                if flag == 0:
                    pos = pos - 1
                    tmp[pos] += enw[i]
                    if pos == 0:
                        flag = 1

                elif flag == 1:
                    pos = pos + 1
                    tmp[pos] += enw[i]
                    if pos == k - 1:
                        flag = 0
            ans = "".join(tmp)
            click.echo("栅栏密码加密（w型）:" + "(" + str(k) + "):" + ans)

    elif dew and n:
        if n < 1 or n > len(dew):
            click.echo("错误:" + "n>1 并且 n < len（dew）")
            return
        dew = dew.replace(" ", "")  # 去掉空格
        tmp = []  # 记录每一栏的元素个数
        for i in range(n):
            tmp.append(1)
        flag = 0
        pos = n - 1
        tmp1 = ''  # 记录读取每一栏的顺序
        for i in range(n, len(dew)):
            if flag == 0:
                pos = pos - 1
                tmp1 += str(pos)
                tmp[pos] += 1
                if pos == 0:
                    flag = 1

            elif flag == 1:
                pos = pos + 1
                tmp1 += str(pos)
                tmp[pos] += 1
                if pos == n - 1:
                    flag = 0
        tmp2 = []  # 记录每一栏的元素
        j = 0
        for i in tmp:
            tmp2.append(dew[j:j + i])
            j = j + i
        ans = ''
        tmp3 = []  # 记录每一栏将要访问的元素
        for i in range(n):
            ans += tmp2[i][0]
            tmp3.append(1)
        for j in tmp1:
            j = int(j)
            ans += tmp2[j][tmp3[j]]
            tmp3[j] += 1
        click.echo("栅栏密码解密:" + ans)

    elif dew and n == None:
        l = len(dew)
        for k in range(2, l):  # 注意w型要求栏数大于1
            tmp = []  # 记录每一栏的元素个数
            for i in range(k):
                tmp.append(1)
            flag = 0
            pos = k - 1
            tmp1 = []  # 记录读取每一栏的顺序，注意不要使用字符串，有两位数以上的数据
            for i in range(k, len(dew)):
                if flag == 0:
                    pos = pos - 1
                    tmp1.append(pos)
                    tmp[pos] += 1
                    if pos == 0:
                        flag = 1

                elif flag == 1:
                    pos = pos + 1
                    tmp1.append(pos)
                    tmp[pos] += 1
                    if pos == k - 1:
                        flag = 0
            tmp2 = []  # 记录每一栏的元素
            j = 0
            for i in tmp:
                tmp2.append(dew[j:j + i])
                j = j + i
            ans = ''
            tmp3 = []  # 记录每一栏将要访问的元素
            for i in range(k):
                ans += tmp2[i][0]
                tmp3.append(1)
            for j in tmp1:
                ans += tmp2[j][tmp3[j]]
                tmp3[j] += 1
            click.echo("栅栏密码解密(w型）:" + "(" + str(k) + "):" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option("--en", help="Atbash码加密")
@click.option("--de", help="Atbash码解密")
def atbash(en, de):
    """埃特巴什码"""
    # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    # Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
    # =============================================================================
    # 1.A~Z,a~z以外的字符将原样输出
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）atbash --en "the quick brown fox jumps over the lazy dog"
    # 2.解密
    # （1）atbash --de "gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt"
    # =============================================================================
    alldata = string.ascii_lowercase
    Alldata = string.ascii_uppercase
    if en:
        ans = ""
        for ch in en:
            if ch in Alldata:
                for i in range(26):
                    if ch == Alldata[i]:
                        ans += Alldata[25 - i]
            elif ch in alldata:
                for i in range(26):
                    if ch == alldata[i]:
                        ans += alldata[25 - i]
            else:
                ans += ch
        click.echo("Atbash码加密:" + ans)

    elif de:
        ans = ""
        for ch in de:
            if ch in Alldata:
                for i in range(26):
                    if ch == Alldata[i]:
                        ans += Alldata[25 - i]
            elif ch in alldata:
                for i in range(26):
                    if ch == alldata[i]:
                        ans += alldata[25 - i]
            else:
                ans += ch
        click.echo("Atbash码解密:" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option("--en", help="凯撒加密")
@click.option("--de", help="凯撒解密")
@click.option("-n", type=int, help="偏移量")
def caesar(en, de, n):
    """凯撒密码"""
    # =============================================================================
    # 1.A~Z,a~z以外的字符将原样输出
    # 2.有参数n时,按n的大小进行偏移
    # 3.未指定n时,输出所有情况
    # 4.将n指定为负数也行
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）caesar --en "the quick brown fox jumps over the lazy dog" -n 2
    # （2）caesar --en "the quick brown fox jumps over the lazy dog" -n -1
    # 2.解密
    # （1）caesar --de "vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi" -n 2
    # （2）caesar --de "vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi"
    # =============================================================================

    alldata = string.ascii_lowercase
    Alldata = string.ascii_uppercase
    if en and n:
        ans = ""
        for ch in en:
            if ch in alldata:
                i = alldata.index(ch)
                ans += alldata[(i + n) % 26]
            elif ch in Alldata:
                i = Alldata.index(ch)
                ans += Alldata[(i + n) % 26]
            else:
                ans += ch
                # click.echo("错误:" + "请输入A~Z和a~z内的字符")
                # return
        click.echo("凯撒加密:" + ans)
    elif en and n == None:
        for m in range(1, 26):
            ans = ""
            for ch in en:
                if ch in alldata:
                    i = alldata.index(ch)
                    ans += alldata[(i + m) % 26]
                elif ch in Alldata:
                    i = Alldata.index(ch)
                    ans += Alldata[(i + m) % 26]
                else:
                    ans += ch
                    # click.echo("错误:" + "请输入A~Z和a~z内的字符")
                    # return
            click.echo("凯撒加密(" + str(m) + "):" + ans)

    elif de and n:
        ans = ""
        for ch in de:
            if ch in alldata:
                i = alldata.index(ch)
                ans += alldata[(i - n) % 26]
            elif ch in Alldata:
                i = Alldata.index(ch)
                ans += Alldata[(i - n) % 26]
            else:
                ans += ch
        click.echo("凯撒解密:" + ans)

    elif de and n == None:
        for m in range(1, 26):
            ans = ""
            for ch in de:
                if ch in alldata:
                    i = alldata.index(ch)
                    ans += alldata[(i - m) % 26]
                elif ch in Alldata:
                    i = Alldata.index(ch)
                    ans += Alldata[(i - m) % 26]
                else:
                    ans += ch
            click.echo("凯撒解密(" + str(m) + "):" + ans)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option("--en", help="ROT5/13/18/47加密")
@click.option("--de", help="ROT5/13/18/47解密")
def rot(en, de):
    """ROT5/13/18/47"""
    # =============================================================================
    # 1.无法加密的将原样输出
    # 2.加密和解密相同的字符串，结果一样
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）rot --en "the quick brown fox jumps over the lazy dog"
    # 2.解密
    # （1）rot --de "gur dhvpx oebja sbk whzcf bire gur ynml qbt"
    # （2）rot --de "the quick brown fox jumps over the lazy dog"
    # =============================================================================
    r5 = string.digits
    r13 = string.ascii_lowercase
    R13 = string.ascii_uppercase
    r47 = []
    for i in range(33, 127):
        r47.append(chr(i))
    ans5 = ""
    ans13 = ""
    ans18 = ""
    ans47 = ""

    if en:
        for ch in en:
            if ch in r5:
                i = r5.index(ch)
                ans5 += r5[(i - 5) % 10]
            else:
                ans5 += ch
        click.echo("ROT5加密 :" + ans5)

        for ch in en:
            if ch in r13:
                i = r13.index(ch)
                ans13 += r13[(i - 13) % 26]
            elif ch in R13:
                i = R13.index(ch)
                ans13 += R13[(i - 13) % 26]
            else:
                ans13 += ch
        click.echo("ROT13加密:" + ans13)

        for ch in en:
            if ch in r5:
                i = r5.index(ch)
                ans18 += r5[(i - 5) % 10]
            elif ch in r13:
                i = r13.index(ch)
                ans18 += r13[(i - 13) % 26]
            elif ch in R13:
                i = R13.index(ch)
                ans18 += R13[(i - 13) % 26]
            else:
                ans18 += ch
        click.echo("ROT18加密:" + ans18)

        for ch in en:
            if ord(ch) >= 33 and ord(ch) <= 126:
                i = r47.index(ch)
                ans47 += r47[(i - 47) % 94]
            else:
                ans47 += ch
        click.echo("ROT47加密:" + ans47)


    elif de:
        for ch in de:
            if ch in r5:
                i = r5.index(ch)
                ans5 += r5[(i + 5) % 10]
            else:
                ans5 += ch
        click.echo("ROT5解密 :" + ans5)

        for ch in de:
            if ch in r13:
                i = r13.index(ch)
                ans13 += r13[(i + 13) % 26]
            elif ch in R13:
                i = R13.index(ch)
                ans13 += R13[(i + 13) % 26]
            else:
                ans13 += ch
        click.echo("ROT13解密:" + ans13)

        for ch in de:
            if ch in r5:
                i = r5.index(ch)
                ans18 += r5[(i + 5) % 10]
            elif ch in r13:
                i = r13.index(ch)
                ans18 += r13[(i + 13) % 26]
            elif ch in R13:
                i = R13.index(ch)
                ans18 += R13[(i + 13) % 26]
            else:
                ans18 += ch
        click.echo("ROT18解密:" + ans18)

        for ch in de:
            if ord(ch) >= 33 and ord(ch) <= 126:
                i = r47.index(ch)
                ans47 += r47[(i + 47) % 94]
            else:
                ans47 += ch
        click.echo("ROT47解密:" + ans47)
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option("--en", help="波利比奥斯方阵密码加密")
@click.option("--de", help="波利比奥斯方阵密码解密")
def polybiussq(en, de):
    """波利比奥斯方阵密码"""
    '''
          1 2 3  4  5
        1 A B C  D  E 
        2 F G H I/J K
        3 L M N  O  P
        4 Q R S  T  U
        5 V W X  Y  Z

        F  => 21
        O  => 34
        X  => 53
        '''
    # =============================================================================
    # 1.解密后没保留空格
    # 2.解密后注意i,j可相互替换
    # 3.不可解密和不可加密的字符原样输出,解密后,除A~Z,其他都是不可解字符
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.编码
    # （1）polybiussq --en "the quick brown fox jumps over the lazy dog"
    # 2.解码
    # （1）polybiussq --de "442315 4145241325 1242345233 213453 2445323543 34511542 442315 31115554 143422"
    # =============================================================================
    alldata = string.ascii_uppercase
    alldata = alldata.replace("J", "")
    data = {}
    for i in range(5):
        for j in range(5):
            pos = str(i + 1) + str(j + 1)
            data[pos] = alldata[5 * i + j]
    # print("明密文对应关系：")
    # print(data)
    if en:
        ans = ""
        en = en.upper()
        en = en.replace("J", "I")
        for ch in en:
            if ch in data.values():
                ans += get_key(data, ch)
            else:
                ans += ch
        click.echo("波利比奥斯方阵密码加密:" + ans)

    elif de:
        ans = ""
        de = de.replace(" ", "")
        if len(de) % 2 != 0:
            click.echo("错误：输入数字的个数应为偶数个")
            return
        tmp = []
        for i in range(0, len(de), 2):
            tmp.append(de[i:i + 2])
        for ch in tmp:
            if ch in data.keys():
                ans += data[ch]
            else:
                ans += ch

        click.echo("波利比奥斯方阵密码解密(i,j可替换):" + ans.lower())
    else:
        click.echo("请查看帮助信息：--help")


@click.command()
@click.option("--en", help="维吉尼亚密码加密")
@click.option("--de", help="维吉尼亚密码解密")
@click.option("--key", help="密钥")
def vigenere(en, de, key):
    """维吉尼亚密码"""
    # =============================================================================
    # 1.要求明文或密文与密钥同时输入
    # 2.无法加密和无法解密的字符将原样输出
    # 3.去掉所有空格，可能出现空格与字母相对的情况
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）vigenere --en "the quick fox" --key "ant"
    # 2.解密
    # （1）vigenere --de "tuxqhbcxyok" --key "ant"
    # =============================================================================
    alldata = string.ascii_lowercase
    if key:
        key = ("".join(key.split(" "))).lower()
        for ch in key:
            if ch not in alldata:
                click.echo("错误:" + "关键字的字符为字母")
                return

    if en:
        ans = ""
        en = en.replace(" ", "")
        en = en.lower()
        for i in range(len(en)):
            n = alldata.index(key[i % len(key)])
            if en[i] in alldata:
                m = alldata.index(en[i])
                ans += alldata[(m + n) % 26]
            else:
                ans += en[i]
        click.echo("维吉尼亚密码加密:" + ans.upper())


    elif de:
        ans = ""
        de = "".join((de.lower()).split(" "))
        for i in range(len(de)):
            n = alldata.index(key[i % len(key)])
            if de[i] in alldata:
                m = alldata.index(de[i])
                ans += alldata[(m - n) % 26]
            else:
                ans += de[i]
        click.echo("维吉尼亚密码解密:" + ans)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="仿射密码加密")
@click.option("--de", help="仿射密码解密")
@click.option("-a", type=int, help="????")
@click.option("-b", type=int, help="偏移量")
@click.option("-m", default=26, type=int, help="模数(可选，默认26)")
def affine(en, de, a, b, m):
    """仿射密码"""
    # =============================================================================
    # 1.m默认为26,其他情况暂时没有考虑
    # 2.注意gcd(a,m)==1
    #   math.gcd(a,m) != 1
    # 3.使用了扩展的欧几里的算法，注意最终结果仍要取模,乘法逆元不为负
    #   ani = mulInverse(a,m)[0] % m
    # 4.无法解密和加密的字符将原样输出
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）affine --en "the quick fox" -a 5 -b 8
    # 2.解密
    # （1）affine --de "zrc kewsg hat" -a 5 -b 8
    # =============================================================================
    alldata = string.ascii_lowercase
    Alldata = string.ascii_uppercase

    if en and a and b and m == 26:
        if math.gcd(a, m) != 1:
            click.echo("错误:" + "gcd(a,m) != 1")
            return
        ans = ""
        for ch in en:
            if ch in alldata:
                x = alldata.index(ch)
                ans += alldata[(a * x + b) % m]
            elif ch in Alldata:
                x = Alldata.index(ch)
                ans += Alldata[(a * x + b) % m]
            else:
                ans += ch
        click.echo("仿射密码加密:" + ans)

    elif de and a and b and m == 26:
        if math.gcd(a, m) != 1:
            click.echo("错误:" + "gcd(a,m) != 1")
            return
        ani = mulInverse(a, m)[0] % m
        ans = ""
        for ch in de:
            if ch in alldata:
                x = alldata.index(ch)
                ans += alldata[(ani * (x - b)) % m]
            elif ch in Alldata:
                x = Alldata.index(ch)
                ans += Alldata[(ani * (x - b)) % m]
            else:
                ans += ch
        click.echo("仿射密码解密:" + ans)
    elif m != 26:
        click.echo("仿射密码:" + "暂不支持")
    else:
        click.echo("请查看帮助信息:--help")


def mulInverse(a, b):  # 扩展的欧几里的算法
    if b == 0:
        return 1, 0
    else:
        k = a // b
        r = a % b
        x1, y1 = mulInverse(b, r)
        x, y = y1, x1 - k * y1
        return x, y


@click.command()
@click.option("--en", help="格朗普雷加密")
@click.option("--de", help="格朗普雷解密")
@click.option("-n", type=int, help="每个单词的长度")
@click.option("--wordsfile", type=click.File('rb'), help="所有单词的文件")
def grandpre(en, de, n, wordsfile):
    """格朗普雷密码"""
    # =============================================================================
    # 1.n的取值范围目前为6～9
    # 2.加密结果有多种，目前只取一种，并且是随机
    # 3.注意输入的所有单词中，26个字母必须出现一次以上
    # 4.单词文件中必须为单词，否则报错
    # 5.无法加密或解密的原样输出
    # =============================================================================
    # =============================================================================
    # 测试：
    # 1.加密
    # （1）grandpre --en "the quick fox" -n 8 --wordsfile test.txt
    #
    # 2.解密
    # （2）grandpre --de "662761 4185234445 346783" -n 8 --wordsfile test.txt
    # =============================================================================
    ans = ''

    if wordsfile and n:  # 读取单词文件并转化为字符串
        if n < 6 or n > 9:
            click.echo("错误：" + "目前只支持n取6～9")
            return
        words = "".join((bytes.decode(wordsfile.read())).split(" "))  # 去掉两边空格以及换行符
        words = "".join(words.split("\n"))
        words = words.lower()
        if len(words) != n * n:
            click.echo("错误：单词总长度应为" + str(n * n))
            return
        for ch in string.ascii_lowercase:
            if ch not in words:
                click.echo("错误：" + "所有单词26个字母至少出现一次（并且全为字母）" + "=>" + ch)
                return
        worddict = {}
        for i in range(n):
            for j in range(n):
                pos = str(i + 1) + str(j + 1)
                worddict[pos] = words[n * i + j]
        # print("明密文对应关系：")
        # print(worddict)

    if en:
        en = en.lower()
        #        for ch in en:
        #            if ch not in string.ascii_lowercase:
        #                click.echo("错误：" + "明文应为字母" + "=>" + ch)
        #                return
        for ch in en:
            if ch in worddict.values():
                # print(ch,get_key(worddict,ch))
                ans += get_key(worddict, ch)  # 目前只生成一种密文,且每次输出的密文都可能不同
            else:
                ans += ch
        click.echo("格朗普雷密码加密：" + ans)

    elif de:
        de = de.replace(" ", "")
        if len(de) % 2 != 0:
            click.echo("错误：密文长度为偶数")
            return
        #        for ch in ls:
        #            if ch[0] not in string.digits or ch[1] not in string.digits:
        #                click.echo("错误：" + "密文应为数字" + "=>" + ch)
        #                return
        for i in range(0, len(de), 2):
            ch = de[i:i + 2]
            if ch in worddict.keys():
                ans += worddict[ch]
            else:
                ans += ch
        click.echo("格朗普雷密码解密：" + ans)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="希尔密码加密")
@click.option("--de", help="希尔密码解密")
@click.option("--key", help="密钥")
def hill(en, de, key):
    """希尔密码 """
    # =============================================================================
    # 1.输入的明文或密文中应全为字母
    # 2.逆矩阵的计算有问题
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）hill --en "act" --key "gybnqkurp"
    # 2.解密
    # （1）hill --de "poh" --key "gybnqkurp"
    # =============================================================================
    alldata = string.ascii_lowercase
    ans = ''
    if en and key:
        en = en.replace(" ", "")
        key = key.replace(" ", "")
        en = en.lower()
        if len(en) * len(en) != len(key):
            click.echo("错误：" + "目前只支持关键字长度为明文长度的平方")
            return

        Mls = []
        for ch in en:
            if ch in alldata:
                pos = alldata.index(ch)
                tmp = []
                tmp.append(pos)  # 形成n行1列的矩阵
                Mls.append(tmp)
            else:
                click.echo("错误：明文为字母")
                return
        Mmat = numpy.mat(Mls)  # 明文矩阵
        print("明文矩阵：")
        print(Mmat)
        key = key.lower()
        Kls = []
        tmp = []
        for ch in key:
            if ch in alldata:
                pos = alldata.index(ch)
                tmp.append(pos)
        for i in range(0, len(tmp), len(en)):
            Kls.append(tmp[i:i + len(en)])
        Kmat = numpy.mat(Kls)  # 关键字矩阵
        print("关键字矩阵：")
        print(Kmat)
        Cmat = (Kmat * Mmat) % 26
        print("密文矩阵：")
        print(Cmat)
        for ch in Cmat:
            ans += alldata[int(ch)]
        click.echo("希尔密码加密:" + ans)

    elif de and key:
        if len(de) * len(de) != len(key):
            click.echo("错误：" + "目前只支持关键字长度为密文长度的平方")
            return
        de = de.lower()
        Cls = []
        for ch in de:
            if ch in alldata:
                pos = alldata.index(ch)
                tmp = []
                tmp.append(pos)
                Cls.append(tmp)
            else:
                click.echo("错误：密文为字母")
        Cmat = numpy.mat(Cls)  # 密文矩阵
        print("密文矩阵：")
        print(Cmat)
        key = key.lower()
        Kls = []
        tmp = []
        for ch in key:
            if ch in alldata:
                pos = alldata.index(ch)
                tmp.append(pos)
        for i in range(0, len(tmp), len(de)):
            Kls.append(tmp[i:i + len(de)])
        Kmat = numpy.mat(Kls)
        print("关键字矩阵：")
        print(Kmat)
        Kmat = Kmat.I % 26
        print("关键字逆矩阵：")
        print(Kmat)
        Mmat = (Kmat * Cmat) % 26
        print("明文矩阵：")
        print(Mmat)
        for ch in Mmat:
            ans += alldata[int(ch)]
        click.echo("希尔密码解密:" + ans + "=>逆矩阵的计算有问题")
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="培根密码加密")
@click.option("--de", help="培根密码解密")
def baconian(en, de):
    """培根密码"""
    # =============================================================================
    # 1.无法加解密的将原样输出
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）baconian --en "the quick fox"
    # 2.解密
    # （1）baconian --de "baabb aabbb aabaa  baaaa babaa abaaa aaaba ababa  aabab abbba babbb "
    # =============================================================================
    alldata = string.ascii_lowercase
    ABdata1 = []
    ABdata2 = []
    for i in range(26):
        tmp = ''
        i2 = str(bin(i))[2:]
        i2 = '0' * (5 - len(i2)) + i2
        for ch in i2:
            if ch == '0':
                tmp += 'a'
            elif ch == '1':
                tmp += 'b'

        ABdata1.append(tmp)  # 26个字母一一对应
        if i <= 23:
            ABdata2.append(tmp)  # i/j与v/u
    if en:
        ans = ''
        en = en.lower()
        for ch in en:
            if ch in alldata:
                pos = alldata.index(ch)
                ans += ABdata1[pos] + ' '
            else:
                ans += ch
        click.echo("培根密码加密1：" + ans)
        ans = ''
        for ch in en:
            if ch in alldata:
                pos = alldata.index(ch)
                if ch == 'i' or ch == 'j':
                    pos = 8
                elif ch == 'u' or ch == 'v':
                    pos = 19
                elif ch > 'i' and ch < 'u':
                    pos = pos - 1
                elif ch > 'u':
                    pos = pos - 2

                ans += ABdata2[pos] + ' '
            else:
                ans += ch
        click.echo("培根密码加密2：" + ans)
    elif de:
        ans1 = ''
        ans2 = ''
        ls = []
        de = de.lower()
        de = de.replace(" ", "")
        for i in range(0, len(de), 5):
            ls.append(de[i:i + 5])
        for ch in ls:
            if ch in ABdata1:
                pos = ABdata1.index(ch)
                ans1 += alldata[pos] + ' '
            else:
                ans1 += ch + ' '
            if ch in ABdata2:
                pos = ABdata2.index(ch)
                if pos > 8 and pos <= 19:
                    pos = pos + 1
                elif pos > 19:
                    pos = pos + 2
                ans2 += alldata[pos] + ' '
            else:
                ans2 += ch + ' '

        click.echo("培根密码解密1：" + ans1)
        click.echo("培根密码解密2：" + ans2 + "   注意：i与j，u与v可相互替换")
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="普莱菲尔密码加密")
@click.option("--de", help="普莱菲尔密码解密")
@click.option("--key", help="密钥")
def playfair(en, de, key):
    """普莱菲尔密码"""
    # =============================================================================
    # 1.字母j当作i
    # 2.明文的补充字母为x
    # 3.若明文的长度为奇数，且末尾字母为x，则只能换为x
    # 4.输入的明文或密文只能是字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）playfair --en "the quick brown fox jumps over the lazy dog" --key "culture"
    # （2）playfair --en "测试" --key "culture"
    # 2.解密
    # （1）playfair --de "kundhlgtlfwueswplhsinpcgcragbuvzqavi" --key "culture"
    # （2）playfair --de "测试" --key "culture"
    # =============================================================================
    if key:
        key = "".join((key.lower()).split(" "))
        ls = []
        for ch in key:
            if ch not in ls and ch != 'z' and ch != 'j':  # i与j可替换，z在英文里使用的频率最低，应该去除
                ls.append(ch)
        for ch in string.ascii_lowercase:
            if ch not in ls and ch != 'j':
                ls.append(ch)
        tmp1 = {}
        for i in range(5):
            for j in range(5):
                tmp1[ls[5 * i + j]] = (j, i)  # 纵列
        tmp2 = {}
        for i in range(5):
            for j in range(5):
                tmp2[ls[5 * i + j]] = (i, j)  # 横排

    if en:
        ans1 = ''
        ans2 = ''
        ans3 = ''
        ans4 = ''
        en = en.replace('j', 'i')
        en = "".join((en.lower()).split(" "))
        if len(en) % 2 != 0:
            en += 'x'
        tmp = []
        for i in range(0, len(en), 2):
            tmp.append(en[i:i + 2])
        ls = []
        for ch in tmp:
            if ch[0] not in string.ascii_lowercase or ch[1] not in string.ascii_lowercase:
                click.echo("错误：输入的明文为字母")
                return
            if ch[0] == ch[1]:
                ls.append(ch[0] + 'x')
                ls.append(ch[1] + 'x')
            else:
                ls.append(ch)
        for ch in ls:  # 纵列
            x1 = tmp1[ch[0]][0]
            y1 = tmp1[ch[0]][1]
            x2 = tmp1[ch[1]][0]
            y2 = tmp1[ch[1]][1]
            # print(x1,y1,x2,y2)
            if x1 == x2:  # 同行取右边
                strl = "".join(get_key(tmp1, ((x1, (y1 + 1) % 5))))
                strr = "".join(get_key(tmp1, ((x2, (y2 + 1) % 5))))
                ans1 += strl + strr
                ans2 = ans1
            elif y1 == y2:  # 同列取下边
                strl = "".join(get_key(tmp1, (((x1 + 1) % 5), y1)))
                strr = "".join(get_key(tmp1, (((x2 + 1) % 5), y2)))
                ans1 += strl + strr
                ans2 = ans1
            else:  # 对角
                strl = "".join(get_key(tmp1, ((x1, y2))))  # 同行优先情况
                strr = "".join(get_key(tmp1, ((x2, y1))))
                ans1 += strl + strr
                strl = "".join(get_key(tmp1, ((x2, y1))))  # 同列优先情况
                strr = "".join(get_key(tmp1, ((x1, y2))))
                ans2 += strl + strr
        for ch in ls:  # 横行
            x1 = tmp2[ch[0]][0]
            y1 = tmp2[ch[0]][1]
            x2 = tmp2[ch[1]][0]
            y2 = tmp2[ch[1]][1]
            # print(x1,y1,x2,y2)
            if x1 == x2:  # 同行取右边
                strl = "".join(get_key(tmp2, ((x1, (y1 + 1) % 5))))
                strr = "".join(get_key(tmp2, ((x2, (y2 + 1) % 5))))
                ans3 += strl + strr
                ans4 = ans3
            elif y1 == y2:  # 同列取下边
                strl = "".join(get_key(tmp2, (((x1 + 1) % 5), y1)))
                strr = "".join(get_key(tmp2, (((x2 + 1) % 5), y2)))
                ans3 += strl + strr
                ans4 = ans3
            else:  # 对角
                strl = "".join(get_key(tmp2, ((x1, y2))))  # 同行优先情况
                strr = "".join(get_key(tmp2, ((x2, y1))))
                ans3 += strl + strr
                strl = "".join(get_key(tmp2, ((x2, y1))))  # 同列优先情况
                strr = "".join(get_key(tmp2, ((x1, y2))))
                ans4 += strl + strr

        click.echo("普莱菲尔密码加密（纵列同行）：" + ans1)
        click.echo("普莱菲尔密码加密（纵列同列）：" + ans2)
        click.echo("普莱菲尔密码加密（横行同行）：" + ans3)
        click.echo("普莱菲尔密码加密（横行同列）：" + ans4)

    elif de:
        if len(de) % 2 != 0:
            click.echo("错误：密文应为偶数位")
            return
        ans1 = ''
        ans2 = ''
        ans3 = ''
        ans4 = ''
        de = de.replace('j', 'i')  ####
        de = "".join((de.lower()).split(" "))
        tmp = []
        for i in range(0, len(de), 2):
            if de[i] not in string.ascii_lowercase or de[i + 1] not in string.ascii_lowercase:
                click.echo("错误：输入的明文为字母")
                return
            tmp.append(de[i:i + 2])

        for ch in tmp:  # 纵列
            x1 = tmp1[ch[0]][0]
            y1 = tmp1[ch[0]][1]
            x2 = tmp1[ch[1]][0]
            y2 = tmp1[ch[1]][1]
            # print(x1,y1,x2,y2)
            if x1 == x2:  # 同行取右边
                strl = "".join(get_key(tmp1, ((x1, (y1 - 1) % 5))))
                strr = "".join(get_key(tmp1, ((x2, (y2 - 1) % 5))))
                ans1 += strl + strr
                ans2 = ans1
            elif y1 == y2:  # 同列取下边
                strl = "".join(get_key(tmp1, (((x1 - 1) % 5), y1)))
                strr = "".join(get_key(tmp1, (((x2 - 1) % 5), y2)))
                ans1 += strl + strr
                ans2 = ans1
            else:  # 对角
                strl = "".join(get_key(tmp1, ((x1, y2))))  # 同行优先情况
                strr = "".join(get_key(tmp1, ((x2, y1))))
                ans1 += strl + strr
                strl = "".join(get_key(tmp1, ((x2, y1))))  # 同列优先情况
                strr = "".join(get_key(tmp1, ((x1, y2))))
                ans2 += strl + strr
        for ch in tmp:  # 横行
            x1 = tmp2[ch[0]][0]
            y1 = tmp2[ch[0]][1]
            x2 = tmp2[ch[1]][0]
            y2 = tmp2[ch[1]][1]
            # print(x1,y1,x2,y2)
            if x1 == x2:  # 同行取右边
                strl = "".join(get_key(tmp2, ((x1, (y1 - 1) % 5))))
                strr = "".join(get_key(tmp2, ((x2, (y2 - 1) % 5))))
                ans3 += strl + strr
                ans4 = ans3
            elif y1 == y2:  # 同列取下边
                strl = "".join(get_key(tmp2, (((x1 - 1) % 5), y1)))
                strr = "".join(get_key(tmp2, (((x2 - 1) % 5), y2)))
                ans3 += strl + strr
                ans4 = ans3
            else:  # 对角
                strl = "".join(get_key(tmp2, ((x1, y2))))  # 同行优先情况
                strr = "".join(get_key(tmp2, ((x2, y1))))
                ans3 += strl + strr
                strl = "".join(get_key(tmp2, ((x2, y1))))  # 同列优先情况
                strr = "".join(get_key(tmp2, ((x1, y2))))
                ans4 += strl + strr

        click.echo("普莱菲尔密码解密（纵列同行）：" + ans1)
        click.echo("普莱菲尔密码解密（纵列同列）：" + ans2)
        click.echo("普莱菲尔密码解密（横行同行）：" + ans3)
        click.echo("普莱菲尔密码解密（横行同列）：" + ans4)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="自动密钥密码加密")
@click.option("--de", help="自动密钥密码解密")
@click.option("--keyword", help="关键词")
def autokey(en, de, keyword):
    """自动密钥密码"""
    # =============================================================================
    # 1.输入的明文、密文及密钥必须是字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）autokey --en "the quick brown fox jumps over the lazy dog" --keyword "culture"
    # 2.解密
    # （1）autokey --de "vbpjozgdiveqvhyyaiicxcsnlfwwzvdpwvk" --keyword "culture"
    # =============================================================================
    alldata = string.ascii_lowercase
    if en and keyword:
        key = keyword + en
        key = ("".join(key.split(" "))).lower()
        for ch in key:
            if ch not in alldata:
                click.echo("错误:" + "明文和关键字的字符为A~Z,a~z")
                return
        en = "".join((en.lower()).split(" "))
        ans = ""
        for i in range(len(en)):
            n = alldata.index(key[i % len(key)])
            m = alldata.index(en[i])
            ans += alldata[(m + n) % 26]
        click.echo("自动密钥密码加密：" + ans)

    elif de and keyword:
        de = "".join((de.lower()).split(" "))
        keyword = "".join((keyword.lower()).split(" "))
        for ch in de + keyword:
            if ch not in alldata:
                click.echo("错误:" + "密文和关键字的字符为A~Z,a~z")
                return
        ans = ""
        key = keyword
        for i in range(0, len(de), len(key)):
            if i + len(key) > len(de):
                ch = de[i:]
            else:
                ch = de[i:i + len(key)]
            tmp = ''
            for j in range(len(ch)):  # 注意：可能最后密文段的长度小于关键字
                n = alldata.index(key[j])
                m = alldata.index(ch[j])
                ans += alldata[(m - n) % 26]
                tmp += alldata[(m - n) % 26]
            key = tmp
        click.echo("自动密钥密码解密：" + ans)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="博福特密码加密")
@click.option("--de", help="博福特密码解密")
@click.option("--key", help="密钥")
def beaufort(en, de, key):
    """博福特密码"""
    # =============================================================================
    # 1.关键字的字符必须是字母
    # 2.无法加密或解密的将原样输出
    # 3.加解密的过程相同
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）beaufort --en "the quick brown fox jumps over the lazy dog" --key "culture"
    # 2.解密
    # （1）beaufort --de "jnhdajcstufyezoxczicmozhcbkarumvrdy" --key "culture"
    # =============================================================================
    alldata = string.ascii_lowercase
    if key:
        key = ("".join(key.split(" "))).lower()
        for ch in key:
            if ch not in alldata:
                click.echo("错误:" + "关键字的字符为A~Z,a~z")
                return

    if en:
        ans = ""
        en = "".join((en.lower()).split(" "))
        for i in range(len(en)):
            n = alldata.index(key[i % len(key)])
            if en[i] in alldata:
                m = alldata.index(en[i])
                ans += alldata[(- m + n) % 26]
            else:
                ans += en[i]
        click.echo("博福特密码加密:" + ans)


    elif de:
        ans = ""
        de = "".join((de.lower()).split(" "))
        for i in range(len(de)):
            n = alldata.index(key[i % len(key)])
            if de[i] in alldata:
                m = alldata.index(de[i])
                ans += alldata[(- m + n) % 26]
            else:
                ans += de[i]
        click.echo("博福特密码解密:" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="Porta密码加密")
@click.option("--de", help="Porta密码解密")
@click.option("--key", help="密钥")
def porta(en, de, key):
    """Porta密码"""
    # =============================================================================
    # 1.密钥必须是字母
    # 2.无法加密或解密的将原样输出
    # 3.加密过程和解密过程相同
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）porta --en "the quick brown fox jumps over the lazy dog" --key "culture"
    # 2.解密
    # （2）porta --de "frwhkqryymfmfuaaolwhdalwijptzxhcngv" --key "culture"
    # =============================================================================
    alldata = string.ascii_lowercase
    if key:
        key = ("".join(key.split(" "))).lower()
        for ch in key:
            if ch not in alldata:
                click.echo("错误:" + "关键字的字符为A~Z,a~z")
                return

    if en and key:
        ans = ""
        en = "".join((en.lower()).split(" "))
        for i in range(len(en)):
            n = alldata.index(key[i % len(key)])
            if en[i] in alldata:
                m = alldata.index(en[i])
                if m < 13:  # a~m
                    m = (m + 13 + n // 2) % 13 + 13
                else:  # n~z
                    m = (m + 13 - n // 2) % 13
                ans += alldata[m]
            else:
                ans += en[i]
        click.echo("Porta密码加密:" + ans)


    elif de and key:
        ans = ""
        de = "".join((de.lower()).split(" "))
        for i in range(len(de)):
            n = alldata.index(key[i % len(key)])
            if de[i] in alldata:
                m = alldata.index(de[i])
                if m < 13:  # a~m
                    m = (m + 13 + n // 2) % 13 + 13
                else:  # n~z
                    m = (m + 13 - n // 2) % 13
                ans += alldata[m]
            else:
                ans += de[i]
        click.echo("Porta密码解密:" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="ADFGX密码加密")
@click.option("--de", help="ADFGX密码解密")
@click.option("--matrix", help="矩阵")
@click.option("--key", help="密钥")
def ADFGX(en, de, matrix, key):
    """ADFGX密码"""
    # =============================================================================
    # 1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
    # 2.输入的明文或密文,密钥必须是字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）adfgx --en "the quick brown fox" --matrix "phqgmeaynofdxkrcvszwbutil" --key "howareu"
    # 2.解密
    # （1）adfgx --de "DXADFAGXFXFFXDFXGGXDGFGAADAADXXF" --matrix "phqgmeaynofdxkrcvszwbutil" --key "howareu"
    # =============================================================================
    alldata = string.ascii_lowercase
    if matrix and key:
        if len(matrix) != 25:
            click.echo("错误：矩阵长度为25")
            return
        matrix = "".join((matrix.lower()).split(" "))
        matrix = matrix.replace('j', 'i')
        for ch in alldata:
            if ch not in matrix and ch != 'j':
                click.echo("错误：全部为字母，且25个字母不同，i与j视作同一字母")
                return

        Astr = "ADFGX"
        data = {}
        for i in range(5):
            for j in range(5):
                tmp = Astr[i] + Astr[j]
                data[tmp] = matrix[5 * i + j]

        # print(data)
        key = "".join((key.lower()).split(" "))
        tmp = ''
        for ch in key:
            if ch not in tmp:  # key中的字符不重复
                tmp += ch
            if ch not in alldata:
                click.echo("错误：密钥全部为字母")
                return
        key = tmp
        keytmp = ''
        for ch in alldata:
            # if ch in keydict.keys:
            if ch in key:
                keytmp += ch

    if en:
        ans = ''
        tmp = ''
        en = "".join((en.lower()).split(" "))
        en = en.replace('j', 'i')
        for ch in en:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
            tmp += get_key(data, ch)
        # print(tmp)
        keydict = {}
        for ch in key:
            keydict[ch] = ""
        for i in range(len(tmp)):
            keydict[key[i % len(key)]] += tmp[i]
        # print(keydict)

        for ch in keytmp:
            ans += keydict[ch]

        click.echo("ADFGX密码加密：" + ans)

    elif de:
        tmp = ''
        ans = ''
        de = "".join((de.upper()).split(" "))
        for ch in de:
            if ch not in Astr:
                click.echo("错误：密文只包含ADFGX")
                return
        col_len = len(de) // len(key)  # 每列的最小长度
        if len(de) - len(key) > 0:  # 注意可能存在密钥比密文长的情况
            col_len1 = col_len + 1
        else:
            col_len1 = col_len

        last = col_len1 * len(key) - len(de)  # 较短的最后几列
        key_len_dict = {}
        for i in range(len(key) - last):  # 将长度与密钥的每个字母相对应
            key_len_dict[key[i]] = col_len1
        if last:
            for i in range(len(key) - last, len(key)):
                key_len_dict[key[i]] = col_len
        keydict = {}
        l = 0
        for ch in keytmp:  # 截取每个字母对应的密文段
            m = key_len_dict[ch]
            keydict[ch] = de[l:l + m]
            l = l + m
        # print(keydict)
        for i in range(col_len1):
            for ch in key:
                if len(keydict[ch]) > i:
                    tmp += keydict[ch][i]
        # print(tmp)
        ls = []
        for i in range(0, len(tmp), 2):
            ls.append(tmp[i:i + 2])
        # print(ls)
        for ch in ls:
            ans += data[ch]
        click.echo("ADFGX密码解密：" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="ADFGVX密码加密")
@click.option("--de", help="ADFGVX密码解密")
@click.option("--matrix", help="矩阵")
@click.option("--key", help="密钥")
def ADFGVX(en, de, matrix, key):
    """ADFGVX密码"""
    # =============================================================================
    # 1.输入矩阵的长度为36，由26个字母和0～9组成
    # 2.输入必须为字母
    # 3.输入的明文或密文必须为字母和数字
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）adfgvx --en "the quick brown fox" --matrix "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8" --key "howareu"
    # 2.解密
    # （1）adfgvx --de "DXXFAFGFFXGGGFGXDVGDVGFAVFVAFVGG" --matrix "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8" --key "howareu"
    # =============================================================================
    alldata = string.ascii_lowercase + string.digits
    if matrix and key:
        if len(matrix) != 36:
            click.echo("错误：矩阵长度为36")
            return
        matrix = "".join((matrix.lower()).split(" "))
        for ch in alldata:
            if ch not in matrix:
                click.echo("错误：全部为字母和数字")
                return

        Astr = "ADFGVX"
        data = {}
        for i in range(6):
            for j in range(6):
                tmp = Astr[i] + Astr[j]
                data[tmp] = matrix[6 * i + j]

        # print(data)
        key = "".join((key.lower()).split(" "))
        tmp = ''
        for ch in key:
            if ch not in tmp:
                tmp += ch
            if ch not in string.ascii_lowercase:
                click.echo("错误：密钥全部为字母")
                return
        key = tmp
        keytmp = ''
        for ch in string.ascii_lowercase:
            # if ch in keydict.keys:
            if ch in key:
                keytmp += ch

    if en:
        ans = ''
        tmp = ''
        en = "".join((en.lower()).split(" "))
        for ch in en:
            if ch not in alldata:
                click.echo("错误：全部为字母和数字")
                return
            tmp += get_key(data, ch)
        # print(tmp)
        keydict = {}
        for ch in key:
            keydict[ch] = ""
        for i in range(len(tmp)):
            keydict[key[i % len(key)]] += tmp[i]
        # print(keydict)

        for ch in keytmp:
            ans += keydict[ch]

        click.echo("ADFGVX密码加密：" + ans)

    elif de:
        tmp = ''
        ans = ''
        de = "".join((de.upper()).split(" "))
        for ch in de:
            if ch not in Astr:
                click.echo("错误：密文只包含ADFGVX")
                return
        col_len = len(de) // len(key)  # 每列的最小长度
        if len(de) - len(key) > 0:  # 注意可能存在密钥比密文长的情况
            col_len1 = col_len + 1
        else:
            col_len1 = col_len

        last = col_len1 * len(key) - len(de)  # 较短的最后几列
        key_len_dict = {}
        for i in range(len(key) - last):  # 将长度与密钥的每个字母相对应
            key_len_dict[key[i]] = col_len1
        if last:
            for i in range(len(key) - last, len(key)):
                key_len_dict[key[i]] = col_len
        keydict = {}
        l = 0
        for ch in keytmp:  # 截取每个字母对应的密文段
            m = key_len_dict[ch]
            keydict[ch] = de[l:l + m]
            l = l + m
        # print(keydict)
        for i in range(col_len1):
            for ch in key:
                if len(keydict[ch]) > i:
                    tmp += keydict[ch][i]
        # print(tmp)
        ls = []
        for i in range(0, len(tmp), 2):
            ls.append(tmp[i:i + 2])
        # print(ls)
        for ch in ls:
            ans += data[ch]
        click.echo("ADFGVX密码解密：" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="双密码加密")
@click.option("--de", help="双密码解密")
@click.option("--matrix", help="矩阵")
def bifid(en, de, matrix):
    """双密码"""
    # =============================================================================
    # 1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
    # 2.输入的明文或密文必须是字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）bifid --en "the quick brown fox" --matrix "phqgmeaylnofdxkrcvszwbuti"
    # 2.解密
    # （1）bifid --de "wetedtkznekyomex" --matrix "phqgmeaylnofdxkrcvszwbuti"
    # =============================================================================
    if matrix:
        alldata = string.ascii_lowercase
        if len(matrix) != 25:
            click.echo("错误：矩阵长度为25")
            return
        matrix = "".join((matrix.lower()).split(" "))
        matrix = matrix.replace('j', 'i')
        for ch in alldata:
            if ch not in matrix and ch != 'j':
                click.echo("错误：全部为字母，且25个字母不同，i与j视作同一字母")
                return

        Bstr = "12345"
        data = {}
        for i in range(5):
            for j in range(5):
                tmp = Bstr[i] + Bstr[j]
                data[tmp] = matrix[5 * i + j]
        # print(data)
    if en:
        en = "".join((en.lower()).split(" "))
        for ch in en:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
        row = ''
        col = ''
        for ch in en:
            row += get_key(data, ch)[0]
            col += get_key(data, ch)[1]
        # print(row)
        # print(col)
        tmp = ''
        for i in range(0, len(row), 5):
            if i + 5 < len(row):
                tmp += row[i:i + 5] + col[i:i + 5]
            else:
                tmp += row[i:] + col[i:]
        # print(tmp)
        ans = ''
        for i in range(0, len(tmp), 2):
            ans += data[tmp[i:i + 2]]
        click.echo("双密码加密：" + ans)

    elif de:
        de = "".join((de.lower()).split(" "))
        for ch in de:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
        tmp = ''
        for ch in de:
            tmp += get_key(data, ch)
        # print(tmp)
        row = ''
        col = ''
        for i in range(0, len(tmp), 10):
            if i + 10 < len(tmp):
                row += tmp[i:i + 5]
                col += tmp[i + 5:i + 10]
            else:
                row += tmp[i:i + (len(tmp) - i) // 2]
                col += tmp[i + (len(tmp) - i) // 2:]
        # print(row)
        # print(col)
        ans = ''
        for i in range(len(row)):
            ch = row[i] + col[i]
            ans += data[ch]
        click.echo("双密码解密：" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="四方密码加密")
@click.option("--de", help="四方密码解密")
@click.option("--ru", help="右上矩阵")
@click.option("--ld", help="左下矩阵")
def foursquare(en, de, ru, ld):
    """四方密码"""
    # =============================================================================
    # 1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
    # 2.输入的明文或密文必须是字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）foursquare --en "the quick brown fox" --ru "zgptfoihmuwdrcnykeqaxvsbl" --ld "mfnbdcrhsaxyogvituewlqzkp"
    # 2.解密
    # （1）foursquare --de "eszwqafhgtdkwhrk" --ru "zgptfoihmuwdrcnykeqaxvsbl" --ld "mfnbdcrhsaxyogvituewlqzkp"
    # =============================================================================
    if ru and ld:
        alldata = string.ascii_lowercase
        if len(ru) != 25 or len(ld) != 25:
            click.echo("错误：矩阵长度为25")
            return
        ru = "".join((ru.lower()).split(" "))
        ld = "".join((ld.lower()).split(" "))
        ru = ru.replace('j', 'i')
        ld = ld.replace('j', 'i')
        m = alldata.replace('j', '')
        for ch in m:
            if ch not in ru or ch not in ld:
                click.echo("错误：全部为字母，且25个字母不同，i与j视作同一字母")
                return

        Nstr = "12345"
        rudict = {}
        lddict = {}
        ludict = {}
        rddict = {}
        for i in range(5):
            for j in range(5):
                tmp = Nstr[i] + Nstr[j]
                rudict[tmp] = ru[5 * i + j]
                lddict[tmp] = ld[5 * i + j]
                ludict[tmp] = m[5 * i + j]
                rddict[tmp] = m[5 * i + j]
    #        print(rudict)
    #        print(lddict)
    #        print(ludict)
    #        print(rddict)
    if en:
        en = "".join((en.lower()).split(" "))
        en = en.replace('j', 'i')
        for ch in en:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
        if len(en) % 2 != 0:
            en = en + 'x'
        ls = []
        for i in range(0, len(en), 2):
            ls.append(en[i:i + 2])
        # print(ls)
        ans = ''
        for ch in ls:
            lun = get_key(ludict, ch[0])  # 获得左上明文矩阵中明文的坐标
            rdn = get_key(rddict, ch[1])  # 获得右下明文矩阵中明文的坐标
            ans += rudict[lun[0] + rdn[1]] + lddict[rdn[0] + lun[1]]
        #            print(lun)
        #            print(rdn)
        click.echo("四方密码加密：" + ans)

    elif de:
        de = "".join((de.lower()).split(" "))
        de = de.replace('j', 'i')
        for ch in de:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
        if len(de) % 2 != 0:
            click.echo("错误：密文长度为偶数倍")
            return
        ls = []
        for i in range(0, len(de), 2):
            ls.append(de[i:i + 2])
        ans = ''
        for ch in ls:
            run = get_key(rudict, ch[0])  # 获得右上矩阵中密文的坐标
            ldn = get_key(lddict, ch[1])  # 获得左下矩阵中密文的坐标
            ans += ludict[run[0] + ldn[1]] + rddict[ldn[0] + run[1]]
        click.echo("四方密码解密（i，j可互换，末尾x可去掉）：" + ans)
    else:
        click.echo("请查看帮助信息")


@click.command()
@click.option("--en", help="棋盘密码加密")
@click.option("--de", help="棋盘密码解密")
@click.option("--matrix", help="矩阵")
@click.option("--keyl", help="密钥1")
@click.option("--keyu", help="密钥2")
def checkerboard(en, de, matrix, keyl, keyu):
    """棋盘密码"""
    # =============================================================================
    # 1.输入的矩阵要求25个字母，且不相同，i与j视作同一字母
    # 2.输入的明文或密文必须是字母
    # 3.密钥必须是5个不同的字母
    # =============================================================================
    # =============================================================================
    # 测试
    # 1.加密
    # （1）checkerboard --en "the quick brown fox" --matrix "knighpqrstoyzuamxwvblfedc" --keyl "brown" --keyu "quick"
    # 2.解密
    # （1）checkerboard --de "rkbkniruocbinkbqwkrioqwibunuoqwu" --matrix "knighpqrstoyzuamxwvblfedc" --keyl "brown" --keyu "quick"
    # =============================================================================
    if matrix and keyl and keyu:
        alldata = string.ascii_lowercase
        if len(matrix) != 25:
            click.echo("错误：矩阵长度为25")
            return
        matrix = "".join((matrix.lower()).split(" "))
        matrix = matrix.replace('j', 'i')
        for ch in alldata:
            if ch not in matrix and ch != 'j':
                click.echo("错误：全部为字母")
                return

        keyl = "".join((keyl.lower()).split(" "))
        keyu = "".join((keyu.lower()).split(" "))
        tmp = ''
        for ch in keyl:
            if ch not in tmp:
                tmp += ch
            if ch not in alldata:
                click.echo("错误：密钥全部为字母")
                return
        keyl = tmp
        tmp = ''
        for ch in keyu:
            if ch not in tmp:
                tmp += ch
            if ch not in alldata:
                click.echo("错误：密钥全部为字母")
                return
        if len(keyl) != 5 or len(keyu) != 5:
            click.echo("错误：密钥长度为5")
            return
        data = {}
        for i in range(len(keyl)):
            for j in range(len(keyu)):
                tmp = keyl[i] + keyu[j]
                data[tmp] = matrix[5 * i + j]

        # print(data)
    if en:
        en = "".join((en.lower()).split(" "))
        en = en.replace('j', 'i')
        ans = ''
        for ch in en:
            if ch not in alldata:
                click.echo("错误：全部为字母")
                return
            ans += get_key(data, ch)
        click.echo("棋盘密码加密：" + ans)
    elif de:
        de = "".join((de.lower()).split(" "))
        de = de.replace('j', 'i')
        if len(de) % 2 != 0:
            click.echo("错误：密文长度为偶数倍")
            return
        for ch in de:
            if ch not in keyl and ch not in keyu:
                click.echo("错误：密文中的字母为两个密钥中的字母")
                return
        ls = []
        for i in range(0, len(de), 2):
            ls.append(de[i:i + 2])
        ans = ''
        for ch in ls:
            ans += data[ch]
        click.echo("棋盘密码解密：" + ans)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--md5", help="md5加密")
@click.option("--sha", help="sha家族加密")
def hashed(md5, sha):
    """md5,sha家族"""

    # =============================================================================
    # 只支持加密的情况
    # =============================================================================
    # =============================================================================
    # hashed --md5 "the quick fox"
    # hashed --sha "the quick fox"
    # =============================================================================
    if md5:
        obj = hashlib.md5()  # 创建md5对象
        obj.update(md5.encode('utf-8'))  # update需要一个bytes格式参数
        ans = obj.hexdigest()  # 返回16进制字符串
        click.echo("md5加密:" + ans)
    elif sha:
        obj1 = hashlib.sha1()  # 创建sha1对象
        obj1.update(sha.encode('utf-8'))  # update需要一个bytes格式参数
        obj2 = hashlib.sha224()
        obj2.update(sha.encode('utf-8'))
        obj3 = hashlib.sha256()
        obj3.update(sha.encode('utf-8'))
        obj4 = hashlib.sha384()
        obj4.update(sha.encode('utf-8'))
        obj5 = hashlib.sha512()
        obj5.update(sha.encode('utf-8'))

        click.echo("sha1加密:" + obj1.hexdigest())
        click.echo("sha224加密:" + obj2.hexdigest())
        click.echo("sha256加密:" + obj3.hexdigest())
        click.echo("sha384加密:" + obj4.hexdigest())
        click.echo("sha512加密:" + obj5.hexdigest())
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--mac", help="生成MAC")
@click.option("--htype", help="hash函数的一种")
@click.option("--key", help="密钥")
def maced(key, mac, htype):
    """消息认证码"""

    # =============================================================================
    # 生成消息认证码
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "md5"
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha1"
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha224"
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha256"
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha384"
    # maced --mac "the quick fox" --key "imsS49kraapnUH0Z" --htype "sha512"
    # =============================================================================
    if mac and key and htype:
        mac = mac.encode('utf-8')
        key = key.encode('utf-8')
        ls = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
        if htype not in ls:
            click.echo("请输入其中一种：" + "['md5','sha1','sha224','sha256','sha384','sha512']")
            return
        if htype == 'md5':
            htype = hashlib.md5
        elif htype == 'sha1':
            htype = hashlib.sha1
        elif htype == 'sha224':
            htype = hashlib.sha224
        elif htype == 'sha256':
            htype = hashlib.sha256
        elif htype == 'sha384':
            htype = hashlib.sha384
        else:
            htype = hashlib.sha512
        mac_op = hmac.new(key, digestmod=htype)
        mac_op.update(mac)
        click.echo("消息认证码:" + mac_op.hexdigest())
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", help="当铺密码加密")
@click.option("--de", help="当铺密码解密")
def dangpu(en, de):
    """当铺密码"""
    s1 = '田由中人工大王夫井羊'
    if en:
        ans = ""
        for ch in en:
            if ch == " ":
                ans += ch
            elif ch in string.digits:  # int('a')
                ans += s1[int(ch)]
            else:
                ans += ch
        click.echo("当铺密码加密：" + ans)
        click.echo("(可替换：壮-羊，士-土-大，田-口)")
    elif de:
        ans = ""
        de = de.replace("壮", "羊")
        de = de.replace("土", "大")
        de = de.replace("士", "大")
        de = de.replace("口", "田")
        for ch in de:
            if ch in s1:
                ans += str(s1.index(ch))
            else:
                ans += ch
        click.echo("当铺密码解密：" + ans)
    else:
        click.echo("请查看帮助信息:--help")


@click.command()
@click.option("--en", type=int, help="RSA加密")
@click.option("--de", type=int, help="RSA解密")
@click.option("-e", type=int, help="公钥")
@click.option("-d", type=int, help="私钥")
@click.option("-n", type=int, help="模数")
@click.option("-p", type=int, help="分解p")
@click.option("-q", type=int, help="分解q")
def rsa(en, de, e, d, n, p, q):
    """RSA"""
    if en and e and n:
        ans = pow(en, e, n)
        click.echo("RSA加密：" + ans)
    elif de and d and n:
        ans = pow(de, d, n)
        click.echo("RSA解密：" + ans)
    elif de and e and n and p and q:
        d1 = int(gmpy2.invert(e, (p - 1) * (q - 1)))
        ans = pow(de, d1, n)
        click.echo("RSA解密：" + ans)
    else:
        click.echo("请查看帮助信息")


crypto.add_command(asciiED)
crypto.add_command(base)
crypto.add_command(qp)
crypto.add_command(uu)
crypto.add_command(url)
crypto.add_command(morse)
crypto.add_command(xx)
crypto.add_command(shellcode)
crypto.add_command(unicode)
crypto.add_command(escape)
crypto.add_command(htmlED)
crypto.add_command(tapcode)
crypto.add_command(railfence)
crypto.add_command(atbash)
crypto.add_command(caesar)
crypto.add_command(rot)
crypto.add_command(polybiussq)
crypto.add_command(vigenere)
crypto.add_command(affine)
crypto.add_command(grandpre)
crypto.add_command(hill)
crypto.add_command(baconian)
crypto.add_command(playfair)
crypto.add_command(autokey)
crypto.add_command(beaufort)
crypto.add_command(porta)
crypto.add_command(ADFGX)
crypto.add_command(ADFGVX)
crypto.add_command(bifid)
crypto.add_command(foursquare)
crypto.add_command(checkerboard)
crypto.add_command(hashed)
crypto.add_command(maced)
crypto.add_command(dangpu)
crypto.add_command(rsa)
if __name__ == "__main__":
    crypto()
