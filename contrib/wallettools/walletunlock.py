from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:4364")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
