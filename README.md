# Twitter Blocker in Python


### Getting Access to twitter API
First of all In order to use this script, you'll need to have access to twitter API and have required keys to use this program. For more information you can read [this link](https://developer.twitter.com/en/support/twitter-api/developer-account).

Now that you have a developer account, you need to create an app to get the required credentials. Use [this link](https://apps.twitter.com/) to create an app.

The script needs **4 credential keys** in order to have access to twitter API.
1. Consumer key
2. Consumer secret key
3. Access token key
4. Access token secret key

If you have passed mentioned steps successfully, now you are ready to use this script. 

### Python Programming Language
As you can see in the title of this article, this script is written in `Python`. Therefore, you should have a basic knowledge of Python if you want to modify the code to meet your needs.

### Installing `TwitterAPI`
In this script, a library was needed to make a connection to twitter API easily. Therefore, `TwitterAPI` was selected from among the libraries introduced by Twitter. In order to see other options for Python or any other programming language you can check [this link](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2).

You can easily install this library using `pip` :
> pip install TwitterAPI

### Completing the code

#### Part 1: Entering Required Credentials
You need to write your credentials in lines `21-30` which is like :

    # the consumer key
    consumer_key='Enter Your Consumer Key here',
    
    # the consumer secret key
    consumer_secret='Enter Your Consumer Secret Key here',

    # the access token key
    access_token_key='Enter Your Access Token Key here',

    # the access token secret key
    access_token_secret='Enter Your Access Token Secret Key here'

#### Part 2: Completing The lists of accounts to be blocked

In line `101` of this code, you can see a list named `block_list` and it is like this :

    block_list = []  # list of usernames to block

The only thing you need to do is to create a list of accounts that you need to block. This list should be filled by usernames, and you have to fill it using strings. Here is an example :

    block_list = ['account1', 'account2', 'account3']

### Using code

Now that everything is filled correctly, you are ready to use this code. Enjoy!

If you had any questions related to this script, feel free to ask me.