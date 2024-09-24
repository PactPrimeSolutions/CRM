import pandas as pd
import os
from django.core.management.base import BaseCommand
from myapp.models import State, County

class Command(BaseCommand):
    help = "Load states and counties from an Excel sheet"

    def handle(self, *args, **kwargs):
        # Define the absolute path to the Excel file
        excel_path = 'G:/admin_02_09_15/US_State_and_County_Details_1.xlsx'

        # Print the absolute path for debugging
        self.stdout.write(f"Excel file path: {excel_path}")

        if not os.path.exists(excel_path):
            self.stdout.write(self.style.ERROR(f'File not found: {excel_path}'))
            return

        # Load the Excel file
        try:
            df = pd.read_excel(excel_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading Excel file: {e}'))
            return

        for _, row in df.iterrows():
            # Create or get the State
            state, _ = State.objects.get_or_create(name=row['State'])

            # Create the County
            County.objects.get_or_create(name=row['County'], state=state)

        self.stdout.write(self.style.SUCCESS('States and counties loaded successfully.'))
