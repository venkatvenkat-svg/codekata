def fact1(a):
    if(a==0):
        fa=1
    else:
        fa=1
        for i in range(1,a+1):
            fa=fa*i
    return fa
def fact2(b):
    if (b==0):
        fb=1
    else:
        fb=1
        for j in range(1,b+1):
            fb=fb*j
    return fb
def div(fa,fb):
    result=fa//fb
    print(result)
def main():
    a,b=map(int,input().split())
    fa=fact1(a)
    fb=fact2(b)
    #div(fact1(a),fact2(b))
    div(fa,fb)
main()
