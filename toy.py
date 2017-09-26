from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry("605x330")
#root.wm_attributes("-topmost", 1)
nb = ttk.Notebook(root)

f1 = Frame(nb)
f2 = Frame(nb)
f3 = Frame(nb)
f4 = Frame(nb)
f5 = Frame(nb)
f6 = Frame(nb)

nb.pack(fill='both', expand='yes')
nb.add(f1, text='Commands')
nb.add(f2, text='Anything else?')
nb.add(f3, text='Windows')
nb.add(f4, text= "Forms")
nb.add(f5, text= "G-Notes")
nb.add(f6, text= "Stall")

r_1_1 = "Reports, 1 - Vehicle Inventory Reports, then 1 - Price List. "
menuBar = Menu(root)
selection = IntVar()
prefix = StringVar()
prefix.set("")
status = StringVar()
status.set("")
temp = StringVar()

# leftFrame = Frame(root)

# middleFrame = Frame(root)

# rightFrame = Frame(root)
# rightLabel = Label(rightFrame, text="Forms:").pack()

# creates and displays "status" bar on bottom
statusBar = Label(root, fg="green", anchor=W, textvariable=status, bd=1, relief=SUNKEN)

def copyToClipboard(needsToBeCopied):
	status.set(needsToBeCopied)
	root.clipboard_clear()
	root.clipboard_append(needsToBeCopied)
	print(status.get())

# scripts
Button(f1, bg= "steelblue1", text="flush", command=lambda: copyToClipboard("ipconfig /flushdns & ipconfig /release & ipconfig /renew & ipconfig /flushdns")).pack(side = TOP, pady = 1.5)
Button(f1, bg= "steelblue1", text="zombie", command=lambda: copyToClipboard("START SHELL:::{26EE0668-A00A-44D7-9371-BEB064C98683}\\0\\::{2227A280-3AEA-1069-A2DE-08002B30309D} && NET STOP SPOOLER && echo y| DEL %systemroot%\System32\spool\PRINTERS\* && NET START SPOOLER && PAUSE && EXIT")).pack(side = TOP, pady = 1.5)
Button(f1, bg= "steelblue1", text="CACLS", command=lambda: copyToClipboard("FOR /D %A IN (C:\Frazer*) do ICACLS %A /setowner Administrators /t /c /q & ICACLS %A /t /c /q /grant Everyone:F & ATTRIB -h -s %A\* /s /d & Echo Complete")).pack(side = TOP, pady = 1.5)	
	

# forms
Button(f4, bg= "pale green", text="Form Number(s)", command=lambda: copyToClipboard("Can you provide me with the Form Number of the form(s) that you're speaking of, please?")).pack(pady = 1.5)
Button(f4, bg= "pale green", text="Added form", command=lambda: copyToClipboard('I have added that form for you, and you can "Load Latest Frazer Update" on your main computer to add it to your Print Forms menu.')).pack(pady = 1.5)
Button(f4, bg= "pale green", text="Added formS", command=lambda: copyToClipboard('I have added those forms for you, and you can "Load Latest Frazer Update" on your main computer to add them to your Print Print menu.')).pack(pady = 1.5)

# call us
Button(f2, bg = "tomato2", text="No problem! (call)", command=lambda:copyToClipboard("No problem! Thank you for using Frazer chat and we'll wait for your call!")).pack(side = TOP, anchor = W, pady = 1.5)
Button(f2, bg = "tomato2", text="You bet! (call)", command=lambda:copyToClipboard("You bet! Thank you for using Frazer chat and we'll wait for your call!")).pack(side = TOP, anchor = W, pady = 1.5)
Button(f2, bg = "tomato2", text="Thank you! (call)", command=lambda:copyToClipboard("Thank you for using Frazer chat and we'll wait for your call!")).pack(side = TOP, anchor = W, pady = 1.5)

# ending/anything else?
Button(f2, bg= "steelblue1", text="No prob - ?", command=lambda: copyToClipboard("No problem! Is there anything else I can help you with?")).pack(side = TOP, pady = 1.5)
Button(f2, bg= "steelblue1", text="You bet - ?", command=lambda: copyToClipboard("You bet! Is there anything else I can help you with?")).pack(side = TOP, pady = 1.5)
Button(f2, bg= "steelblue1", text="Anything else?", command=lambda: copyToClipboard("Is there anything else I can help you with?")).pack(side = TOP, pady = 1.5)

# successful endings
Button(f2, bg= "yellow2", text="No problem! (end)", command=lambda: copyToClipboard("No problem! Thank you for using Frazer chat and have a great day!")).pack(anchor = E, pady = 1.5)
Button(f2, bg= "yellow2", text="You bet! (end)", command=lambda:copyToClipboard("You bet! Thank you for using Frazer chat and have a great day!")).pack(anchor = E,pady = 1.5)
Button(f2, bg= "yellow2", text="Thank you! (end)", command=lambda:copyToClipboard("Thank you for using Frazer chat and have a great day!")).pack(anchor = E, pady = 1.5)

# Windows
Button(f3, text= "main or w/s?", command=lambda: copyToClipboard("Is this happening on the main computer, or a secondary/workstation computer?")).pack()
Button(f3, text= "File Explorer?", command=lambda: copyToClipboard("Do you know how to pull up a File Explorer in Windows?")).pack()
Button(f3, text= "Devices and Printers?", command=lambda: copyToClipboard("Do you know how to pull up your Devices and Printers menu in Windows?")).pack(pady = 1.5)
Button(f3, text= "Printer Model?", command=lambda: copyToClipboard("What model of printer are you trying to print to?")).pack(pady = 1.5)
Button(f3, text= "Check Oki Driver", command=lambda: copyToClipboard("Right click on your Okidata printer, then on Printer Properties. Click on the Advanced tab, and tell me what is listed as a driver, please.")).pack(pady = 1.5)
Button(f3, text= "Okidata/Generic 9pin", command=lambda: copyToClipboard("Do you see Generic IBM Graphics 9pin, or Okidata ML 320 Turbo/D (IBM) listed here?")).pack(pady = 1.5)
Button(f3, text= "Windows10?", command=lambda: copyToClipboard("Do you happen to run Windows 10 on your main computer?")).pack(pady = 1.5)
Button(f3, text= "What OS?", command=lambda: copyToClipboard("This webpage will guide you through finding out which operating system your main computer is using: https://support.microsoft.com/en-us/help/13443/windows-which-operating-system")).pack(pady = 1.5)
Button(f3, text= "Network/Sharing?", command=lambda: copyToClipboard('Do you how to get to your "Advanced sharing settings" menu on your main computer?')).pack(pady = 1.5)

# common gnotes
Button(f5, bg= "orange", text="PW/Sharing - w/s + main", command=lambda: copyToClipboard("w/s '' down with moogly. connected up to see that w/s to see network/sharing and all that looked good. tried to navigate to main computer over the network, but then got prompted for network credentials - generic/default windows ones didn't work. connected up to main computer, '', and turned off password protected sharing. frazer pulls up fine on the w/s now. all set.")).pack()
Button(f5, bg= "orange", text="PW/Sharing - main ONLY", command=lambda: copyToClipboard("w/s down with moogly. connected up to main computer, '', and turned off password protected sharing. frazer pulls up fine on the w/s now. all set.")).pack()
Button(f5, bg= "orange", text="PW/Sharing - talk", command=lambda: copyToClipboard("w/s down with moogly, but Frazer on main is up and running fine. talked him ** her through turning off PW protected sharing, which was the fix. all set.")).pack(pady = 1.5)
Button(f5, bg= "yellow", text="Oki driver - connect", command=lambda: copyToClipboard("not able to print to okidata from Frazer on ''. connected up and switched from ESC to Okidata ML 320 Turbo/D (IBM) ** generic 9pin driver. prints just fine now. all set.")).pack(pady = 1.5)
Button(f5, bg= "yellow", text="Oki driver - talk", command=lambda: copyToClipboard("okidata not printing from frazer. talked him ** her through switching from ESC to Generic IBM Graphics 9pin ** Okidata ML 320 Turbo/D (IBM), which was the fix. all set.")).pack(pady = 1.5)
Button(f5, bg= "yellow", text="Oki driver - VU", command=lambda: copyToClipboard("okidata not printing from frazer. asked him ** her to run VU, verify printer selection in M-0, then try to print again. all set.")).pack(pady = 1.5)
Button(f5, bg= "tomato2", text="Server xfer", command=lambda: copyToClipboard("server xfer from '' to ''. verified C-1 and V-1, photos to restore, set main to never sleep, ran online backup, ***w/s***. all set.")).pack(pady = 1.5)
Button(f5, bg= "tomato2", text="network w/s", command=lambda: copyToClipboard("connected up to and networked '' with client. all set.")).pack(pady = 1.5)
Button(f5, text= "Dead?", command=lambda: copyToClipboard("went AFK/DC'd without saying anything. all set.")).pack(anchor= E, pady = 1.5)

# stall
Button(f6, bg= "pale green", text="One moment, please.", command=lambda: copyToClipboard("One moment, please.")).pack(pady = 1.5)

def test(reportCode):
	status.set("")
	if selection.get() == 0:
		status.set(reportCode)
		return
	else:
		status.set(prefix.get() + reportCode)
		return
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
	"""
def r_1_1():
	r11Text = "Reports, 1 - Vehicle Inventory Reports, then 1 - Price List. "
	status.set("")	
	if selection.get() == 0:
		status.set(r11Text)
	else:
		status.set(prefix.get() + r11Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
"""
def r_1_2():
	r12Text = "Reports, 1 - Vehicle Inventory Reports, then 2 - Inventory Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r12Text)
	else:
		status.set(prefix.get() + r12Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_3():
	r13Text = "Reports, 1 - Vehicle Inventory Reports, then 3 - List of Vehicles Purchased. "
	status.set("")	
	if selection.get() == 0:
		status.set(r13Text)
	else:
		status.set(prefix.get() + r13Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_1_4():
	r14Text = "Reports, 1 - Vehicle Inventory Reports, then 4 - Vehicle Tracking Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r14Text)
	else:
		status.set(prefix.get() + r14Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_1_5():
	r15Text = "Reports, 1 - Vehicle Inventory Reports, then 5 - Floor Planning. "
	status.set("")	
	if selection.get() == 0:
		status.set(r15Text)
	else:
		status.set(prefix.get() + r15Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_1_6():
	r16Text = "Reports, 1 - Vehicle Inventory Reports, then 6 - Inventory Valuation and Status. "
	status.set("")	
	if selection.get() == 0:
		status.set(r16Text)
	else:
		status.set(prefix.get() + r16Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_1_7():
	r17Text = "Reports, 1 - Vehicle Inventory Reports, then 7 - Cars on Lot Evaluation. "
	status.set("")	
	if selection.get() == 0:
		status.set(r17Text)
	else:
		status.set(prefix.get() + r17Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_8():
	r18Text = "Reports, 1 - Vehicle Inventory Reports, then 8 - No Duplicate Keys. "
	status.set("")	
	if selection.get() == 0:
		status.set(r18Text)
	else:
		status.set(prefix.get() + r18Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_9():
	r19Text = "Reports, 1 - Vehicle Inventory Reports, then 9 - Draft Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r19Text)
	else:
		status.set(prefix.get() + r19Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_0():
	r10Text = "Reports, 1 - Vehicle Inventory Reports, then 0 - Added Costs Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r10Text)
	else:
		status.set(prefix.get() + r10Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_a():
	r1aText = "Reports, 1 - Vehicle Inventory Reports, then A - Added Costs Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1aText)
	else:
		status.set(prefix.get() + r1aText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_b():
	r1bText = "Reports, 1 - Vehicle Inventory Reports, then B - Added Costs Vendor Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1bText)
	else:
		status.set(prefix.get() + r1bText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_c():
	r1cText = "Reports, 1 - Vehicle Inventory Reports, then C - Titles Received/Not Yet Received. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1cText)
	else:
		status.set(prefix.get() + r1cText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_d():
	r1dText = "Reports, 1 - Vehicle Inventory Reports, then D - Vehicle Inspections. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1dText)
	else:
		status.set(prefix.get() + r1dText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_e():
	r1eText = "Reports, 1 - Vehicle Inventory Reports, then E - Vehicle Vendor Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1eText)
	else:
		status.set(prefix.get() + r1eText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_f():
	r1fText = "Reports, 1 - Vehicle Inventory Reports, then F - Vehicle Notes. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1fText)
	else:
		status.set(prefix.get() + r1fText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_g():
	r1gText = "Reports, 1 - Vehicle Inventory Reports, then G - Trade-In Payoffs. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1gText)
	else:
		status.set(prefix.get() + r1gText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_1_h():
	r1hText = "Reports, 1 - Vehicle Inventory Reports, then H - Vehicle Activity Log. "
	status.set("")	
	if selection.get() == 0:
		status.set(r1hText)
	else:
		status.set(prefix.get() + r1hText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_1():
	r21Text = "Reports, 2 - Sale Reporting, then 1 - Sales Totals. "
	status.set("")	
	if selection.get() == 0:
		status.set(r21Text)
	else:
		status.set(prefix.get() + r21Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_2():
	r22Text = "Reports, 2 - Sale Reporting, then 2 - Sales Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r22Text)
	else:
		status.set(prefix.get() + r22Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_3():
	r23Text = "Reports, 2 - Sale Reporting, then 3 - Back End Sales Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r23Text)
	else:
		status.set(prefix.get() + r23Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_4():
	r24Text = "Reports, 2 - Sale Reporting, then 4 - Sales Tax Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r24Text)
	else:
		status.set(prefix.get() + r24Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_5():
	r25Text = "Reports, 2 - Sale Reporting, then 5 - Cash Position Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r25Text)
	else:
		status.set(prefix.get() + r25Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_6():
	r26Text = "Reports, 2 - Sale Reporting, then 6 - Special Tax Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r26Text)
	else:
		status.set(prefix.get() + r26Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_7():
	r27Text = "Reports, 2 - Sale Reporting, then 7 - Salesman Reporting. "
	status.set("")	
	if selection.get() == 0:
		status.set(r27Text)
	else:
		status.set(prefix.get() + r27Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_8():
	r28Text = "Reports, 2 - Sale Reporting, then 8 - Vehicle Evaluations by Profitability. "
	status.set("")	
	if selection.get() == 0:
		status.set(r28Text)
	else:
		status.set(prefix.get() + r28Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_9():
	r29Text = "Reports, 2 - Sale Reporting, then 9 - Lien Holder Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r29Text)
	else:
		status.set(prefix.get() + r29Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_0():
	r20Text = "Reports, 2 - Sale Reporting, then 0 - Zip Code Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r20Text)
	else:
		status.set(prefix.get() + r20Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_a():
	r2aText = "Reports, 2 - Sale Reporting, then A - IRS/FinCEN Form 8300. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2aText)
	else:
		status.set(prefix.get() + r2aText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_b():
	r2bText = "Reports, 2 - Sale Reporting, then B - Source of Customer Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2bText)
	else:
		status.set(prefix.get() + r2bText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_c():
	r2cText = "Reports, 2 - Sale Reporting, then C - OFAC Names Checked. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2cText)
	else:
		status.set(prefix.get() + r2cText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_d():
	r2dText = "Reports, 2 - Sale Reporting, then D - Government and Dealer Service Fees. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2dText)
	else:
		status.set(prefix.get() + r2dText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_e():
	r2eText = "Reports, 2 - Sale Reporting, then E - Temporary Tag Log. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2eText)
	else:
		status.set(prefix.get() + r2eText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_f():
	r2fText = "Reports, 2 - Sale Reporting, then F - Static Pool Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2fText)
	else:
		status.set(prefix.get() + r2fText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_g():
	r2gText = "Reports, 2 - Sale Reporting, then G - Purchased Account Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2gText)
	else:
		status.set(prefix.get() + r2gText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_2_h():
	r2hText = "Reports, 2 - Sale Reporting, then H - Deposit Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2hText)
	else:
		status.set(prefix.get() + r2hText)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_2_i():
	r2iText = "Reports, 2 - Sales Reporting, then I - Prospect Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r2iText)
	else:
		status.set(prefix.get() + r2iText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_1():
	r31Text = "Reports, 3 - Customer Reporting, then 1 - Current or Past Due Customers. "
	status.set("")	
	if selection.get() == 0:
		status.set(r31Text)
	else:
		status.set(prefix.get() + r31Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_3_2():
	r32Text = "Reports, 3 - Customer Reporting, then 2 - Customer Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r32Text)
	else:
		status.set(prefix.get() + r32Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_3():
	r33Text = "Reports, 3 - Customer Reporting, then 3 - Accounts Receivable Balances. "
	status.set("")	
	if selection.get() == 0:
		status.set(r33Text)
	else:
		status.set(prefix.get() + r33Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_4():
	r34Text = "Reports, 3 - Customer Reporting, then 4 - Transaction Totals. "
	status.set("")	
	if selection.get() == 0:
		status.set(r34Text)
	else:
		status.set(prefix.get() + r34Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_5():
	r35Text = "Reports, 3 - Customer Reporting, then 5 - Transaction Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r35Text)
	else:
		status.set(prefix.get() + r35Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_6():
	r36Text = "Reports, 3 - Customer Reporting, then 6 - Projected Collections. "
	status.set("")	
	if selection.get() == 0:
		status.set(r36Text)
	else:
		status.set(prefix.get() + r36Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_7():
	r37Text = 'Reports, 3 Customer Reporting, 7 - Reports on "Tracking".'
	status.set("")	
	if selection.get() == 0:
		status.set(r37Text)
	else:
		status.set(prefix.get() + r37Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_8():
	r38Text = "Reports, 3 - Customer Reporting, then 8 - Insurance Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r38Text)
	else:
		status.set(prefix.get() + r38Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_9():
	r39Text = "Reports, 3 - Customer Reporting, then 9 - Pick-Up Notes Owed. "
	status.set("")	
	if selection.get() == 0:
		status.set(r39Text)
	else:
		status.set(prefix.get() + r39Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_3_0():
	r30Text = "Reports, 3 - Customer Reporting, then 0 - Repair Billings Owed. "
	status.set("")	
	if selection.get() == 0:
		status.set(r30Text)
	else:
		status.set(prefix.get() + r30Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_3_a():
	r3aText = "Reports, 3 - Customer Reporting, then A - Other Receivables Owed. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3aText)
	else:
		status.set(prefix.get() + r3aText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_b():
	r39Text = "Reports, 3 - Customer Reporting, then B - Repossession Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r39Text)
	else:
		status.set(prefix.get() + r39Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_c():
	r3cText = "Reports, 3 - Customer Reporting, then C - Interest Received. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3cText)
	else:
		status.set(prefix.get() + r3cText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_d():
	r3dText = "Reports, 3 - Customer Reporting, then D - Customer Spread Sheet. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3dText)
	else:
		status.set(prefix.get() + r3dText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_e():
	r3eText = "Reports, 3 - Customer Reporting, then E - Low Balances & Paid Outs. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3eText)
	else:
		status.set(prefix.get() + r3eText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_f():
	r3fText = "Reports, 3 - Customer Reporting, then F - Payment Schedule Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3fText)
	else:
		status.set(prefix.get() + r3fText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_g():
	r3gText = "Reports, 3 - Customer Reporting, then G - Down Payment Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3gText)
	else:
		status.set(prefix.get() + r3gText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_h():
	r3hText = "Reports, 3 - Customer Reporting, then H - Write-Off Analysis. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3hText)
	else:
		status.set(prefix.get() + r3hText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_j():
	r3jText = "Reports, 3 - Customer Reporting, then J - Birthday Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3jText)
	else:
		status.set(prefix.get() + r3jText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_k():
	r3kText = "Reports, 3 - Customer Reporting, then K - Released Starter Interrupt Codes. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3kText)
	else:
		status.set(prefix.get() + r3kText)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_3_L():
	r3LText = "Reports, 3 - Customer Reporting, then L - Contracts in Transit. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3LText)
	else:
		status.set(prefix.get() + r3LText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_m():
	r3mText = "Reports, 3 - Customer Reporting, then M - Electronic Payment Log. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3mText)
	else:
		status.set(prefix.get() + r3mText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_n():
	r3nText = "Reports, 3 - Customer Reporting, then N - Recurring Payments Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3nText)
	else:
		status.set(prefix.get() + r3nText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_p():
	r3pText = "Reports, 3 - Customer Reporting, then P - Recency Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3pText)
	else:
		status.set(prefix.get() + r3pText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_q():
	r3qText = "Reports, 3 - Customer Reporting, then Q - Unearned Interest Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3qText)
	else:
		status.set(prefix.get() + r3qText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_r():
	r3rText = "Reports, 3 - Customer Reporting, then R - Special Message Report. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3rText)
	else:
		status.set(prefix.get() + r3rText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_3_s():
	r3sText = "Reports, 3 - Customer Reporting, then S - Sales of Receivables. "
	status.set("")	
	if selection.get() == 0:
		status.set(r3sText)
	else:
		status.set(prefix.get() + r3sText)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_4_1():
	r41Text = "Reports, 4 - Accounting, then 1 - Financial Statements. "
	status.set("")	
	if selection.get() == 0:
		status.set(r41Text)
	else:
		status.set(prefix.get() + r41Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())
	
def r_4_2():
	r42Text = "Reports, 4 - Accounting, then 2 - G/L Listings. "
	status.set("")	
	if selection.get() == 0:
		status.set(r42Text)
	else:
		status.set(prefix.get() + r42Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())	
	
def r_4_3():
	r43Text = "Reports, 4 - Accounting, then 3 - Transaction Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r43Text)
	else:
		status.set(prefix.get() + r43Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())	
	
def r_4_4():
	r44Text = "Reports, 4 - Accounting, then 4 - Year End Reports. "
	status.set("")	
	if selection.get() == 0:
		status.set(r44Text)
	else:
		status.set(prefix.get() + r44Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())

def r_4_5():
	r45Text = "Reports, 4 - Accounting, then 5 - Change In Receivables. "
	status.set("")	
	if selection.get() == 0:
		status.set(r45Text)
	else:
		status.set(prefix.get() + r45Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())	

def r_4_6():
	r46Text = "Reports, 4 - Accounting, then 6 - Vendor Cost Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r46Text)
	else:
		status.set(prefix.get() + r46Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())	

def r_4_7():
	r47Text = "Reports, 4 - Accounting, then 7 - Bank Deposit Listing. "
	status.set("")	
	if selection.get() == 0:
		status.set(r47Text)
	else:
		status.set(prefix.get() + r47Text)
	root.clipboard_clear()
	root.clipboard_append(status.get())	
	
# creates Vehicles pulldown menu
vehicles = Menu(menuBar, tearoff=0)
vehicles.add_command(label="1 - Vehicle Files")
vehicles.add_command(label="2 - Added Costs")
vehicles.add_command(label="3 - Print Buyers Guide")
vehicles.add_command(label="4 - Floor Plan Companies")
vehicles.add_command(label="5 - Vendors")
vehicles.add_command(label="6 - Buyers")
vehicles.add_command(label="7 - Vehicle Types")
vehicles.add_command(label="8 - Vehicle Uploads")
vehicles.add_command(label="9 - NADA Value Guide")
vehicles.add_command(label="A - Import Vehicle")
vehicles.add_command(label="B - Kelley Blue Book")
menuBar.add_cascade(label="Vehicles", menu=vehicles)

# creates Sales pulldown menu
sales = Menu(menuBar, tearoff=0)
sales.add_command(label="1 - Enter Sales")
sales.add_command(label="2 - Print Payment Coupons")
sales.add_command(label="3 - Amortization Schedule")
sales.add_command(label="4 - Sales Recap")
sales.add_command(label="5 - Lien Holders")
sales.add_command(label="6 - Calculate Commissions")
sales.add_command(label="7 - Add Pre-Existing Customers")
sales.add_command(label="8 - OFAC's SDN List (Terrorist List)")
sales.add_command(label="9 - Salesman")
sales.add_command(label="A - Deposits")
sales.add_command(label="B - Prospects")
sales.add_command(label="C - Service Contract Providers")
sales.add_command(label="D - Insurance Providers")
sales.add_command(label='E - "Other Fees #1" Providers')
sales.add_command(label='F - "Other Fees #2" Providers')
sales.add_command(label='G - "Other Fees #3" Providers')
sales.add_command(label="H - RouteOne Import")
menuBar.add_cascade(label="Sales", menu=sales)

# creates Customer pulldown menu
customers = Menu(menuBar, tearoff=0)
customers.add_command(label="1 - Customer Activity")
customers.add_command(label="2 - Letters and Labels")
customers.add_command(label="3 - Sale of Receivables")
customers.add_command(label="4 - Generate Late Fees")
customers.add_command(label="5 - Report to Credit Bureau")
customers.add_command(label="6 - Customer Refinancing")
customers.add_command(label="7 - Electronic Payments")
customers.add_command(label="8 - Upload to Finance Company")
menuBar.add_cascade(label="Customers", menu=customers)

# creates Accounting pulldown menu
accounting = Menu(menuBar, tearoff=0)

# creates Accounting, F - Helpful Accounting Tools menu
a_f = Menu(accounting, tearoff=0)
a_f.add_command(label="1 - Was that amount posted?")
a_f.add_command(label="2 - Getting Started With Accounting")
accounting.add_command(label="A - Enter Bills and Hand Printed Checks")
accounting.add_command(label="B - Print Checks or Change and Review Open Bills")
accounting.add_command(label="C - Review Payments and other changes to Cash in Bank")
accounting.add_command(label="D - Record Bank Deposit")
accounting.add_command(label="E - Bank Reconciliation")
accounting.add_cascade(label="F - Helpful Accounting Tools", menu=a_f)
accounting.add_separator()
accounting.add_command(label="1 - Post to General Ledger")
accounting.add_command(label="2 - Change / Delete Previous Postings")
accounting.add_command(label="3 - Chart of Accounts")
accounting.add_command(label="4 - Journals")
accounting.add_command(label="5 - Transfer Data to Quickbooks")
accounting.add_command(label="6 - Vendors")
accounting.add_command(label="7 - Departments")
accounting.add_separator()
accounting.add_command(label="T - Financial Statements")
accounting.add_command(label="U - G/L Listings")
accounting.add_command(label="V - Transaction Listings")
accounting.add_command(label="W - Year End Reports")
accounting.add_command(label="X - Change in Receivables")
accounting.add_command(label="Y - Vendor Cost Listing")
menuBar.add_cascade(label="Accounting", menu=accounting)

# creates Reports pulldown menu
reports = Menu(menuBar, tearoff=0)

# creates Reports, 1 - Vehicle Inventory Reports pulldown menu
r_1 = Menu(reports, tearoff=0)
r_2 = Menu(reports, tearoff=0)
r_3 = Menu(reports, tearoff=0)
r_4 = Menu(reports, tearoff=0)
r_1.add_command(label="1 - Price List", command= test(r_1_1))
r_1.add_command(label="2 - Inventory Listings", command= r_1_2)
r_1.add_command(label="3 - List of Vehicles Purchased", command= r_1_3)
r_1.add_command(label="4 - Vehicle Tracking Report", command= r_1_4)
r_1.add_command(label="5 - Floor Planning", command= r_1_5)
r_1.add_command(label="6 - Inventory Valuation & Status", command= r_1_6)
r_1.add_command(label="7 - Cars on Lot Evaluation", command= r_1_7)
r_1.add_command(label="8 - No Duplicate Keys", command= r_1_8)
r_1.add_command(label="9 - Draft Listings", command= r_1_9)
r_1.add_command(label="0 - Added Costs Listings", command= r_1_0)
r_1.add_command(label="A - Added Costs Analysis", command= r_1_a)
r_1.add_command(label="B - Added Costs Vendor Analysis", command= r_1_b)
r_1.add_command(label="C - Titles Received/Not Yet Received", command= r_1_c)
r_1.add_command(label="D - Vehicle Inspection", command= r_1_d)
r_1.add_command(label="E - Vehicle Vendor Analysis", command= r_1_e)
r_1.add_command(label="F - Vehicle Notes", command= r_1_f)
r_1.add_command(label="G - Trade-In Payoffs", command= r_1_g)
r_1.add_command(label="H - Vehicle Activity Log", command= r_1_h)

r_2.add_command(label="1 - Sales Totals", command=r_2_1)
r_2.add_command(label="2 - Sales Listings", command=r_2_2)
r_2.add_command(label="3 - Back End Sales Listings", command=r_2_3)
r_2.add_command(label="4 - Sales Tax Report", command=r_2_4)
r_2.add_command(label="5 - Cash Position Analysis", command=r_2_5)
r_2.add_command(label="6 - Special Tax Report", command=r_2_6)
r_2.add_command(label="7 - Salesman Reporting", command=r_2_7)
r_2.add_command(label="8 - Vehicle Evaluation by Profitability", command=r_2_8)
r_2.add_command(label="9 - Lien Holder Analysis", command=r_2_9)
r_2.add_command(label="0 - Zip Code Analysis", command=r_2_0)
r_2.add_command(label="A - IRS/FinCEN Form 8300", command=r_2_a)
r_2.add_command(label="B - Source of Customer Analysis", command=r_2_b)
r_2.add_command(label="C - OFAC Names Checked", command=r_2_c)
r_2.add_command(label="D - Government and Dealer Service Fees", command=r_2_d)
r_2.add_command(label="E - Temporary Tag Log", command=r_2_e)
r_2.add_command(label="F - Static Pool Analysis", command=r_2_f)
r_2.add_command(label="G - Purchased Account Listing", command=r_2_g)
r_2.add_command(label="H - Deposit Listing", command=r_2_h)
r_2.add_command(label="I - Prospect Report", command=r_2_i)
r_3.add_command(label="1 - Past Due or Current Due Customers", command=r_3_1)
r_3.add_command(label="2 - Customer Listings", command=r_3_2)
r_3.add_command(label="3 - Accounts Receivable Balances", command=r_3_3)
r_3.add_command(label="4 - Transaction Totals", command=r_3_4)
r_3.add_command(label="5 - Transaction Listings", command=r_3_5)
r_3.add_command(label="6 - Projected Collections", command=r_3_6)
r_3.add_command(label='7 - Reports on "Tracking"', command=r_3_7)
r_3.add_command(label="8 - Insurance Reports", command=r_3_8)
r_3.add_command(label="9 - Pick-Up Notes Owed", command=r_3_9)
r_3.add_command(label="0 - Repair Billings Owed", command=r_3_0)
r_3.add_command(label="A - Other Receivables Owed", command=r_3_a)
r_3.add_command(label="B - Repossession Listings", command=r_3_b)
r_3.add_command(label="C - Interest Received", command=r_3_c)
r_3.add_command(label="D - Customer Spread Sheet", command=r_3_d)
r_3.add_command(label="E - Low Balances & Paid Outs", command=r_3_e)
r_3.add_command(label="F - Payment Schedule Analysis", command=r_3_f)
r_3.add_command(label="G - Down Payment Analysis", command=r_3_g)
r_3.add_command(label="H - Write-Off Analysis", command=r_3_h)
r_3.add_command(label="J - Birthday Listing", command=r_3_j)
r_3.add_command(label="K - Released Starter Interrupt Codes", command=r_3_k)
r_3.add_command(label="L - Contracts in Transit", command=r_3_L)
r_3.add_command(label="M - Electronic Payment Log", command=r_3_m)
r_3.add_command(label="N - Recurring Payments Listing", command=r_3_n)
r_3.add_command(label="P - Recency Report", command=r_3_p)
r_3.add_command(label="Q - Unearned Interest Report", command=r_3_q)
r_3.add_command(label="R - Special Message Report", command=r_3_r)
r_3.add_command(label="S - Sales of Receivables", command=r_3_s)
r_4.add_command(label="1 - Financial Statements", command=r_4_1)
r_4.add_command(label="2 - G/L Listings", command=r_4_2)
r_4.add_command(label="3 - Transaction Listing", command=r_4_3)
r_4.add_command(label="4 - Year End Reports", command=r_4_4)
r_4.add_command(label="5 - Change in Receivables", command=r_4_5)
r_4.add_command(label="6 - Vendor Cost Listing", command=r_4_6)
r_4.add_command(label="7 - Bank Deposit Listing", command=r_4_7)

reports.add_cascade(label="1 - Vehicle Inventory Reports", menu=r_1)
reports.add_cascade(label="2 - Sales Reporting", menu=r_2)
reports.add_cascade(label="3 - Customer Reporting", menu=r_3)
reports.add_cascade(label="4 - Accounting", menu=r_4)
menuBar.add_cascade(label="Reports", menu=reports)

# creates Miscellaneous pulldown menu
miscellaneous = Menu(menuBar, tearoff=0)
miscellaneous.add_command(label="1 - System Options")
miscellaneous.add_command(label="2 - Life/Disability Rates")
miscellaneous.add_command(label="3 - Password System")
miscellaneous.add_command(label="4 - Audit File Reporting")
miscellaneous.add_command(label="5 - Miscellaneous Receipts")
miscellaneous.add_command(label="6 - Change Seller's Name on Receipts")
miscellaneous.add_command(label="7 - Miscellaneous Contacts")
miscellaneous.add_command(label="8 - Export Data")
miscellaneous.add_command(label="9 - Pulled Credit Reports")
miscellaneous.add_command(label="0 - Printer Setup")
menuBar.add_cascade(label="Miscellaneous", menu=miscellaneous)

# creates Help pulldown menu
help = Menu(menuBar, tearoff=0)
help.add_command(label="1 - Help Manual")
help.add_command(label="2 - Video Tutorials")
help.add_separator()
help.add_command(label="3 - Contact Frazer")
help.add_command(label="4 - About Frazer")
help.add_separator()
help.add_command(label="5 - File Manager")
help.add_separator()
help.add_command(label="6 - Pay For Frazer")
help.add_separator()
help.add_command(label="7 - Frazer Help Desks")
menuBar.add_cascade(label="Help", menu=help)

# creates Backup pulldown menu
backup = Menu(menuBar, tearoff=0)
backup.add_command(label="1 - Backup")
backup.add_command(label="2 - Backup History")
menuBar.add_cascade(label="Backup", menu=backup)

update = Menu(menuBar, tearoff=0)
menuBar.add_command(label="Update")

messages = Menu(menuBar, tearoff=0)
menuBar.add_command(label="Messages")

# leftFrame.pack(anchor= NW, expand= NO)
# middleFrame.pack(anchor= N)
# rightFrame.pack(anchor= E)
statusBar.pack(anchor=W, side= BOTTOM, fill= X)

# adds menuBar to top of root
root.config(menu=menuBar)
root.mainloop()