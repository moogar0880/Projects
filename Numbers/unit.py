'''
Converts various units between one another. The user
enters the type of unit being entered, the type of
unit they want to convert to and then the value. The
program will then make the conversion.

Note: the gist of it is here but looking up the
      conversions is already getting boring
'''

temps    = ['k','c','f']
currency = ['usd','euro','yen']
volume   = ['l','oz','gal']
mass     = ['g','kg']

input_unit   = raw_input('What type of unit would you like to convert?: ')
input_value  = input('Value to be converted: ')
output_unit  = raw_input('What would you like to convert ' + input_unit + ' to?: ')
output_value = 0

if input_unit in temps and output_unit in temps:
  if input_unit == 'k':
    if output_unit == 'c':
      output_value = input_value - 273.15
    elif output_unit == 'f':
      output_value = ((input_value - 273.15)*1.8)+32
  elif input_unit == 'c':
    if output_unit == 'k':
      output_value = input_value + 273.15
    elif output_unit == 'f':
      output_value = (input_value * 1.8) + 32
  elif input_unit == 'f':
    if output_unit == 'k':
      output_value = ((input_value - 32)/1.8)+273.15
    elif output_unit == 'c':
      output_value = (input_value - 32)/1.8
elif input_unit in currency:
  pass
elif input_unit in volume:
  pass
elif input_unit in mass:
  pass
else:
  print "Input unit not recognized"

