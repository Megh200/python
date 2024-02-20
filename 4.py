class Document:
    def __init__(self, content):
        self.content = content

class Printer:
    def __init__(self, brand):
        self.brand = brand

# Implement PrintedDocument class
class PrintedDocument(Document, Printer):
    def __init__(self, content, printer):
        # Call the constructors of the parent classes
        Document.__init__(self, content)
        Printer.__init__(self, printer)

# Example usage:
printed_document = PrintedDocument(content="Hello, World!", printer="Epson")
print(f"Content: {printed_document.content}, Printer Brand: {printed_document.brand}")
