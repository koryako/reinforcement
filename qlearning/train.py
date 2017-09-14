from qlearn import Qlearn
from maze_env import Maze

def updata():

    for episode in range(100):
              s=env.reset()
              while True:
                  env.render()
                  action=RL.choose_action(str(s))
                  s_,reward,done=env.step(action)
                  RL.learn(str(s),action,reward,str(s_))
                  s=s_
                  if done:
                      break

    print('game over')
    env.distroy()

if __name__=="__main__":
    env=Maze()
    RL=Qlearn(action=list(range(env.n_actions)))
    env.after(100,updata)
    env.mainloop()

