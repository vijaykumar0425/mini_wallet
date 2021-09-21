###The first thing to do is to clone the repository:

>$ git clone https://github.com/vijaykumar0425/mini_wallet.git
>___
>$ cd mini_wallet

###Create a virtual environment to install dependencies in and activate it:

>$ python/python3 -m venv venv
> ___
>$ source env/bin/activate

###Then install the dependencies:

>$ pip install -r requirements.txt

>(venv)$ cd project
>
>(venv)$ python manage.py runserver

###Initialize my account for wallet

>curl --location --request POST 'http://localhost/api/v1/init' \
--form 'customer_xid="39c46492-276d-44aa-a020-7cf966b2f09a"'

###Enable my wallet
>curl --location --request POST 'http://localhost/api/v1/wallet' \
--header 'Authorization: Token 61f84c25cbebd4609e0ec0b14bc9d4f6439c460c'

###View my wallet balance

>curl --location --request GET 'http://localhost/api/v1/wallet' \
--header 'Authorization: Token 61f84c25cbebd4609e0ec0b14bc9d4f6439c460c'

###Add virtual money to my wallet

>curl --location --request POST 'http://localhost/api/v1/wallet/deposits' \
--header 'Authorization: Token 61f84c25cbebd4609e0ec0b14bc9d4f6439c460c' \
--form 'amount="100000"' \
--form 'reference_id="50535246-dcb2-4929-8cc9-004ea06f5241"'

###Use virtual money from my wallet

>curl --location --request POST 'http://localhost/api/v1/wallet/withdrawals' \
--header 'Authorization: Token 61f84c25cbebd4609e0ec0b14bc9d4f6439c460c' \
--form 'amount="60000"' \
--form 'reference_id="4b01c9bb-3acd-47dc-87db-d9ac483d20b2"'

###Disable my wallet

>curl --location --request PATCH 'http://localhost/api/v1/wallet' \
--header 'Authorization: Token 61f84c25cbebd4609e0ec0b14bc9d4f6439c460c' \
--form 'is_disabled="true"'