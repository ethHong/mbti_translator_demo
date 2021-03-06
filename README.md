# Text to MBTI (Zero Shot - model)
๐ ์ฌ๋ฏธ๋ก ๋ง๋๋ MBTI ํด์๊ธฐ - MBTI Translator (๋๋ ์ค๋ ์ด๋ค MBTI์ฒ๋ผ ์ด์์๊น?)

์๋ ๋ชจ๋ธ์ ํ๋กํ ํ์์ streamlit ์ผ๋ก ๊ตฌํํ๊ณ ์์ต๋๋ค: https://github.com/ethHong/text_mbti

## About the project & Examples
* ๋ฌธ์ฅ์ ์๋ ฅํ์ธ์! ๋ค๋ฅํ๋ค๋ฉด '์ฑ๊ฒฉ์ ํ' ์ ์ฑํฅ์ด ๋๋ฌ๋ ๋งํ ๋ฌธ์ฅ์ ์๋ ฅํ์ธ์. ์๋์ ๊ฐ์ด ์ด๋ค ์ฑ๊ฒฉ์ ํ์ ๊ฐ๊น์ด ๋ฐํ์ธ์ง ์ถ๋ ฅํฉ๋๋ค
<img width="531" alt="image" src="https://user-images.githubusercontent.com/43837843/155150705-24830c0b-91a9-4aba-a168-d099e712ca25.png">

## How it works?
* Facebook ์ Zero-shot classification ๋ชจ๋ธ์ ์ฌ์ฉํฉ๋๋ค. 
* ๋ชจ๋ธ์ ๊ฐ MBTI ์์๋ค๊ณผ ๊ด๋ จ๋ ๋จ์ด์ dictionary ํตํด, ๋ฌธ์ฅ์ด ๊ฐ ๋จ์ด๋ค๊ณผ ์ฐ๊ด๋์ด์์ ํ๋ฅ ์ ์ถ๋ ฅํฉ๋๋ค. 

## Model and requirements
* ์ฌ์ฉ ๋ชจ๋ธ: https://huggingface.co/facebook/bart-large-mnli
* Huggingface ์ ๊ณต์ ๋ Facebook ์ผ Zero-shot text classification ๋ชจ๋ธ์ ์ฌ์ฉํฉ๋๋ค. 
* ์๋์ ๊ฐ์ด requirements๋ฅผ ์ค์ ํด์ฃผ์ธ์. ๋จ, torch์ ๊ฒฝ์ฐ GPU๋ฅผ ์ฌ์ฉํ๊ณ ์ถ๋ค๋ฉด ์๋ง์ ๋ฒ์ ์ ์ค์นํด์ฃผ์ธ์. 
> 02.20 update: Streamlit Sharing์ ํตํ ๋ฐ๋ชจ ๋ฐฐํฌ๋ฅผ ์ํด requirement.txt๋ง์ ์ฌ์ฉํฉ๋๋ค

```
pip install -r requirements.txt
```
```
streamlit run app.py
```
Zero-shot model ์ ๋ํ ๋ ํผ๋ฐ์ค๋ https://joeddav.github.io/blog/2020/05/29/ZSL.html ์ด ๋งํฌ๋ฅผ ์ฐธ๊ณ ํด์ฃผ์ธ์!

## Module Description 
Zero-shot text classification์, ํ์คํธ๋ฅด input์ผ๋ก ๋ฐ์, ์๋ ฅ๋ label ๋ค๊ณผ ๊ด๋ จ๋ ์ฃผ์ ์ผ ํ๋ฅ ์ outputํฉ๋๋ค. 
์ด๋ฅผ ํ์ฉํด, MBTI์ ๊ฐ ์์๋ค๊ณผ ๊ด๋ จ๋ ๋จ์ด๋ค์ JSONํํ๋ก ์๋ ฅํด ๋น๊ตํ ๋ค, MBTI ๋ฅผ ์ถ๋ ฅํด์ค๋๋ค. 

## Plans
* ์์ง์ ๊ฐ๋จํ ๋ฐ๋ชจ๋ง ๋ง๋ค์ด๋์ ์ํฉ์๋๋ค.
* ์ถํ MBTI-dictionary ๋ฅผ ์๋ฐ์ดํธํด, ์ ํ๋๋กธ ์ค๋๋ ฅ์ ์ฌ๋ฆฌ๋ ์์์ ํ  ์์ ์๋๋ค. 
* MT (machine translation) ์ ์ด์ฉํ ์ค์ญ ๋ฐ, ์นด์นด์ค๋ธ๋ ์ธ ์คํ์์ค zero-shot model ๋ฑ์ ํ์ฉํด ํ๊ตญ์ด์ ๋ํ ์ง์์ ํ๋ํด๋ณผ ์์ ์๋๋ค. 
