################################################################################
# Gozde DOGAN
# 131044019
# CSE321 - Introduction to Algorithm Design
# Homework 5
# Question 3
################################################################################

################################################################################
#
# Metodlarin uzerinde yorum bloklari icinde neler yaptiklari ve karmasikliklari 
# ayrintili olarak anlatildi.
# decentNumber metodunun karmasikligi worst case de n, best case de 1 
# olarak bulundu.
# Tasarlanan algoritmanin karmasikligi da best case'de 1, worst case'de n'dir.
#
################################################################################

import sys

def main():
    dn = decentNumber(1)
    #print "\nnum:1"
    print(dn)
    #Output: -1
    
    dn = decentNumber(2)
    #print "\nnum:2"
    print(dn)
    #Output: -1
    
    dn = decentNumber(3)
    #print "\nnum:3"
    print(dn)
    #Output: 555
    
    dn = decentNumber(4)
    #print "\nnum:4"
    print(dn)
    #Output: -1
    
    dn = decentNumber(5)
    #print "\nnum:5"
    print(dn)
    #Output: 33333
    
    dn = decentNumber(6)
    #print "\nnum:6"
    print(dn)
    #Output: 555555
    
    dn = decentNumber(7)
    #print "\nnum:7"
    print(dn)
    #Output: -1
    
    dn = decentNumber(8)
    #print "\nnum:8"
    print(dn)
    #Output: 55533333
    
    dn = decentNumber(11)
    #print "\nnum:11"
    print(dn)
    #Output: 55555533333
    
    dn = decentNumber(14)
    #print "\nnum:14"
    print(dn)
    #Output: 55555555533333
    
    dn = decentNumber(29)
    #print "\nnum:29"
    print(dn)
    #print dn + "\n"
    #Output: 55555555555555555555555533333

    
    
    
################################################################################
#
# 2 ve asagisindaki her sayi icin -1 return edilir.
# Oncelikle sayinin 3 e gore modunun 0 olup olmadigi kontrol edilir.
# Boylece kac tane 5 yazilacagi bulunmus olur. 
# Bu islem 5 cikartilarak devam eder, boylece kac tane 5 yazilacagi bulunmus olur. 
# Return edilirken kac tane 5 yazilacagi bulundugu icin inputtan yazilacak 5 sayisi
# cikartilarak kac tane 3 yazilacagi bulunur ve string return edilir.
# 
# Best case de while dongusu remainder%3 == 0 oldugunda biter, bu da ilk defa if
# sartina gelindiginde olabilir. Bu nedenle best case'i constant time'dir.
# Worst case de while dongusu remainder'den 5 cikarma isleminin remainder'in 
# 2'den kucuk olmasi durumunda biter. remainder/5 = n/5 oldugu icin worst case 
# linear time'dir.
#
# decentNumber complexity;
# decentNumber worst case complexity = O(n)
# decentNumber best case complexity = O(1)
#
################################################################################
def decentNumber(n):
    countOfThrees = 0
    countOfFives  = 0
    remainder = n 
    
    while remainder > 2:
        if remainder % 3 == 0:
            countOfFives = remainder
            break
            
        remainder -= 5
 
    countOfThrees = n - countOfFives
    if remainder < 0 or countOfThrees % 5:
        return "-1"

    return '5'*countOfFives + '3'*countOfThrees


################################################################################
#
# Internetten buldugum kod parcasi, test edip mantigini anlamak icin kullandim.
# Asil kod parcasi yukaridaki kod parcasidir.
#
################################################################################
def _decentNumber(n):
    a, b = partition35(n)
    if a < 0:
        return "-1"
    else:
        return ''.join(('5'*a, '3'*b))

def partition35(n):
    k = (4*n - 1) // 3 + 1  # rounded up int division
    a = 21*n - 15*k  # (7*n - 5*k)*3
    b = 15*k - 20*n  # (3*k - 4*n)*5
    return a, b

           
        
if __name__ == "__main__":
    main() 
