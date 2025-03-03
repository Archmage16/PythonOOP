import time

def time_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Прошло {elapsed_time} секунд.")
            return result
        return wrapper
    
    
class Prime():
    def __init__(self, ran):
        self.ran = ran
    
    @time_decorator
    def get_primes_up_to_1000(self):
        primes = []

        for i in range(2, self.ran + 1):
            is_prime = True
            for n in range(2, i):
                if i % n == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)

        return primes
    
    @property
    def primes(self):
        return self.get_primes_up_to_1000()
    
    @primes.setter
    def primes(self, new_ran):
        self.ran = new_ran

    def Print(self):
        print(self.primes)
        
        
p = Prime(1000)
p.Print()