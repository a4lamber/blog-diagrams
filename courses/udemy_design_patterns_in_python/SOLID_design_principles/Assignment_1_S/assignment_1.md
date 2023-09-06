The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning it should have only one responsibility or job. To practice SRP in Python, you can work on refactoring exercises that involve splitting responsibilities among classes. Here are some exercises with Python code that you can modify to conform to SRP:

1. **User Authentication and User Data Management:**

   Original Code:
   ```python
   class User:
       def __init__(self, username, password):
           self.username = username
           self.password = password

       def login(self, username, password):
           # Code to authenticate the user
           pass

       def update_profile(self, new_info):
           # Code to update user profile
           pass
   ```

   Refactor the code to separate user authentication and user data management into two different classes.

2. **File Reader and Data Processor:**

   Original Code:
   ```python
   class DataProcessor:
       def __init__(self, filename):
           self.filename = filename

       def read_data(self):
           # Code to read data from a file
           pass

       def process_data(self, data):
           # Code to process the data
           pass
   ```

   Refactor the code to create separate classes for reading data from a file and processing the data.

3. **Order Management:**

   Original Code:
   ```python
   class Order:
       def __init__(self, order_id, customer, items):
           self.order_id = order_id
           self.customer = customer
           self.items = items

       def calculate_total(self):
           # Code to calculate the total order cost
           pass

       def print_invoice(self):
           # Code to print the order invoice
           pass
   ```

   Refactor the code to separate order calculation and invoice printing into distinct classes.

4. **Email Sending and Logging:**

   Original Code:
   ```python
   class EmailService:
       def __init__(self, smtp_server):
           self.smtp_server = smtp_server

       def send_email(self, recipient, subject, body):
           # Code to send an email
           pass

       def log_email_sent(self, recipient, subject):
           # Code to log the sent email
           pass
   ```

   Refactor the code to split email sending and logging into separate classes.

5. **Shape Calculations:**

   Original Code:
   ```python
   class Circle:
       def __init__(self, radius):
           self.radius = radius

       def calculate_area(self):
           # Code to calculate the area of the circle
           pass

       def calculate_circumference(self):
           # Code to calculate the circumference of the circle
           pass
   ```

   Refactor the code to have separate classes for circle area calculation and circumference calculation.

In each exercise, focus on separating the distinct responsibilities into different classes while maintaining clear and meaningful interfaces. This practice will help you better understand and apply the Single Responsibility Principle in your Python code.