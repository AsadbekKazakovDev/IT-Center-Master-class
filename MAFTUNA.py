'''
(int)List elementlari ichida juft o`rindagi elementlar chop etadigan dastur tuzing.
main() funksiya orqali ishlansin
'''
def List(a):
    for i in a[1::2]:
        print(i)

a = [1,2,3,4,5,6,7,8]
List(a)