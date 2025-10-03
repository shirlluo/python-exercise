prices={
    'info':	[600,630,620],
    'ril':	[1430,1490,1567],
    'mtl':	[234,180,160]
}
print(prices)
import statistics

def print_all():
    for s,p in prices.items():
        avg=statistics.mean(p)
        print(f'{s} ==> {p} ==> avg:{avg}')
def add():
    stock=input('Enter the stock ticker: ')
    stock=stock.lower()
    price=input(f'Enter the price of {stock}: ')
    price=float(price)
    if stock in prices:
        prices[stock].append(price)
    else:
        prices[stock]=[price]
    print_all()

def main():
    x = input('Enter the command: ')
    if x.lower()=='print':
        print_all()
    elif x.lower()=='add':
        add()
    else:
        print('please enter a valid command')
if __name__=='__main__':
    main()
