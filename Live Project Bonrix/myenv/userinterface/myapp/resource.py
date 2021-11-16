from import_export import resources
from .models import ExpenseCategory, IncomeCategory, Members_Vendor_Account,Income_Expense_LedgerValue


class ExpenseResource(resources.ModelResource):
    class Meta:
        model = ExpenseCategory


class IncomeResource(resources.ModelResource):
    class Meta:
        model = IncomeCategory


class Members_VendoorsResource(resources.ModelResource):
    class Meta:
        model = Members_Vendor_Account

class Income_Expense_LedgerResource(resources.ModelResource):
    class Meta:
        model = Income_Expense_LedgerValue
