def minSchedular(slots1,slots2,duration):
    sorted(slots1)
    sorted(slots2)

    n1,n2 = len(slots1), len(slots2)
    i=j=0

    while i<n1 and j<n2:
        s1,e1 = slots1[i]
        s2,e2 = slots2[j]

        start = max(s1,s2)
        end = min(e1,e2)

        if end- start >= duration:
            return [start, start+duration]
        if e1>e2:
            j+=1
        else:
            i+=1

    return []

if __name__=='__main__':
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    durattion = 8
    print(minSchedular(slots1,slots2,durattion))


