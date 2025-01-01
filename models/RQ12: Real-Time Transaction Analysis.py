# Sample code in Python to analyze transactions and flag suspicious activity

def analyze_transactions(transactions):
    suspicious_transactions = []  
    
    for transaction in transactions:  # Loop through each transaction
        if transaction["amount"] > 1000:  
            if transaction["location"] != "local":  
                suspicious_transactions.append(transaction)  # Flag as suspicious if transaction amount is more than 1000 and not local
    return suspicious_transactions

#Example transactions
transactions = [
    {"id": 1, "amount": 1200, "location": "remote"},
    {"id": 2, "amount": 850, "location": "local"},
    {"id": 3, "amount": 2150, "location": "remote"},
    {"id": 4, "amount": 200, "location": "local"},
    {"id": 5, "amount": 1030, "location": "remote"},
    {"id": 7, "amount": 1520, "location": "local"},
    
]

# Call the function
suspicious = analyze_transactions(transactions)

#print suspicious transactions
for s in suspicious:
    print(f"Suspicious Transaction: ID {s['id']} - Amount: {s['amount']} - Location: {s['location']}")
