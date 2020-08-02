<img src="resources/banner.png" style="width: 200%">

## About
Sanitara is a machine-learning and heuristics based Parental Control system.
This is a PoC developed using the RAD (Rapid Application Development) method. Thus, not every part will be perfect nor are they going to be.

## How it Works
Currently, the service works by exposing an API, in which one can send
a domain url, and recieve a safety prediction via. a series of 
data formatting, heuristics and machine learning models.

### The Models
A large part of sanitation comes from heuristics, however.  We've also
developed a model using sklearn to predict how child-friendly a website will be, based on its url.

To do this, we're using an sklearn model - the SGD classifier.  We trained it on ~200.000 labeled domain names.\
Here are the information and metrics for our current model:


#### Dataset:
- ##### Size: `{"training_set_length": 135955, "testing_set_length": 58267}`
- ##### Features: `[URL, Extension, HTTP(S), External_Review]`
- ##### Labels: `[Safe (0), Not Safe (1.0]`
- ##### Test set percentage: `30.0%`

 
#### Metrics:
##### Mean Accuracy: `0.8973346834400261`

||Label|precision|recall|f1-score|support|
|---|---|---|---|---|
||0|0.85|0.96|0.90|29133|
||1|0.96|0.83|0.89|29134|
|accuracy||||0.90|58267|
|macro avg||0.90|0.90|0.90|58267|
|weighted avg||0.90|0.90|0.90|58267|

##### Cross Validation:
 - fit_time: `[1.37127185 1.92903113 1.43998051 1.51016569 1.28997445]`
 - score_time: `[0.23392534 0.30216718 0.22985435 0.25978017 0.25476122]`
 - test_score: `[0.92016991 0.98741151 0.95873237 0.96645557 0.61770158]`
 - train_score: `[0.95832717 0.95061045 0.9569952  0.95640309 0.99188431]`

#### Parameters & Pipeline

```python
sgd = Pipeline([
     ('vect', CountVectorizer(max_df=1.0, max_features=None, ngram_range=(1,1))),
     ('tfidf', TfidfTransformer(norm='l1', use_idf=True)),
     ('sgd', SGDClassifier(max_iter=50, penalty='l2', alpha=1e-05))
])
```

### Heuristics
// RegEx, Whitelist, Blacklist, External APIs'

## <a id="run_service">Running the Service</a>
```bash
> git clone https://github.com/frederikgram/sanitara.git
> cd sanitara
> python -m venv env
> ./sanitara/env/Scripts/activate.bat # Depends on system
> pip install -r requirements.tx
> cd sanitara
> uvicorn main:app --reload
```
### Testing the Installation
```bash>
> curl http://127.0.0.1:8000/api/v1/predict/?message=porn.com
> {"prediction":1.0,"err":null,"input":"porn.com"}

  # 1.0 is the label for a "not_safe" website.
```

### FastAPI
FastAPI is a framework designed to serve production quality APIs' without
to much effort or overhead. We're using this to deploy our machine learning models,
and automatically generate documentation for our API.

## Documentation
After running the service, as mentioned [here](#run_service). It's as simple as navigating to `http://127.0.0.1:8000/docs` to see the documentation as provided by [swagger](https://swagger.io)
