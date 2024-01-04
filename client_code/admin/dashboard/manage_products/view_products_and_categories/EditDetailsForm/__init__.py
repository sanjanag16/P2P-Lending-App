from ._anvil_designer import EditDetailsFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert

class EditDetailsForm(EditDetailsFormTemplate):
    def __init__(self, selected_row, **properties):
        self.init_components(**properties)

        # Set the initial values for the input components
        self.text_box_1.text = selected_row['name']
        #self.text_box_2.text = selected_row['name_categories']
        
        # Store the selected row for later use
        self.selected_row = selected_row

    def button_1_click(self, **event_args):
        """Save changes button click event"""
        # Get the updated value from the input component
        updated_group = self.text_box_1.text.lower()  # Convert to lowercase

        # Check if the updated value is the same as the existing value
        if updated_group != self.selected_row['name'].lower():
            # Convert the existing group names to lowercase for case-insensitive comparison
            existing_names_lower = [row['name'].lower() for row in app_tables.product_group.search()]
            
            if updated_group in existing_names_lower:
                alert(f'Group "{self.text_box_1.text}" already exists. Please choose a different name.')
            else:
                # Update the existing row in the product_categories table
                self.selected_row['name'] = updated_group

                # Save changes to the database
                self.selected_row.update()

                alert("Changes saved successfully!")
                open_form('admin.dashboard.manage_products.view_products_and_categories')

        else:
            # No changes were made
            alert("No changes made.")
            open_form('admin.dashboard.manage_products.view_products_and_categories')
          
    def button_2_click(self, **event_args):
        """Cancel button click event"""
        # Close the form without saving changes
        open_form('admin.dashboard.manage_products.view_products_and_categories')
