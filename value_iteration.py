#Backend-File
#Environment
from environment import GraphicDisplay, Env

class ValueIteration:
    def __init__(self, env):
        self.env = env
        # 2-d list for the value function
        self.value_table = [[0.0] * env.width for _ in range(env.height)]
        self.discount_factor = 0.9 

    #we will get next value function table from the current value function table
    def value_iteration(self):
        next_value_table = [[0.0] * self.env.width
                                    for _ in range(self.env.height)]
        for state in self.env.get_all_states():
            if state == [2, 2]:
                next_value_table[state[0]][state[1]] = 0.0
                continue
            value_list = []
            # Appending the value list based on rewards and discount factor
            for action in self.env.possible_actions:
                next_state = self.env.state_after_action(state, action)
                reward = self.env.get_reward(state, action)
                next_value = self.get_value(next_state)
                value_list.append((reward + self.discount_factor * next_value))
            # return the maximum value(it is the optimality equation!!)
            next_value_table[state[0]][state[1]] = round(max(value_list), 2)
        self.value_table = next_value_table

    # we are initiating the action based on the value function table
    def get_action(self, state):
        action_list = []
        max_value = -99999

        if state == [2, 2]:
            return []

        # calculating q values for the all actions and
        # append the action to action list which has maximum q value
        # Considers all the possible actions based on value table and the discount factor
        for action in self.env.possible_actions:

            next_state = self.env.state_after_action(state, action)
            reward = self.env.get_reward(state, action)
            next_value = self.get_value(next_state)
            value = (reward + self.discount_factor * next_value)

            if value > max_value:
                action_list.clear()
                action_list.append(action)
                max_value = value
            elif value == max_value:
                action_list.append(action)

        return action_list

    def get_value(self, state):
        return round(self.value_table[state[0]][state[1]], 2)

if __name__ == "__main__":
    env = Env()
    value_iteration = ValueIteration(env)
    grid_world = GraphicDisplay(value_iteration)
    grid_world.mainloop()
