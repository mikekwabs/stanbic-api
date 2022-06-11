<h1> Stanbic Bank API Assessment</h1>

<p>The project covers 6 endpoints in the assessment. They are as follows: </p>
<ol>
    <li>Add a new customer.  {http://127.0.0.1:8000/api/add-customer/}</li>
    <li> Retrieve all customers.  {http://127.0.0.1:8000/api/get-customers/}</li>
    <li>Retrieve a customer’s info by Email or phone number.  {http://127.0.0.1:8000/api/get-customer-phone/<str:pk>}</li>
    <li>Update Customer info.  {http://127.0.0.1:8000/api/update-customer/<int:pk>}</li>
    <li> Add a new account to an existing customer.  {http://127.0.0.1:8000/api/add-account/}</li>
    <li>Retrieve all accounts of a customer using email or phone number. {http://127.0.0.1:8000/api/get-accounts-phone/<str:pk>}</li>
    <li>Delete an account by account number.  {N/A}</li>
    <li>Delete a customer and all linked accounts.  {N/A}</li>

</ol>

<h3> To get started..... <h3>

<ul>
<li>Clone the repository</li>

```
git clone https://github.com/mikekwabs/stanbic-api.git
```

<p> then..<p>

<li>Change directory to the project</li>

```
cd into stanbic
```

<p> then..<p>

<li>Install dependencies</li>

```
run pip install -r requirement.txt
```

<p> then..<p>

<li>run the development server</li>

```
run python manage.py runserver
```

</ul>

<p> Next: </p>

<ul>
    <li> Implement signals</li>
</ul>
