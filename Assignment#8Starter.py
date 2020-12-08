# -*- coding: utf-8 -*-
"""
Created on Oct 27 16:10:38 2020
assignment8
cosc1306
@author: dan doan 1986920
FOUR SCORE AND SEVEN YEARS AGO OUR FATHERS BROUGHT FORTH ON THIS 
CONTINENT, A NEW NATION, CONCEIVED IN LIBERTY, AND DEDICATED TO THE PROPOSITION 
THAT ALL MEN ARE CREATED EQUAL.

NOW WE ARE ENGAGED IN A GREAT CIVIL WAR, TESTING WHETHER THAT NATION, OR ANY NATION 
SO CONCEIVED AND SO DEDICATED, CAN LONG ENDURE. WE ARE MET ON A GREAT BATTLE-FIELD 
OF THAT WAR. WE HAVE COME TO DEDICATE A PORTION OF THAT FIELD, AS A FINAL RESTING 
PLACE FOR THOSE WHO HERE GAVE THEIR LIVES THAT THAT NATION MIGHT LIVE. IT IS ALTOGETHER 
FITTING AND PROPER THAT WE SHOULD DO THUS.

BUT, IN A LARGER SENSE, WE CAN NOT DEDICATE -- WE CAN NOT CONSECRATE -- WE CAN NOT 
HALLOW -- THIS GROUND. THE BRAVE MEN, LIVING AND DEAD, WHO STRUGGLED HERE, HAVE 
CONSECRATED IT, FAR ABOVE OUR POOR POWER TO ADD OR DETRACT. THE WORLD WILL LITTLE 
NOTE, NOR LONG REMEMBER WHAT WE SAY HERE, BUT IT CAN NEVER FORGET WHAT THEY DID 
HERE. IT IS FOR US THE LIVING, RATHER, TO BE DEDICATED HERE TO THE UNFINISHED WORK 
WHICH THEY WHO FOUGHT HERE HAVE THUS FAR SO NOBLY ADVANCED. IT IS RATHER FOR US 
TO BE HERE DEDICATED TO THE GREAT TASK REMAINING BEFORE US -- THAT FROM THESE HONORED 
DEAD WE TAKE INCREASED DEVOTION TO THAT CAUSE FOR WHICH THEY GAVE THE LAST FULL 
MEASURE OF DEVOTION -- THAT WE HERE HIGHLY RESOLVE THAT THESE DEAD SHALL NOT HAVE 
DIED IN VAIN -- THAT THIS NATION, UNDER GOD, SHALL HAVE A NEW BIRTH OF FREEDOM -- 
AND THAT GOVERNMENT OF THE PEOPLE, BY THE PEOPLE, FOR THE PEOPLE, SHALL NOT PERISH 
FROM THE EARTH.
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
cypher = encryption(plain_text, code_word)
#3. Print out the cypher-text <-- This is the goal of the assignment!  
print(cypher)


#BONUS FUNCTION FOR DECRYPTION BELOW THIS LINE

def decrypt_letter(letter, code_letter):
    alphabet = list(string.ascii_uppercase)
    index = alphabet.index(code_letter)
    row = alphabet[index:] + alphabet[:index]
    number = (row.index(letter))
    return alphabet[number]


