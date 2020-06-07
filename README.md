# CoffeeHouse SpamDetection

Library for detecting spam by classifying input as spam/ham

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