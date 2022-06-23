
def printer_atom(arg_list):
    command = arg_list[0];
    curstate = "Initial";
    curstep = 0;

    for cmd in command:
        if (curstep == 0):
            if (cmd == "S"):
                curstep = 1;
                curstate = "Login";
                continue;
            else:
                break;
        if (curstep == 1):
            if (cmd == "1" and curstate == "Login"):
                curstep = 2;
                curstate = "Choosing";
                continue;
            elif (cmd == "2" and curstate == "Login"):
                curstate = "Login";
                continue;
            elif (cmd == "G" and curstate == "Login"):
                curstep = 2;
                curstate = "Exit";
                continue;
            else:
                curstate = "Failure";
                break;
        if (curstep == 2):
            if (cmd == "3" and curstate == "Choosing"):
                curstep = 3;
                curstate = "AlterCode";
                continue;
            elif (cmd == "6" and curstate == "Choosing"):
                curstep = 3;
                curstate = "Deposit";
                continue;
            elif (cmd == "8" and curstate == "Choosing"):
                curstep = 3;
                curstate = "Withdrawal";
                continue;
            elif (cmd == "A" and curstate == "Choosing"):
                curstep = 3;
                curstate = "Transfer";
                continue;
            elif (cmd == "C" and curstate == "Choosing"):
                curstep = 3;
                curstate = "Inquiry";
                continue;
            elif (cmd == "G" and curstate == "Choosing"):
                curstep = 3;
                curstate = "Exit";
                continue;
            elif (cmd == "E" and curstate == "Exit"):
                curstep = 3;
                curstate = "End";
                break;
            else:
                curstate = "Failure";
                break;
        if (curstep == 3):
            if (cmd == "5" and curstate == "AlterCode"):
                curstep = 4;
                curstate = "AlterCode";
                break;
            elif (cmd == "4" and curstate == "AlterCode"):
                curstep = 4;
                curstate = "Login";
                break;
            elif (cmd == "7" and curstate == "Deposit"):
                curstep = 4;
                curstate = "Choosing";
                break;
            elif (cmd == "9" and curstate == "Withdrawal"):
                curstep = 4;
                curstate = "Choosing";
                break;
            elif (cmd == "B" and curstate == "Transfer"):
                curstep = 4;
                curstate = "Choosing";
                break;
            elif (cmd == "D" and curstate == "Inquiry"):
                curstep = 4;
                curstate = "Choosing";
                break;
            elif (cmd == "E" and curstate == "Exit"):
                curstep = 4;
                curstate = "End";
                break;
            else:
                curstate = "Failure";
                break;
        if (curstep == 4):
            curstate = "Failure";
            break;

    return curstate;

if __name__ == '__main__':
    print(printer_atom(['S135']))
