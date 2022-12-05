import colorama

def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(color + f'\r|{bar}| {percent:.2f}%', end='\r')
    if progress == total:
        print(colorama.Fore.GREEN + f'\r|{bar}| {percent:.2f}%', end='\r')

def getNumericalValue(message,min=0,max=1000):    
    while True:
        try:
            numerical_value = int(input(message))
            assert min <= numerical_value <= max
            return numerical_value
        except ValueError:
            print("Not a number. Please enter again")
        except AssertionError:
            print(f"Please enter a number between {min} and {max}")

def getStringValue(message,min=0,max=1000,func = None):    
    while True:
        try:
            value = input(message)
            assert min <= len(value) <= max
            if func!=None:
                func()
            return value
        except AssertionError:
            print(f"Please enter a string length between {min} and {max}")           