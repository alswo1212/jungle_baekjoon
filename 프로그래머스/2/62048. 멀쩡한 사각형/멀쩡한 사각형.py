def solution(w,h):
    def gcd(a:int,b:int)->int:
        if a % b == 0:
            return b
        return gcd(b, a%b)
    
    return w*h - w - h + gcd(w,h)