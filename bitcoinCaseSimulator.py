from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
from random import choices
import time

balance = 15000.0
btcBalance = 0.0

btc = BtcConverter()
btcSymb = btc.get_symbol()

symbol = CurrencyCodes().get_symbol("USD")

while True:
	print("\n### Welcome to Bitcoin Case Simulator ###"
					" (1 " + btcSymb + " ~ " + str(btc.get_latest_price("USD")) + " )"+
					"\n\t[A] Account"+
					"\n\t[O] Open Case"+
					"\n\t[Q] Quit!")

	if balance == 0:
		print("[>] You have no money on your account! Deposit from [A] Account page to start.")
	
	menu = input("[>] Select > ")

	if menu == "o" or menu == "O":
		while True:
			if balance == 0:
				print("[>] You have no money on your account! Please deposit first!")
				time.sleep(1)
				break

			elif balance != 0:
				
				try:
					bet = int(input("[>] Enter your bet : "))

					if bet <= balance:
						balance = balance - bet
						items = [bet/5, bet/4, bet/3, bet/2, bet, bet*2]
						probs = [0.75, 0.5, 0.45, 0.35, 0.25, 0.05]
						win = str(choices(items, probs))
						win = win.replace("[", "")
						win = win.replace("]", "")
						win2btc = float(win) / btc.get_latest_price("USD")
						btcBalance = btcBalance + win2btc
						print("[>] You won : " + str(win2btc) + " " + btcSymb)

						again = input("[>] Do you want to continue? [Y] / [N]\n[>] Select > ")

						if again == "y" or again == "Y":
							pass
						elif again == "n" or again == "N":
							break
						else:
							print("[>] Please enter valid input!")
							time.sleep(1)
					
					elif bet > balance:
						print("[>] [>] You don't have enough money on your account! ")
						again = input("[>] Do you want to continue? [Y] / [N]\n[>] Select > ")

						if again == "y" or again == "Y":
							pass
						elif again == "n" or again == "N":
							break
						else:
							print("[>] Please enter valid input!")
							time.sleep(1)
				except:
					print("[>] Please enter valid input! (Hint: Use numbers)")
					time.sleep(1)

		else:
			print("[>] An error occured!")
			time.sleep(1)

	elif menu == "a" or menu == "A":
		
		while True:
			if balance == 0:
				print("Balance \t | \t" + str(balance) + " " + symbol + "\t ~ 0 " + btcSymb)
				print("BTC \t\t | \t" + str(btcBalance) + " " + btcSymb + "\t ~ " + str(btcBalance*(btc.get_latest_price("USD"))) + " " + symbol)
			
			elif balance != 0:
				print("\nBalance \t | \t" + str(balance) + " " + symbol + "\t ~ " + str(balance/(btc.get_latest_price("USD"))) + " " + btcSymb)
				print("BTC \t\t | \t" + str(btcBalance) + " " + btcSymb + "\t ~ " + str(btcBalance*(btc.get_latest_price("USD"))) + " " + symbol)

			else:
				print("[>] An error occured!")
				time.sleep(1)

			accmenu = input("\n\t[D] Deposit"+
							"\n\t[C] Convert"+
							"\n\t[W] Withdraw"+
							"\n\t[B] Back\n[>] Select > ")

			if accmenu == "d" or accmenu == "D":
				try:
					money = float(input("[>] Enter the amount of money : "))
					if money > 0:
						balance = balance + money
						print("[>] Transaction verifying...")
						time.sleep(1)
					elif money <= 0:
						print("[>] Please enter valid amount to Deposit!")
						time.sleep(1)
					else:
						print("[>] An error occured!")
						time.sleep(1)
				except:
					print("[>] Please enter valid input! (Hint: Use numbers)")
					time.sleep(1)

			elif accmenu == "w" or accmenu == "W":
				try:
					money = float(input("[>] Enter the amount of money : "))
					if balance >= money:
						balance = balance - money
						print("[>] Balance = " + str(balance))
						time.sleep(1)
					
					elif balance < money:
						print("[>] You dont enough balance to Withdraw!")
						time.sleep(1)

					else:
						print("[>] An error occured!")
						time.sleep(1)
				
				except:
					print("[>] Please enter valid input! (Hint: Use numbers)")
					time.sleep(1)

			elif accmenu == "c" or accmenu == "C":

				try:
					amount = float(input("[>] Enter the amount of BTC convert to USD (Min:0.01) : "))
					if amount <= btcBalance:
						if amount > 0.01:
							btcBalance = btcBalance - amount
							balance = balance + amount*btc.get_latest_price("USD")
						elif amount <= 0:
							print("[>] Please enter valid amount to Convert!")
							time.sleep(1)
						elif amount % 0.01 != 0:
							print("[>] Amount is lower than 0.01")

					elif amount > btcBalance:
						print("[>] You dont have this amount BTC!")
						time.sleep(1)

				except:
					print("[>] Please enter valid input! (Hint: Use numbers)")
					time.sleep(1)

			elif accmenu == "b" or accmenu == "B":
				break

			else:
				print("[>] Please enter valid menu selection!")
				time.sleep(1)

	elif menu == "q" or menu == "Q":
		print("[>] Bye Bye...")
		time.sleep(1)
		break
	
	else:
		print("[>] Please enter valid menu selection!")
		time.sleep(1)