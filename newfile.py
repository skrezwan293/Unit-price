from termcolor import colored
import pyfiglet

banner = pyfiglet.figlet_format("Unit - Price Calculator")
print(colored(banner, "green"))

price = 0

net_unit = float(input(colored("Net unit amount: ", "cyan")))

if net_unit < 100:
    price = 0
    print(colored("Price is: $0 (No charge for usage under 100 units)", "green"))

elif 100 < net_unit <= 200:
    price = (net_unit - 100) * 5
    print(colored(f"Price is: ${price} (Calculated at $5 per unit for usage between 100 and 200 units)", "yellow"))

elif net_unit > 200 and net_unit <= 500:
    price = (net_unit - 200) * 10 + 500
    print(colored(f"Price is: ${price} (Calculated at $10 per unit for usage over 200 units plus $500)", "red"))
    
elif net_unit > 500 and net_unit <= 1000:
    price = (net_unit - 500) * 20 + 1000
    print(colored(f"Price is : ${price} (Calculated at $20 per unit for usage over 500 unit plus $1000"),"blue")  