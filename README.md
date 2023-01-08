# Text to MBTI (Zero Shot - model)
😄 MBTI Translator (Infer you personality type based on your sentence)

Using Streamlit library, this project is implementing application with UI of following project: https://github.com/ethHong/text_mbti

## About the project & Examples
* Pur the sentence and click 'generate' button. Using Zero shot classification model, the app predict the most probable MBTI of yourself. 
<img width="708" alt="Screenshot 2023-01-08 at 3 04 29 PM" src="https://user-images.githubusercontent.com/43837843/211182872-e0db4da8-9c7e-48bd-a3ec-04165baf5c7e.png">

<img width="697" alt="Screenshot 2023-01-08 at 3 05 18 PM" src="https://user-images.githubusercontent.com/43837843/211182926-cd88e370-4790-40f3-a7f1-a964d09366ef.png">


## How it works?
* This app uases  Zero-shot classification model from Facebook. 
* The model uses pre-defined dictionary data which representes each of 16 personality type
* It compute probability input keyword be relevant to each of the keywords mapped in dictionary of 16 personality types. 
![image](https://user-images.githubusercontent.com/43837843/211183359-ad2cf761-99a7-467f-8bb9-cdf308bc019e.png)


## Output sample
```
Input: "I stayed home all day"

===

Output:

You are:  ISFP
Ratio {'E': 27.338588094108168, 'I': 72.66141190589182} {'N': 22.149243913056992, 'S': 77.85075608694301} {'T': 46.17274433748438, 'F': 53.82725566251562} {'P': 57.30466611213056, 'J': 42.69533388786944}
```

```
Input: "I'm making plans for my trip to Osaka. I'm so excited!"

===

Output:

You are:  ESTJ
Ratio {'E': 71.53464326345417, 'I': 28.46535673654582} {'N': 35.33135528913844, 'S': 64.66864471086156} {'T': 58.70273162646018, 'F': 41.29726837353982} {'P': 46.96476087995551, 'J': 53.03523912004449}
```

## Model and requirements
* Model reference: https://huggingface.co/facebook/bart-large-mnli
* Environment setup:
> 02.20 update: Use requirements.txt to setup required libraries. 

```
pip install -r requirements.txt
```
```
streamlit run app.py
```
