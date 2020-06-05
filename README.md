# CoffeeHouse SpamDetection

Library for detecting spam by classifying input as spam/ham

```py
from coffeehouse_spamdetection.main import SpamDetection

spam_detection = SpamDetection()
spam_detection.predict("Test")
# {'ham': 0.998092, 'spam': 0.0017609089}
```