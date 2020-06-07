# CoffeeHouse SpamDetection

Library for detecting spam by classifying input as spam/ham

## Installation

Install the following packages using the corresponding setup and makefile
operations provided by the repo, or use CoffeeHouse-Server's install script
to install all the required components

 - Hyper-Internal-Service
 - CoffeeHouse-NLPFR
 - CoffeeHouse-DLTC 
 - CoffeeHouseMod-Tokenizer
 - CoffeeHouseMod-StopWords
 - CoffeeHouseMod-APT
 
Finally, install CoffeeHouse-SpamDetection by running `python3 setup.py install`

## Example Usage
```py
from coffeehouse_spamdetection.main import SpamDetection

spam_detection = SpamDetection()
spam_detection.predict("Test")
# {'ham': 0.998092, 'spam': 0.0017609089}
```

## Start as server
```shell script
python3 -m coffeehouse_spamdetection --start-server
```

This process will run using port `5601` and only accepts POST requests
with the parameter `input` as plain text. You should recieve a JSON 
response that looks like this

```json
{
  "status": true,
  "results": {
    "ham": "0.998092",
    "spam": "0.0017609089"
  }
}
```