from pexpect import pxssh


def Login(server, username, password):
    try:
        s = pxssh.pxssh()
        s.login(server, username, password)
        print("yes")
    except:
        print("no")


def main():
    Login("192.168.153.128", "kali", "kali")


if __name__ == '__main__':
    main()
