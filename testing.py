customer = {'Address': 'Hawai', 'Distance': 358,'refund':50}
#printing using Index
print(customer["Address"])

#printing using get
print('Address: ', customer.get('Address'))
print('Distance: ', customer.get('Distance'))

# Key is absent in the list
print('Amount: ', customer.get('Amount'))

# A value is provided for a new key
print('Amount: ', customer.get('Amount', 2050.0))

print('refund:',customer.get('refund',34.00))