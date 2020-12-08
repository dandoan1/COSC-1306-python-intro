# -*- coding: utf-8 -*-
"""
Created on Oct 27 16:10:38 2020
assignment8
cosc1306
@author: dan doan 1986920
"""
import string

def decrypt_letter(letter, code_letter):
    alphabet = list(string.ascii_uppercase)
    index = alphabet.index(code_letter.upper())
    row = alphabet[index:] + alphabet[:index]
    number = (row.index(letter.upper()))
    result = alphabet[number]
    if letter.islower():
        result = result.lower()
    return result

def decrypt(plainText, codeword):
    codeword = (((len(plainText))//(len(codeword)))+1)*codeword
    result = ""
    word = ""
    for x in range(len(plainText)):
        if plainText[x].isalpha():
            word += plainText[x]
    for x in range(len(word)):
        result += decrypt_letter(word[x], codeword[x])
    for x in range(len(plainText)):
        if plainText[x].isalpha():
            pass
        else:
            result = result[:x] + plainText[x] + result[x:]
    return result
secret_message = """Gchl kdcey sor fynfb lyssg nag pie zsuvrlk cfboyih sijuv bh liwf 
wgohvhwoh, n hwx bnnapb, pifdsvpwe wa Facsenq, bbq xwewpulfr gi lis clgqcfcljca 
nzbh nfd nsa ujf qeysusq yivoy.

Hgx kr ujf saashsq cf b ueysu qvpam knl, lfggcfh kuylise nzbh auljca, ij bbl hsuwbh 
kp qbhufwiyv bbq mg esqcubhrx, ubb yifh saxmss. Jy sss zyl pb n ajfog vsuhyy-xjsyx 
gg huul xoe. Qw ioiy upar ng esqcubhr u hpfgcgo cs nzbh scwmr, nm s gwaud ssfnaou 
cfsds sij uvbmw xvb bwss tunf huyas zvpwt huul uvnn fbhvif nwtbl mwiy. Au wf uductylise 
zauhvhy bbq jjpdrl liog qw tvbode rb nzvg.

Ool, jb n fssurl kfbfy, of qnh fph qyvjqnnw -- xs puf ocg wgogrwjbhr -- qw doa hgu 
vnfdpk -- gbat ueimor. Gbw cfnpw nsa, fawwaa sor qyse, kui kufhaymsq bwss, uunf 
qbhkfqeulfr vn, xbf nvgws boj qcbl hpkrl lp oqx gs rrnjbqg. Nzf kblde kvfd mwgndf 
bbnw, oce fgou eyefaoyj xvnn of gns zffr, vmu wg wso brpws tblyfh jbsu huyq ewq 
bwss. Vn at tbl mt huy djjvhy, sogbws, hb vw esqcubhrx zffr ng uvr ofgwackisq qgsy 
jbadv gbwz kui xpitbl isey zbjr nzvg suj tc aitmm nxnbbpyv. Jh vm jbhuyj gce ok 
uc oy zffr xwewpulfr gi lis tlwbh gukl frgsjbvhy cssijf if -- nzbh slgn huykf vbhgssq 
xwbr jy lbyr cfdfrukfr qynphvif uc gbsu qnokf tbl oiwpb lisl asws gbw mofn xvzy 
gwbghlw pt qynphvif -- uvnn of vrlw iwtbdz frmgmjr nzbh gbwts qyse guudm bbn zbjr 
xafr vh nbwa -- nzbh gbat bnnapb, hhvff Tiv, tvnfd ioiy s osj vashu ix gfryvpa -- 
nhv uvnn ypjrlfnsan gg huy hfccfw, cm gbw qsbjdf, tbl lis cygqzr, mzbzy hgu drlatv 
slgn huy wbfgb."""


cypher = decrypt(secret_message, "bonus")

print(cypher)

