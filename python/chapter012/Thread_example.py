from time import sleep
import threading

def music(music_name):
    for i in range(2):
        print('Listening {}'.format(music_name))
        sleep(1)
    print('music over')

def game(game_name):
    for i in range(2):
        print('Pleying {}'.format(game_name))
        sleep(3)
    print('game over')

threads = []
t1 = threading.Thread(target=music,args=('Beat it',))
threads.append(t1)
t2 = threading.Thread(target=game,args=('Need for Speed',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        #t.setDaemon(True)
        t.start()
        
    #for t in threads:
    #    t.join()
    print('Main Thread is over')