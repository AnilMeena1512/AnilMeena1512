from collections import Counter
n = int(input());
a=list(map(int,input().strip().split()))[:n]
a.sort()
sum1=sum(a);
mean=sum1/n;
print(round(mean,1))
median=0;
count=0;
def medianMode(n):
    if n%2==0:
        median=(a[n//2]+a[(n//2)-1])/2;
    else:
        median=a[(n//2)];
    return(round(median,1));

print(medianMode(n))

data=Counter(a);
get_mode=dict(data);
mode=[k for k, v in get_mode.items() if v==max(list(data.values()))]

if len(mode)==n:
    get_mode=min(a);
else:
    get_mode="mode is/are: " + ','.join(map(str,mode))
print(get_mode)
