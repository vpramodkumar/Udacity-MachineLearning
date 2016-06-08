import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint

        # TODO: Initialize any additional variables here
        self.Q_Table = {}
        self.valid_actions = self.env.valid_actions

        # Q-learning Variables
        self.alpha = .05
        self.gamma = .5

        #csv file title name
        self.trial_parameters = "Gamma={}_Alpha={}".format(self.gamma,self.alpha)

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    #intialize all possible actions for a particular state in the Q-Table.
    def init_Q_Values (self, state):
        possible_actions = {possible_action: 0 for possible_action in self.valid_actions }
        self.Q_Table[state] = possible_actions

    #For the current state, iterates over all possible actions and returns the action which maximizes the Q value
    def ArgMAX_Q (self, state):
        #if the sum of the values is greater than 0, then there is an entry, so choose the max
        if sum(self.Q_Table[state].values()) != 0:
            return max(self.Q_Table[state].iteritems(), key= lambda x : x[1])[0]
        else:
            #Otherwise, just pick a random action.  We have to force this because max doesn't randomly break ties, it will choose the same option again and again for different unseen states.
            return random.choice(self.valid_actions)

    #for the current state, iterates over all possible actions and returns the largest Q value
    def MAX_Q (self, state):
        return max(self.Q_Table[state].values())


    def update(self, t):
        # Gather inputs
        self.next_waypoint = self.planner.next_waypoint()  # from route planner, also displayed by simulator
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        #self.state = (inputs,self.next_waypoint,deadline)
        #this state will act as a key in the Q-table dictionary
        self.state = (('time_left', deadline), ('light', inputs['light'] ), ('next_waypoint', self.next_waypoint))

        #initialize the state into the Q_Table will do nothing if it's already there.
        if self.state not in self.Q_Table:
            self.init_Q_Values(self.state)

        # TODO: Select action according to your policy
        #action = random.choice(self.env.valid_actions[1:])
        action = self.ArgMAX_Q(self.state)

        # Execute action and get reward
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward
        #sense environment again,  in order to update Q_Table.
        inputs_next = self.env.sense(self)
        deadline -= 1  #we have to force this because the deadline only updates with env.step(), it won't update from env.act().
        self.next_waypoint = self.planner.next_waypoint()
        state_next = (('time_left', deadline), ('light', inputs_next['light'] ), ('next_waypoint', self.next_waypoint))

        #initialize the new state into the Q_Table will do nothing if it's already there.
        if state_next not in self.Q_Table:
            self.init_Q_Values(state_next)


        # Q-learning
        self.Q_Table[self.state][action] = (1-self.alpha) * self.Q_Table[self.state][action] + self.alpha * (reward + self.gamma * self.MAX_Q(state_next))

        #print "LearningAgent.update(): deadline = {}, inputs = {}, action = {}, reward = {}".format(deadline, inputs, action, reward)  # [debug]


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # set agent to track

    # Now simulate it
    # Create simulator (uses pygame when display=True, if available)
    sim = Simulator(e, update_delay=0.0, display=False)  # reduce update_delay to speed up simulation
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=1000)  # press Esc or close pygame window to quit
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line

    #initiliaze file for CSV logging
    with open('smartCabLog.txt', 'ab') as log:
        log.write("\n-----------------------------------")
        log.write("\nAlpha is set to {}".format(a.alpha))
        log.write("\nGamma is set to {}".format(a.gamma))
        log.write("\nThe agent FAILED : {} times".format(e.agent_ran_out_time))
        log.write("\nThe agent SUCCEEDED : {} times".format(e.agent_reached_in_time))
        log.write("\nSuccess rate of : {}".format(e.agent_reached_in_time/float(e.agent_reached_in_time+e.agent_ran_out_time)))

if __name__ == '__main__':
    run()
