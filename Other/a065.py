def main():
  from sys import stdin
  d = stdin.readline().strip()
  ans = [abs(ord(d[i])-ord(d[i+1])) for i in range(len(d)-1)]
  print("".join(map(str, ans)))
main()