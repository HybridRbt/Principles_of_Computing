"""
Cookie Clicker Simulator

Mini project for week 1
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor

#codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
# SIM_TIME = 10000000000.0
SIM_TIME = 100.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_time = 0.0
        self.current_cps = 1.0
        self.game_history = [(0.0, None, 0.0, 0.0)]
        self.current_state = ""

    def __str__(self):
        """
        Return human readable state
        """
        self.current_state = "Current State:\n"
        self.current_state += "Total cookies: " + str(self.total_cookies) + "\n"
        self.current_state += "Current cookies: " + str(self.current_cookies) + "\n"
        self.current_state += "Current time: " + str(self.current_time) + "\n"
        self.current_state += "Current CPS: " + str(self.current_cps) + "\n"
        return self.current_state

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self.current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self.game_history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time_u = None
        if self.current_cookies < cookies:
            while not time_u is None and time_u * 10 % 10 != 0:
                # if time_u has value and it's a fractional number, re compute
                time_u = (cookies - self.current_cookies) / self.current_cps

        return time_u

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            # only update when time > 0
            self.current_time += time
            self.update_cookies(time)
            self.__str__()

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        my_cost = float(cost)
        my_add_cps = float(additional_cps)
        if my_cost < self.current_cookies:
            # can buy items only when cookies are enough
            self.current_cookies -= my_cost  # subtract cost first
            self.current_cps += my_add_cps  # increase cps
            self.game_history.append((self.current_time, item_name, my_cost, self.total_cookies))  # update history

    def update_cookies(self, time):
        """
        Update the total cookies and current cookies based on elapsed time

        """
        self.total_cookies += self.current_cps * time
        self.current_cookies = self.total_cookies
        for each_buy in self.game_history:
            # for each item bought before the current time, subtract the cost from total, to get current cookies
            self.current_cookies -= each_buy[2]


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    # make a clone of the build_info object
    my_build_info = build_info.clone()

    # create a new ClickerState object
    my_state = ClickerState()

    #  loop until the time in the ClickerState object reaches the duration of the simulation
    while my_state.get_time() <= duration:
        next_upgrade = strategy(my_state.get_cookies(), my_state.get_cps(), duration - my_state.get_time(),
                               my_build_info)
        if next_upgrade is None:
            break
        else:
            time = my_state.time_until(my_build_info.get_cost(next_upgrade))
            if time > duration - my_state.get_time():
                break
        my_state.wait(time)
        my_state.buy_item(my_build_info, my_build_info.get_cost, my_build_info.get_cps())
        my_build_info.update_item()
    return ClickerState()


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"


def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, time_left, build_info):

    return None


def strategy_expensive(cookies, cps, time_left, build_info):
    return None


def strategy_best(cookies, cps, time_left, build_info):
    return None


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)


#run()

# def test_state():
#     my_state = ClickerState()  # initiate a state
#     print str(my_state)  # print initial state
#
#     my_state.wait(30)
#     print "After 30 second: \n" + str(my_state)
#
#     my_state.buy_item("test", "1", "0.5")
#     my_state.wait(30)
#     print "Buy a test item and after another 30 seconds: \n" + str(my_state)
#
# test_state()



