import dhooks

webhook = input("Webhook : ")
message = input("Message : ")
message_2 = input("Message : ")
threads = int(input("Threads : "))

hook = dhooks.Webhook(webhook)

def loop():

    for x in range(threads) :
        hook.send(message)
        print(f"[+] {webhook}")
        hook.send(message_2)
        print(f"[+] {webhook}")

loop()


