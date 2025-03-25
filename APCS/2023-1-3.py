def main():
    from sys import stdin
    e = stdin.readline
    def caculate_f(d):

        idx = 0
        len_d = len(d)
        arr = []
        s = ""

        while idx < len_d:

            if d[idx] == "f":
                layer = 0
                d_f = ""
                idx += 2

                while True:

                    if d[idx] == ")":
                        if layer == 0: break
                        layer -= 1
                    
                    if d[idx] == "f":
                        layer += 1

                    d_f += d[idx]
                    idx += 1

                result = caculate_f(d_f)
                s += str(result)
                idx += 1
                continue

            if d[idx] == ",":

                multi = s.split("*")
                final_multi = [sum([int(j) for j in i.split("+")]) for i in multi]
                result = 1
                for i in final_multi: result *= i
                arr.append(int(result))

                s = ""
                idx += 1
                continue

            s += d[idx]
            idx += 1
        
        multi = s.split("*")
        final_multi = [sum([int(j) for j in i.split("+")]) for i in multi]
        result = 1
        for i in final_multi: result *= i
        arr.append(int(result))

        return max(arr) - min(arr)
            
    d = e().strip()

    idx = 0
    len_d = len(d)
    s = ""

    while idx < len_d:

        if d[idx] == "f":
            layer = 0
            d_f = ""
            idx += 2

            while True:

                if d[idx] == ")":
                    if layer == 0: break
                    layer -= 1
                
                if d[idx] == "f":
                    layer += 1

                d_f += d[idx]
                idx += 1

            result = caculate_f(d_f)
            s += str(result)
            idx += 1
            continue

        s += d[idx]
        idx += 1
    
    multi = s.split("*")
    final_multi = [sum([int(j) for j in i.split("+")]) for i in multi]
    result = 1
    for i in final_multi: result *= i

    print(result)

main()