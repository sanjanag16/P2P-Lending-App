from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form, server
from ...lendor_registration_form.dashboard import lendor_main_form_module as main_form_module



class wallet(walletTemplate):
  def __init__(self, **properties):
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.deposit_placeholder = "5000"
    self.withdraw_placeholder = "0.00"
    
    # self.email=main_form_module.email
    # wallet=app_tables.wallet.get(user_email=self.email)
    # if wallet:
    #   self.amount_text_box.text=wallet['e_wallet']
      

    # self.user_id = main_form_module.userId
    # user_id = self.user_id
    
    # ### Fetch user details from user_profile database
    # user_profiles = app_tables.user_profile.search()  

    # # Mapping and inserting data into the wallet table
    # for profile in user_profiles:
    #   print(f"Adding row for customer ID: {profile['customer_id']}")
    # # Add similar print statements for other column values

    # wallet_row = app_tables.wallet.add_row(
    #     customer_id=profile['customer_id'],
    #     user_name=profile['full_name'],
    #     user_email=profile['email_user'],
    #     user_type=profile['usertype']
    # )
    # print("Row added successfully")


  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_contact")

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.dashboard.notification')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def deposit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = False
    self.text_box_5.visible = False
    self.icon1.visible = False
    self.amount_text_box.placeholder = self.deposit_placeholder
    self.deposit_money_btn.visible = True
    self.withdraw_money_btn.visible = False


  def withdraw_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_9.visible = True
    self.text_box_5.visible = True
    self.icon1.visible = True
    self.amount_text_box.placeholder = self.withdraw_placeholder
    self.deposit_money_btn.visible = False
    self.withdraw_money_btn.visible = True
    self.deposit_btn.visible = True

  def wallet_dashboard_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def deposit_money_btn_click(self, **event_args):
    amount_entered = self.amount_text_box.text
    
    # Ensure the amount entered is numeric (you may add additional validation if required)
    try:
        deposit_amount = float(amount_entered)
    except ValueError:
        
        return  

    customer_id = 1000 
    
    # Call the server function to deposit money
    if anvil.server.call('deposit_money', customer_id, deposit_amount):
        alert("Deposit successful!")
    else:
        alert("Deposit failed!")

  def withdraw_money_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    amount_entered = self.amount_text_box.text
    
    # Ensure the amount entered is numeric (you may add additional validation if required)
    try:
        withdraw_amount = float(amount_entered)
    except ValueError:
        # Handle the case where the entered amount is not a valid number
        return 

    customer_id = 1000 
    
    # Call the server function to withdraw money
    if anvil.server.call('withdraw_money', customer_id, withdraw_amount):
        alert("Withdrawal successful!")
    else:
        alert("Withdrawal failed!")

   
 