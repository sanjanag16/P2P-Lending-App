from ._anvil_designer import check_out_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import borrower_main_form_module as main_form_module
from anvil import app as anvil_app
class check_out_form(check_out_formTemplate):
  def __init__(self, product_group, product_cat,loan_amount, tenure, **properties):
        self.proctct_g = product_group
        self.prodct_cate = product_cat
        self.loan_amount = loan_amount
        self.tenure = tenure
    
    
        self.init_components(**properties)
        # loan_details = anvil_app.tables.loan_details.search(borrower_customer_id=user_id)
        # if loan_details:
        #   self.label_2.text = f"['loan_amount']"
        #   self.label_6.text = f"['tenure']"
        # else:
        #   self.label_2.text = f"None"
        #   self.label_6.text = f"None"
        user_request = app_tables.product_details.get(product_categories=self.prodct_cate)
        if user_request:
            self.roi = user_request['roi']
        self.label_2.text = self.loan_amount
        self.label_6.text = self.tenure
        p = int(self.loan_amount)
        t = int(self.tenure)
        r = (self.roi/10/12)*t
        interest_amount = (p*r*t)/100
        self.label_8.text = interest_amount
        Total_Repayment_Amount = p+interest_amount
        self.label_12.text = Total_Repayment_Amount

         
  def submit_click(self, **event_args):
      alert('your request is submitted')
      open_form('bank_users.borrower_dashboard.choose_lender')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard.new_loan_request')

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('bank_users.borrower_dashboard')

  
  def fetch_product_data(self):
        return app_tables.product_details.search(
            product_name=self.proctct_g,
            product_categories=self.prodct_cate
        )

  def display_label_text(self, label, column_name):
        product_data = self.fetch_product_data()
        if product_data:
            label_text = [str(data[column_name]) for data in product_data]
            label.text = label_text[0] if label_text else None

  def label_4_show(self, **event_args):
    self.display_label_text(self.label_4, 'roi')


# def label_2_show(self, **event_args):
#     borrower_customer_id = self.borrower_customer_id
#     loan_amount = anvil.server.call('add_loan_details', borrower_customer_id)
#     if loan_amount is not None:
#         self.label_2.text = f"Loan Amount: {loan_amount}"
#     else:
#         self.label_2.text = "Loan Amount not available"

  # def label_2_show(self, **event_args):
  #   self.display_label_text(self.label_2,self.loan_amount)

  # def label_6_show(self, **event_args):
  #   self.display_label_text(self.label_6,self.tenure)


