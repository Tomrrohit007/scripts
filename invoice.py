from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice(customer_name, address, amount):
    # Create a new PDF canvas
    invoice_canvas = canvas.Canvas('invoice.pdf', pagesize=letter)

    # Set the font and font size for the invoice
    invoice_canvas.setFont('Helvetica', 12)

    # Draw the customer name
    invoice_canvas.drawString(50, 700, 'Customer Name:')
    invoice_canvas.drawString(200, 700, customer_name)

    # Draw the address
    invoice_canvas.drawString(50, 670, 'Address:')
    invoice_canvas.drawString(200, 670, address)

    # Draw the amount
    invoice_canvas.drawString(50, 640, 'Amount:')
    invoice_canvas.drawString(200, 640, str(amount))

    # Save the invoice
    invoice_canvas.save()

    return 'invoice.pdf'

# Example usage
customer_name = 'John Doe'
address = '123 Main St, City'
amount = 100.00

invoice_path = generate_invoice(customer_name, address, amount)
print(f"Invoice generated and saved at: {invoice_path}")
