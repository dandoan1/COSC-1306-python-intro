# -*- coding: utf-8 -*-
"""
Created on Oct 27 16:10:38 2020
assignment8
cosc1306
@author: dan doan 1986920

Four score and seven years ago our fathers brought forth on this 
continent, a new nation, conceived in Liberty, and dedicated to the proposition 
that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation 
so conceived and so dedicated, can long endure. We are met on a great battle-field 
of that war. We have come to dedicate a portion of that field, as a final resting 
place for those who here gave their lives that that nation might live. It is altogether 
fitting and proper that we should do thus.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not 
hallow -- this ground. The brave men, living and dead, who struggled here, have 
consecrated it, far above our poor power to add or detract. The world will little 
note, nor long remember what we say here, but it can never forget what they did 
here. It is for us the living, rather, to be dedicated here to the unfinished work 
which they who fought here have thus far so nobly advanced. It is rather for us 
to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full 
measure of devotion -- that we here highly resolve that these dead shall not have 
died in vain -- that this nation, under God, shall have a new birth of freedom -- 
and that government of the people, by the people, for the people, shall not perish 
from the earth.
"""
import string

def encrypt_letter(letter, code_letter):
    alphabet = list(string.ascii_uppercase)
    index = alphabet.index(code_letter)
    row = alphabet[index:] + alphabet[:index]
    col = alphabet.index(letter.upper())
    result = row[col]
    if letter.islower():
        result = result.lower()
    return result

def encryption(plainText, codeword):
    codeword = (((len(plainText))//(len(codeword)))+1)*codeword
    Text = ""
    cypher_text = ""
    for x in range(len(plainText)):
        if plainText[x].isalpha():
            Text += plainText[x]
    for x in range(len(Text)):
        cypher_text += encrypt_letter(Text[x], codeword[x])
    for x in range(len(plainText)):
        if plainText[x].isalpha():
            pass
        else:
            cypher_text = cypher_text[:x] + plainText[x] + cypher_text[x:]
    return cypher_text
#This is the plain-text to be encrypted. Do Not delete this!
plain_text = """The quick brown fox jumps over the lazy dog."""
plain_text2 = """A test string, just for practice - here in Houston."""

#This is the easy secret message for optional decryption and testing
easy_secret = """S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp."""

#This is the Full secret message for optional (bonus) decryption
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


#TO DO:
#1. Ask the user for a code word and store it for use later
while True:
    code_word = input("Please enter a code word with all letters: ")
    code_word = code_word.upper()
    if code_word.isalpha():
        break
    else:
        print ("Some nonletter detected please try again.")
        pass
    
#2. Call an encryption function with the plainText above and the code word and save the result it gives back (cypher-text)
cypher = encryption(plain_text2, code_word)
#3. Print out the cypher-text <-- This is the goal of the assignment!  
print(cypher)


#BONUS FUNCTION FOR DECRYPTION BELOW THIS LINE
"""

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

cypher = decrypt(secret_message, "bonus")

print(cypher)

"""
