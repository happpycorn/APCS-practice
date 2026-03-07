

def main():
    from sys import stdin
    e = stdin.readline

    digits = "零壹貳參肆伍陸柒捌玖"
    units = ["", "拾", "佰", "仟"]
    group_units = ["", "萬", "億", "兆"]

    def transform(num):
        if num == 0: return "零"

        result = ""
        group_count = 0
        
        while num > 0:
            section = num % 10000
            section_str = ""
            last_is_zero = True
            
            for i in range(4):
                digit = section % 10
                if digit == 0:
                    if not last_is_zero:
                        section_str = digits[0] + section_str
                    last_is_zero = True
                else:
                    section_str = digits[digit] + units[i] + section_str
                    last_is_zero = False
                section //= 10
            
            if section_str: result = section_str + group_units[group_count] + result
                
            num //= 10000
            group_count += 1

        while "零零" in result:
            result = result.replace("零零", "零")
        return result.strip("零")

    while True:
        try:
            n = int(e().strip())
        except:
            break
        print(transform(n))
main()