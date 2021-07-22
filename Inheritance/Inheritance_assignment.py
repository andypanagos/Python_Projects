
# Creating Parent class "Customer"
class Customer:
    name: ' '
    membership_number: 0
    email: ' '
    mailing_address: ' '
    mailing_list = True

# Creating Child class "Standard_Subscription"
class Standard_Subscription(Customer):
    weekly_email_list = True 
    standard_access = True
    standard_sub_price: 10.00
    
# Creating 2nd Child class "Premium_Subscription"
class Premium_Subscription(Customer):
    Premium_number: 0
    Premium_access = True
    daily_email_list = True
    weekly_email_list = True
    monthly_email_list = True
    Premium_sub_price: 20.00
    
