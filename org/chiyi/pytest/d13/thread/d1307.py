from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # acquire the lock
        self._lock.acquire()
        try:
            # calc the balance after deposit
            new_balance = self._balance + money
            # simulate accepting the deposit business, cost 0.01 seconds.
            sleep(0.01)
            self._balance = new_balance
        finally:
            # release the lock in finally ensures 
            # that the locck can be released either normal or exception
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # create a deposit of 100 deposits to save money in the same account
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # wait until all the deposited threads have been executed.
    for t in threads:
        t.join()
    print('账户余额为:￥%d元' % account.balance)


if __name__ == "__main__":
    main()
