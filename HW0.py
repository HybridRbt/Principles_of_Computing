__author__ = 'jeredyang'

# # val1 = [1, 2, 3]
# # val2 = val1[1:]
# # val1[2] = 4
# #
# # print val2[1]
# #
# # a = dict(None)
# # print a
#
#
# # def appendsums(lst):
# #     """
# #     Repeatedly append the sum of the current last three elements of lst to lst. loop for 25 times
# #     """
# #     for times in range(0, 25):
# #         new_add = sum(lst[len(lst) - 3:])
# #         lst.append(new_add)
# #
# #     return lst
# #
# #
# # sum_three = [0, 1, 2]
# # appendsums(sum_three)
# # print sum_three[10], sum_three[20]
#
#
# class BankAccount:
#     acc_balance = 0
#     accumulated_fees = 0
#
#     def __init__(self, initial_balance):
#         """Creates an account with the given balance."""
#         self.acc_balance = initial_balance
#         self.accumulated_fees = 0
#
#     def deposit(self, amount):
#         """Deposits the amount into the account."""
#         self.acc_balance += amount
#
#     def withdraw(self, amount):
#         """
#         Withdraws the amount from the account.  Each withdrawal resulting in a
#         negative balance also deducts a penalty fee of 5 dollars from the balance.
#         """
#         if self.acc_balance - amount < 0:
#             self.acc_balance -= (amount + 5)
#             self.accumulated_fees += 5
#         else:
#             self.acc_balance -= amount
#
#     def get_balance(self):
#         """Returns the current balance in the account."""
#         return self.acc_balance
#
#     def get_fees(self):
#         """Returns the total fees ever deducted from the account."""
#         return self.accumulated_fees
#
#
# def test():
#     my_account = BankAccount(10)
#     my_account.withdraw(15)
#     my_account.deposit(20)
#     print my_account.get_balance(), my_account.get_fees()
#
#
# def runrun():
#     my_account = BankAccount(10)
#     my_account.withdraw(5)
#     my_account.deposit(10)
#     my_account.withdraw(5)
#     my_account.withdraw(15)
#     my_account.deposit(20)
#     my_account.withdraw(5)
#     my_account.deposit(10)
#     my_account.deposit(20)
#     my_account.withdraw(15)
#     my_account.deposit(30)
#     my_account.withdraw(10)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.withdraw(50)
#     my_account.deposit(30)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.withdraw(5)
#     my_account.deposit(20)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.deposit(30)
#     my_account.withdraw(25)
#     my_account.withdraw(5)
#     my_account.deposit(10)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.withdraw(10)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.deposit(30)
#     my_account.withdraw(25)
#     my_account.withdraw(10)
#     my_account.deposit(20)
#     my_account.deposit(10)
#     my_account.withdraw(5)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.withdraw(5)
#     my_account.withdraw(15)
#     my_account.deposit(10)
#     my_account.withdraw(5)
#     print my_account.get_balance(), my_account.get_fees()
#
# # test()
# runrun()

def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60

clock_helper(90)