import pandas as pd
data = [
  {
    "user_id": 1,
    "name": "Ashish",
    "transactions": [
      {
        "transaction_id": "txn_1001",
        "date_time": "2025-09-01 14:32:00",
        "amount": 250.00,
        "type": "debit",
        "merchant": "Starbucks",
        "payment_mode": "UPI",
        "location": "Delhi",
        "recurring": False,
        "category": "Food & Dining"
      },
      {
        "transaction_id": "txn_1002",
        "date_time": "2025-09-02 10:15:00",
        "amount": 1200.00,
        "type": "debit",
        "merchant": "Uber",
        "payment_mode": "Card",
        "location": "Delhi",
        "recurring": False,
        "category": "Transport"
      },
      {
        "transaction_id": "txn_1003",
        "date_time": "2025-09-05 09:00:00",
        "amount": 799.00,
        "type": "debit",
        "merchant": "Netflix",
        "payment_mode": "UPI",
        "location": "Online",
        "recurring": True,
        "category": "Entertainment"
      },
      {
        "transaction_id": "txn_1004",
        "date_time": "2025-09-07 18:45:00",
        "amount": 5000.00,
        "type": "credit",
        "merchant": "Salary",
        "payment_mode": "Bank Transfer",
        "location": "Delhi",
        "recurring": True,
        "category": "Income"
      }
    ]
  },
  {
    "user_id": 2,
    "name": "Neha",
    "transactions": [
      {
        "transaction_id": "txn_2001",
        "date_time": "2025-09-01 11:30:00",
        "amount": 1500.00,
        "type": "debit",
        "merchant": "Amazon",
        "payment_mode": "Card",
        "location": "Mumbai",
        "recurring": False,
        "category": "Shopping"
      },
      {
        "transaction_id": "txn_2002",
        "date_time": "2025-09-02 07:30:00",
        "amount": 75.00,
        "type": "debit",
        "merchant": "Mumbai Metro",
        "payment_mode": "UPI",
        "location": "Mumbai",
        "recurring": True,
        "category": "Transport"
      },
      {
        "transaction_id": "txn_2003",
        "date_time": "2025-09-04 21:00:00",
        "amount": 350.00,
        "type": "debit",
        "merchant": "Pizza Hut",
        "payment_mode": "Cash",
        "location": "Mumbai",
        "recurring": False,
        "category": "Food & Dining"
      },
      {
        "transaction_id": "txn_2004",
        "date_time": "2025-09-05 10:00:00",
        "amount": 20000.00,
        "type": "credit",
        "merchant": "Salary",
        "payment_mode": "Bank Transfer",
        "location": "Mumbai",
        "recurring": True,
        "category": "Income"
      }
    ]
  },
  {
    "user_id": 3,
    "name": "Rahul",
    "transactions": [
      {
        "transaction_id": "txn_3001",
        "date_time": "2025-09-01 16:10:00",
        "amount": 220.00,
        "type": "debit",
        "merchant": "Cafe Coffee Day",
        "payment_mode": "UPI",
        "location": "Bangalore",
        "recurring": False,
        "category": "Food & Dining"
      },
      {
        "transaction_id": "txn_3002",
        "date_time": "2025-09-03 09:20:00",
        "amount": 1200.00,
        "type": "debit",
        "merchant": "Ola",
        "payment_mode": "Card",
        "location": "Bangalore",
        "recurring": False,
        "category": "Transport"
      },
      {
        "transaction_id": "txn_3003",
        "date_time": "2025-09-05 20:00:00",
        "amount": 499.00,
        "type": "debit",
        "merchant": "Spotify",
        "payment_mode": "UPI",
        "location": "Online",
        "recurring": True,
        "category": "Entertainment"
      },
      {
        "transaction_id": "txn_3004",
        "date_time": "2025-09-06 11:00:00",
        "amount": 15000.00,
        "type": "credit",
        "merchant": "Freelance Project",
        "payment_mode": "Bank Transfer",
        "location": "Bangalore",
        "recurring": False,
        "category": "Income"
      }
    ]
  },
  {
    "user_id": 4,
    "name": "Priya",
    "transactions": [
      {
        "transaction_id": "txn_4001",
        "date_time": "2025-09-01 08:00:00",
        "amount": 2500.00,
        "type": "debit",
        "merchant": "Electricity Bill",
        "payment_mode": "Net Banking",
        "location": "Chennai",
        "recurring": True,
        "category": "Utilities & Bills"
      },
      {
        "transaction_id": "txn_4002",
        "date_time": "2025-09-02 13:00:00",
        "amount": 900.00,
        "type": "debit",
        "merchant": "Flipkart",
        "payment_mode": "Card",
        "location": "Chennai",
        "recurring": False,
        "category": "Shopping"
      },
      {
        "transaction_id": "txn_4003",
        "date_time": "2025-09-03 15:00:00",
        "amount": 400.00,
        "type": "debit",
        "merchant": "Dominos",
        "payment_mode": "UPI",
        "location": "Chennai",
        "recurring": False,
        "category": "Food & Dining"
      },
      {
        "transaction_id": "txn_4004",
        "date_time": "2025-09-07 09:30:00",
        "amount": 25000.00,
        "type": "credit",
        "merchant": "Salary",
        "payment_mode": "Bank Transfer",
        "location": "Chennai",
        "recurring": True,
        "category": "Income"
      }
    ]
  },
  {
    "user_id": 5,
    "name": "Ankit",
    "transactions": [
      {
        "transaction_id": "txn_5001",
        "date_time": "2025-09-01 12:00:00",
        "amount": 600.00,
        "type": "debit",
        "merchant": "Zomato",
        "payment_mode": "UPI",
        "location": "Pune",
        "recurring": False,
        "category": "Food & Dining"
      },
      {
        "transaction_id": "txn_5002",
        "date_time": "2025-09-02 17:30:00",
        "amount": 200.00,
        "type": "debit",
        "merchant": "Pune Metro",
        "payment_mode": "UPI",
        "location": "Pune",
        "recurring": True,
        "category": "Transport"
      },
      {
        "transaction_id": "txn_5003",
        "date_time": "2025-09-04 14:00:00",
        "amount": 1500.00,
        "type": "debit",
        "merchant": "Reliance Trends",
        "payment_mode": "Card",
        "location": "Pune",
        "recurring": False,
        "category": "Shopping"
      },
      {
        "transaction_id": "txn_5004",
        "date_time": "2025-09-06 10:00:00",
        "amount": 18000.00,
        "type": "credit",
        "merchant": "Salary",
        "payment_mode": "Bank Transfer",
        "location": "Pune",
        "recurring": True,
        "category": "Income"
      }
    ]
  }
]


df = pd.DataFrame(data)
print(df)


# 2. Categorization Dimensions

# To enable analytics by category, you should classify transactions into:

# Food & Dining

# Transport & Fuel

# Bills & Utilities (electricity, rent, phone, internet, etc.)

# Shopping & Lifestyle (clothes, electronics, etc.)

# Entertainment & Subscriptions (OTT, Spotify, etc.)

# Education & Learning

# Healthcare

# Savings & Investments (FD, mutual funds, SIPs, etc.)

# Income (salary, freelance, cashback, refunds, etc.)






