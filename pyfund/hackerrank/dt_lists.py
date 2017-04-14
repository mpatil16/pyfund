def input_command(n):
    l = []
    for _ in range(n):
        s = raw_input()
        cmd = s[0]
        args = s[1:]
        print cmd
        print args
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
        else:
            print l

if __name__ == '__main__':
    input_command(int(raw_input()))