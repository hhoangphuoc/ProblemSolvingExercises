
e = lambda:map(int,input().split())
for _ in range(int(input())):
    W,H=e()
    A,B,C,D=e()
    w,h=e()
    print(max(0,min(l))if(l:=(w-A,w-W+C)*(w+C-A<=W)+(h-B,h-H+D)*(h+D-B<=H))else-1)