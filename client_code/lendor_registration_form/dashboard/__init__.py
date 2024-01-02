from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from anvil.tables import app_tables
from anvil import open_form, server
#from anvil import get_current_user
# from bank_users.dashboard import main_form_module


class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.


  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.avlbal")

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.lender_view_loans")

  def outlined_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def outlined_button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def outlined_button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def outlined_button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def outlined_button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def outlined_button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def outlined_button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.cp")

  def login_signup_button_click(self, **event_args):
    """This method is called when the button is clicked"""

    alert("Logged out sucessfully")
    anvil.users.logout()
    open_form('bank_users.main_form')

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard")

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_about")

  def contact_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.dasboard_contact")

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def button_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  
  def toggleswitch_1_x_change(self, **event_args):
    
    if self.toggleswitch_1.checked:
      self.button_status.text = "ONLINE"
      self.button_status.background = '#0876e8'  # Green color
      self.button_status.foreground = '#FFFFFF'  # White text
      # Update 'make_visibility' column in the 'lender' table to True
      lender_row = app_tables.lender.search() # Assuming you have a row with id=1 for the lender
      lender_row[0]['make_visibility'] = True
      lender_row[0].update()
    else:
      self.button_status.text = "OFFLINE"
      self.button_status.background = '#FFFFFF'  # White color
      self.button_status.foreground = '#FF0000'  # Red text
      lender_row = app_tables.lender.search()# Assuming you have a row with id=1 for the lender
      lender_row[0]['make_visibility'] = False
      lender_row[0].update()

  def notification_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('lendor_registration_form.dashboard.notification')

  def wallet_dashboard_link_click(self, **event_args):
    customer_id = 1000  
    server.call('update_wallet_with_profile', customer_id)
    # Notify after successful data fetch and update
    notification = anvil.Notification("Fetched Data successfully!", style="success")
    notification.show()
    # Optionally, perform additional actions after updating the wallet with profile
    open_form('wallet.wallet')
  
  # def wallet_dashboard_link_click(self, **event_args):
  #       user_email = anvil.users.get_user()["email"]
  #       if user_email:
  #           profile = app_tables.user_profile.search(email_user=user_email)
  #           if profile is not None and len(profile) > 0:
  #               customer_id = profile[0]['customer_id']
  #               server.call('update_wallet_with_profile', customer_id)
  #               notification = anvil.Notification("Fetched Data successfully!", style="success")
  #               notification.show()
  #               open_form('wallet.wallet')
  #           else:
  #               print("No user profile found")
  #       else:
  #           print("User email is None")