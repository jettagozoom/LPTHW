#! /usr/local/bin/python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", help="Cost of meal")
parser.add_option("-t", "--tax", dest="tax", help="Food tax rate")
parser.add_option("-p", "--tip", dest="tip", help="Food tip rate", default="15")

(options,args) = parser.parse_args()

if (not options.meal or not options.tax):
	parser.error("You need to supply a value for the cost and the tax of the meal: -m -t")

meal = float(options.meal)
tax = float(options.tax)
tip = float(options.tip)

tax_value = meal * (tax / 100.0)
meal_with_tax = meal +  tax_value
tip_value = meal_with_tax * (tip / 100.0)

total = meal_with_tax + tip_value

print "The cost of the meal is $%.2f" % meal
print "The tax on the meal is $%.2f" % tax_value
print "The tip on the meal is $%.2f" % tip_value
print "The total bill for the meal is $%.2f" % total
